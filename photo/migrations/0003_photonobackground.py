# Generated by Django 2.2.7 on 2019-12-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_remove_photo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoNoBackground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='photo/%Y/%m%d')),
            ],
        ),
    ]
