# Generated by Django 5.0.3 on 2024-03-13 11:51

import ckeditor.fields
import cloudinary.models
import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('img', models.ImageField(blank=True, default='', null=True, upload_to='project')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('urgent', 'Urgent'), ('progress', 'Progress'), ('on_hold', 'On Hold'), ('completed', 'Completed')], default='progress', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Project',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('due_date', models.DateTimeField()),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('priority', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Critical')], default=2)),
                ('iscompleted', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('urgent', 'Urgent'), ('progress', 'Progress'), ('on_hold', 'On Hold'), ('completed', 'Completed')], default='progress', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('proj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.project')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Task',
                'ordering': ['priority'],
            },
        ),
    ]