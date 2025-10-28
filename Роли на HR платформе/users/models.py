from django.db import models
from django.contrib.auth.models import Permission, AbstractUser

class User(AbstractUser):
    CANDIDATE = 'candidate'
    HR_MANAGER = 'hr_manager'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (CANDIDATE, 'Кандидат'),
        (HR_MANAGER, 'HR-менеджер'),
        (ADMIN, 'Администратор'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CANDIDATE,
        verbose_name='Роль пользователя',
        help_text='Роль определяет уровень доступа пользователя в системе'
    )

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'
