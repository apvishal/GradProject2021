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
    UserProfile,
)
from wger.gym.models import (
    Gym,
)
from requests import patch

from wger.core.views import user
from django.contrib.auth import authenticate
from django.urls import (
    reverse,
    reverse_lazy, resolve
)
from django.test import RequestFactory
from wger.core.forms import UserProfileForm
# wger
from wger.core.tests.base_testcase import (
    WgerTestCase
)
from django.test import TestCase

from django.contrib.sessions.middleware import SessionMiddleware

class UserProfileTestCase(WgerTestCase):

    """ attributes for a new users specifically for testing a user profile """
    username = 'profileTestUser'
    email = 'newuser@csu.fullerton.edu'
    userpw = 'userpw'

    def test_verify_profile_user(self):
        """ verify profile test user from test-user-data.json exists """
        user = User.objects.get(username=self.username)
        self.assertIsNotNone(user)

    def test_authenticate_profile_user(self):
        """ login the user """
        self.user_login(self.username)

        """ get the user object """
        user = User.objects.get(username=self.username)

        """ verify authentication """
        self.assertTrue(user.is_authenticated)

    # @patch('wger.core.views.login_required', lambda func: func)
    def test_user_profile_page(self):
        self.user_login(self.username)
        temp = User.objects.get(username=self.username)

        # need a request object
        request = RequestFactory().get('/en/user/profile/')
        request.user = AnonymousUser()
        request.user.id = temp.pk

        # need middle ware to allow session to execute
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        # call the correct function for generating the html
        response = user.profile(request)

        # begin verifying the output
        self.assertEqual(response.status_code, 200)

        html = str(response.content.decode('utf-8'))
        result = "profileTest@example.com" in html
        self.assertTrue(result)

