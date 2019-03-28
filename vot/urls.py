"""vot_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomAuthToken

urlpatterns = [
    path('', admin.site.urls),
    path('api/v1/', include('authentication_authorization.urls')),
    path('api/v1/', include('guild_calendar.urls')),
    path('api/v1/', include('user.urls')),
    path('api/v1/', include('articles.urls')),
    path('api/v1/', include('newsletters.urls')),
    path('api/v1/', include('galleries.urls')),
    path('api/v1/', include('message_system.urls')),
    path('api/v1/', include('poll_system.urls')),
    path('api/v1/', include('ticket_system.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/v1/login/', CustomAuthToken.as_view())
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
