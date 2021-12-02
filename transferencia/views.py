from rest_framework import viewsets
from transferencia.models import Transacao
from transferencia.serializer import TransferenciaSerializer


class TransferenciaViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransferenciaSerializer
