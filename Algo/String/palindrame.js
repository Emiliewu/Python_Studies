Algo 1:
/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @return {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) {
  newStr = "";
  for(i = 0; i < length; i++) {
    newStr += str[length-i-1];
  }
  if(newStr == str) {
    return true;
  }
  else {
    return false;
  }
}
function isPalindrome(str) {
  for(i = 0; i < length/2; i++) {
    if(arr[i] != arr[arr.length-1-i]){
      return false;
    }
  return true;
}
function isPalindrome(str) {
  let leftIdx = 0, rightIdx = str.length - 1;
  while (str[leftIdx] === str[rightIdx]) {
      leftIdx += 1;
      rightIdx -= 1;
      if (leftIdx >= rightIdx) {
          return true;
      }
  }
  return false;
}
module.exports = { isPalindrome };

/*****************************************************************************/
Ninja Bonus Algo:
/* 
  Longest Palindrome
  For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
  Strings longer or shorter than complete words are OK.
  All the substrings of "abc" are:
  a, ab, abc, b, bc, c
*/

const { isPalindrome } = require("./isPalindrome");

const str1 = "what up, daddy-o?";
const expected1 = "dad";

const str2 = "uh, not much";
const expected2 = "u";

const str3 = "Yikes! my favorite racecar erupted!";
const expected3 = "e racecar e";

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @return {string} The longest palindromic substring from the given string.
 */

function longestPalindromicSubstring(str) {
  for (var i = 0; i < str.length; i++) {
    if(str[i] == str[str.length -1-i]) {
      var idx = i;
      var j = str.length - i;
      while(j>0 && str[i+j] == str[j]){
        var count +=1;
        temp = j;
        j -= 1;
      }
      i += temp;
    }
  }     
  var newStr = substring(idx, count);
  return newStr;
}

module.exports = { longestPalindromicSubstring };

/*****************************************************************************/
function longestPalindrome(str) {
  var palArr = [];
  for(var i = 0; i < str.length-1; i++) {
      var leftIdx = rightIdx = tempL = tempR = 0, j = str.length-1;
      while(i < j) {
          var  palStr = "", equal = valid = false;
          if(str[i] != str[j]) {
              equal = false;
              j -= 1;
              continue;
          }
          if(!equal) {
              leftIdx = tempL = i;
              rightIdx = tempR = j;
          }
          equal = true;
          while(str[tempL] == str[tempR]) {
              tempL += 1;
              tempR -= 1;
              if(tempL >= tempR) {
                  valid = true;
                  break;
              }
          }
          if(valid) {
              palStr = str.substring(leftIdx, rightIdx+1);
              if(palStr.replace(/[^a-zA-Z]/g, ''))  palArr.push(palStr);
              break;
          }
          j -= 1;
      }
  }
  var longestPalArr = [];
  // var maxLen = palArr[0].length;
  // for(var i = 1; i < palArr.length; i++) {
  //     if(palArr[i].length > maxLen)  maxLen = palArr[i].length;
  // }
  let maxLen = Math.max(...palArr.map(x => x.length))
  for(var i = 0; i < palArr.length; i++) {
      if(palArr[i].length == maxLen)  longestPalArr.push(palArr[i]);
  }
  console.log(palArr);
  return longestPalArr;
}
console.log(longestPalindrome(str));