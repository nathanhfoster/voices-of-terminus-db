# Generated by Django 2.1.2 on 2018-11-18 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0007_auto_20181117_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='articles.Article')),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articleLikesModifier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article Like',
                'verbose_name_plural': 'Articles Likes',
                'ordering': ('-last_modified',),
            },
        ),
    ]
