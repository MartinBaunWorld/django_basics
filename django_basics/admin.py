from django.contrib import admin
from .models import SEO


class SEOAdmin(admin.ModelAdmin):
    list_display = ('title', 'path')


admin.site.register(SEO, SEOAdmin)
