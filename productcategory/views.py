from django.http import HttpResponse
from product.models import Category

from .serializers import (
	ProductcateggorySerializer,
	MessageSerializer
)

from productcategory.models import Productcategory
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from . tests import Message
from rest_framework.views import APIView


from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import  viewsets


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])

def listproducts(request):
	all_product = Productcategory.objects.all()
	pro_serilizers = ProductcateggorySerializer(all_product,many=True)
	context = {
		'pro_data' : pro_serilizers.data
	}
	return Response(context)



@api_view(['GET','POST'])

def listmessage(request):
	message = Message(email='leila@example.com', content='foo bar')
	pro_serilizers = MessageSerializer(message)
	context = {
		'pro_data' : pro_serilizers.data
	}
	return Response(context)


class ListProducts(APIView):
	def get(self,request):
		all_product = Productcategory.objects.all()
		pro_serilizers = ProductcateggorySerializer(all_product,many=True)
		context = {
			'pro_data' : pro_serilizers.data
		}
		return Response(context)



class ListProductsMixins(mixins.ListModelMixin,generics.GenericAPIView):
	
	queryset = Productcategory.objects.all()
	serializer_class = ProductcateggorySerializer
	
	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)




class DetailedProductsMixins(mixins.RetrieveModelMixin,
							mixins.UpdateModelMixin,
							mixins.CreateModelMixin,
							mixins.DestroyModelMixin,
							generics.GenericAPIView):

	
	queryset = Productcategory.objects.all()
	serializer_class = ProductcateggorySerializer
	
	def get(self,request,*args,**kwargs):
		return self.retrieve(request,*args,**kwargs)

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)


class ListProductsGenerics(generics.ListAPIView):

	queryset = Productcategory.objects.all()
	serializer_class = ProductcateggorySerializer
	



class RetrieveProductsGenerics(generics.RetrieveAPIView,
							generics.UpdateAPIView,
						   generics.DestroyAPIView):

	queryset = Productcategory.objects.all()
	serializer_class = ProductcateggorySerializer



class SpecialGenerics(generics.ListCreateAPIView,
							generics.RetrieveUpdateDestroyAPIView
						   ):

	queryset = Productcategory.objects.all()
	serializer_class = ProductcateggorySerializer


class ProductViewSet(viewsets.ModelViewSet):  # ReadOnlyModelViewSet used for only read
	queryset = Productcategory.objects.all()
	serializer_class = ProductcateggorySerializer