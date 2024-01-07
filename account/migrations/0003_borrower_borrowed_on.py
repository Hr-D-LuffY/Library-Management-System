# Generated by Django 4.2.7 on 2024-01-07 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='borrowed_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
