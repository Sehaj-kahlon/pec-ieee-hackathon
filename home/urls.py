from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [

    # path('index', views.index, name = 'index'),

    path("", views.index),
    path('index', views.index, name = 'index'),
    # change
    # path('admin/', admin.site.urls),
    # path('', include('views.index')),
    # # new
    # # path('', views.challenge2),
    path('contact', views.contact),
    path('tutorial', views.tutorial),
]
