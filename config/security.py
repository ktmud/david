# coding: utf-8
from flask.ext.babel import lazy_gettext as _

SECURITY_URL_PREFIX = '/account'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'keyboardcat2'
SECURITY_EMAIL_SENDER = 'no-reply@tongdawei.cc'
#SECURITY_CONFIRMABLE = False
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
#SECURITY_TRACKABLE = False
#SECURITY_PASSWORDLESS = False
SECURITY_CHANGEABLE = True

SECURITY_CONFIRM_SALT = 'afaA<@i'
SECURITY_RESET_SALT = '03nfm@I#'
SECURITY_LOGIN_SALT = 'safa92J!@'
SECURITY_REMEMBER_SALT = 'f#34fk12t3@'



_messages = {
    'UNAUTHORIZED': (_('You do not have permission to view this resource.'), 'error'),
    'CONFIRM_REGISTRATION': (_('Thank you. Confirmation instructions have been sent to %(email)s.'), 'success'),
    'EMAIL_CONFIRMED': (_('Thank you. Your email has been confirmed.'), 'success'),
    'ALREADY_CONFIRMED': (_('Your email has already been confirmed.'), 'info'),
    'INVALID_CONFIRMATION_TOKEN': (_('Invalid confirmation token.'), 'error'),
    'EMAIL_ALREADY_ASSOCIATED': (_('%(email)s is already associated with an account.'), 'error'),
    'PASSWORD_MISMATCH': (_('Password does not match'), 'error'),
    'RETYPE_PASSWORD_MISMATCH': (_('Passwords do not match'), 'error'),
    'INVALID_REDIRECT': (_('Redirections outside the domain are forbidden'), 'error'),
    'PASSWORD_RESET_REQUEST': (_('Instructions to reset your password have been sent to %(email)s.'), 'info'),
    'PASSWORD_RESET_EXPIRED': (_('You did not reset your password within %(within)s. New instructions have been sent to %(email)s.'), 'error'),
    'INVALID_RESET_PASSWORD_TOKEN': (_('Invalid reset password token.'), 'error'),
    'CONFIRMATION_REQUIRED': (_('Email requires confirmation.'), 'error'),
    'CONFIRMATION_REQUEST': (_('Confirmation instructions have been sent to %(email)s.'), 'info'),
    'CONFIRMATION_EXPIRED': (_('You did not confirm your email within %(within)s. New instructions to confirm your email have been sent to %(email)s.'), 'error'),
    'LOGIN_EXPIRED': (_('You did not login within %(within)s. New instructions to login have been sent to %(email)s.'), 'error'),
    'LOGIN_EMAIL_SENT': (_('Instructions to login have been sent to %(email)s.'), 'success'),
    'INVALID_LOGIN_TOKEN': (_('Invalid login token.'), 'error'),
    'DISABLED_ACCOUNT': (_('Account is disabled.'), 'error'),
    'EMAIL_NOT_PROVIDED': (_('Email not provided'), 'error'),
    'INVALID_EMAIL_ADDRESS': (_('Invalid email address'), 'error'),
    'PASSWORD_NOT_PROVIDED': (_('Password not provided'), 'error'),
    'PASSWORD_INVALID_LENGTH': (_('Password must be at least 6 characters'), 'error'),
    'USER_DOES_NOT_EXIST': (_('Specified user does not exist'), 'error'),
    'INVALID_PASSWORD': (_('Invalid password'), 'error'),
    'PASSWORDLESS_LOGIN_SUCCESSFUL': (_('You have successfuly logged in.'), 'success'),
    'PASSWORD_RESET': (_('You successfully reset your password and you have been logged in automatically.'), 'success'),
    'PASSWORD_CHANGE': (_('You successfully changed your password.'), 'success'),
    'LOGIN': (_('Please log in to access this page.'), 'info'),
    'REFRESH': (_('Please reauthenticate to access this page.'), 'info'),
}

_field_labels = {
    'email': _('Email Address'),
    'password': _('Password'),
    'remember_me': _('Remember Me'),
    'login': _('Login'),
    'retype_password': _('Retype Password'),
    'register': _('Register'),
    'send_confirmation': _('Resend Confirmation Instructions'),
    'recover_password': _('Recover Password'),
    'reset_password': _('Reset Password'),
    'retype_password': _('Retype Password'),
    'new_password': _('New Password'),
    'change_password': _('Change Password'),
    'send_login_link': _('Send Login Link'),
}


globals().update([('MSG_' + k, v) for k, v in _messages.items()])
