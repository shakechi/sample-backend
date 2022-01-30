from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, CreateUserView, TaskListView, TaskRetrieveView, PostListView, PostRetrieveView

# viewsetsで登録するとrouter
router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

# genericsで登録するとurlpatterns
urlpatterns = [
    path('list-post/', PostListView.as_view(), name='list-post'),
    path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name='detail-post'),
    path('list-task/', TaskListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>/', TaskRetrieveView.as_view(), name='detail-task'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    # routerの内容を取りに行く
    path('', include(router.urls)),
]