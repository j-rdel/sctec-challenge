from django.db import models

from core.enums import STATUS_CHOICES, StatusEnum
from core.models import BaseModel
from enterprises.enums import BUSINESS_SEGMENT_CHOICES


class Enterprise(BaseModel):
    name = models.CharField(max_length=255)
    entrepreneur_name = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    segment = models.IntegerField(choices=BUSINESS_SEGMENT_CHOICES)
    contact_email = models.EmailField()
    status = models.CharField(choices=STATUS_CHOICES, default=StatusEnum.ACTIVE.value)

    class Meta:
        db_table = "enterprises"
        ordering = ["created_at"]

    def __str__(self):
        return self.name
