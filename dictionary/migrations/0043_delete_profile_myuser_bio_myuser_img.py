# Generated by Django 4.0.6 on 2022-08-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0042_profile_remove_myuser_bio_remove_myuser_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='myuser',
            name='bio',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
