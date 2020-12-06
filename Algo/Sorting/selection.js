arr = [9,3,1,4,5,9,7,8,11,10]
function selection(arr) {
  count = 0;
  for(var i = 0; i < arr.length-1; i++) {
    min_index = i;
    for(var j = i+1; j < arr.length; j++ ) {
      if(arr[j] < arr[min_index]) {
        min_index = j;
        count += 1;
      }
    }
    if(min_index != i) {
      [arr[i], arr[min_index]] = [arr[min_index], arr[i]];
    }
  }
  return count, arr;
}
console.log(selection(arr), count);