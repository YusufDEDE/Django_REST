from rest_framework import serializers
from BackEnd.models import Lead
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')