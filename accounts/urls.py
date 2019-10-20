from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.homepage, name="home"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^edit/$', views.edit_profile, name="edit"),
    url(r'^registration_done/$', views.registration_done, name="registration_done"),
    url(r'^logout/$', views.logout_view, name="logout"),
]