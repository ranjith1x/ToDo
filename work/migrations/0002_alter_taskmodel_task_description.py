# Generated by Django 5.0.3 on 2024-04-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='task_description',
            field=models.TextField(null=True),
        ),
    ]