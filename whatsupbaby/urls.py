"""whatsupbaby URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rodzic/login/$', 'rodzic.views.login'),
    url(r'^rodzic/auth/$', 'rodzic.views.auth_view'),
    url(r'^rodzic/logout/$', 'rodzic.views.logout'),
    url(r'^rodzic/loggedin/$', 'rodzic.views.loggedin'),
    url(r'^rodzic/invalid/$', 'rodzic.views.invalid_login'),
    url(r'^opiekun/loggedin/$', 'opiekun.views.loggedin'),
    url(r'^tablica/', 'tablica.views.posty'),
]
