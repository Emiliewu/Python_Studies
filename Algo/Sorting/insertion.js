arr = [9,3,1,4,5,9,7,8,11,10];
function insertion(arr) {
  count = 0;
  for(var i = 1; i < arr.length; i++) {
    while(i > 0 && arr[i-1] > arr[i]) {
      [arr[i-1], arr[i]] = [arr[i], arr[i-1]];
      count += 1;
      i -= 1;
    }
  }
  return count, arr;
}
console.log(insertion(arr), count);