# Generated by Django 2.1.7 on 2019-04-19 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll_system', '0018_poll_private'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='private',
            new_name='is_private',
        ),
    ]
