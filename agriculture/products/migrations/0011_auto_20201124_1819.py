# Generated by Django 3.1.3 on 2020-11-24 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_customer_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]
