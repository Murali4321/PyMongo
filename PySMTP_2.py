import os
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication

path=input("Please enter path in the correct format to view files(e.g,C:\\Users\\Murali\\Pictures\\Files\\):")

class files():
    def __init__(self):
        pass
        
    def view_files(self):
        print("Below files are present in the directory")
        print("#########################################")
        files = [f for f in glob.glob(path + "**/*.*", recursive=True)]
        for f in files:
            print(f)
        
    def user_interests(self):
        print("Enter 1 for creating a new file")
        print("Enter 2 for deleting an existing file")
        print("Enter 3 for extracing and sending the text files in an email as attachments:")
        Choice=int(input("Please enter your choice:"))
        return Choice        
        
Obj=files()

Obj.view_files()
Choice=Obj.user_interests()
if Choice==1:
    filename=input("Please enter the file name:")
    path=input("Please specify the path where you want to create this file in correct format(e.g,C:\\Users\\Murali\\Pictures\\Files\\):")
    content=input("Please enter the content of the file:")
    if not os.path.exists(path):
        os.mkdir(path)
    file = open(path+filename, 'w') 
    file.write(content) 
    file.close()
    print("File created!!")    
elif Choice==2:
    filename=input("please enter the file name you want to delete:")
    os.remove(path+filename)
    print("File Removed!")
        
    
elif Choice==3:
    fromaddr = "murali52q7@gmail.com"
    toaddr = "murali52q7@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Files for reference"
    body = "Hi,\n\nPlease find the files attached\n\nThanks,\nMuralidhar"
    msg.attach(MIMEText(body, 'plain'))
    files=[f for f in glob.glob(path + "**/*.txt", recursive=True)]
    for file in files:
        attachment = open(file, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % file)
        msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,"zxcvasd1")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Sent an email with attachments!!")  

else:
    print("Please verify your choice. Its incorrect!")              
 