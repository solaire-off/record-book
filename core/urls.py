from django.conf.urls import url,include
from django.contrib import admin
from django.core.urlresolvers import reverse
from rest_framework import routers
from journal.views import StudentViewSet, SubjectViewSet, MarkViewSet

# Router for API view
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('journal.urls')),
    url(r'', include('django.contrib.auth.urls'), name="logout"),
    url(r'^', include(router.urls)),
    url(r'^marks/', MarkViewSet.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
