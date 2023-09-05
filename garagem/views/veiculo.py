from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from garagem.models import  Veiculo
from garagem.serializers import VeiculoSerializer,VeiculoDetailSerializer , VeiculoListSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    
    serializer_classes = {
        "list": VeiculoListSerializer,
        "retrieve": VeiculoDetailSerializer,
    }
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, VeiculoSerializer)