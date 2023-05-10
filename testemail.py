import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

my_sg = sendgrid.SendGridAPIClient('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')


# Change to your verified sender
from_email = Email("pritish.kr3@gmail.com")

# Change to your recipient
to_email = To("onelinehits@gmail.com")

subject = "Boarding Notification"
content = Content("text/plain", "You have boarded the LUCKNOW METRO Corp. from Charbagh metro station INC at time: {data['entry time']}")

mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = my_sg.client.mail.send.post(request_body=mail_json)

