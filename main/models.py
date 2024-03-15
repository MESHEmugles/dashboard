from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

STATUS_CHOICES = [
    ('urgent', 'Urgent'),
    ('progress', 'Progress'),
    ('on_hold', 'On Hold'),
    ('completed', 'Completed')
]
PRIORITY_CHOICES = [
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High'),
    (4, 'Critical')
]


class Project(models.Model):
    name = models.CharField(max_length = 100, null = True, blank = True)
    slug = models.SlugField(unique = True, blank=True, null=True)
    img = models.ImageField(upload_to='project',
    default='', null = True, blank= True
    )
    image = CloudinaryField(overwrite= True, format= 'jpg', blank=True, null=True)
    status = models.CharField(max_length = 20, choices=STATUS_CHOICES, default='progress')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = ("Project")
        ordering = ["-created",]
    


class Task(models.Model):
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE, null=True, blank=True)
    proj = models.ForeignKey(Project, related_name = 'tasks', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length = 100, null = True, blank = True)
    slug = models.SlugField(unique = True, blank=True, null=True)
    img = models.ImageField(upload_to='task',
    default='img/avatar.jpg', null = True, blank= True
    )
    due_date = models.DateTimeField(null = True, blank = True)
    text =  RichTextField(null= True, blank=True)
    priority = models.PositiveIntegerField(choices=PRIORITY_CHOICES, default=2)
    iscompleted = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='progress')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = ("Task")
        ordering = ["priority",]
    

