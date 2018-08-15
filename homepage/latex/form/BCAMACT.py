from django import forms

# importing BCA_MACT models:
# --------------------------
# Sem - 1
from ..models import  EI, FOM, ESASI, CFAO, ITL, PIC, CPL, LL
# Sem - 2
from ..models import EII, ESASII, RATI, OS, DSUC, OWCPP, SCAM, DSL, CPPL
# Sem - 3
from ..models import RATII, ES, CN, SE, ISF, PIJ, ITD, LJ, LD
# Sem - 4
from ..models import ES, MAAAD, SOSI, FODC, ITCT, BAP, ITCTL, BAPL, STAT, ITIL
# Sem - 5
from ..models import PS, FOS, MEABM, AAP, WTAVASIM, POV, SOSII, SOSIIL, AAPL, SIWVAMA, AS
# Sem - 6
from ..models import MT, ITWA, MPI

class EIForm(forms.ModelForm):
    class Meta:
        model = EI
        exclude = ('update_count',)

class FOMForm(forms.ModelForm):
    class Meta:
        model = FOM
        exclude = ('update_count',)

class ESASIForm(forms.ModelForm):
    class Meta:
        model = ESASI
        exclude = ('update_count',)

class CFAOForm(forms.ModelForm):
    class Meta:
        model = CFAO
        exclude = ('update_count',)

class ITLForm(forms.ModelForm):
    class Meta:
        model = ITL
        exclude = ('update_count',)

class PICForm(forms.ModelForm):
    class Meta:
        model = PIC
        exclude = ('update_count',)

class CPLForm(forms.ModelForm):
    class Meta:
        model = CPL
        exclude = ('update_count',)

class LLForm(forms.ModelForm):
    class Meta:
        model = LL
        exclude = ('update_count',)

class EIIForm(forms.ModelForm):
    class Meta:
        model = EII
        exclude = ('update_count',)

class ESASIIForm(forms.ModelForm):
    class Meta:
        model = ESASII
        exclude = ('update_count',)

class RATIForm(forms.ModelForm):
    class Meta:
        model = RATI
        exclude = ('update_count',)

class OSForm(forms.ModelForm):
    class Meta:
        model = OS
        exclude = ('update_count',)

class DSUCForm(forms.ModelForm):
    class Meta:
        model = DSUC
        exclude = ('update_count',)

class OWCPPForm(forms.ModelForm):
    class Meta:
        model = OWCPP
        exclude = ('update_count',)

class SCAMForm(forms.ModelForm):
    class Meta:
        model = SCAM
        exclude = ('update_count',)

class DSLForm(forms.ModelForm):
    class Meta:
        model = DSL
        exclude = ('update_count',)

class CPPLForm(forms.ModelForm):
    class Meta:
        model = CPPL
        exclude = ('update_count',)
