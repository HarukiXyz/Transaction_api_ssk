
from django.contrib import admin
from django.urls import path, include
from transactions.views import indexPage
from rest_framework.routers import DefaultRouter
from transactions.views import TransactionViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', indexPage(), name='index'),
    path('api/token/', TokenObtainPairView.as_view(), name='Token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='Token_refresh'),

]

