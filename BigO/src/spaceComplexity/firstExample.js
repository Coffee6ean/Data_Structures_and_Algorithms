//Determine the Space Complexity of each function
function boo(array) {
    for (let i = 0; i < array.length; i++) {
        console.log("Booooo!!");
    }
}

boo([1,2,3,4,5]) 

//A: SpC = O(1)
/* 
Exp:
The function boo takes an array as input but does not create any additional data structures that depend on the input size.
The only variables used are:
- i: A single integer used in the loop.
- array: The input array, but it is not copied or modified.

Since the memory usage does not grow with the input size, the Space Complexity is constant, or O(1).
*/

function arrayOfHiNTimes(array) {
    let hiArray = [];
    for (let i = 0; i < array.length; i++) {
        hiArray[i] = "hi";
    }
    return hiArray;
}

arrayOfHiNTimes(6) 
//A: O(n)
/* 
Explanation:
The function arrayOfHiNTimes creates a new array (hiArray) of size n.
The memory usage depends on the input size n because:
- The array hiArray grows linearly with n.
- Each element in the array requires a fixed amount of memory.

Therefore, the Space Complexity is linear, or O(n). 
*/
