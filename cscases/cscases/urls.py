"""
URL configuration for cscases project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from cases import views as case_views
from roket import views as roket_views
from contracts import views as contract_views

urlpatterns = [
    path('test/', case_views.test),
    path("open/", case_views.open_case),
    path("append_case/", case_views.append_case),
    path("win_roket/", roket_views.win_in_roket),
    path("lose_roket/", roket_views.lose_in_roket),
    path("csrf/", roket_views.get_csrf),
    path("add_contract_item", contract_views.insert_item_to_contract),
    path("contract", contract_views.start_contract)
]
