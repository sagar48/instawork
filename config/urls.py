"""instawork_assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path

from instawork_assignment.members import views as member_view

urlpatterns = [
    # Fetch member list(GET), Create New Member(POST) APIs
    path('members/', member_view.MemberListCreateView.as_view(), name='member'),

    # Fetch member details(GET), Update member details, partial update(PUT, PATCH), Delete Member(DELETE) APIs
    path('members/<str:pk>/', member_view.MemberUpdateDeleteView.as_view(), name='member_update'),

    # Django Admin URL
    path(settings.ADMIN_URL, admin.site.urls),
]
