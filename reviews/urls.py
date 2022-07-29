from . import views
from django.urls import path

urlpatterns = [
    path(
        '', views.ReviewList.as_view(),
        name='home'),
    path(
        'create_review/', views.CreateReview.as_view(),
        name='create_review'),
    path(
        'posted_review/', views.PostedReview.as_view(),
        name='posted_review'),
    path(
        'edit_review/', views.EditReview.as_view(),
        name='edit_review'),
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
