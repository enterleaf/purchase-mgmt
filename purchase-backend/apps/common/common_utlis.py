import threading

from django.core.mail import EmailMessage


class EmailThread(threading.Thread):
    """
        This class is reponsible to make email sending process faster
    """

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)


# def email(Subject, body, to ):
def email(to ):
    print(f'sending email to ${to}')
    print('comming from email fucntion')
    # email_subject = Subject
    # email_body = body
    email_subject = "Contact new joinee"
    email_body = "Thanks for enrolling"
    email = EmailMessage(
        email_subject,
        email_body,
        'noreply@gmail.com',
        [to]
    )

    print(email_body)
    EmailThread(email).start()
