# Generated by Django 2.1.1 on 2018-10-14 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_document_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='date_modified',
        ),
    ]