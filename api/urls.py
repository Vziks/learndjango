# -*- coding: utf-8 -*-
from rest_framework import routers
from api.views import ArticleViewSet, DetailsArticleView

router = routers.DefaultRouter()

router.register(r'articles', ArticleViewSet)
# router.register(r'articles/(?P<id>d+)/$', DetailsArticleView)
router.register(r'selections', DetailsArticleView)
# router.register(r'selections/(?P<id>d+)/$', DetailsSectionView)

urlpatterns = router.urls


