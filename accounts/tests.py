from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse
from accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import json


# class TestViews(SimpleTestCase):
#     def test_views(self):
#         client = Client()
#         response = client.get(reverse('player-words', args=['somename']))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'accounts/profile.html')

# fields = ['username', 'email', 'password1', 'password2']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']


class TestForms_Registration(TestCase):

    def test_registration_form_with_data(self):
        form = UserRegisterForm(data={
            'username':'RediTest',
            'email':'RediTest@gmail.com',
            'password1':'1234helloworld',
            'password2':'1234helloworld'
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_no_data(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

class TestForms_UserUpdate(TestCase):
    def test_userupdate_form_no_data(self):
        form = UserUpdateForm(data={
            'username':'RediTest',
            'email':'RediTest@gmail.com'
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

class TestForms_ProfileUpdate(TestCase):
    def test_profileupdate_form_no_data(self):
        form = ProfileUpdateForm(data={
            'image':'RediTest.jpg'
        })
        print("form", form)
        self.assertTrue(form.is_valid())
        # form = UserRegisterForm(data={})
        # self.assertFalse(form.is_valid())
        # self.assertEquals(len(form.errors), 2)

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
