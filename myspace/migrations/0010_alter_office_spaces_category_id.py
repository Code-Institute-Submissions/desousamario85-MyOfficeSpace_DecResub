# Generated by Django 3.2.15 on 2022-08-27 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0009_auto_20220827_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_spaces',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='myspace.category'),
        ),
    ]
