// BUCLE FOR

// for (inicialización; condición; expresión de actualización) {
        // Bloque de código a repetir
//}

/* 
- inicialización: variable de control que se inicializa antes que comience el bucle
- condición: Se evalúa una condición que dará verdadero o falso
- actualización: expresión que se evalúa después de cada iteración

for(let i = 1; i <= 5; i++) {
    console.log(i);
}

EJEMPLO
#######

var empleados = [
    {
        nombre: 'Juan',
        apellido: 'Gonzalez',
        edad: 40
    },
    {
        nombre: 'Ana',
        apellido: 'Gutierrez',
        edad: 25
    },
    {
        nombre: 'Fernando',
        apellido: 'Perez',
        edad: 34
    }
]

var mensaje = '';

for(let i = 0; i < empleados.length; i++) {
    mensaje += empleados[i].nombre + ' ' + empleados[i].apellido + ' - ';
}

console.log(mensaje);

*/

var contar, numero, mensaje='';

numero = parseInt(prompt("Coloque un numero entero"));
for(contar = numero; contar > 0;  contar--) {
  mensaje += contar + ", ";
}
mensaje += contar; 
alert(mensaje);


// Clase siguiente a la del 27-7

// let o const - tienen ambito de bloque
// var - Tiene un alcance de Función

// SCOPE

// Global - Variables y Funciones pueden ser accedidas desde cualquier parte del código

// Local - Todas las variables o funciones declaradas dentro de otra función tienen alcance local
//          o en caso de variables let y const tienen alcance local dentro de otros bloques

/*
var articulo = prompt("Nombre del artículo"); // variable global
var precio = parseInt(prompt("Precio del artículo")); // variable global

producto();

function producto() {
    var iva = 1.21; // variable local
    precioConIva = precio * iva; // variable global
    var mensaje = "El artículo " + articulo + " cuesta $ " + precio + " (IVA no incluido)"; // variable local

    console.log(mensaje);
}

console.log("El precio con IVA incluido es de: " + precioConIva.toFixed(2));
*/

// FUNCIONES
/*
function saludar() {
    console.log("Hola!");
}

function sumar(a, b) {
    return a + b;
}

saludar();

var resultado = sumar(5, 5);
console.log(resultado);
*/

// TIPOS DE FUNCIONES

// Funciones Anónimas
/*
const saludar = function(nombre) {
    console.log('Hola, ' + nombre + '!');
};

saludar('Carlos');

// Arrow Functions o Funciones de Flecha

const saludo = (nombre) => {
    console.log('Hola, ' + nombre + '!');
};

saludo('María');
*/

// CLOSURES
/*
function contador() {
    let cuenta = 0;

    function incrementar() {
        cuenta++; // Se incrementa en 1
        console.log(cuenta); // devuelve por consola
    }

    return incrementar;
}

const contador1 = contador();
contador1();
contador1();
contador1();
contador1();
contador1();
*/

// Funcion pasada como argumento
/*
function ejecutarFuncion(func) {
    func(); // saludar();
}

function saludar() {
    console.log('Hola!');
}

ejecutarFuncion(saludar);

// Devolver funciones como valores

function crearFuncion() {
    return function() {
        console.log("Función devuelta");
    };
}

const miFuncion = crearFuncion();
miFuncion();
*/
// Recursividad
/*
function factorial(n) {
    if (n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

console.log(factorial(5)); // devuelve 120
*/
/*
n = 5 -> 5 * factorial(5 - 1)
n = 4 -> 4 * factorial(4 - 1)
n = 3 -> 3 * factorial(3 - 1)
n = 2 -> 2 * factorial(2 - 1)
n = 1 -> 1 * factorial(1 - 1)
n = 0 -> 1

1 * 1 = 1
2 * 1 = 2
3 * 2 = 6
4 * 6 = 24
5 * 24 = 120
*/ 

// THIS -> ESTO
/*
const persona = {
    nombre: 'Juan',
    saludar: function() {
        console.log(this.nombre);
    },
};

persona.saludar();
*/
// Métodos y Propiedades de las Funciones

//El objeto Function
/*
function sumar(a, b) {
    return a + b;
}

console.log(typeof sumar); 
console.log(sumar instanceof Function);

// length

console.log(sumar.length);
*/
// Método bind() - crea una nueva función con un valor de this específico, sin llamar a la función
// original
/*
function saludo() {
    console.log ('Hola, ' + this.nombre + '!');
}

const hombre = {
    nombre: 'Julieta'
};

const saludarPersona = saludo.bind(hombre);
saludarPersona();

// Funciones setTimeout() y setInterval()

function levantarLaMano() {
    console.log("Levanté la mano");
}
*/
//setTimeout(levantarLaMano, 2000); // Ejecuta la función luego de trascurridos "x" milisegundos

//setInterval(levantarLaMano, 2000); // Ejecuta la función cada "x" cantidad de tiempo


// EVENTOS
/*
function miFuncion(nombre) {
    console.log("Hola, " + nombre);
}

var boton = document.getElementsByTagName('button');

for(var i = 0; i < boton.length; i++) {
    boton[i].onclick = function() {
        miFuncion(this.innerHTML);
    };
}*/

var boton = document.querySelectorAll('button');

for(var i = 0; i < boton.length; i++){
    
        boton[i].onclick = function(){
            console.log("El color es: " + this.innerHTML);
        };
        
    }
