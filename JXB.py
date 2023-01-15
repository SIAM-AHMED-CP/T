#coding=utf-8
import os, sys, platform
os.system('xdg-open https://facebook.com/groups/302474258349320/')
os.system('git pull')
 
bit = platform.architecture()[0]
if bit == '64bit':
    import x18
    x18.run()
 
elif bit == '32bit':
    import x1832
    x1832.run()
