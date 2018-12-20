from django.shortcuts import render
from winesearch.models import Wine
from api.serializers import WineSerializer
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response


class WineViewSet(viewsets.ModelViewSet):
	"""
	This ViewSet provides both 'list' and 'detail' views.
	"""
	queryset = Wine.objects.select_related('variety').order_by('wine')
	serializer_class = WineSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def delete(self, request, pk, format=None):
		site = self.get_object(pk)
		self.perform_destroy(self, wine)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):
		instance.delete()


'''
class WineListAPIView(generics.ListCreateAPIView):
	queryset = Wine.objects.select_related('variety').order_by('wine')
	serializer_class = WineSerializer
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
'''

'''
class WineDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Wine.objects.select_related('variety').order_by('wine')
	serializer_class = WineSerializer
	permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
'''