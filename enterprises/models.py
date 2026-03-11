import uuid

from django.db import models

from .enums import BUSINESS_SEGMENT_CHOICES, ENTERPRISE_STATUS_CHOICES, EnterpriseStatusEnum


class Enterprise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    entrepreneur_name = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    segment = models.IntegerField(choices=BUSINESS_SEGMENT_CHOICES)
    contact_email = models.EmailField()
    status = models.CharField(choices=ENTERPRISE_STATUS_CHOICES, default=EnterpriseStatusEnum.ACTIVE.value)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "enterprises"
        ordering = ["created_at"]

    def __str__(self):
        return self.name
