lines = []
for line_num, line in enumerate(open('script.sh').readlines()):
    if line_num % 2 == 1:
        lines.append(line)
    else:
        lines.append('echo $RANDOM > file.txt \n')

open('script.sh', 'w').writelines(lines)