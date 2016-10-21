from django.conf.urls import url
from rango import views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^test1/',views.test1, name='test1'),
    url(r'^about/',views.about, name='about'),

]
