from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from authentication.views import UserListCreateAPIView
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^api/v1/auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/v1/users/', UserListCreateAPIView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', TemplateView.as_view(template_name='index.html')),
)
