// Esta es una línea de comentarios

/*
Estas son
varias
líneas de
comentarios
*/

/*
//alert('Hola de nuevo');

var edad = 25; // entero
var precio = 15.40; // float
var cadenaDeTexto = "Esta es un String" // string
var pregunta = false; // booleano
var noDefinido = undefined;

var persona = {
    nombre: 'Juan', // Key: value pair
    edad: 30,
    ciudad: 'CABA'
};

// Array
const numeros = [1, 2, 3, 4, 5];
/*
console.log(numeros[0]); // Elemento 1
console.log(numeros.length); // Cantidad de elementos
numeros.push(6); // Agrega un elemento AL FINAL del ARRAY
console.log(numeros);
numeros.pop(); // Elimina el último elemento del array
console.log(numeros);
numeros.forEach(numero => {
    console.log(numero);
});
*/
/*
//
document.write('<h1>Hola como te va</h1>');
document.write('<p>Esto es un <strong>párrafo</strong>.</p>');
//

//var nombre = prompt('Ingrese su nombre:');
//var age = prompt('Ingrese su edad');
//var confirmacion = confirm('Su nombre es ' + nombre + ' y tiene ' + age + ' años.\nConfirma los datos?');
/*
console.log(edad);
edad++;
console.log(edad);
edad--;
console.log(edad);
*/
/*
var suma = 1 + 1; // Operador de Suma
var resta = 2 - 1; // Operador de resta
var mult = 2 * 4; // Operador de multiplicación
var division = 10 / 2; // Operador de división
var modulo = 10 % 2; // Operador de módulo

//console.log("La variable suma da como resultado " + suma);

//console.log(!pregunta);
var vacio = !suma; 
//console.log(vacio);

// && y || ->and y or

var valorA = true;
var valorB = false;

resultado1 = valorA && valorB;
resultado2 = valorA || valorB;

//console.log("El resultado de && es: " + resultado1);
//console.log("El resultado de || es: " + resultado2);

// Operadores Relacionales

var numero1 = 1;
var numero2 = 20;

resultado = numero1 > numero2; // false
resultado = numero1 < numero2; // true

numero1 = 10;
numero2 = 10;
resultado = numero1 >= numero2; // true
resultado = numero1 <= numero2; // true
resultado = numero1 == numero2; // true
resultado = numero1 != numero2; // false

// Operador de igualdad estricta ===
console.log(5 == 5); // true
console.log(5 == '5'); // true
console.log(5 === '5'); // false
console.log(5 === 5); // true

numb1 = 500;
numb2 = 200;
console.log("La suma de los valores es " + (parseInt(numb1) + parseInt(numb2)));

// parseInt() 
// parseFloat()

// NaN -> Not a Number
*/
/*
let sueldo = parseInt(prompt('Ingrese su sueldo'));
let bonus = parseInt(prompt("Ingrese su bonus"));

let total = sueldo + bonus;

alert("Gana por mes: " + total)
*/
/*
var edad = prompt("Cual es tu edad?:");

if (edad >= 20) {
    let nombre = prompt("Cuál es tu nombre?:");
    if (nombre == "Pedro") {
        alert("Hola Pedro");
    } else {
        alert("Tenés 20 años o más pero tu nombre no es Pedro");
    }
} else {
    alert("Tenés menos de 20 años");
}
*/

// SWITCH (Switch - Case)
//--------
/*
var estadoCivil = prompt("Cuál es su estado civil?:");

switch(opciones) {
    case 1:
        //Ejecuta un bloque de código
        break;
    case 2:
        console.log('Estás casado!');
        break;
    case 3:
        console.log('Estás divorciado!');
        break;
    case 'viudo':
        console.log('Lo siento');
        break;
    default:
        console.log('No reconozco ese estado civil');
        break;
}
*/

// La Clase Date()
//----------------

/*
var fecha = new Date();
var dia = fecha.getDate();
var diaDeLaSemana = fecha.getDay();
var mes = fecha.getMonth();
var anio = fecha.getFullYear();

var meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
var semana = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'];

mes = meses[mes];
diaDeHoy = semana[diaDeLaSemana];

document.write("Hoy es " + diaDeHoy + " " + dia + " de " + mes + " del año " + anio);
document.write(typeof(fecha));

console.log(diaDeLaSemana);


// getElementById()
//-----------------

//var enunciado = document.getElementById('enunciado');
//console.log(enunciado.innerHTML);
//enunciado.innerHTML = "Este es mi H1 modificado";
//console.log(enunciado.innerHTML);

//var otro_enunciado = document.querySelectorAll('h1');
//console.log(otro_enunciado[1].innerHTML);

// WHILE y DO WHILE
//-----------------
/*
var incremento = 60;
var maximo = 50;

/*while(incremento <= maximo) {
    // Bloque de codigo a ejecutar
    incremento++;
    console.log(incremento);
}*/
/*
do {
    // Bloque de código a ejecutar
    incremento++;
    document.write('Incremento vale: ' + incremento);
} while (incremento <= maximo);
*/
/*
var nombre;
var edad;
var categoria;

do {
    let respuestaCorrecta = false;
    while(!respuestaCorrecta) {
        nombre = prompt("Ingrese su nombre:");
        edad = prompt("Ingrese su edad:");
        categoria = prompt("Asigne una categoría: A2 - B4 - C6 - F8");

        switch(categoria) {
            case 'A2':
                respuestaCorrecta = true;
                break;
            case 'B4':
                respuestaCorrecta = true;
                break;
            case 'C6':
                respuestaCorrecta = true;
                break;
            case 'F8':
                respuestaCorrecta = true;
                break;
            default:
                alert("La categoría elegida no existe. Intente nuevamente.");
                break;
        }
    }
} while (!confirm('Desea guardar los datos?'));

document.write('Su nombre es ' + nombre + ', su edad es de ' + edad + ' años y su categoría es ' + categoria);
*/
/*
var num1 = prompt("Ingrese un numero");
var num2 = prompt("Ingrese un segundo numero");
var num3 = prompt("Ingrese un tercer numero");

if (num1 > num2 && num1 > num3) {
    alert("El numero mayor es " + num1 + " que es el primer ejemplo");
}
else if (num2 > num1 && num2 > num3) {
    alert("El numero mayor es " + num2 + " que es el 2do");
}
else if (num3 > num1 && num3 > num2) {
    alert("El numero mayor es " + num3 + " que es el 3ero");
}
else {  
    alert("Los numeros son iguales");
}
*/

