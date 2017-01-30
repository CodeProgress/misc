// Typescript test
function greet(name: string){
    return "Hello, " + name;
}
var me = "Me";
console.log( greet(me));

// create project within folder using cmd line:
// tsc --init

// Boolean
let isDone: boolean = false;

// Numbers
let myNum: number = 4;

// Text, string
let aName: string = "Name";

// Template strings
let oldGreeting: string = "Hello, " + aName;
let greeting: string = `Hello, ${aName}`;

// Arrays
let odds: number[] = [1, 3, 5];
let evens: Array<number> = [2, 4, 6];

// Unknown type (Avoid using this)
let anything: any = 4;
anything = "Text";
anything = false;

// Returning nothing
function logSomeText(name: string): void {
    console.log("Some text.");
}

// Enums
let arrowkeyPressed = 1;

// automatically creates indexed array for values
enum Directions{ Up, Down, Left, Right};

if (arrowkeyPressed === Directions.Down){
    console.log("Down arrow pressed");
}

