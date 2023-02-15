#Script to check for updates using the apt update command
#Last changed by Maximilian Tobitsch on 15.02.2023 07:00
#Last changes: set sender as hostname

import apt
import smtplib
import socket
from email.mime.text import MIMEText

# Define the recipients of the email
to = ['recipient']
sender = [socket.gethostname()+'@domain']

# Set up the SMTP server
smtp_server = 'SMTP-Server'
smtp_port = 587
smtp_username = 'username'
smtp_password = 'password'

# Connect to the package manager and check for updates
cache = apt.Cache()
cache.update()
cache.open(None)
updates = [pkg for pkg in cache if pkg.is_upgradable]

if updates:
    # Construct the message body
    msg = MIMEText('The following packages have updates available:\n\n' + '\n'.join(str(pkg) for pkg in updates))

    # Set the sender, recipients, and subject of the email
    msg['From'] = ', '.join(sender)
    msg['To'] = ', '.join(to)
    msg['Subject'] = 'Updates available on ' + socket.gethostname()

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(msg['From'], to, msg.as_string())

