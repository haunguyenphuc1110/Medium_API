"""medium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from main import views as view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.SimpleRouter()

# Basic Route
router.register("category", view.CategoryList, base_name="category")
router.register("users", view.UserList, base_name="user")
router.register("cateprod", view.CateProductList, base_name="cateprod")
router.register("products", view.ProductList, base_name="product")

# Popular
router.register("products/popularity", view.PopularityList, base_name="popularity")

# Cate 1
router.register("category_1", view.Category_1, basename="category_1")

# router.register("topcate1", view.TopCat1)

# router.register(r"topcat1/", view.TopCat1, base_name="TopCat1")
# urlpatterns = [
#     url(r"^topcat1/$", view.TopCat1.as_view()),
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
