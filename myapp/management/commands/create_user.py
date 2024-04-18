from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Create user"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('phone', type=str, help='User phone')
        parser.add_argument('address', type=str, help='User address')

    def handle(self, *args, **kwargs):
        user = User(
            name=kwargs['name'], 
            email=kwargs['email'],
            phone=kwargs['phone'], 
            address=kwargs['address'],
        )
        user.save()
        self.stdout.write(f'User {user.name} created with email {user.email}')
