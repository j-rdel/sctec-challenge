from enum import Enum


class BusinessSegmentEnum(Enum):
    TECHNOLOGY = 0
    COMMERCE = 1
    INDUSTRY = 2
    SERVICES = 3
    AGRIBUSINESS = 4


BUSINESS_SEGMENT_CHOICES = (
    (BusinessSegmentEnum.TECHNOLOGY.value, 'Tecnologia'),
    (BusinessSegmentEnum.COMMERCE.value, 'Comércio'),
    (BusinessSegmentEnum.INDUSTRY.value, 'Indústria'),
    (BusinessSegmentEnum.SERVICES.value, 'Serviços'),
    (BusinessSegmentEnum.AGRIBUSINESS.value, 'Agronegócio')
)


class EnterpriseStatusEnum(Enum):
    INACTIVE = 0
    ACTIVE = 1


ENTERPRISE_STATUS_CHOICES = (
    (EnterpriseStatusEnum.INACTIVE.value, 'Inativo'),
    (EnterpriseStatusEnum.ACTIVE.value, 'Ativo')
)
