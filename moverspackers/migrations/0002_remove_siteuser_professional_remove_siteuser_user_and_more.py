# Generated by Django 4.2.6 on 2023-12-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moverspackers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteuser',
            name='professional',
        ),
        migrations.RemoveField(
            model_name='siteuser',
            name='user',
        ),
        migrations.AddField(
            model_name='siteuser',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
