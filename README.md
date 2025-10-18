# linux_reflective_loader
python based reflective elf loader for linux

This was mostly vibe coded so I can't take full credit for it. Using the C code from the article https://medium.com/confluera-engineering/reflective-code-loading-in-linux-a-new-defense-evasion-technique-in-mitre-att-ck-v10-da7da34ed301 for reflectively loading an ELF executable on Linux I asked MS Co-Pilot to convert it to python for me. Surrisingly it generated a script that worked first try if I manaully closed connection on remote end for sending the ELF. Adding in size before sending data fixed the hang issue and now works with no issues.

This was test on Kali Linux with no AnitVirus or EDR. The goal was to practice reflection and not work on evaision yet. Using a python one liner you can cpull the loader in memory to execute so that nothing is ever written to disk.

<img width="897" height="506" alt="image" src="https://github.com/user-attachments/assets/882d82aa-d0e6-4881-bbc9-9d8d197bb8ff" />


<img width="892" height="500" alt="image" src="https://github.com/user-attachments/assets/444e82ee-bd13-4365-a2e4-536983cc4c60" />

<img width="895" height="509" alt="image" src="https://github.com/user-attachments/assets/cccd8804-cb96-48f4-9951-a3af21f13bd3" />

<img width="1074" height="508" alt="image" src="https://github.com/user-attachments/assets/98a45afb-c142-45ff-a88c-41a53a3eced9" />

<img width="1376" height="514" alt="image" src="https://github.com/user-attachments/assets/a4003e67-a89e-4cfa-b7fb-2905d271f970" />
