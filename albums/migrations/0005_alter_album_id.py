# Generated by Django 3.2.3 on 2021-06-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_auto_20210531_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
