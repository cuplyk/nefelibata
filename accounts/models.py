from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.urls import reverse

class BlogUser(AbstractUser):
    nickname = models.CharField(_('nick name'), max_length=100, blank=True)
    creation_time = models.DateTimeField(_('creation time'), default=now)
    last_modify_time = models.DateTimeField(_('last modify time'), default=now)
    source = models.CharField(_('create source'), max_length=100, blank=True)

    # Add custom related_name to avoid clashes with auth.User's groups
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='bloguser_set',
        related_query_name='bloguser',
    )

    # Add custom related_name to avoid clashes with auth.User's user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='bloguser_set',
        related_query_name='bloguser',
    )

    def get_absolute_url(self):
        return reverse('blog:author_detail', kwargs={'author_name': self.username})

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = _('user')
        verbose_name_plural = _('users')
