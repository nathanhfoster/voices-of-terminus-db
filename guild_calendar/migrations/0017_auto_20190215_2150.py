# Generated by Django 2.1.7 on 2019-02-16 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guild_calendar', '0016_auto_20190215_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgroupmember',
            name='filled',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventGroupMemberAuthorName', to='user.Character'),
        ),
    ]