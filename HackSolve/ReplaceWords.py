FilePath = 'C:\\Users\\Administrator\Desktop\HackSolve\SourceFile\CMD.txt'
File = open(FilePath, 'r')
Data = File.read(100)
File.seek(0, 0)  # �ļ�ָ�����ʼλ�õ��趨��Offset������
Lines = File.readlines()
File.close()
Change = input('Please input what you want to Check:')
for i in range(len(Lines)):
    if Lines[i].split(' ')[0] == Change:
        print('We get that Line', i, 'contains a data named ', Change, ',the content is:', Lines[i].replace('\n', ''))
        In = input('Would you want to change it(y/n)?')
        if In == 'y':
            File = open(FilePath, 'w')
            Replace = input('Please enter the data you want to replace:')
            Temp = Lines[i].replace(Change, Replace)
            File.seek(i, 0)
            Lines[i] = Temp
            File.writelines(Lines)
            print('Congratulations!You did it!')
            File.close()
        else:
            print('Thank you for checking!')
