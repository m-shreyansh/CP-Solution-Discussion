# Generated by Django 3.1.7 on 2021-03-29 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210329_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='top',
        ),
        migrations.AddField(
            model_name='comment',
            name='last_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_last_comment', to='home.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='next_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_next_comment', to='home.comment'),
        ),
    ]