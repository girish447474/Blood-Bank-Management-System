from django import forms
from bloodcamps.models import bloodcamp,bloodcampdonor
class newcamp(forms.ModelForm):
    class Meta:
        model=bloodcamp
        fields='__all__'
class newdonor(forms.ModelForm):
    class Meta:
        model=bloodcampdonor
        fields='__all__'
class newupcomingcamp(forms.ModelForm):
    class Meta:
        model=bloodcamp
        fields='__all__'