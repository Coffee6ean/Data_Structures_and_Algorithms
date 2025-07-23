// What is the Big O of the below function? (Hint, you may want to go line by line)
function anotherFunChallenge(input) {
    let a = 5; // O(1)
    let b = 10; // O(1)
    let c = 50; // O(1)
    for (let i = 0; i < input; i++) { // O(n)
        let x = i + 1; // O(n)
        let y = i + 2; // O(n)
        let z = i + 3; // O(n)

    }
    for (let j = 0; j < input; j++) { // O(n)
        let p = j * 2; // O(n)
        let q = j * 2; // O(n) 
    }
    let whoAmI = "I don't know"; // O(1)
}


//A: O(n)
/* 
Exp:
- The function has two separate loops, each running n times. However, since they are not nested, their time complexities add up rather than multiply.
- The rule for adding time complexities is:
    O(n) + O(n) = O(n)

*The constant-time operations (O(1)) do not affect the overall complexity for large values of n
*/
