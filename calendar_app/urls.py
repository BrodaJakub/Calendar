"""
URL configuration for calendar_app project.

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
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.contrib.auth.views import LoginView, LogoutView # type: ignore
from calendar_module.views import add_event, home, event_detail, edit_event, delete_event

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add-event/', add_event, name='add_event'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('event/<int:event_id>/edit/', edit_event, name='edit_event'),
    path('event/<int:event_id>/delete/', delete_event, name='delete_event'),
]
