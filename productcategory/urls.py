from django.urls import path, include
from . import views
from productcategory.views import ListProducts,ProductViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(
  'productViewset',ProductViewSet,basename='product'
)






urlpatterns = [
    path("listproduct/", views.listproducts),
    path("listmessage/", views.listmessage),


    path("list/product/", ListProducts.as_view()),

    path('mixinpath/',views.ListProductsMixins.as_view()),
    path('productmixin/<int:pk>',views.DetailedProductsMixins.as_view()),

    path('productgenerics/',views.ListProductsGenerics.as_view()),

    path('productgenerics/<int:pk>',views.RetrieveProductsGenerics.as_view()),
    path('special/<int:pk>',views.SpecialGenerics.as_view())


]+router.urls
