# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
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

# Standard Library
import logging

# Django
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView
)
from django.http import (
    HttpResponseForbidden,
    HttpResponseRedirect
)
from django.shortcuts import (
    get_object_or_404,
    render,
    redirect
)
from django.template.context_processors import csrf
from django.urls import (
    reverse,
    reverse_lazy
)
from django.utils import translation
from django.utils.translation import (
    ugettext as _,
    ugettext_lazy
)
from django.views.generic import (
    DetailView,
    ListView,
    RedirectView,
    UpdateView
)
from django.http import HttpResponse

# Third Party
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    ButtonHolder,
    Column,
    Layout,
    Row,
    Submit
)
from rest_framework.authtoken.models import Token

# wger
from wger.config.models import GymConfig
from wger.core.forms import (
    ForumPostForm,
)

from wger.core.models import (
    Language,
    UserProfile  # VPATEL
)

from wger.core.models import (
    ContentModel,
    PostModel,
    ForumCategoryModel,
    ForumModel
)

logger = logging.getLogger(__name__)


def view_community_forum(request):
    # there really is no post request on the home page...
    if request.method == 'POST':
        pass

    elif request.method == 'GET':
        print("THIS IS A GET REQUEST FOR THE COMMUNITY FORUM HOME PAGE")
        all_categories = list(ForumCategoryModel.objects.all())

    return render(request, 'forum/community-forum.html', { 'name': 'vishal', 'categories': all_categories })

def view_forum(request, slug):
    template_data = {}
    # get the appropriate forum model (TODO: use slug instead)
    forum_model = ForumModel.objects.get(form_name__iexact=slug.replace('-', ' '))
    query_string = slug.replace('-', ' ')

    if request.method == 'POST':
        post = PostModel.objects.create()
        post.post_title = request.POST['post-title']
        post.slug = request.POST['post-title'].lower().replace(' ', '-')
        post.post_content = request.POST['post-content']
        post.post_creator_name = request.user.username
        post.save()

        forum_model.posts.add(post)
        forum_model.save()

        return redirect(request.path)
    elif request.method == 'GET':
        pass

    # always make a new PostForm
    template_data['forum_title'] = query_string.title()
    template_data['posts'] = forum_model.posts.all()

    return render(request, 'forum/forum.html', template_data)

def view_post(request, slug):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        # search_string = slug.replace('-', ' ')
        print("THIS IS A GET REQUEST FORUM POST for" + slug)
        post = PostModel.objects.get(post_title__iexact=slug.replace('-', ' '))

    return render(request, 'forum/post.html', { 'post_title': slug.replace('-', ' ').title(), 'post':post, 'replies':post.replies.all()})
