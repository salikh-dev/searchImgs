# Generated by Django 4.0.6 on 2022-09-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0020_alter_post_creat_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creat_time',
            field=models.IntegerField(default='13:21:35'),
        ),
    ]