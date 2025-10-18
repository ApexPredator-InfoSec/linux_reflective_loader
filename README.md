# linux_reflective_loader
python based reflective elf loader for linux

This was mostly vibe coded so I can't take full credit for it. Using the C code from the article https://medium.com/confluera-engineering/reflective-code-loading-in-linux-a-new-defense-evasion-technique-in-mitre-att-ck-v10-da7da34ed301 for reflectively loading an ELF executable on Linux I asked MS Co-Pilot to convert it to python for me. Surrisingly it generated a script that worked first try if I manaully closed connection on remote end for sending the ELF. Adding in size before sending data fixed the hang issue and now works with no issues.

This was test on Kali Linux with no AnitVirus or EDR. The goal was to practice reflection and not work on evaision yet. Using a python one liner you can cpull the loader in memory to execute so that nothing is ever written to disk.

<img width="897" height="506" alt="image" src="https://github.com/user-attachments/assets/882d82aa-d0e6-4881-bbc9-9d8d197bb8ff" />

<img width="899" height="510" alt="image" src="https://github.com/user-attachments/assets/d870ad83-fda9-4f25-9871-8817941d0a6b" />

<img width="889" height="504" alt="image" src="https://github.com/user-attachments/assets/ce4fb7de-48e4-4066-9b4a-f27daf0f7b46" />

<img width="1366" height="511" alt="image" src="https://github.com/user-attachments/assets/a0064a47-d3ea-496d-b85f-d9a9dc12fb92" />

<img width="1376" height="514" alt="image" src="https://github.com/user-attachments/assets/a4003e67-a89e-4cfa-b7fb-2905d271f970" />
