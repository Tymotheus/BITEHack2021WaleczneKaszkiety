<<<<<<< HEAD
# from django.conf.urls import url, path, include
# from rest_framework import routers
# from .views import views

from django.urls import path
from .views import views
# import views
# # # from django.urls import include, path
# # from rest_framework import routers
# from .views import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

# ]


urlpatterns = [
    path('api/lead/', views.PostCreate.as_view() ),
]
=======
from django.urls import path, re_path
from . import views
from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views


app_name = 'WisHUB'
urlpatterns = [
    path('tags', views.tags),
    path('fields', views.fields),
    path('tag/<slug:tag_id>/', views.tag),
    path('field/<slug:field_id>/', views.field),
    path('posts/<slug:tag_id>/', views.field),
    path('post/<slug:post_id>/', views.field),
    path('login', views.login),
    path('register', views.register),
    path('login_data',views.login_data),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
>>>>>>> 495e584a9dbcea8e7e4dfd557422ac2e94654621
