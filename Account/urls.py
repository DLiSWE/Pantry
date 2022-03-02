from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Account/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('edit_user/<int:pk>', views.EditUser.as_view(template_name='Account/edit_user.html'), name='edituser'),
    path('profile/<int:pk>', views.ProfileView.as_view(template_name='Account/profile_page.html'),name='profileview'),
    path('profile/<int:pk>/edit', views.UpdateProfile.as_view(),name='editprof')
]  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)