# Generated by Django 2.2.5 on 2021-03-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20200811_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='How many people will be staying?'),
        ),
    ]
