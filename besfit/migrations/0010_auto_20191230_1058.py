# Generated by Django 3.0.1 on 2019-12-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('besfit', '0009_auto_20191226_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='option4',
        ),
        migrations.AddField(
            model_name='questions',
            name='A',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='questions',
            name='B',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='questions',
            name='C',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='questions',
            name='D',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2),
        ),
    ]
