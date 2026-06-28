import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "YOUR_EMAIL@gmail.com"  # Replace with your actual email
    password = "YOUR_APP_PASSWORD"  # Replace with your actual app password

    receiver = "YOUR_EMAIL@gmail.com"  # Replace with your actual email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

