// ECMAScript

// ECMA - European Computer Manufacturers Association

// ECMAScript 1 (ES1) (ES2) (ES6) (ES 2016) ES 2020

// var - Nos permitia hacer reasignacion y redefinicion

// reasignacion: cambiar el dato actual
// redefinicion: cambiar su ubicacion en la memoria

// const - variables no se pueden redefinir ni reasignarse
// let - variables que no se pueden redefinir pero SI reasignarse

// Funciones flecha (Arrow Functions)

/*
const sumar = (a, b) => {
    return a + b;
} // Función flecha standard

const sumar2 = (a, b) => a + b; // Escribir una función como expresión
console.log(sumar2(2, 3));

// String Templates
edad = 20;

console.log("María tiene " + edad + " años.");

console.log(`María tiene ${edad} (con String Template)`) // AltGr - ]

function saludar() {
    const nombre = prompt("Ingresá tu nombre:");
    const mensaje = `Hola, ${nombre}! Bienvenido a mi página`;
    const saludo = document.getElementById("saludo");
    saludo.innerHTML = mensaje;
}
*/

// Librerías
// jQuery
/*
const contenedor1 = $('#id1');
const contenedor2 = $('.class1');
const botones = $('button');

console.log($('#id1'));
console.log(contenedor2);
console.log(botones);
*/

// Disparar eventos en 1 botón - Método 1
// Ubica el botón con id #saludo, cuando hacemos click ejecuta la función
// que le pasamos por parámetro.
/*
$('#saludo').on('click', function() {
    console.log('Hiciste click en el botón');
});

// Disparar eventos en 1 botón - Método 2
$('#saludo').click(function(){
    console.log('Hiciste click con el Método 2');
});
*/
// $.get(url, function())
/*
$('#datos').click(function(){
    const url = 'https://jsonplaceholder.typicode.com/posts/';
    $.get(url, function(data){
        $('#id1').html('Se descargaron los datos correctamente');
        console.log(data);
    });
});
*/

// Handlebars
/*
const contenedor1 = document.getElementById('contenedor');
const plantilla = Handlebars.compile(`
    <h2>Bienvenido a esta página con Handlebars!, {{ nombre }}.</h2>
    {{#each series}}
        {{#if netflix}}
            <p>Podés ver {{ serie }} en Netflix</p>
        {{else}}
            <p>{{ serie }} no está en Netflix</p>
        {{/if}}
        {{#unless hayLuz}}
            <p>Te cortaron la luz</p>
        {{/unless}}
    {{/each}}
`);

contenedor1.innerHTML = plantilla({ 
    nombre: "Sebastián",
    series: [{
            netflix: true,
            serie: "The Witcher",
            hayLuz: true,
        },
        {
            netflix: false,
            serie: "House of the Dragon",
            hayLuz: true,
        },
        {
            netflix: true,
            serie: "Sweet Tooth",
            hayLuz: true,
        }
    ]    
});

// Helpers en handlebars

// Helpers se ponen entre 2 juegos de llaves. Para apertura se usa {{#if}}
// Para el cierre del bloque se usa {{/if}}
*/

var array = [7, 3, 5, 51, 38];

function ordenar(array){
    array.sort((a, b) => a - b);
    return array;
}

function guardar(array){
    var array2 = [];
    array2.push(array[1], array[array.length - 2]);
    return array2;
}

console.log(guardar(ordenar(array)));