from django.urls import path

from pybo.views import index

urlpatterns = [path("", index)]
