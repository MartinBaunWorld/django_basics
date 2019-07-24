from django.db import models
from django.utils import timezone


class CoreModel(models.Model):
    created = models.DateTimeField(
        'Created',
        editable=False,
        null=False,
        blank=False,
    )

    updated = models.DateTimeField(
        'Updated',
        editable=False,
        null=False,
        blank=False,
    )

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(CoreModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['updated']


class SEO(CoreModel):
    title = models.CharField(
        max_length=256,
        blank=True
    )
    html_title = models.CharField(
        blank=True,
        max_length=120,
    )
    meta_description = models.TextField(
        blank=True,
        help_text='Recommended length is 120-160 chars',
    )
    meta_keywords = models.TextField(
        blank=True,
    )
    path = models.CharField(max_length=128)

    def __str__(self, ):
        return self.title
