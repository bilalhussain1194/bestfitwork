# Generated by Django 3.0.1 on 2019-12-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('besfit', '0008_auto_20191218_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='correct_answer',
            field=models.CharField(max_length=2),
        ),
    ]
