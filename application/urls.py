"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls import url, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profiles', views.ProfileViewSet)

from chat import views

router.register(r'chats', views.ChatViewSet)

from like import views

router.register(r'likes', views.LikeViewSet)

from message import views
router.register(r'messages', views.MessageViewSet)

from pet import views
router.register(r'pets', views.PetViewSet)

from post import views
router.register(r'posts', views.PostViewSet)

from django.contrib.auth.views import logout, login

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^auth/$', login, {'template_name': 'login.html'}, name="auth"),
]
