def copy(l):
    #1.打開源文件
    f = open(l,'rb+')
    #f2 = f.name#得到一個打開的文件名
    #n = f.read()#2.讀取源文件內容
    p = l.rfind('.')#找到文件中.的位置下標
    name = l[:p]#截取文件的名稱部分
    namek = l[p:]#截取文件的拓展名部分
    #3.打開一個新的備份文件
    f1 = open(name+'-副本'+namek,'wb+')
    while True:
        n = f.read(4096)
        if len(n) == 0:
            break
    #4.將內容寫入新文件裏
        f1.write(n)
    #5.關閉打開的文件
    f.close()
    f1.close()
f3 = input('請輸入要備份的文件名')
copy(f3)
