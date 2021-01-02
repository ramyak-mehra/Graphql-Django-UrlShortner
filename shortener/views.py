from django.shortcuts import get_object_or_404, redirect, render
from .models import URL
from django.contrib.auth.decorators import login_required
from .forms import CreateLinkForm
from django.contrib.sites.models import Site
from shorty.settings import WEBSITE_NAME

site_name = Site.objects.get_current().domain


def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicked()
    if url.is_flagged:
        context = {
            'site_name': site_name,
            'website_name': WEBSITE_NAME,
            'link': url.full_url
        }
        return render(request, 'denied.html',  context)
    else:
        return redirect(url.full_url)


@login_required
def createlink(request):

    if request.method == 'POST':
        full_url = request.POST.get('full_url', False)
        url_obj = False
        try:
            url_obj = URL.objects.get(full_url=full_url)
        except Exception:
            pass

        if url_obj:
            context = {
                'form': CreateLinkForm,
                'shortened_url': url_obj.shortened_url,
                'website_name': WEBSITE_NAME
            }
            return render(request, 'index.html', context)

        if form.is_valid():
            obj = form.save()
            context = {
                'form': CreateLinkForm,
                'shortened_url': obj.shortened_url,
                'website_name': WEBSITE_NAME
            }
            return render(request, 'index.html', context)
    context = {
        'form': CreateLinkForm,
        'website_name': WEBSITE_NAME
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'site_name': site_name,
        'website_name': WEBSITE_NAME
    }
    return render(request, 'about.html', context)
