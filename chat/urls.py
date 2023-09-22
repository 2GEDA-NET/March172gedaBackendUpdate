from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'conversations', views.ConversationViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'status', views.StatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('threads/', views.ThreadListView.as_view(), name='thread-list'),
    path('upload-story/', views.StoryUploadAPI.as_view(), name='upload-story'),
    path('get-stories/', views.GetStories.as_view(), name='get-stories'),
    path('viewed-lifestyle/<int:story_id>/', views.ViewedLifeStyle.as_view(), name='viewed-lifestyle'),
    path('delete-lifestyle/', views.LifeStyleDelete.as_view(), name='delete-lifestyle'),
    path('user-lifestyle/<int:user_id>/', views.SingleUserLifeStyle.as_view(), name='user-lifestyle'),
]

