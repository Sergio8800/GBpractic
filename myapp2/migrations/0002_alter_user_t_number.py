# Generated by Django 5.0.4 on 2024-05-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='t_number',
            field=models.CharField(max_length=15),
        ),
    ]