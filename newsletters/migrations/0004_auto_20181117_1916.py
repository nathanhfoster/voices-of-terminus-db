# Generated by Django 2.1.2 on 2018-11-18 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0003_auto_20181117_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettercomment',
            name='document_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='newsletters.Newsletter'),
        ),
    ]
