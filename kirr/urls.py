from django.contrib import admin
from django.urls import re_path, path
# from django.conf import settings
# from django.conf.urls.static import static


from shortener.views import HomeView, URLRedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    re_path(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
