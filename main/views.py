from django.shortcuts import render
from main.models import Account, Organization, Contact, Invoice, Role, UserAccount
from main.serializers import AccountSerializer,OrganizationSerializer,ContactSerializer,InvoiceSerializer,RoleSerializer,UserAccountSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET','POST'])
def reservation_operations(request):

    if request.method =='POST':
        account = Account.objects.filter(name=name,owner=owner,address=address)
        serializer=AccountSerializer(account,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'owner','address']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset=Organization.objects.all()
    serializer_class=OrganizationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'place','account']

class ContactViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset=Role.objects.all()
    serializer_class=RoleSerializer

class UserAccountViewSet(viewsets.ModelViewSet):
    queryset=UserAccount.objects.all()
    serializer_class=UserAccountSerializer
