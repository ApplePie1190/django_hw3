from django.core.management.base import BaseCommand
from myapp.models import User, Product, Order


class Command(BaseCommand):
    help = "Delete all data from the database"

    def handle(self, *args, **kwargs):
        try:
            # Удаление всех объектов из модели CustomUser
            User.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All CustomUser data deleted successfully.'))

            # Удаление всех объектов из модели Product
            Product.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All Product data deleted successfully.'))

            # Удаление всех объектов из модели Order
            Order.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All Order data deleted successfully.'))

            self.stdout.write(self.style.SUCCESS('All data in the database has been deleted successfully.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error deleting data: {e}'))
