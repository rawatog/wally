from django.urls import path, include
from .views import register_view, CustomLoginView, logout_view, upload_image, profile_view,edit_description,like_post



urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('post/', upload_image, name='post'),
    path('profile/', profile_view, name='profile'),
    path('edit_description/<int:image_id>/', edit_description, name='edit_description'),
    path('like/<int:post_id>/', like_post, name='like_post'),

]  