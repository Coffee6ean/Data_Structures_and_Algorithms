// What is the Big O of the below function? (Hint, you may want to go line by line)
function funChallenge(input) {
    let a = 10;
    a = 50 + 3;
  
    for (let i = 0; i < input.length; i++) { //O(n)
      anotherFunction(); //O(1)
      let stranger = true; //O(1)
      a++; //O(1)
    }
    return a;
  }

//A: 0(n)
/* 
Exp:
- The function's runtime grows linearly with the size of the input array (input.length).
- The constant-time operations (O(1)) outside and inside the loop become insignificant compared to the loop itself when n is large.

Therefore, the overall time complexity is O(n). 
*/
