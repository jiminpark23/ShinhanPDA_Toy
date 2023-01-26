from django.contrib.auth.hashers import check_password
from .models import Member

class MemberAuth:   # 어떤 것도 상속받지 않았음
    
    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        if not username or not password:
            if request.user.is_authenticated:
                return request.user
            else:
                return None
        
        try:
            member = Member.objects.get(username=username)
        except Member.DoesNotExist:
            return None
        
        if check_password(password, member.password):
            if member.status == '일반':
                return member        # 로그인 성공을 의미함
        
        return None
    
    def get_user(self, pk):     # 사용자 객체 자체를 받아오는 함수
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return None
        
        return member #if member.is_active and member.status == '일반' else None   <- 위에서 인증단계 있기 때문에 필요없음