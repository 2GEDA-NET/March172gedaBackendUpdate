from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'business-categories', BusinessCategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    #     Authentication urls
    path('register/', create_user, name='user_register'),
    path('login/', obtain_auth_token, name='api_token'),
    path('', UserAPIView.as_view(), name='user_detail'),
    path('update-profile/', update_user_profile, name='update_user_profile'),
    path('users-list/', list_users, name='list_users_by_creation_date'),
    path('delete-account/', delete_account, name='delete_account'),
    path('delete-user/<str:username>/', delete_account_by_username,
         name='delete_account_by_username'),
    path('delete-user-by-id/<int:user_id>/',
         delete_account_by_id, name='delete_account_by_id'),
    path('delete-user-by-username-or-id/', delete_user_by_username_or_id,
         name='delete_user_by_username_or_id'),


    #     Stick urls
    path('stick/<int:user_id>/', stick_user, name='stick_user'),
    path('list-stickers/<int:user_id>/',
         list_stickers, name='list_stickers'),
    path('list-sticking/<int:user_id>/',
         list_sticking, name='list_sticking'),
    path('my-sticking/', my_sticking, name='my_sticking'),
    path('my-stickers/', my_stickers, name='my_stickers'),


    # CRSF token
    path('get-csrf-token/', get_csrf_token, name='get-csrf-token'),

    #     Report Users urls
    path('report_user/', report_user, name='report_user'),
    path('reported_user_list/<int:user_id>/',
         ReportUserViewSet.as_view(), name='reported_user_list'),

    #     Business Profile urls
    path('create-business-profile/', create_business_profile,
         name='create-business-profile'),
    path('update-business-profile/<int:pk>/',
         update_business_profile, name='update-business-profile'),
    path('business-availability/', BusinessAvailabilityListCreateView.as_view(),
         name='business-availability-list'),
    path('business-availability/<int:pk>/',
         BusinessAvailabilityDetailView.as_view(), name='business-availability-detail'),

    path('business-profile/', BusinessProfileListCreateView.as_view(),
         name='business-profile-list'),
    path('business-profile/<int:pk>/', BusinessProfileDetailView.as_view(),
         name='business-profile-detail'),

    path('business-category/', BusinessCategoryListCreateView.as_view(),
         name='business-category-list'),
    path('business-category/<int:pk>/',
         BusinessCategoryDetailView.as_view(), name='business-category-detail'),


    # Address Urls
    path('address/', AddressListCreateView.as_view(), name='address-list'),
    path('address/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),


]

urlpatterns += router.urls
