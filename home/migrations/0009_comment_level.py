# Generated by Django 3.1.7 on 2021-03-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210329_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
