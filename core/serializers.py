from rest_framework import serializers


class ChoiceDisplayField(serializers.ChoiceField):

    def to_representation(self, value):
        return {
            "value": value,
            "label": self.choices.get(value, value)
        }
