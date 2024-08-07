from django.conf import settings
from django.core.mail import send_mail


def send_email_for_newsletter(email):
    send_mail(
        "Сообщение с сайта dj-fitness",
        f"Вы успешно подписались на наши рассылки новостей",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
