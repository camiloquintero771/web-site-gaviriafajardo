from django.contrib.auth import get_user_model
from django.db import models

from crum import get_current_user

from commons.managers import AuditActiveManager


class Audit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación", editable=False)
    modified_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización", editable=False)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
        verbose_name="creado por",
        editable=False,
    )
    modified_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="%(class)s_modified_by",
        null=True,
        blank=True,
        verbose_name="modificado por",
        editable=False,
    )
    is_active = models.BooleanField(verbose_name="está activo", default=True)

    objects = models.Manager()
    active_objects = AuditActiveManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user:
            if self.created_at is None and not user.is_anonymous:
                self.created_by = user
                self.modified_by = user
            elif not user.is_anonymous:
                self.modified_by = user
        super().save(*args, **kwargs)
