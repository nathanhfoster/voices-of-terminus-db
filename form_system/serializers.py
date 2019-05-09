from rest_framework import serializers, fields
from form_system.models import Form, FormQuestion, FormChoice, FormResponse, FormRecipient
from django.contrib.auth.models import User


class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = ('id', 'title', 'author', 'author_username',
                  'date_created', 'last_modified', 'expiration_date',)
        read_only_fields = ('id', 'date_created', )


class FormQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormQuestion
        fields = ('id', 'author', 'author_username', 'question', 'question_type',
                  'image', 'date_created', 'last_modified', 'form_id', 'position',
                  )
        read_only_fields = ('id', 'date_created',)


class FormChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormChoice
        fields = ('id', 'author', 'author_username', 'title',
                  'date_created', 'last_modified', 'position',
                  'question_id', )
        read_only_fields = ('id',)


class FormResponseSeializer(serializers.ModelSerializer):
    class Meta:
        model = FormResponse
        fields = ('id', 'author', 'author_username', 'response',
                  'date_created', 'last_modified',
                  'choice_id', )
        read_only_fields = ('id',)


class FormRecipientSeializer(serializers.ModelSerializer):
    class Meta:
        model = FormRecipient
        fields = ('id', 'recipient',
                  'recipient_username', 'recipient_poll_id',)
        read_only_fields = ('id',)
