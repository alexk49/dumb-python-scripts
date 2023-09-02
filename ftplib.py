from ftplib import FTP
import os

# you need os to change directory within the ftp

# you will often only be connected to the route directory
ftp = FTP('domainname.com')

ftp.login(user='username', passwd='password')

ftp.cwd('//specificdomain-or-location')

def grabFile():
    # define file you want to download
    fileName = 'fileName.txt'
    # definie file you are writing to your pc
    localfile = open(filename, 'wb')
    # retrieve
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    # always quit ftp 
    ftp.quit()
    localfile.close()

def placeFile():
    fileName = 'fileName.txt'
    # storing binary 
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    ftp.quit()


