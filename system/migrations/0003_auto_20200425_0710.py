# Generated by Django 3.0.2 on 2020-04-25 07:10

from django.db import migrations, models
import system.models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20200425_0630'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', system.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
