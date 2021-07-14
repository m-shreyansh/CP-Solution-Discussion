from django import forms

class new_sol_form(forms.Form):
	question = forms.IntegerField()
	hint = forms.CharField()
	solution = forms.CharField(widget=forms.Textarea)
	code = forms.CharField(widget=forms.Textarea)

class login_form(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

class textArea(forms.Form):
	content = forms.CharField(widget=forms.Textarea)
