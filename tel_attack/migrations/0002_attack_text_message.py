# Generated by Django 3.2.5 on 2022-07-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tel_attack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='text_message',
            field=models.CharField(default='hi', max_length=200),
        ),
    ]
