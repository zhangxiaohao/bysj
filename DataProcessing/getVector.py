import codecs
import sys
fileNeg = open('NEGword.txt', 'r')
filePos = open('POSword.txt', 'r')

Neg = fileNeg.readlines()
Pos = filePos.readlines()
Out = open('trainVec.txt', 'w')

fileNeg.close()
filePos.close()

for i in range(len(Neg)) :
    Neg[i] = Neg[i][:-1]

for i in range(len(Pos)) :
    Pos[i] = Pos[i][:-1]

fileNP = open('NorP.txt', 'r')
fileRP = open('ripecontent.txt', 'r')

NG = fileNP.readlines();
RP = fileRP.readlines();

for i in range(len(RP)) :
    if NG[i] == "NEG\n":
        Out.write('0 ')
    else :
        Out.write('1 ')
    RP[i] = RP[i].split(' ')
    is1 = is2 = 0
    PosNum = NegNum = 0
    dict1 = {}
    for j in range(len(RP[i])) :
        RP[i][j] = RP[i][j].split('/')
        if RP[i][j][0] == '?' :
            is1 = is1 + 1
        if RP[i][j][0] == '!' :
            is2 = is2 + 1
        if RP[i][j][0] in Neg :
            NegNum = NegNum + 1
        if RP[i][j][0] in Pos :
            PosNum = PosNum + 1
        if len(RP[i][j]) > 1 :
            RP[i][j] = RP[i][j][1]
        else :
            continue
        if RP[i][j] in dict1 :
            dict1[RP[i][j]] = dict1[RP[i][j]] + 1
        else :
            dict1[RP[i][j]] = 1
    if 'a' in dict1 :
        Out.write ("1:%d "% dict1['a'])
    else :
        Out.write ("1:0 ")
    if 'e' in dict1 :
        Out.write ("2:%d "% dict1['e'])
    else :
        Out.write ("2:0 ")
    if 'y' in dict1 :
        Out.write ("3:%d "% dict1['y'])
    else :
        Out.write ("3:0 ")
    Out.write ("4:%d "% is1)
    Out.write ("5:%d "% is2)
    Out.write ("6:%d "% PosNum)
    Out.write ("7:%d\n"% NegNum)

Out.close()
