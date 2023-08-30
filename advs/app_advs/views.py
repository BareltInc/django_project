from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .models import Advertisement
from .forms import AdvertisementForm


def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__contains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements, 'title': title}
    return render(request, 'app_advs/index.html', context=context)

def top_sellers(request):
    return render(request, 'app_advs/top-sellers.html')


@login_required(login_url=reverse_lazy('login'))
def adv_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            # advertisement.user = User.objects.all()[0]
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    if request.method == "GET":
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advs/advertisement-post.html', context=context)


@login_required(login_url=reverse_lazy('login'))
def adv(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {'advertisement': advertisement}
    return render(request, 'app_advs/advertisement.html', context=context)