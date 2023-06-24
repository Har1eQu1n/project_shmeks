from django.test import TestCase

from main.forms import UserRegistrationForm

class UserRegistrationFormTest(TestCase):
    def test_registration_form_password_field_label(self):
        form = UserRegistrationForm()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Пароль')

    def test_registration_form_password2_field_label(self):
        form = UserRegistrationForm()
        self.assertTrue(form.fields['password2'].label == None or form.fields['password2'].label == 'Повтор пароля')

    def test_registration_form_password_equal_password2(self):
        form = UserRegistrationForm()
        form.fields['password'] = '12345poRARA!'
        form.fields['password2'] = '12345poRARA!'
        self.assertEqual(form.fields['password'], form.fields['password2'])