import os
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication



class files():
    def __init__(self):
        pass
        
    def view_files(self):
        self.path=input("Please enter path where files to be displayed are present in correct format e.g,C:\\Users\\Murali\\Pictures\\Files\\:")
        print("Below files are present in the directory")
        print("######################################################")
        files = [f for f in glob.glob(self.path + "**/*.*", recursive=True)]
        for f in files:
            print(f)
        
    def user_interests(self):
        print("#####################################################")
        print("Enter 1 for creating a new file")
        print("Enter 2 for deleting an existing file")
        print("Enter 3 for extracing and sending the text files in an email as attachments:")
        Choice=int(input("Please enter your choice:"))
        return Choice
    def execution(self,Choice):
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
            if os.remove(self.path+filename):
                print("File Removed!")
            else:
                print("Incorrect file name!!")    
        
    
        elif Choice==3:
            fromaddr = "murali52q7@gmail.com"
            toaddr = "murali52q7@gmail.com"
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Files for reference"
            body = "Hi,\n\nPlease find the files attached\n\nThanks,\nMuralidhar"
            msg.attach(MIMEText(body, 'plain'))
            ftype=input("Please enter file extension-e.g, txt,pdf etc:")
            files=[f for f in glob.glob(self.path + "**/*."+ftype, recursive=True)]
            password=input("Please enter password of your email account:")
            for file in files:
                attachment = open(file, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % file)
                msg.attach(part)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr,password)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            print("Sent an email with attachments!!")  

        else:
            print("Please verify your choice. Its incorrect!")              
             
        
Obj=files()

Obj.view_files()
Choice=Obj.user_interests()
Obj.execution(Choice)