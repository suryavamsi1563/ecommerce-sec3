from django.conf.urls import url
from .views import (ProductListView,
                    # ProductDetailView,
                    ProductDetailSlugView,
                    # ProductfeaturedDetailView,
                    # ProductfeaturedListView
                    )


urlpatterns = [
    url(r'^$',ProductListView.as_view(),name='list'),
    # url(r'^products/(?P<pk>\d+)/$',ProductDetailView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view(),name='detail'),
    # url(r'^featured/$',ProductfeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$',ProductfeaturedDetailView.as_view())
]