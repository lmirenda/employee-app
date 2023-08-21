import datetime

from rest_framework import serializers

from employees.models.employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Employee

    @staticmethod
    def validate_name(value):
        if len(value) < 2:
            raise serializers.ValidationError(
                "The name is must be at least 2 characters long."
            )
        return value

    @staticmethod
    def validate_birthday(value):
        if value > datetime.date.today():
            raise serializers.ValidationError("The birth date cannot be in the future.")
        return value
