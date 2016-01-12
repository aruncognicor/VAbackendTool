from django.conf.urls import patterns, include, url

from .views import HomeView,FetchView,LaunchView

urlpatterns = patterns('',
	url(r'^$',HomeView.as_view(),name='home_view',),

	url(r'^fetch_parmeters/',FetchView.as_view(),name='fetch_view',),
	url(r'^launchva/',LaunchView.as_view(),name='launch_view',),
)