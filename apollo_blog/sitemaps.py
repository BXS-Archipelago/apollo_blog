from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import Category, Post


class CategorySitemap(Sitemap):
    def items(self):
        # this returns all the categories from the database
        return Category.objects.all()


class PostSitemap(Sitemap):
    def items(self):
        # this returns all the active posts from the database
        return Post.objects.filter(status=Post.ACTIVE)

    def lastmod(self, obj):
        # this returns the last-modified date of the object
        return obj.created_at
