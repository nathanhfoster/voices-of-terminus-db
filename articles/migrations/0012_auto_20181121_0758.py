# Generated by Django 2.1.2 on 2018-11-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20181117_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(default='Article', max_length=128),
        ),
    ]
