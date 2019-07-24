from django.contrib import admin
from .models import SEO


class SEOAdmin(admin.ModelAdmin):
    list_display = ('path', 'title', 'html_title', 'site')


admin.site.register(SEO, SEOAdmin)
