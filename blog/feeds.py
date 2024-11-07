from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import post


class LatestEntriesFeed(Feed):
    title = "lates posts"
    link = "/rss/feeds"
    description = "best post ever ."

    def items(self):
        return post.objects.filter(status=True)

    def item_title(self, item):
        return item.titel

    def item_description(self, item):
        return item.content