fhand = open('new.txt')

for line in fhand:
    if 'know' in line:
        print(line)