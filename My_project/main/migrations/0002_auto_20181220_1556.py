# Generated by Django 2.1.4 on 2018-12-20 10:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(blank=True, choices=[('C', 'Current_Account'), ('S', 'Saving_Account'), ('F', 'Fixed_Deposit'), ('R', 'Recurring_Deposit')], max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='mob',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(10)]),
        ),
    ]
