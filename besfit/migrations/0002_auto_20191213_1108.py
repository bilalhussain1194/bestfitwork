# Generated by Django 2.2.5 on 2019-12-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('besfit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='correct_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='question_attempt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='total_questions',
            field=models.IntegerField(default=0),
        ),
    ]
