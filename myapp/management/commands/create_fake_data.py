from django.core.management.base import BaseCommand
from myapp.models import User, Product, Order


class Command(BaseCommand):
    help = "Fill the database with predefined data"

    def handle(self, *args, **kwargs):

        # Создаем 10 пользователей
        for i in range(1, 11):
            user = User.objects.create(
                name=f"user{i}",
                email=f"user{i}@example.com",
                phone=f"12345678{i}",
                address=f"Address {i}"
            )
            user.save()

        self.stdout.write(self.style.SUCCESS('10 User records created successfully.'))

        # Создаем 20 продуктов
        for i in range(1, 21):
            Product.objects.create(
                name=f"Product{i}",
                description=f"Description for product {i}",
                price=i * 10,
                quantity=i * 2
            )

        self.stdout.write(self.style.SUCCESS('20 Product records created successfully.'))

        # Создаем 30 заказов
        users = User.objects.all()
        products = Product.objects.all()

        for i in range(1, 31):
            customer = users[i % len(users)]
            selected_products = products[(i - 1) % len(products):(i + 4) % len(products)]

            total_price = sum(product.price for product in selected_products)

            order = Order.objects.create(
                customer=customer,
                total_price=total_price
            )
            order.products.set(selected_products)

        self.stdout.write(self.style.SUCCESS('30 Order records created successfully.'))
