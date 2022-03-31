import os
#print(os.system('date'))
#os.mkdir('/Users/WELCOME/Desktop/TestFolder')
#print(os.getcwd())
#print(os.listdir())
#print(os.listdir('/Users/WELCOME'))
#print(os.path.exists('/Users/WELCOME/Desktop/TestFolder2'))
#print(os.path.splitext('/Users/WELCOME/Desktop/python/count.py')[1])
import shutil
src = input('Enter source here: ')
des = input('Enter destination here: ')
src = src + '/'
des = des + '/'

files = os.listdir(src)
for i in files: 
    shutil.copy((src + i),des)
