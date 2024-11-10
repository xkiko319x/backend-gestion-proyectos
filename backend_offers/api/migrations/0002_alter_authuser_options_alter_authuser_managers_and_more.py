# Generated by Django 5.1.2 on 2024-10-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='authuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='last_name',
        ),
        migrations.AddField(
            model_name='authuser',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]