# Generated by Django 4.0.3 on 2022-03-26 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]