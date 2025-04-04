# Generated by Django 3.2.25 on 2025-03-29 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='data_envio',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='arquivo',
            name='arquivo',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='arquivo',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
