# debug_for_hashcat
1. `flag2.7z` is compressed with unknown password.
2. `flag2.hash` created by `7z2hashcat64-1.5.exe flag2.7z > flag2.hash`.
3. `word.py` is the password generate program.
4. `word.txt` created by `python3 word.py`.
5. Use command `hashcat.exe -m 11600 flag2.hash word.txt` to find the password for flag2.7z.
