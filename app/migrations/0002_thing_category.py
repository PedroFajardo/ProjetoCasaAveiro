# Generated by Django 2.1.7 on 2019-03-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='category',
            field=models.CharField(default='Fruta', max_length=30),
            preserve_default=False,
        ),
    ]
