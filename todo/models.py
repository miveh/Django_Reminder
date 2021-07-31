import datetime

from django.db import models

# Create your models here.
from django.urls import reverse


class CategoryManager(models.Manager):
    def get_null_category(self):
        null_category = Category.objects.filter(task__isnull=True)
        return null_category

    def get_notnull_category(self):
        not_null_category = Category.objects.exclude(task__isnull=True)
        return not_null_category


class TaskManager(models.Manager):


    def get_expired_task(self):
        """
        :return: all of expired tasks.
        """
        dt2 = datetime.datetime.now()
        tasks = Task.objects.all()
        expired_tasks = []
        for task in tasks:
            if (task.expired.replace(tzinfo=None) - dt2).days <= 0:
                expired_tasks.append(task)
        return expired_tasks

    def get_notexpired_task(self):
        """
        :return: all of not expired tasks.
        """
        dt2 = datetime.datetime.now()
        tasks = Task.objects.all()
        notexpired_tasks = []
        for task in tasks:
            if (task.expired.replace(tzinfo=None) - dt2).days > 0:
                notexpired_tasks.append(task)
        return notexpired_tasks


class Category(models.Model):
    """
    Each category have just a title.
    """
    title = models.CharField(max_length=20)
    objects = CategoryManager()

    def __str__(self):
        return f'{self.id}-{self.title}'

    def get_absolute_url(self):
        return reverse('catdetail', args=[str(self.id)])


class Task(models.Model):
    """
    Each task have a multiple categories.
    """

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
    objects = TaskManager()

    def __str__(self):
        return f'"{self.title}" status: {self.status}'

    def get_absolute_url(self):
        return reverse('detailview', args=[str(self.id)])
