# Generated by Django 5.0.2 on 2024-02-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='time_purchased',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
