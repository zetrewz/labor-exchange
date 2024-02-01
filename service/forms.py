from django.forms import Form, CharField


class SearchForm(Form):
    query = CharField()
