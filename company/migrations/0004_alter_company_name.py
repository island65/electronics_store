# Generated by Django 5.1.1 on 2024-09-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='название'),
        ),
    ]
