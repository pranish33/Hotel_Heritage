# Generated by Django 4.1.7 on 2023-02-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0004_alter_rating_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]