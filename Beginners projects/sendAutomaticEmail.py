from email.message import EmailMessage
import smtplib
import getpass

def credentials_entries():
    username = input("Please enter your email address: ")
    password = getpass.getpass("Please enter your password: ")
    smtp_server = input("Please enter the smtp server name to use: ")
    port = int(input("PLease enter the port number: "))
    return username, password, smtp_server, port

def email_setup(user_email):
    email = EmailMessage()
    email["From"] = user_email
    email["To"] = input("Please enter the receiver email address: ")
    email["Subject"] = input("Please enter the mail subject: ")
    content = input("Please enter the content of your email: ")
    email.set_content(content)
    return email

username, password, smtp_server, port = credentials_entries()

email = email_setup(username)

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(email)
except smtplib.SMTPConnectError:
    print("Erreur de connexion au serveur SMTP.")
except smtplib.SMTPAuthenticationError:
    print("Erreur d'authentification. Veuillez vérifier vos identifiants.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")


