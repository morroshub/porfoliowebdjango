# Data representations.
# ou can also use primary key and various other relationships, 
# but hyperlinking is good RESTful design.

from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Post'
        fields = ('id', 'title', 'date')
        # all fields can with this syntax 
        #    fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'