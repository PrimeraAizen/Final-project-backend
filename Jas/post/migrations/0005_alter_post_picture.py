# Generated by Django 4.1.3 on 2023-05-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to='images/post/', verbose_name='Picture'),
        ),
    ]
