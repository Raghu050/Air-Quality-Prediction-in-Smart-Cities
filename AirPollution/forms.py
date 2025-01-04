from django import forms

class CSVUploadForm(forms.Form):
    file = forms.FileField()

# forms.py
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import AirQuality

class AirQualityForm(forms.ModelForm):
    District = forms.CharField()
    CO = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    NMHC = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    C6H6 = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    NO2 = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    temp = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    humidity = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)])

    class Meta:
        model = AirQuality
        fields = ['District', 'CO', 'NMHC', 'C6H6', 'NO2', 'temp', 'humidity']


# forms.py
from django import forms

class AirQualityForm(forms.Form):
    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop('exclude', [])
        super(AirQualityForm, self).__init__(*args, **kwargs)
        
        if 'absolute_humidity' in exclude_fields:
            del self.fields['absolute_humidity']

    date = forms.DateField(label='Date', input_formats=['%d/%m/%Y'])
    time = forms.TimeField(label='Time', input_formats=['%H.%M.%S'])
    co = forms.FloatField(label='CO(GT)', required=False)
    pt08_s1_co = forms.FloatField(label='PT08.S1(CO)', required=False)
    nmhc = forms.FloatField(label='NMHC(GT)', required=False)
    c6h6 = forms.FloatField(label='C6H6(GT)', required=False)
    pt08_s2_nmhc = forms.FloatField(label='PT08.S2(NMHC)', required=False)
    nox = forms.FloatField(label='NOx(GT)', required=False)
    pt08_s3_nox = forms.FloatField(label='PT08.S3(NOx)', required=False)
    no2 = forms.FloatField(label='NO2(GT)', required=False)
    pt08_s4_no2 = forms.FloatField(label='PT08.S4(NO2)', required=False)
    pt08_s5_o3 = forms.FloatField(label='PT08.S5(O3)', required=False)
    temperature = forms.FloatField(label='Temperature (°C)', required=False)
    relative_humidity = forms.FloatField(label='Relative Humidity (%)', required=False)
