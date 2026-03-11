from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from enterprises.views import EnterpriseViewSet

router = DefaultRouter()
router.register(r"enterprises", EnterpriseViewSet)

default_version = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(default_version, include(router.urls)),
]
