from django.conf.urls import url, include
# from rest_framework import routers
from mainContent import views
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r'persons', views.PersonViewSet)

# router = routers.DefaultRouter()
# router.register(r'snippets/', views.snippet_list)
# router.register(r'snippets/(?P<page>\d+)/$', views.snippet_list)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'', include(router.urls)),
    url(r'snippets/', views.snippet_list),
    url(r'snippets/(?P<page>\d+)/$', views.snippet_detail),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
