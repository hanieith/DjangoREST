from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women, Category
from .serializers import WomenSerializer
from django.forms import model_to_dict
from rest_framework.decorators import action


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Women.objects.all()[:3]
        else:
            return Women.objects.filter(pk=pk) #dont use get, becose filter return list

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats':cats.name})

#class WomenAPIList(generics.ListCreateAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer
#
#class WomenAPIUpdate(generics.UpdateAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer
#
#class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#        queryset = Women.objects.all()
#        serializer_class = WomenSerializer


#class WomenAPIView(APIView):
#   def get(self, request):
#       lst = Women.objects.all().values()
#       return Response({'posts':WomenSerializer(lst, many=True).data})

#   def post(self, request):
#       serializer = WomenSerializer(data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({'post':serializer.data})

#   def put(self, request, *args, **kwargs):
#       pk = kwargs.get("pk", None)
#       if not pk:
#           return Response({"error":"Method PUT not allowed"})

#       try:
#           instance = Women.objects.get(pk=pk)
#       except:
#           return Response({"error":"Object does not exists"})

#       serializer = WomenSerializer(data=request.data, instance=instance)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({"post":serializer.data})


#class WomenAPIView(generics.ListAPIView):
#queryset = Women.objects.all()
#serializer_class = WomenSerializer
