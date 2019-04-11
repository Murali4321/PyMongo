import os
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
import time



class files:
    def __init__(self):
        pass
        
    def view_files(self):
        self.path=input("Please enter path where files to be displayed are present:")
        print("Below files are present in the directory")
        print("######################################################")
        files = [f for f in glob.glob(self.path + "**/*.*", recursive=True)]
        for f in files:
            print(f)
        
    def user_interests(self):
        print("#####################################################")
        print("Enter 1 for creating a new file")
        print("Enter 2 for deleting an existing file")
        print("Enter 3 for extracing and sending the files in an email as attachments:")
        print("########################################################################################################")
        print("NOTE:Turn off 2 step verification and enable third party access in your gmail account before entering 3") 
        Choice=int(input("Please enter your choice:"))
        return Choice
    def execution(self,Choice):
        if Choice==1:
            filename=input("Please enter the file name with its extension:")
            new_p=int(input("Please enter 1 for new path else enter 0 for same path:"))
            if new_p==1:
                new_path=input("Please specify your new path:")
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                content=input("Please enter the content of the file:")   
                file = open(new_path+filename, 'w') 
                file.write(content) 
                file.close()
                print("File created!!")
            elif new_p ==0:
                content=input("Please enter the content of the file:")   
                file = open(self.path+filename, 'w') 
                file.write(content) 
                file.close()
                print("File created!!")    
              
        elif Choice==2:
            filename=input("please enter the file name you want to delete:")
            if os.remove(self.path+filename):
                print("File Removed!")  
            else:
                print("File could not be removed. Please check file name")
            
        elif Choice==3:
            fromaddr = input("Please enter your gmail id:")
            toaddr = input("Please enter receivers email id:")
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
            t=server.sendmail(fromaddr, toaddr, text)
            print("Please wait. This may take some time")
            time.sleep(30)
            if t=={} :   
                print("Sent an email with attachments!!")
            else:
                print("Email not sent!!")    
            server.quit()
                
            
              
                    
        
Obj=files()

Obj.view_files()
Choice=Obj.user_interests()
Obj.execution(Choice)