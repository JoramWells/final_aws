from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('pepper', views.pepper, name='pepper'),
    path('tomato', views.tomato, name='tomato'),
    path('potato', views.potato, name='potato'),
    path('result', views.result, name='result'),
    path('tomato_result', views.tomato_result, name='tomato_result'),
    path('potato_result', views.potato_result, name='potato_result'),
    
]
