from django.db import models
from django.contrib.auth.models import User


class Executor(models.Model):
    """Модель исполнителя"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.user}, phone: {self.phone}'


class Service(models.Model):
    """Модель услуг исполнителя"""

    SERVICE_TYPES = [
        ('1', 'Веб разработка'),
        ('2', 'Маркетинг'),
        ('3', 'Копирайтинг'),
        ('4', 'Рерайтинг'),
        ('5', 'Переводы'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотографии'),
    ]

    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    service_type = models.CharField(choices=SERVICE_TYPES, default='1', max_length=1)

    def __str__(self):
        return f'{self.name}, {self.get_service_type_display()}, price: {self.price}'


class Customer(models.Model):
    """Модель заказчика"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.user}, phone: {self.phone}'


class Order(models.Model):
    """Модель услуг для заказа"""

    ORDER_TYPES = [
        ('1', 'Веб разработка'),
        ('2', 'Маркетинг'),
        ('3', 'Копирайтинг'),
        ('4', 'Рерайтинг'),
        ('5', 'Переводы'),
        ('6', 'Видеомонтаж'),
        ('7', 'Фотографии'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    service_type = models.CharField(choices=ORDER_TYPES, default='1', max_length=1)

    def __str__(self):
        return f'{self.name}, {self.get_service_type_display()}, price: {self.price}'


class Tag(models.Model):
    """Модель тэгов"""

    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)


class Ordering(models.Model):
    """Модель заказа"""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return f'{self.order_date}, {self.deadline}, Customer: {self.customer}, ' \
               f'Executor: {self.executor}'


class Message(models.Model):
    """Модель сообщений"""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    msg_date = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    message = models.CharField(max_length=1000)


class Ticket(models.Model):
    """Модель тикетов (жалоб)"""

    SEVERITIES = [
        ('1', 'Низкая'),
        ('2', 'Средняя'),
        ('3', 'Высокая'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    severity = models.CharField(choices=SEVERITIES, default='1', max_length=1)
    description = models.CharField(max_length=1000)
    ticket_date = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.get_severity_display()}, {self.ticket_date}, Is resolved? {self.is_resolved}'


class Review(models.Model):
    """Модель отзыва"""

    RATING_FILLED = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    ]

    rating = models.CharField(choices=RATING_FILLED, default='1', max_length=1)
    description = models.CharField(max_length=1000)


class Authoring(models.Model):
    """Модель составления отзыва"""

    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}, {self.review_date}'
