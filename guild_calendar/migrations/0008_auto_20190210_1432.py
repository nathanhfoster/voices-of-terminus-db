# Generated by Django 2.1.4 on 2019-02-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guild_calendar', '0007_auto_20190208_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventgroupmember',
            name='class_preferences',
        ),
        migrations.RemoveField(
            model_name='eventgroupmember',
            name='role_preferences',
        ),
        migrations.AddField(
            model_name='eventgroupmember',
            name='role_class_preferences',
            field=models.TextField(blank=True, null=True),
        ),
    ]