from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from conta.models import Conta
from transferencia.models import Transacao
from transferencia.serializer import TransferenciaSerializer


class TransferenciaViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransferenciaSerializer
    def create(self, request, *args, **kwargs):
        print(request.data)

        id_remetente = request.data.get("remetente")
        id_destinatario = request.data.get("destinatario")
        valor_transferido = request.data.get("valor_transferido")

        try:
            valor_transferido = int(valor_transferido)

        except ValueError:
            return Response("Números decimais não são válidos",
                            status=status.HTTP_400_BAD_REQUEST)

        if id_remetente == id_destinatario:
            return Response("Não é permitido remetente igual ao destinatário",
                     status=status.HTTP_400_BAD_REQUEST)

        remetente = Conta.objects.get(id=id_remetente)
        print(remetente)
        destinatario = Conta.objects.get(id=id_destinatario)
        print(destinatario)

        print("Saldo do remetente: " + str(remetente.saldo))
        print("Valor da transferência: " + str(valor_transferido))

        if remetente.saldo >= valor_transferido:
            print("Cliente pode fazer transferência")

            serializer = TransferenciaSerializer(data=request.data)
            if serializer.is_valid():
                remetente.saldo -= valor_transferido
                destinatario.saldo += valor_transferido

                with transaction.atomic():
                    serializer.save()
                    remetente.save()
                    destinatario.save()

                print("Efetuou transferência")

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response("Cliente não possui dinheiro suficiente para a transferência",
                        status=status.HTTP_400_BAD_REQUEST)
