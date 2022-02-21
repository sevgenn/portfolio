from django.urls import path, re_path
import mainapp.views as mainapp_views


app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp_views.main, name='main'),
    re_path(r'^category/(?P<pk>\d+)/$', mainapp_views.categories, name='category'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp_views.categories, name='page'),
    re_path('^recipe/(?P<pk>\d+)/$', mainapp_views.recipe, name='recipe'),
]
