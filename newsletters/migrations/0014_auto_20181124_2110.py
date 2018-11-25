# Generated by Django 2.1.2 on 2018-11-25 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0013_auto_20181122_2047'),
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
