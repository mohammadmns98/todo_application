import datetime, pytz
from django import forms
from .models import Work


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class UserCreateTask(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
        exclude = ('status',)
        widgets = {'end_date': DateTimeInput()}

    def clean_end_date(self):
        end_date = self.cleaned_data["end_date"]
        date_create = datetime.datetime.now()
        utc = pytz.utc

        if not end_date:
            return end_date

        if end_date.replace(tzinfo=utc) <= date_create.replace(tzinfo=utc):
            raise forms.ValidationError('End date can not be lower than current date')

        return end_date
