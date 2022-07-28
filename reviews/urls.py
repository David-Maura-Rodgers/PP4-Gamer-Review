from . import views
from django.urls import path

urlpatterns = [
    path(
        '', views.ReviewList.as_view(),
        name='home'),
    path(
        'create', views.CreateReview.as_view(),
        name='create'),
    path(
        '<slug:pk>/<str:title>/', views.ReviewDetail.as_view(),
         name='review_detail'),
    path(
        'like/<slug:pk>', views.ReviewLike.as_view(),
        name='review_like'),
    path(
        'funny/<slug:pk>', views.ReviewFunny.as_view(),
        name='review_funny'),
    path(
        'insightful/<slug:pk>', views.ReviewInsightful.as_view(),
         name='review_insightful'),
]
