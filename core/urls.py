from django.conf.urls import url,include
from django.contrib import admin
from django.core.urlresolvers import reverse


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('django.contrib.auth.urls'), name="logout"),
    url(r'',include('journal.urls')),
]
