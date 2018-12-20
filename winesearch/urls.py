
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('wines/', views.WineListView.as_view(), name='wine_list'),
    path('wines/<int:pk>/', views.WineDetailView.as_view(), name='wine_detail'),
    path('wines/<int:pk>/delete/', views.WineDeleteView.as_view(), name='wine_delete'),
    path('wines/<int:pk>/update/', views.WineUpdateView.as_view(), name='wine_update'),
    path('wines/new/', views.WineCreateView.as_view(), name='wine_new'),
    path('winery/', views.WineryListView.as_view(), name='winery_list'),
    path('winery/<int:pk>/', views.WineryDetailView.as_view(), name='winery'),
    path('wine_filter/', views.WineFilterView.as_view(), name='wine_filter'),

]

# ReverseMatch -->@method_decorator(login_required, name='dispatch')   refer to name='xxx'