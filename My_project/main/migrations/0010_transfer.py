# Generated by Django 2.1.4 on 2018-12-25 12:19

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_debit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(500)])),
                ('description', models.CharField(default='Transfer', max_length=100)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
        ),
    ]
