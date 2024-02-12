from django.http import HttpResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from patinetes.models import Patinete
from patinetes.permissions import PatinetePermission
from patinetes.serializers import PatineteSerializer


# Create your views here.

class PatineteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Patinete.objects.all()
    serializer_class = PatineteSerializer

    #Para los permisos de un método concreto con el ViewSet se hace así
    def get_permissions(self):
        if self.action == 'test':
            self.permission_classes = [PatinetePermission, ]
        else:
            self.permission_classes = []
        return super(PatineteViewSet, self).get_permissions()

    #La lógica del alquiler no tiene sentido, simplementeestoy probando funcionalidades
    @action(detail=True, methods=['GET'])
    def test(self, request, pk):
        patinete = get_object_or_404(Patinete, pk=pk)
        patinete.numero = 2345
        serializer = PatineteSerializer(patinete, many=False, context={'request': self.request})
        patinete.save()
        response = Response(serializer.data)
        return Response({'test': 'Hola, esto es un test'}, status=status.HTTP_403_FORBIDDEN)
