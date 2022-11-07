from Attendive import mail
from flask_mail import Message
from flask import url_for


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender=('Attendive', 'support@tejearning.com'), recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link. The link will expire in 10 minutes:
{url_for('student.reset_token', token=token, _external=True)}

If your did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


def send_confirm_email(email, token):
    msg = Message('Confirm Your Account',
                  sender=('Attendive', 'support@tejearning.com'), recipients=[email])
    msg.body = f'''To confirm your email, visit the following link. The link will expire in 10 minutes:
{url_for('student.confirm_email', token=token, _external=True)}

'''
    mail.send(msg)
