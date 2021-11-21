with open('word.txt', 'w', encoding='utf-8') as f:
    for i in range(43,46):
        for j in range(60):
            f.write('Wakarimasu! Sat 06 Nov 2021 03:{0:02d}:{1:02d} PM CST you-kali-vm x86_64 GNU/Linux 8\n'.format(i,j))
