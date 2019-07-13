from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from learnovate import views


urlpatterns = [
    url('viewallresources/', views.viewAll, name='viewAll'),
    url('viewspecificresource/<int:resource_id>', views.viewOne, name='viewOne'),
    path('like/<int:resource_id>/', views.like, name = "like"),
    path('comment/<int:resource_id>/', views.comment, name = "comment"),
    #url('^onevideo$', views.view_all_resources, name = "view_all_resources"),
]



urlpatterns += [
    url('', views.homeView, name='home'),
]