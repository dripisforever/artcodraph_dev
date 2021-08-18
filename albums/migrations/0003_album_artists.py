# Generated by Django 3.1.7 on 2021-05-08 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_auto_20210508_0229'),
        ('albums', '0002_auto_20210507_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(related_name='albums', to='artists.Artist'),
        ),
    ]
