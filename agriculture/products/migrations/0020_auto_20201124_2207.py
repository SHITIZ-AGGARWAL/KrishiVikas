# Generated by Django 3.1.3 on 2020-11-24 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20201124_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(default='New Delhi', max_length=255)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.jpg', null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.vendor'),
        ),
    ]
