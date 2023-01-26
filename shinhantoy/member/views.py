from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.hashers import check_password, make_password

from .serializers import MemberSerializer
from .models import Member

# Create your views here.

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView   
):
    serializer_class = MemberSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
    
    
class MemberChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        ## 로그인한 사용자만 들어올 수 있는 곳! (즉, request.user가 있음)
        current = request.data.get('current')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        # 새로 변경할 비밀번호와 확인용 비밀번호가 다르면 400
        if password1 != password2:
            return Response({
                'detail': 'Wrong new passwords',
            }, status=status.HTTP_400_BAD_REQUEST)

        # pw가 맞는지 확인 -> 틀리다면 400
        member = request.user
        if not check_password(current, member.password):
            return Response({
                'detail': 'Wrong password',
            }, status=status.HTTP_400_BAD_REQUEST)

        # id, pw 모두 맞고 / 바꿀 비밀번호 2개도 일치한다면
        # 변경 비밀번호 암호화하여 저장
        member.password = make_password(password1)
        member.save()

        return Response(status=status.HTTP_200_OK)