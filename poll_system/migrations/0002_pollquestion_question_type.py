# Generated by Django 2.1.2 on 2019-01-19 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollquestion',
            name='question_type',
            field=models.CharField(default='Multiple', max_length=28),
        ),
    ]
