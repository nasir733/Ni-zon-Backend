"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/v1/ads/", include("ads.urls")),
    # path("api/v1/users/", include("users.urls")),

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/v1/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('sentry-debug/', trigger_error),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]



urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)


urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]