from django.contrib import admin
from django.urls import path,include
from myapp import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin.urls')),
    path('',views.home,name="home"),
]
