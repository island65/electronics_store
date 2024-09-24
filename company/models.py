from django.db import models

from user.models import Users

SUPPLIERS_CHOICE = [('individual', 'ИП'), ('manufacture', 'завод'), ('retail', 'розница'), ]
NULLABLE = {'blank': True, 'null': True}


class Company(models.Model):
    name = models.CharField(unique=True, max_length=255, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='эл.почта')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    number_bld = models.CharField(max_length=50, verbose_name='номер дома')
    level = models.IntegerField(default=0, verbose_name='уровень')
    company_type = models.CharField(max_length=30, choices=SUPPLIERS_CHOICE, verbose_name='тип компании')
    suppliers_name = models.CharField(max_length=150, verbose_name='название поставщика', **NULLABLE)
    supplier_id = models.IntegerField(verbose_name='id поставщика', **NULLABLE)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='владелец компании', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название компании"
        verbose_name_plural = "Названия компаний"


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=150, verbose_name='название поставщика', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='задолженность')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    customer = models.IntegerField(verbose_name='заказчик')
    supplier = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='поставщик')
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='владелец поставщика', **NULLABLE)

    def __str__(self):
        return self.supplier_name

    class Meta:
        verbose_name = "поставщик"
        verbose_name_plural = "поставщики"
