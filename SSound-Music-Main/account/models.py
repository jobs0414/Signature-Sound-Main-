import os
from hashlib import sha1, md5


class User(AbstractBaseUser, PermissionsMixin):

    ... 생략 ...

    salt = models.CharField(
        verbose_name=_('Salt'),
        max_length=10,
        blank=True
    )

    ... 생략 ...

    def set_password(self, raw_password):
        # Opencart의 salt 값은 9자리의 alphanumeric 문자열
        salt = md5(os.urandom(128)).hexdigest()[:9]

        # Opencart PHP 프로그램의 비밀번호 암호화 알고리즘
        hashed = sha1(
            (salt + sha1(
                (salt + sha1(
                    raw_password.encode('utf8')
                ).hexdigest()).encode('utf8')
            ).hexdigest()).encode('utf8')
        ).hexdigest()

        self.salt = salt
        self.password = hashed

     def check_password(self, raw_password):
        try:
            user = User.objects.get(email=self.email)

            hashed = sha1(
                (user.salt + sha1(
                    (user.salt + sha1(
                        raw_password.encode('utf8')
                    ).hexdigest()).encode('utf8')
                ).hexdigest()).encode('utf8')
            ).hexdigest()

            if user.password == hashed:
                return True
            else:
                return False

        except User.DoesNotExist:
            return False
