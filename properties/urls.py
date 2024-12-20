"""
URL configuration for properties project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView # Import TemplateView
from django.conf import settings # Import settings 
from django.conf.urls.static import static # Import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home/index.html'), name='home'), # Home page # Serve index.html at the root URL
    path('listings/', include(('listings.urls', 'listings'), namespace='listings')),# Include listings app URLs with namespace
    path('users/', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('profiles/', include('profiles.urls')),
    path('bookings/', include('bookings.urls')),  # Include bookings app URLs
    path('profiles/', include('profiles.urls')),
    path('pages/',include('pages.urls')), # Contact form URL
] + static (settings.MEDIA_URL, document_root =settings.MEDIA_ROOT) #go to settings.py
    #if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)