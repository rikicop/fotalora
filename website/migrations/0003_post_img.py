# Generated by Django 2.2 on 2021-05-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]