# Generated by Django 3.2 on 2022-08-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(max_length=1000),
        ),
    ]
