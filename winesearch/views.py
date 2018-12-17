from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views import generic
from django.urls import reverse_lazy


from .models import Country
from .models import Province
from .models import Region1
from .models import Region2
from .models import Variety
from .models import Wine
from .models import Winery
from .models import Taster
#from .forms import HeritageSiteForm
#from .filters import HeritageSiteFilter


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from django_filters.views import FilterView



def index(request):
   return HttpResponse("Hello, world. You're at the Winesearch Sites index.")


#Take the template and displays: Non-dynamic content
class AboutPageView(generic.TemplateView):
    template_name = 'winesearch/about.html'


class HomePageView(generic.TemplateView):
    template_name = 'winesearch/home.html'