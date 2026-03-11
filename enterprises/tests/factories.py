import factory
from django.utils import timezone

from core.enums import StatusEnum
from enterprises.enums import BusinessSegmentEnum
from enterprises.models import Enterprise


class EnterpriseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Enterprise

    name = factory.Faker("company")
    entrepreneur_name = factory.Faker("name")
    municipality = factory.Faker("city")
    segment = BusinessSegmentEnum.TECHNOLOGY.value
    contact_email = factory.Faker("email")
    status = StatusEnum.ACTIVE.value
    created_at = factory.LazyFunction(timezone.now)
    updated_at = factory.LazyFunction(timezone.now)
