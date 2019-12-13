from rest_framework import serializers
# polls.models
from words.models import Words


class Wordserializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ('noun', 'define')

# class ChoiceSerializer(serializers.ModelSerializer):
#     votes = Voteserializer(many=True, required=False)
#
#     class Meta:
#         model = Choice
#         fields = '__all__'
# class PollSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True, read_only=True, required=False)
#
#     class Meta:
#         model = Poll
#         fields = '__all__'
