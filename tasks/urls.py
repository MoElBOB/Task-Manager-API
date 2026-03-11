from django.urls import path
from . import views

urlpatterns = [

    # endpoint لعرض المهام
    path('tasks/', views.TaskListCreateView.as_view()),

     # endpoint للتعديل والحذف
    path('tasks/<int:id>/', views.task_detail),

      # register endpoint
    path('register/', views.register_user),

    path('categories/', views.CategoryListCreateView.as_view()),

    path('profile/', views.ProfileView.as_view()),
]