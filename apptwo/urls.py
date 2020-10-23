from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='apptwo'

urlpatterns = [
path('admin/', admin.site.urls),
path('',views.Homes1.as_view(),name='Homes1'),
path('<pk>',views.Details.as_view(),name='Details'),
]
