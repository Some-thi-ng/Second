from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    # Диспетчер кастомной модели пользователя
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Пользователь должен иметь логин')
        if email is None:
            raise TypeError('Пользователь должен иметь email')
        user = self.model(
            username=username, email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Администратор должен иметь пароль.')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
