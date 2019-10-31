from rest_framework import serializers

class ExampleSerializer(serializers.Serializer):
    ename = serializers.CharField(max_length=7)
    