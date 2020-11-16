from rest_framework import serializers
from articles.models import *
from django.template.loader import render_to_string
from articles.tasks import *
from cloudinary.forms import CloudinaryFileField

def Emailsendserializer(**data):
    mail_subject = "SUCCESS MAIL"
    contentmessage = render_to_string('verification_email', {
        'user': data['first_name']+" "+data["last_name"],
        'email': data['email'],
    })
    send_mail(mail_subject, contentmessage, "bupathidinesh@gmail.com", [data["email"], ])
    return "success"

class ArticlesSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self,obj):
        return '{}'.format(obj.user)

    image = CloudinaryFileField(
        options={
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'images'
        }
    )
    class Meta:

        model = Article
        fields = serializers.ALL_FIELDS

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = serializers.ALL_FIELDS
    def create(self, validated_data):
        Emailsendserializer(**validated_data)
        return Suggestions.objects.create(**validated_data)

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = serializers.ALL_FIELDS