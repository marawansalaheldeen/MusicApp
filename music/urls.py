from django.conf.urls import url ,include
from . import views

app_name = 'music'


urlpatterns = [
    url(r'^$',views.msc,name="U_U"),
    #/music/
    url(r'^music/$',views.index,name="index"),

    #/music/id-num
    url(r'^music/(?P<album_id>[0-9]+)',views.detail,name="detail"),


    #/music/id-num/favorite
    url(r'^music/(?P<album_id>[0-9]+)/favorite',views.favorite,name="favorite"),


]
