# Generated by Django 2.1.2 on 2019-01-28 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-date_created',), 'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='usergroup',
            options={'ordering': ('-date_created',), 'verbose_name': 'UserGroup', 'verbose_name_plural': 'UserGroups'},
        ),
    ]
