# -*- coding: utf-8 -*-
from rest_framework import routers
from api.views import ArticleViewSet, SelectionViewSet, DetailsArticleView, DetailsSectionView

router = routers.DefaultRouter()

router.register(r'articles', ArticleViewSet)
router.register(r'articles/(?P<article_id>d+)/$', DetailsArticleView)
router.register(r'selections', SelectionViewSet)
router.register(r'selections/(?P<section_id>d+)/$', DetailsSectionView)

urlpatterns = router.urls


