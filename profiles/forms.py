form django import forms 
from .models impor UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):

        """
        Add placeholder and classes remove
        auto-generated labels
        """
    super().__init__(*args, **kwargs)
    placeholders = {
        'default_phone_number': 'Phone Number',
        'default_postcode': 'Poste Code',
        'default_town_or_city': 'Town or City',
        'default_street_address1': 'Street Adress 1',
        'default_street_address2': 'Street Adress 2',
        'default_county': 'County or Locality'
    }

     self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False

