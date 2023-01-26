from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Too short password')
        
        
        # 유효성 검사가 끝난 값을 반환
        return make_password(value)
    
    class Meta:
        model = Member
        fields = ('id', 'username', 'tel', 'password')   #'__all__'
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'password': {
                'write_only': True
            }
        }