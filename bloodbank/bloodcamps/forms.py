from django import forms
from bloodcamps.models import bloodcamp,bloodcampdonor
class newcamp(forms.ModelForm):
    class Meta:
        model=bloodcamp
        fields=('campid','startdate','enddate','location')
class newdonor(forms.ModelForm):
    class Meta:
        model=bloodcampdonor
        fields='__all__'
