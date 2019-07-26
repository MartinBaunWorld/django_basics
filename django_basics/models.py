from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


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
    path = models.CharField(
        max_length=128,
        help_text=(
            'URL of place to override seo elements. E.g. /something/here'
        )
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

    site = models.ForeignKey(
        'sites.Site',
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self, ):
        return self.html_title

    class Meta:
        unique_together = ['path', 'site']
        verbose_name = _('SEO')
        verbose_name_plural = _('SEOs')
