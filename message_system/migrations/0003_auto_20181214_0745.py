# Generated by Django 2.1.4 on 2018-12-14 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message_system', '0002_auto_20181214_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='groupAuthorName', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='uri',
            field=models.CharField(default=1, max_length=280),
            preserve_default=False,
        ),
    ]
