# Generated by Django 2.1.7 on 2019-05-08 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(default='Report', max_length=512),
        ),
    ]