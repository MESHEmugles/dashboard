# Generated by Django 5.0.3 on 2024-03-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_task_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
