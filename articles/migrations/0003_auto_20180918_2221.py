# Generated by Django 2.1.1 on 2018-09-19 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_auto_20180917_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='author',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='document',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, related_name='document_modifiers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='document',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]