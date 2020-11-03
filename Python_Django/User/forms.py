from django.contrib.auth import authenticate, get_user_model
from django import forms

User = get_user_model()

class UsersLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput,)

	def __init__(self, *args, **kwargs):
		super(UsersLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"username"})
		self.fields['password'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"password"})

	def clean(self, *args, **keyargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username = username, password = password)
			if not user:
				raise forms.ValidationError("This user does not exists")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("User is no longer active")

		return super(UsersLoginForm, self).clean(*args, **keyargs)


class UsersRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			"email",
			"password",
			"confirm_email",
			"confirm_password", 
			"username",
            "first_name",
            "last_name",
		]
	username = forms.CharField()
	email = forms.EmailField(label = "Email")
	confirm_email = forms.EmailField(label = "Confirm Email")
	password = forms.CharField(widget = forms.PasswordInput)
	confirm_password = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput)
	first_name = forms.CharField()
	last_name = forms.CharField()
	

	def __init__(self, *args, **kwargs):
		super(UsersRegisterForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"username"})
		self.fields['email'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"email"})
		self.fields['confirm_email'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"confirm_email"})
		self.fields['password'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"password"})
		self.fields['confirm_password'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"confirm_password"})	
		self.fields['first_name'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"first_name"})
		self.fields['last_name'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"last_name"})
	


	def clean(self, *args, **keyargs):
		email = self.cleaned_data.get("email")
		confirm_email = self.cleaned_data.get("confirm_email")
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		confirm_password = self.cleaned_data.get("confirm_password")

		if email != confirm_email:
			raise forms.ValidationError("Email must match")
		
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Email is already registered")

		username_qs = User.objects.filter(username=username)
		if username_qs.exists():
			raise forms.ValidationError("User with this username already registered")
		
		#you can add more validations for password

		if len(password) < 8:	
			raise forms.ValidationError("Password must be greater than 8 characters")


		return super(UsersRegisterForm, self).clean(*args, **keyargs)

		if password != confirm_password:
			raise forms.ValidationError("Password must match")
 

