from django.contrib import admin
from django.urls import path,include
from faculty import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('faculty.urls')),
    path('',views.home,name="home"),
]
