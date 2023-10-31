from django import forms
from .models import Curso


class FormularioCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('id', 'nombre', 'inscripciones', 'turno')
        labels = {
            'nombre': 'Nombre',
            'inscripciones': 'Inscripciones',
            'turno': 'Turnos'
        }

        nombre = forms.CharField(max_length=128)
        inscripciones = forms.IntegerField()
        turno = forms.ChoiceField()
        
        #fecha_inicio = forms.DateField(
        #    label="Fecha de Inicio",
            #input_formats=["%d/%m/%Y"] # ---> dd/mm/AAAA
        #    widget=forms.DateInput(attrs={"type": "date"})
        #)


class FormularioPelicula(forms.Form):
    nombre = forms.CharField(label="Nombre de la Película", max_length=128)
    fecha_estreno = forms.DateField(
        label="Fecha de Estreno",
        widget=forms.DateInput(attrs={"type": "date"})
    )
    edad_minima = forms.IntegerField(label="Apta para Mayores de ...")
    preventa_online = forms.BooleanField(
        label="¿Con Preventa Online?",
        required=False
    )

