from django.urls import path
from rest import views

urlpatterns = [
    path('users/',views.user_list,name="user_list"),
    path('users/<int:pk>/',views.user_detail,name="user_detail"),

    path('post/',views.post_list,name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_list, name='post_new'),
    path('post/<int:pk>/edit/', views.post_detail, name='post_edit'),
    # path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/remove/', views.post_detail, name='post_remove'),
    path('post/<int:pk>/publish/', views.post_detail, name='post_publish'),
    path('post/<int:pk>/comment/', views.post_detail, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.post_detail, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_detail, name='comment_remove'),
]
