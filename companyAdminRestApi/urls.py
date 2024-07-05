"""
URL configuration for companyAdminRestApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from main import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('account',views.AccountViewSet)
router.register('organization',views.OrganizationViewSet)
router.register('contact',views.ContactViewSet)
router.register('invoice',views.InvoiceViewSet)
router.register('role',views.RoleViewSet)
router.register('useraccount',views.UserAccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accountServices/',include(router.urls)),
]
