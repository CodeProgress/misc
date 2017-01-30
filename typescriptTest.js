// Typescript test
function greet(name) {
    return "Hello, " + name;
}
var me = "Me";
console.log(greet(me));
// create project within folder using cmd line:
// tsc --init
// Boolean
var isDone = false;
// Numbers
var myNum = 4;
// Text, string
var aName = "Name";
// Template strings
var oldGreeting = "Hello, " + aName;
var greeting = "Hello, " + aName;
// Arrays
var odds = [1, 3, 5];
var evens = [2, 4, 6];
// Unknown type (Avoid using this)
var anything = 4;
anything = "Text";
anything = false;
// Returning nothing
function logSomeText(name) {
    console.log("Some text.");
}
// Enums
var arrowkeyPressed = 1;
// automatically creates indexed array for values
var Directions;
(function (Directions) {
    Directions[Directions["Up"] = 0] = "Up";
    Directions[Directions["Down"] = 1] = "Down";
    Directions[Directions["Left"] = 2] = "Left";
    Directions[Directions["Right"] = 3] = "Right";
})(Directions || (Directions = {}));
;
if (arrowkeyPressed === Directions.Down) {
    console.log("Down arrow pressed");
}
