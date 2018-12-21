from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views import generic
from django.urls import reverse_lazy

from .models import Country, Province, Region1, Region2, Variety, Wine, Winery, Taster
from .forms import WineForm
from .filters import WineFilter
from .filters import WineryFilter

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django_filters.views import FilterView
from django.utils import timezone


def index(request):
   return HttpResponse("Hello, world. You're at the Winesearch Sites index.")


#Take the template and displays: Non-dynamic content
class AboutPageView(generic.TemplateView):
    template_name = 'winesearch/about.html'


class HomePageView(generic.TemplateView):
    template_name = 'winesearch/home.html'


#The SiteListView() class requires an ORM query that retrieves all Winesearch records.
#all_entries = Entry.objects.all()
class WineListView(generic.ListView):
    model = Wine
    context_object_name = 'wines'
    template_name = 'winesearch/wine_list.html'
    paginate_by = 4000

    #def dispatch(self, *args, **kwargs):
        #return super().dispatch(*args, **kwargs)
    # .select_related can only work with Foreignkey

    def get_queryset(self):
        return Wine.objects.select_related('winery').order_by('wine')


#@method_decorator(login_required, name='dispatch')
class WineDetailView(generic.DetailView):
    model = Wine
    context_object_name = 'wine'
    template_name = 'winesearch/wine_detail.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Wine.objects \
            .select_related('country', 'province', 'region1', 'region2', 'variety') \
            .order_by('wine')


@method_decorator(login_required, name='dispatch')
class WineryListView(generic.ListView):
    model = Winery
    context_object_name = 'wineries'
    template_name = 'winesearch/winery_list.html'
    paginate_by = 1000

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Winery.objects \
            .order_by('winery_name')


@method_decorator(login_required, name='dispatch')
class WineryDetailView(generic.DetailView):
    model = Winery
    context_object_name = 'winery'
    template_name = 'winesearch/winery_detail.html'


    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Winery.objects \
            .order_by('winery_name')




@method_decorator(login_required, name='dispatch')
class WineCreateView(generic.CreateView):
    model = Wine
    form_class = WineForm
    success_message = "Wine created successfully"
    template_name = 'winesearch/wine_new.html'


    # fields = '__all__' <-- superseded by form_class]
    #  success_url = reverse_lazy('wines/wine_list')

    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
    #
    # def post(self, request):
    #     form = WineForm(request.POST)
    #     if form.is_valid():
    #         wine = form.save(commit=False)
    #         wine.save()
    #         return render(request, 'winesearch/wine_new.html', {'form': form})
    #
    # def get(self, request):
    #     form = WineForm()
    #     return render(request, 'winesearch/wine_new.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class WineUpdateView(generic.UpdateView):
    model = Wine
    form_class = WineForm
    # fields = '__all__' <-- superseded by form_class
    context_object_name = 'wine'
    #pk_url_kwarg = 'wine_pk'
    success_message = "Wine updated successfully"
    template_name = 'winesearch/wine_update.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
            wine = form.save(commit=False)
            wine.updated_by = self.request.user
            wine.updated_at = timezone.now()
            wine.save()
            return render(self.request, 'winesearch/wine_update.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class WineDeleteView(generic.DeleteView):
    model = Wine
    success_message = "Wine deleted successfully"
    success_url = reverse_lazy('wine_list')
    context_object_name = 'wine'
    template_name = 'winesearch/wine_delete.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



class PaginatedFilterView(generic.View):
    def get_context_data(self, **kwargs):
        context = super(PaginatedFilterView, self).get_context_data(**kwargs)
        if self.request.GET:
            querystring = self.request.GET.copy()
            if self.request.GET.get('page'):
                del querystring['page']
            context['querystring'] = querystring.urlencode()
        return context


class WineFilterView(PaginatedFilterView, FilterView):
    model = Wine
    #form_class = SearchForm
    filterset_class = WineFilter
    context_object_name = 'wine_list'
    template_name = 'winesearch/wine_filter.html'
    paginate_by = 4000


class WineryFilterView(PaginatedFilterView, FilterView):
    model = Winery
    #form_class = SearchForm
    filterset_class = WineryFilter
    context_object_name = 'winery_list'
    template_name = 'winesearch/winery_filter.html'
    paginate_by = 4000
