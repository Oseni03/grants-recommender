from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import debug_toolbar

urlpatterns = [
    path('finances/', include('apps.finances.urls.main', namespace="finances")),
    path('users/', include('apps.users.urls', namespace="users")),
    path('notifications/', include('apps.notifications.urls', namespace="notifications")),
    path('funds/', include('apps.funds.urls', namespace="funds")),
    path('tools/', include('apps.tools.urls', namespace="tools")),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.home.urls', namespace="home")),
]

handler400 = "config.views.handler_400"
handler403 = "config.views.handler_403"
handler404 = "config.views.handler_404"
handler500 = "config.views.handler_500"

if settings.DEVELOPMENT_MODE is True:
    urlpatterns.append(
        path("__debug__", include(debug_toolbar.urls))
    )