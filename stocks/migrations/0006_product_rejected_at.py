# Generated by Django 4.2.4 on 2024-11-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_product_platform_comission'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rejected_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]