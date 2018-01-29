# -*- coding: utf-8 -*-

from os import path as ospath
import time
import pickle

db = {}
usertime = {}

time_now1 = time.time()
time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
    db[name] = pwd
    usertime[name] = time_now
    #savedata()
    print usertime[name]

def olduser():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')
        print 'welcome back', name
        loadtime()
    else:
        print 'login incorrect'

def loadtime():
    if (time.time() - time_now1) / 3600 <= 4:#测试时将登陆间隔实践定为100s
        print 'lastime you load is %s.' % time_now
    else:
        print 'your loadtime is %s: ' % time_now

def savedata():
    if not ospath.exists('c:/text/data.txt'):        #判断文件是否存在，如果不存在则创建后写入，存在不操作提示
	    with open('c:/text/data.txt', 'wt') as f:    #后期要改为如果存在则读取，写入也不能是覆盖写入
		    f.write(db{})
    else:
	    print('file already exists!')

def showmenu():
    prompt = '''
    (N)ew User Login
    (E)xisting User Login
    (Q)uit
    
Example 7.1 Dictionary Example (userpw.py) (continued)

    Enter choice: '''

    while True:
        try:
            choice = raw_input(prompt).strip()[0].lower()
        except(EOFError, KeyboardInterrupt):
            choice = 'q'
        print '\nYou picked: [%s]' % choice
        if choice not in 'neq':
            print 'incalid option, try again'
        else:
            if choice == 'n':
                newuser()
            elif choice == 'e':
                olduser()
            elif choice == 'q':
                print 'quit'
                break

if __name__ == '__main__':
    showmenu()