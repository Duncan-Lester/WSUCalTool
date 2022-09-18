from django import forms


class scraperForm(forms.Form):
    term_choices = [
        ('1','Spring'),
        ('2','Summer'),
        ('3','Fall'),
        ]
    campus_choices = [
        ('Pullman','Pullman'),
        ('DDP','Global Campus'),
        ('Spokane','Spokane'),
        ('Tri-Cities','Tri-Cities'),
        ('Vancouver','Vancouver'),
        ('Everett','Everett')]
    your_campus = forms.ChoiceField(label='Your Campus', choices= campus_choices)
    your_year = forms.CharField(label='Your class year:', max_length=4)
    your_term = forms.ChoiceField(label='Your academic term:', choices= term_choices)
    your_subject = forms.CharField(label='Your class prefix:')
    your_crn = forms.CharField(label='Your Class Number:', max_length=3)

