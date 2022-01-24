from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'cover', 'cover_2', 'author', 'title', 'slug', 'text', 'text_2', 'l_heading', 'l_heading_text', 'quote', 'quotes_name', 's_heading', 's_heading_text', 'category', 'created_date', 'tag_1', 'tag_2', 'tag_3')
