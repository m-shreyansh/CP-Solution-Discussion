# Generated by Django 3.1.7 on 2021-03-29 06:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_solution_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='liked_by',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None),
        ),
    ]
