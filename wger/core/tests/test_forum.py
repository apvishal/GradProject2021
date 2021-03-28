# This file is part of wger Workout Manager.
# This file is also part of VPATEL's GRAD PROJECT 2021
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

# Django
from django.contrib.auth.models import (
    User,
    AnonymousUser
)
from wger.core.models import (
    ContentModel,
    PostModel,
    ForumModel,
    ForumCategoryModel
)

from requests import patch

from wger.core.views import user
from django.contrib.auth import authenticate
from django.urls import (
    reverse,
    reverse_lazy, resolve
)
from django.test import RequestFactory

# wger
from wger.core.tests.base_testcase import (
    WgerTestCase
)
from django.test import TestCase

from django.contrib.sessions.middleware import SessionMiddleware

class PublicForumTestCase(WgerTestCase):

    content = []
    post = []
    def test_content_model(self):
        
        """ verify content model is created successfully """     
        self.content = ContentModel.objects.get(content_creator_name="Test Replier")
 
        """ check applicable attributes """
        self.assertEqual(self.content.content_creator_name, "Test Replier")
        self.assertEqual(self.content.content, "This is the reply")

    def test_post_model(self):
        
        """ verify post model is create """
        self.post = PostModel.objects.get(post_title="Some Post")

        """ check applicable attributes """
        self.assertEqual(self.post.post_title, "Some Post")

        self.assertEqual(self.post.post_content, "This is a test post")

        """ verify replies are set """
        replies = self.post.replies.all()
        self.assertEqual(len(replies), 1)
        self.assertEqual(replies[0].content, "This is the reply")

    def test_forum_model(self):
        self.forum = ForumModel.objects.get(pk=1)
        
        self.assertEqual(self.forum.form_name, "Hobbies")

        existing_posts = self.forum.posts.all()

        self.assertEqual(existing_posts[0].post_content, "This is a test post")

    def test_forum_category_model(self):
        category = ForumCategoryModel.objects.get(pk=1)

        self.assertEqual(category.forum_category_name, "General Chat")
