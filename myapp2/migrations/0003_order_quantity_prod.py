# Generated by Django 5.0.4 on 2024-05-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_alter_user_t_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity_prod',
            field=models.IntegerField(default=1),
        ),
    ]