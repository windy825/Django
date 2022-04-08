from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    genre_1 = '코미디'
    genre_2 = '공포/스릴러'
    genre_3 = '액션'
    genre_4 = '전쟁'
    genre_5 = '판타지'
    genre_6 = '뮤지컬'
    genre_7 = 'SF'
    genre_8 = '스포츠'
    genre_9 = '음악'

    GENRE_CASE = [
        (genre_1, '코미디'),
        (genre_2, '공포/스릴러'),
        (genre_3, '액션'),
        (genre_4, '전쟁'),
        (genre_5, '판타지'),
        (genre_6, '뮤지컬'),
        (genre_7, 'SF'),
        (genre_8, '스포츠'),
        (genre_9, '음악'),
    ]
    genre = forms.ChoiceField(choices=GENRE_CASE, widget=forms.Select())

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'step': '.5',
                'min': '0',
                'max': '5',
            }
        )
    )

    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'