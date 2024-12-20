from django.urls import path
from django.views.generic import TemplateView

from .views import contact_view, about_view, blog_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),  # URL for the contact form
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),  # Success page
    path('about/', about_view, name='about'),  # URL for the about page
    path('blog/', blog_view, name='blog'),
    path('faq/', TemplateView.as_view(template_name='faq.html'), name='faq'),

]