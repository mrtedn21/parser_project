from rest_framework import serializers

from parser.models import Bill


class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'


class BillFileSerializer(serializers.Serializer):
    file = serializers.FileField(allow_empty_file=False)
