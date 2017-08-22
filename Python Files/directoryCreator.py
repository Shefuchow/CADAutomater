#__Author__ Mohammed Sefath Chowdhury
import shutil
import os
import sys

print("What is the date of this Bulletin? (ex: 20170818)")
date = input()
print('What is the number of this Bulletin? (Only type in a number, ex: 18 or 10.2)')
num = input()
dirName = date+' Bulletin '+num
os.startfile('M:/4500 VDC/4510 VDC Documents/4510.05 CAD Files/Bulletins Unzipped/')
os.mkdir('M:/4500 VDC/4510 VDC Documents/4510.05 CAD Files/Bulletins Unzipped/'+dirName)

dirName +=' Conformed CAD set'
os.startfile('M:/4500 VDC/4510 VDC Documents/4510.05 CAD Files/Bulletins Not yet released/')
#os.mkdir('M:/4500 VDC/4510 VDC Documents/4510.05 CAD Files/Bulletins Not yet released/'+dirName)
#shutil.copytree('ENTER LATEST CONFORMED CAD SET PATH HERE', 'C:/Users/Mohammed.chowdhury/Desktop/Conformed CAD Automater/Conformed CAD/Bulletins Not yet released/'+dirName)
shutil.copytree('M:/4500 VDC/4510 VDC Documents/4510.05 CAD Files/20170801 Current (Unapproved) Conformed CAD Set/', 'M:/4500 VDC/4510 VDC Documents/4510.05 CAD Files/Bulletins Not yet released/'+dirName)

print('New folders made for the new Bulletin')