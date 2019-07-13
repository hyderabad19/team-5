"""learnovate_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from learnovate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url('teacher/register', views.TeacherSignUpView.as_view(), name='register'),
    url('playone/<int:resource_id>', views.viewVideo, name='play-video'),
    url('playall/', views.viewAllVideos, name='play-videos'),
    url('viewpdf/<int:resource_id>', views.viewPDF, name='view-pdf'),
    url('viewallpdfs/', views.viewAllPDFs, name='view-all-pdfs'),
    path('like/<int:resource_id>/', views.like, name = "like"),
    path('comment/<int:resource_id>/', views.comment, name = "comment"),
    #url('^onevideo$', views.view_all_resources, name = "view_all_resources"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url('', views.homeView, name='home'),
]