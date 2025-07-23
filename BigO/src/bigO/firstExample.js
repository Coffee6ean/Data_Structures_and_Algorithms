/* const nemo = ["nemo"];
const everyone = [
    "dory", "bruce", "marlin", 
    "nemo", "gill", "bloat", 
    "nigel", "squirt", "darla", 
    "hank"
];
const large = new Array(1000).fill("nemo");

function findNemo(array) {
    let t0 = performance.now();

    for (let i = 0; i < array.length; i++) {
        if(array[i] === "nemo") {
            console.log("Found Nemo!");
            break;
        }
    }

    let t1 = performance.now();
    console.log("Call: " + (t1-t0));
}

findNemo(large); // 0(n) -> Linear Time */

/* const boxes = [0,1,2,3,4,5];

function logFirstTwoBoxes(boxes) {
    console.log(boxes[0]);
    console.log(boxes[1]);
}

logFirstTwoBoxes(boxes); // 0(2) = 0(1) -> Constant Time */


//Log all pairs of array
const arr = [1,2,3,4,5]

function logPairs(array) {
    let result = []
    array.forEach(item => {
        for (let i = 0; i < array.length; i++) {
            if (arr[i] != item) {
                result.push([item, arr[i]]);
            }
        }
    });
    
    console.log(result);
    console.log("Number of pairs: " + result.length)
    return result;
}

logPairs(arr); // O(n^2)