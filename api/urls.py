from django.urls import path,include
from . import views
urlpatterns = [
        path('', views.getRoutes, name="routes"),
        path('add_name',views.add_name),
        path('check_name',views.check_name)
]