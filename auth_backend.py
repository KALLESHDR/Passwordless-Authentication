from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class PasswordlessAuthBackend(ModelBackend):
    """Log in to Django without providing a password.
    """
    def authenticate(self, request, email):
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
            
            
from twilio.rest import Client
from django.conf import settings
class SendOTP:
    def send_code(receiver):
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        client = Client(account_sid, auth_token)

        verification = client.verify \
                     .services(settings.SERVICE_ID) \
                     .verifications \
                      .create(channel_configuration={
                           'template_id': settings.TEMPLATE_ID,
                           'from': settings.DEFAULT_FROM_EMAIL,
                           'from_name': 'Ashi Garg'
                       }, to=receiver, channel='email')

        return verification.status