from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('deletestu/<stroll>',views.deletestu,name='deletestu'),
    path('updatestu/<stroll>',views.updatestu,name='updatestu'),
    path('update/',views.update,name='update'),
]


