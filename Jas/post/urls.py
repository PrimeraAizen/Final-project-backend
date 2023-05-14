from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from post import views
from post.views import Tags, like, favourite, UserProfile, EditProfile

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('create-post', views.create_post, name='create-post'),
    path('<uuid:post_id>', views.post_details, name='post-details'),
    path('tag/<slug:tag_slug>', Tags, name='tags'),
    path('<uuid:post_id>/like', like, name='like'),
    path('<uuid:post_id>/favourite', favourite, name='favourite'),
    path('<username>/', UserProfile, name='profile'),
    path('<username>/saved/', UserProfile, name='profilefavourite'),
    path('profile/edit', EditProfile, name="editprofile"),
    path('<username>/follow/<option>/', views.follow, name='follow'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)