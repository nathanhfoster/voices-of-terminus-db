# Generated by Django 2.1.1 on 2018-09-25 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(null=True)),
                ('body', models.TextField()),
                ('tags', models.CharField(blank=True, max_length=128)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, related_name='author_name', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, related_name='document_modifiers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
