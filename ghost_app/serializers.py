from rest_framework import serializers
from ghost_app.models import GhostPost

class GhostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GhostPost
        fields = '__all__'
