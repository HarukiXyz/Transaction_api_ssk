from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, permissions
from .models import Transactions
from .serializers import TransactionSerializer
# Create your views here.

def indexPage(request):
    return render(request, "index.html")

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transactions.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
