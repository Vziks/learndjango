from rest_framework import serializers
from article import models as ArticleModels


class SectionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:section-detail')
    class Meta:
        model = ArticleModels.Section
        fields = ('url', 'section_title', 'section_url', 'section_description')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:article-detail')
    #link
    # section = serializers.StringRelatedField(many=True)
    # section = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='api:section-detail'
    # )
    # name
    # section = serializers.StringRelatedField()
    section = SectionSerializer(read_only=True)
    class Meta:
        model = ArticleModels.Article
        # fields = ('url', 'title', 'content', 'section')
        exclude = ()