from django.db import models

NODE_TYPE = {
    ('factory', 'Завод'),
    ('retail_network', 'Розничная сеть'),
    ('entrepreneur', 'ИП')
}


class SupplierNode(models.Model):
    """Модель для описания узла в цепи поставщиков"""

    name = models.CharField(max_length=100, verbose_name='Название')
    type = models.CharField(max_length=30, choices=NODE_TYPE, verbose_name='Тип структуры')
    supplier = models.ForeignKey('SupplierNode', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Поставщик')
    debts = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    hierarchy_level = models.IntegerField(null=True, blank=True, verbose_name="Уровень иерархии")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.hierarchy_level = self.get_level()
        super(SupplierNode, self).save(*args, **kwargs)

    def get_level(self):
        """Функция получения уровня иерархии в цепи поставщиков"""

        if self.supplier is None:
            self.hierarchy_level = 0
        else:
            self.hierarchy_level = self.supplier.hierarchy_level + 1

        return self.hierarchy_level

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Contacts(models.Model):
    """Контакты, предоставляемые поставщиком"""

    supplier = models.ForeignKey('SupplierNode', on_delete=models.CASCADE, verbose_name='Поставщик',
                                 related_name='contacts')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}. {self.house}"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    """Модель продуктов, предоставляемых поставщиком"""

    supplier = models.ManyToManyField('SupplierNode', verbose_name='Сеть', related_name='products')
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Модель')
    release_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
