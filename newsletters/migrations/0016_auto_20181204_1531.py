# Generated by Django 2.1.2 on 2018-12-04 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0015_auto_20181124_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettercomment',
            name='document_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='newsletters.Newsletter'),
        ),
        migrations.AlterField(
            model_name='newsletterlikes',
            name='document_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='newsletters.Newsletter'),
        ),
    ]
