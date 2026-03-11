from enum import Enum


class StatusEnum(Enum):
    INACTIVE = 0
    ACTIVE = 1


STATUS_CHOICES = (
    (StatusEnum.INACTIVE.value, 'Inativo'),
    (StatusEnum.ACTIVE.value, 'Ativo')
)