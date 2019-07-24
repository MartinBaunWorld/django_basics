from .models import SEO


def seo(request):
    seo = SEO.objects.filter(path=request.path).first()
    return {'seo': seo}
