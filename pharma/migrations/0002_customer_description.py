# Generated by Django 3.1.3 on 2020-11-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
