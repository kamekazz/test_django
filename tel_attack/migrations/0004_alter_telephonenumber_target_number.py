# Generated by Django 3.2.5 on 2022-07-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tel_attack', '0003_alter_attack_text_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telephonenumber',
            name='target_number',
            field=models.CharField(max_length=10),
        ),
    ]
