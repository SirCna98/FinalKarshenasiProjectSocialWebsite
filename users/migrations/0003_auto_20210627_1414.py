# Generated by Django 3.1.3 on 2021-06-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.gif', upload_to='profile_pics'),
        ),
    ]