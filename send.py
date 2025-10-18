import socket
import struct
import argparse

def main():
    parser = argparse.ArgumentParser(description="ELF sender")
    parser.add_argument("-i","--ip", help="IP to bind or 0.0.0.0", required=True)
    parser.add_argument("-p","--port", type=int, help="Port to listen on", required=True)
    parser.add_argument("-f", "--file_path", help="Path to ELF binary", required=True)
    args = parser.parse_args()
    # Load ELF binary
    with open(args.file_path, 'rb') as f:
        elf_data = f.read()

    elf_size = len(elf_data)
    print(f"[+] Loaded ELF binary ({elf_size} bytes)")

    # Create socket and bind
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((args.ip, args.port))
        s.listen(1)
        print(f"[+] Listening on {args.ip}:{args.port}...")

        conn, addr = s.accept()
        with conn:
            print(f"[+] Connection from {addr}")

            # Send 4-byte little-endian size prefix
            conn.sendall(struct.pack('<I', elf_size))

            # Send ELF binary
            conn.sendall(elf_data)
            print(f"[+] Sent {elf_size} bytes")

if __name__ == '__main__':
    main()
