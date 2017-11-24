from django.conf.urls import url

from cards import views

urlpatterns = [
    url(r'^cards/$', views.CardList.as_view(), name='card-list'),
]