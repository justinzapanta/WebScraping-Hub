# Generated by Django 4.2.5 on 2024-04-13 00:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_view', '0002_alter_user_subscription_subscription_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_subscription',
            name='subscription_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
