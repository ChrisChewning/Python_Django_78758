from django.contrib import admin
from django.contrib.auth import views as auth_views 
from users import views as user_views
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')), #now when we go to /forum it'll 
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('main.urls')),
    url(r'^comments/', include('django_comments.urls')),
] 

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#login and logout are class based views.
#in as view function, the arg is pointing to the template

#https://docs.djangoproject.com/en/2.2/howto/static-files/ 