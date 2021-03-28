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
    render
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
    PasswordConfirmationForm,
    RegistrationForm,
    RegistrationFormNoCaptcha,
    UserLoginForm,
    UserPersonalInformationForm,
    UserPreferencesForm,
    UserProfileForm,
    GymForm
)

from wger.core.models import (
    Language,
    UserProfile  # VPATEL
)

from wger.gym.models import (
    AdminUserNote,
    Contract,
    GymUserConfig
)
from wger.manager.models import (
    Workout,
    WorkoutLog,
    WorkoutSession
)
from wger.nutrition.models import NutritionPlan
from wger.utils.generic_views import (
    WgerFormMixin,
    WgerMultiplePermissionRequiredMixin
)
from wger.weight.models import WeightEntry


logger = logging.getLogger(__name__)


def view_forum(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        print("THIS IS A GET REQUEST")

    return render(request, 'forum/forum.html', { 'name': 'vishal'})
