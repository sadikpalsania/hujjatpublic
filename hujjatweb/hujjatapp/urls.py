from django.conf import settings
from django.urls import path
from .import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Hujjat Form"),
    path('thanks', views.submit, name='Thanks'),
    path('educational', views.educational, name='Educational'),
    path('medical', views.medical, name='Medical'),
    path('samajik', views.samajik, name='Samajik'),
    path('pardes', views.pardes, name='Pardes'),
    path('any', views.any, name='Any'),
    path('datalogin', views.datalogin, name='Datalogin'),
    path('daan', views.daan, name='Daan'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)