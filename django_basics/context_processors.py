from django.contrib.sites.shortcuts import get_current_site

from .models import SEO


def seo(request):
    site = get_current_site(request)
    seo = SEO.objects.filter(path=request.path, site=site).first()
    return {'seo': seo}
