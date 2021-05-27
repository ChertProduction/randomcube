from rest_framework import serializers
from api.models import Results

class RandomRequestSerializer(serializers.Serializer):
    input_value = serializers.FloatField()

class RandomResponseSerializer(serializers.Serializer):
    output_value = serializers.IntegerField()

class ResultsSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(required=False)
	class Meta:
		model = Results
		fields =['id', 'number']