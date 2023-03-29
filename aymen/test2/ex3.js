/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function (arr) {
  let res = []
  let i = 0
  while (res.length < arr.length) {
    if (arr[i] === 0) {
      res.push(0)
      if (res.length < arr.length) {
        res.push(0)
      }
    } else {
      res.push(arr[i])
    }
    i++
  }
  return res
};
console.log(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
