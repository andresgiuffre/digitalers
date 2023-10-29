from django import forms


class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    inscripciones = forms.IntegerField(label="Inscriptos")
    solo_empresas = forms.BooleanField(label="Solo empresas?", required=False)
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche")
    )
    turno = forms.ChoiceField(label="Turno", choices=TURNOS)
    fecha_inicio = forms.DateField(
        label="Fecha de Inicio",
        #input_formats=["%d/%m/%Y"] # ---> dd/mm/AAAA
        widget=forms.DateInput(attrs={"type": "date"})
    )


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

