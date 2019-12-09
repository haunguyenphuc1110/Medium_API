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

# -------ALL CATEGORY CLASS-----------
# Cate 1
router.register("category_1", view.Category_1, basename="category_1")

# Cate 2
router.register("category_2", view.Category_2, basename="category_2")

# Cate 3
router.register("category_3", view.Category_3, basename="category_3")
# ------------END OF CATEGORY CLASS-------------

# -------SUB CATEGORY------------
# router.register("category_1_2", view.Category_1_2, basename="category_1_2")
# --------END OF SUB CATEGORY
# Top 10 Cate 1
# router.register(
#     "r'^category/(?P<cate1_id>\w{0,50})/$'",
#     view.Category_1_top10.as_view(),
#     base_name="top10_cat1",
# )

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
    path("category/prod/first/<str:cate1_id>/", view.Category_prod_1_top.as_view()),
    path("category/prod/second/<str:cate2_id>/", view.Category_prod_2_top.as_view()),
    path("category/prod/third/<str:cate3_id>/", view.Category_prod_3_top.as_view()),
    path("category/cate/first/<str:cate1_id>/", view.Category_cate_1_top.as_view()),
    path("category/cate/second/<str:cate2_id>/", view.Category_cate_2_top.as_view()),
    path("category/", view.CategoryFilter.as_view()),
    path("category/level_2/", view.CategoryFilter_level2.as_view()),
    path("category/level_3/", view.CategoryFilter_level3.as_view()),
    path("user/<str:username>/<str:password>/", view.UserLogin.as_view()),
    path("user/history/", view.UserHistory.as_view()),
    path("api/v1/users", view.UserFilter.as_view()),
    path("api/v1/users/recommend", view.RecommendView.as_view()),
    path("api/v1/users/survey", view.testPOST),
    path("api/v1/products/related/", view.ProductRelated.as_view()),
]
