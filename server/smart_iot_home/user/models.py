from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name="사용자명")
    ## char(64)
    ## verbose_name : 애트리뷰트 이름

    useremail = models.CharField(max_length=128,
                                 verbose_name="사용자 이메일")

    ## max_length: 문자의 최대 길이
    password = models.CharField(max_length=64,
                                verbose_name="비밀번호")

    registered_dttm = models.DateField(auto_now_add=True,
                                       verbose_name="등록시간")

    ## auto_now_add: 자동으로 현재 시간 추가

    ## 새로운 User(클래스) 생성시 object이름이 아닌 오브젝트 속성 문자열로 출력하게 한다.
    ## __str__:인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수.
    def __str__(self):
        return self.username

    # meta 데이터: 어떤 목적을 가지고 만들어진 데이터
    # https: // docs.djangoproject.com / en / 3.0 / ref / models / options /
    class Meta:
        db_table = "user"

        verbose_name = '사용자'
        verbose_name_plural = "사용자"
        # verbose: 부팅시 상세한 정보를 보여줌