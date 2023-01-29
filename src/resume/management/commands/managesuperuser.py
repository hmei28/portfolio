from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    """
    Create a superuser if none exist. Update password user if changed. Not return error if exist
    Example:
        manage.py managesuperuser --user=admin --password=changeme or use env 
    """
    
    def add_arguments(self, parser):
        parser.add_argument("--user", default=os.environ.get('DJANGO_SUPERUSER_USERNAME'))
        parser.add_argument("--password", default=os.environ.get('DJANGO_SUPERUSER_PASSWORD'))
        parser.add_argument("--email", default=os.environ.get('DJANGO_SUPERUSER_EMAIL'))
 

    def handle(self, *args, **options):
        
        username = options["user"]
        password = options["password"]
        email = options["email"]

        if get_user_model().objects.filter(username=username).exists():

            get_user = get_user_model().objects.get(username = username)
            if get_user.check_password(password):
                self.stdout.write(f'User {username} already exist ')
                return
            else:
                try:
                    get_user.set_password(password)
                    get_user.save()
                    self.stdout.write(f'Password of user "{username}" was updated ')
                except Exception as e: 
                    self.stdout.write(f'Err : {e.message}')
                    return
        else:
            get_user_model().objects.create_superuser(username=username, password=password, email=email)
            self.stdout.write(f'User "{username}" was created')