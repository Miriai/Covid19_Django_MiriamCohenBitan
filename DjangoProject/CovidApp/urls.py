

from django.urls import path, re_path as url
from CovidApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^personalDetails$',views.PersonalDetailsAPI),
    url(r'^personalDetails/([0-9+])$',views.PersonalDetailsAPI),

    path('Excel', views.save_file),
]