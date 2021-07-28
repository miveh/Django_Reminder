from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Task(models.Model):
    class Meta:
        ordering = ('expired',)

    PRIORITY_CHOICES = [
        (0, 'unimportant'),
        (1, 'insignificant'),
        (2, 'important'),
        (3, 'Necessary'),
    ]
    STATUS_CHOICES = [
        ('deleted', 'deleted'),
        ('doing', 'doing'),
        ('done', 'done'),
        ('expire', 'expire'),
        ('archive', 'archive'),
    ]

    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, blank=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=0)
    category = models.ManyToManyField(Category, default='unknown')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='doing')
    expired = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'"{self.title}" on: {self.expired.date()}'

    def get_absolute_url(self):
        return reverse('detailview', args=[str(self.id)])
