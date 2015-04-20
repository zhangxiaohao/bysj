file = open('raw.txt', 'r')
file2 = open('ripe.txt', 'w')

List = file.readlines()
cnt = 0;
for str in List :
    if cnt % 2 :
        file2.write(str)
    cnt = cnt + 1
