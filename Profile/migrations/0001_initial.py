# Generated by Django 5.1.3 on 2024-11-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='user_name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone_number', models.CharField(max_length=50, verbose_name=' phone_number')),
            ],
        ),
    ]