from django.db import models

node_type = {
    ('factory', 'завод'),
    ('retail_network', 'розничная сеть'),
    ('entrepreneur', 'ИП')
}


class NetworkNode(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    type = models.CharField(max_length=30, choices=node_type, verbose_name='Тип структуры')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='Поставщик')
    debts = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Звено'
        verbose_name_plural = 'Звенья'


class Product(models.Model):
    Node = models.ForeignKey(NetworkNode, on_delete=models.CASCADE, related_name='Сеть')
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
