import os

from django.core.management import BaseCommand
from users.models import User
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.com',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password(os.getenv('CSU_PASSWORD'))
        user.save()
