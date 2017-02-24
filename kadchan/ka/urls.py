"""kadchan.ka URL Configuration"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.Info.as_view(), name="home"),  # view information of ka (Kiss Anime Video Downloader)
    url(r'^info', views.Info.as_view(), name="info"),  # view information of ka (Kiss Anime Video Downloader)
    # url(r'^downloads', None, name="downloads"),  # view current downloads and statuses
    # url(r'^updates', None, name="updates"),      # view updates of future downloads and new episodes and series
    # url(r'^search', None, name="search"),        # search without advertisements
    # url(r'^cron', None, name="cron"),            # run tasks via a cron task or task scheduling application
    # url(r'^api', None, name="api"),               # view API document
]