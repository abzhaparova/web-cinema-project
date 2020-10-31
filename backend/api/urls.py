from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import user_views, movie_views, comment_views

urlpatterns = [
    path('user/create/', user_views.create_user),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('movies/', movie_views.MovieList.as_view()),
    path('movies/<int:movie_id>/', movie_views.MovieListAPIView.as_view()),
    path('comments/<int:page_id>/', comment_views.get_comments),
    path('comments/<int:page_id>/post/', comment_views.post_comment),
    path('comments/change/<int:comment_id>', comment_views.change_score),
    path('comments/delete/<int:comment_id>', comment_views.delete_comment),
]