# Generated by Django 2.1.1 on 2018-10-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20181025_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='images/default.png', upload_to='images/profiles'),
        ),
    ]
