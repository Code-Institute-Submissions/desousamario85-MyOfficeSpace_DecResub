# Generated by Django 3.2.15 on 2022-09-06 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0014_auto_20220905_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_spaces_booked',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
