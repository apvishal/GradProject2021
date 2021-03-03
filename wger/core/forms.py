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

# Django
from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import (
    CharField,
    EmailField,
    Form,
    PasswordInput,
    widgets
)
from django.utils.translation import ugettext as _

# Third Party
from captcha.fields import ReCaptchaField
from crispy_forms.bootstrap import (
    Accordion,
    AccordionGroup,
    Tab,
    TabHolder
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    ButtonHolder,
    Column,
    Layout,
    Row,
    Submit,
    Div,
    Field,
    HTML
)

# wger
from wger.core.models import UserProfile
from wger.gym.models import Gym


class UserLoginForm(AuthenticationForm):
    """
    Form for logins
    """

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Login'), css_class='btn-success btn-block'))
        self.helper.form_class = 'wger-form'
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-6 mb-0'),
                Column('password', css_class='form-group col-6 mb-0'),
                css_class='form-row'
            )
        )


class UserPreferencesForm(forms.ModelForm):
    first_name = forms.CharField(label=_('First name'),
                                 required=False)
    last_name = forms.CharField(label=_('Last name'),
                                required=False)
    email = EmailField(label=_("Email"),
                       help_text=_("Used for password resets and, optionally, email reminders."),
                       required=False)
    city = forms.CharField(label=_('Gym City'), required=False)
    state = forms.CharField(label=_('Gym State'), required=False)

    class Meta:
        model = UserProfile
        fields = ('show_comments',
                  'show_english_ingredients',
                  'workout_reminder_active',
                  'workout_reminder',
                  'workout_duration',
                  'notification_language',
                  'weight_unit',
                  'timer_active',
                  'timer_pause',
                  'ro_access',
                  'num_days_weight_reminder',
                  'birthdate',
                  'profilePicture',
                  'goal',
                  'age',
                  'height',
                  'goal',
                  'fitness_activity'
                  )

    def __init__(self, *args, **kwargs):
        super(UserPreferencesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'wger-form'
        self.helper.layout = Layout(
            Accordion(
                AccordionGroup(_("Personal data"),
                               'email',
                               Row(Column('first_name', css_class='form-group col-6 mb-0'),
                                   Column('last_name', css_class='form-group col-6 mb-0'),
                                   css_class='form-row'
                                    ),
                               Row(Column('age', css_class='form-group col-6 mb-0'),
                                   Column('height', css_class='form-group col-6 mb-0'),
                                   css_class='form-row'
                                   ),
                               Row(Column('goal', css_class='form-group col-6 mb-0'),
                                   Column('fitness_activity', css_class='form-group col-6 mb-0'),
                                   css_class='form-row'
                                   )
                               ),
                AccordionGroup(_("Workout reminders"),
                               'workout_reminder_active',
                               'workout_reminder',
                               'workout_duration',
                               ),
                AccordionGroup("{} ({})".format(_("Gym mode"), _("mobile version only")),
                               "timer_active",
                               "timer_pause",

                               ),
                AccordionGroup(_("Other settings"),
                               "ro_access",
                               "city",
                               "state",
                               "notification_language",
                               "weight_unit",
                               "show_comments",
                               "show_english_ingredients",
                               "num_days_weight_reminder",
                               "birthdate",
                               "profilePicture"
                               )
            ),
            ButtonHolder(Submit('submit', _("Save"), css_class='btn-success btn-block'))
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
        )

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.data = kwargs['initial']
        # self.imageDiv = FormHelper()
        # self.imageDiv.form_tag = False
        # self.helper.form_class = 'wger-form'
        # self.imageDiv.layout = Layout(
        #     Div(, css_class="col-sm-3")
        # )

        # self.nameDiv = FormHelper()
        # self.nameDiv.form_tag = False
        # # self.helper.form_class = 'wger-form'
        # self.nameDiv.layout = Layout(
        #     Div(Field('first_name'), css_class="col-sm-3 offset-sm-5")
        # )

        # create all lines of text for the html...
        self.full_name = "<p><strong>Full Name:</strong>&emsp;&ensp;" + self.data['full_name'] + "</p>"
        self.age = "<p><strong>Age:</strong>&emsp;&ensp;" + self.data['age'] + "</p>"
        self.city = "<p><strong>Gym Location:</strong>&emsp;&ensp;" + self.data['location'] + "</p>"
        self.gender = "<p><strong>Gender:</strong>&emsp;&ensp;" + ("Male" if self.data['gender'] else "Female") + "</p>"
        self.weight = "<p><strong>Weight:</strong>&emsp;&ensp;" + self.data['weight'] + " lbs</p>"
        self.height = "<p><strong>Height:</strong>&emsp;&ensp;" + self.data['height'] + " cm</p>"
        self.goal = "<p><strong>Primary Goal:</strong>&emsp;&ensp;" + self.data['goal'] + "</p>"
        self.activity = "<p><strong>Fitness Activity:</strong>&emsp;&ensp;" + self.data['activity'] + "</p>"
        self.calories = "<p><strong>Daily Intake:</strong>&emsp;&ensp;" + self.data['calories'] + "</p>"
        self.sportHours = "<p><strong>Hours of Fitness:</strong>&emsp;&ensp;" + self.data['sport_hrs'] + " hours / day</p>"
        self.sportIntensity = "<p><strong>Fitness Intensity</strong>&emsp;&ensp;" + self.data['sport_intensity'] + "</p>"


        self.anotherHelper = FormHelper()
        self.anotherHelper.form_tag = False
        self.anotherHelper.layout = Layout(
            TabHolder(
                Tab('Personal Information',
                    Row(
                        Column(HTML(self.full_name), css_class='form-group col-6 mb-0'),
                        Column(HTML(self.gender), css_class='form-group col-6 mb-0')
                    ),
                    Row(
                        Column(HTML(self.city), css_class='form-group col-6 mb-0'),
                        Column(HTML(self.weight), css_class='form-group col-6 mb-0')
                    ),
                    Row(
                        Column(HTML(self.age), css_class='form-group col-6 mb-0'),
                        Column(HTML(self.height), css_class='form-group col-6 mb-0')
                    ),
                ),
                Tab('More Information',
                    Row(
                        Column(HTML(self.goal), css_class='form-group col-6 mb-0'),
                        Column(HTML(self.calories), css_class='form-group col-6 mb-0')
                    ),
                    Row(
                        Column(HTML(self.sportHours), css_class='form-group col-6 mb-0'),
                        Column(HTML(self.sportIntensity), css_class='form-group col-6 mb-0')
                    )
                )
            )
        )
        # self.anotherHelper = FormHelper()
        # # self.anotherHelper.form_class = 'wger-form'
        # self.anotherHelper.form_tag = False
        # self.anotherHelper.layout = Layout(
        #     Div('email', css_class="float-container")
        # )


class UserEmailForm(forms.ModelForm):
    email = EmailField(label=_("Email"),
                       help_text=_("Used for password resets and, optionally, email reminders."),
                       required=False)

    class Meta:
        model = User
        fields = ('email', )

    def clean_email(self):
        """
        Email must be unique system wide

        However, this check should only be performed when the user changes his
        email, otherwise the uniqueness check will because it will find one user
        (the current one) using the same email. Only when the user changes it, do
        we want to check that nobody else has that email
        """

        email = self.cleaned_data["email"]
        if not email:
            return email
        try:
            user = User.objects.get(email=email)
            if user.email == self.instance.email:
                return email
        except User.DoesNotExist:
            return email

        raise ValidationError(_("This email is already used."))


class UserPersonalInformationForm(UserEmailForm):
    first_name = forms.CharField(label=_('First name'),
                                 required=False)
    last_name = forms.CharField(label=_('Last name'),
                                required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class GymForm(forms.ModelForm):
    city = forms.CharField(label=_('Gym City'),
                                 required=False)
    state = forms.CharField(label=_('Gym State'),
                                required=False)

    class Meta:
        model = Gym
        fields = { 'city', 'state' }

class PasswordConfirmationForm(Form):
    """
    A simple password confirmation form.

    This can be used to make sure the user really wants to perform a dangerous
    action. The form must be initialised with a user object.
    """
    password = CharField(label=_("Password"),
                         widget=PasswordInput,
                         help_text=_('Please enter your current password.'))

    def __init__(self, user, data=None):
        self.user = user
        super(PasswordConfirmationForm, self).__init__(data=data)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'password',
            ButtonHolder(Submit('submit', _("Delete"), css_class='btn-danger btn-block'))
        )

    def clean_password(self):
        """
        Check that the password supplied matches the one for the user
        """
        password = self.cleaned_data.get('password', None)
        if not self.user.check_password(password):
            raise ValidationError(_('Invalid password'))
        return self.cleaned_data.get("password")


class RegistrationForm(UserCreationForm, UserEmailForm):
    """
    Registration form
    """

    # Manually set the language to 'en', otherwise the language used seems to
    # randomly one of the application languages. This also appears to happen
    # only on wger.de, perhaps because there the application is behind a reverse
    # proxy. See  #281.
    captcha = ReCaptchaField(label=_('Confirmation text'),
                             help_text=_('As a security measure, please enter the previous words'))


class RegistrationFormNoCaptcha(UserCreationForm, UserEmailForm):
    """
    Registration form without captcha field
    """

    def __init__(self, *args, **kwargs):
        super(RegistrationFormNoCaptcha, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'wger-form'
        self.helper.layout = Layout(
            'username',
            'email',
            Row(
                Column('password1', css_class='form-group col-6 mb-0'),
                Column('password2', css_class='form-group col-6 mb-0'),
                css_class='form-row'
            ),
            ButtonHolder(Submit('submit', _("Register"), css_class='btn-success btn-block'))
        )


class FeedbackRegisteredForm(forms.Form):
    """
    Feedback form used for logged in users
    """
    contact = forms.CharField(max_length=50,
                              min_length=10,
                              label=_('Contact'),
                              help_text=_('Some way of answering you (email, etc.)'),
                              required=False)

    comment = forms.CharField(max_length=500,
                              min_length=10,
                              widget=widgets.Textarea,
                              label=_('Comment'),
                              help_text=_('What do you want to say?'),
                              required=True)


class FeedbackAnonymousForm(FeedbackRegisteredForm):
    """
    Feedback form used for anonymous users (has additionally a reCaptcha field)
    """
    captcha = ReCaptchaField(label=_('Confirmation text'),
                             help_text=_('As a security measure, please enter the previous words'),)
