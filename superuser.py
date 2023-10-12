import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studybud.settings")
django.setup()

from base.models import User  # Assuming your custom user model is in the 'base' app

username = "admin"
email = "admin@gmail.com"
password = "your_password_here"

user, created = User.objects.get_or_create(username=username, email=email)
if created:
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print(f'Superuser "{username}" created successfully!')
else:
    print(f'Superuser "{username}" already exists.')
