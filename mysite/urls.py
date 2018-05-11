from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import UserRegisterView, UserRegisterDoneView
# from .views import HomeView
from . import views
urlpatterns = [
    # url(r'^$', HomeView.as_view(), name='home'),
    url(r'^$', views.HomeView, name='home'),
    url(r'^product/', include('board.urls', namespace='product')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserRegisterView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserRegisterDoneView.as_view(), name='register_done'),
    url(r'^admin/', admin.site.urls),
]
urlpatterns += static('media', document_root=settings.MEDIA_ROOT)