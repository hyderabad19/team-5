from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from learnovate import views

urlpatterns = []

urlpatterns = [
    url(r'^learnovate/', include('learnovate.urls', namespace='learnovate')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]





# urlpatterns = [
#     url(r'^learnovate/', include(('learnovate.urls', 'learnovate'), namespace='learnovate')),
#     path('admin/', admin.site.urls),
#     path('accounts/', include('django.contrib.auth.urls')),
#     url('teacher/register', views.TeacherSignUpView.as_view(), name='register'),
# ]
#
#
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += [
#
# ]