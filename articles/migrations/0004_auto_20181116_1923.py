# Generated by Django 2.1.2 on 2018-11-17 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20181116_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('last_modified',), 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='articlecomment',
            options={'ordering': ('last_modified',), 'verbose_name': 'Article Comment', 'verbose_name_plural': 'Article Comments'},
        ),
    ]