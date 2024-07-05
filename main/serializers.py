from rest_framework import serializers
from main.models import Account, Organization, Invoice, Role, Contact, UserAccount

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields='__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields='__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields='__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields='__all__'

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields='__all__'
