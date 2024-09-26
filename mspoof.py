import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse



class Email:

    def __init__(self):

       pass

    def send(self):
        try:
            smtp_ip = "localhost"
            smtp_port = 25


            msg = MIMEMultipart()
            msg["From"] = f"{self.sender_name} <{self.sender}>"
            msg["To"] = self.reciver
            msg["Subject"] = self.title

            
            msg.attach(MIMEText(self.message, "plain"))


            smtp_server = smtplib.SMTP(smtp_ip, smtp_port)


            smtp_server.sendmail(self.sender, self.reciver, msg.as_string())

            smtp_server.quit()

            print("Sended")

        except Exception as error:
            print("There was an error \n")
            print(error)




def arguments():
    parser = argparse.ArgumentParser(description='eMail Spoofing')
    
    parser.add_argument('-s', '--sender', required=True, help='Mail to spoof')
    parser.add_argument('-r', '--reciver', required=True, help='Mail to send')
    parser.add_argument('-m', '--message', required=True, help='Content of the message')
    parser.add_argument('-t', '--title', required=True, help='Subject of the mail')
    parser.add_argument('-n', '--name', required=True, help='Name of the sender')

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        exit()
    
    if args.sender:
        mail.sender = args.sender
        
    
    if args.reciver:
        mail.reciver = args.reciver

    if args.message:
        mail.message = args.message
    
    if args.title:
        mail.title = args.title
    
    if args.name:
        mail.sender_name = args.name
    




if __name__ == "__main__":
    mail = Email()
    arguments()
    mail.send()
