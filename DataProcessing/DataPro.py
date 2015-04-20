import xml.dom.minidom

dom = xml.dom.minidom.parse('ipad.xml')

root = dom.documentElement
filehandle = open('Ans.txt', 'w')
filehandle2 = open('context.txt', 'w')

tmp = root.getElementsByTagName('weibo')
for i in tmp :
    content = i.getElementsByTagName('sentence')
    for j in content :
        Is = j.getAttribute('opinionated')
        Ans = j.getAttribute('polarity')
        if Is == 'Y' :
            filehandle.write(Ans + '\n')
            filehandle2.write(j.firstChild.data + '\n')
filehandle2.write('q')
filehandle.close()
filehandle2.close()

