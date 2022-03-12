from django.urls import path
from api import views
urlpatterns = [
    path('todos',views.TodoListCreate.as_view()),
    path('todos/<int:pk>',views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete',views.TodoUpdate.as_view()),
    path('todos/completed',views.TodoCompletedList.as_view()),
    path('signup',views.signup),
]
