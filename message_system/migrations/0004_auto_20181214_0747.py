# Generated by Django 2.1.4 on 2018-12-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_system', '0003_auto_20181214_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='uri',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
    ]