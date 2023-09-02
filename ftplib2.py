import ftplib

ftpHost = 'localhost'
ftpPort = 21
ftpUname = 'abcd'
ftpPass = 'pass'

ftp = ftplib.FTP()
# ftplib.FTP_TLS

# connect to server
ftp.connect(ftpHost, ftpPort)
# login to the FTP 
ftp.login(ftpUname, ftpPass)

# setup secure data connection
ftp.prot_p()

# get list of file names
ftp.nlst()

# change directory 
ftp.cwd("folder1/folder2")

ftp.quit()