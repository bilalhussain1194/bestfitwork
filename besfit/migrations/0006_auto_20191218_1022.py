# Generated by Django 2.2.5 on 2019-12-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('besfit', '0005_auto_20191218_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='correct_answer2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='correct_answer3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
