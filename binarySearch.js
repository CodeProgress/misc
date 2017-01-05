
function binarySearch(needle, haystack){
    var start = 0;
    var end = haystack.length - 1;
    var mid =  Math.floor(end/2);

    while (start < end){
        if (haystack[mid] < needle){
            start = mid + 1;
        } else if (haystack[mid] > needle){
            end = mid - 1;
        } else {
            return mid;
        }
        mid =  Math.floor(start + (end-start)/2);
    }
    
    return haystack[mid] == needle ? mid : -1;
}

function getRandomSortedArray(numVals, limit){
    var numArray = [];
    for(var i = 0; i < numVals; i++){
        var randomInt = Math.floor(Math.random()*limit);
        numArray.push(randomInt);
    }
    
    numArray.sort(function(a, b){return a-b});

    return numArray;
}

var randomSortedArray = getRandomSortedArray(100, 100);
var numToFind = 50;

console.log(binarySearch(numToFind, randomSortedArray));
