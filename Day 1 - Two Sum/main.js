const nums = [3, 3]
const target = 6

function twoSum(nums, target) {
    for (var i = 0; i <= nums.length; i++) {
        for (var j = 0; j <= nums.length; j++) {
            if (i === j) continue
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
}

console.log(twoSum(nums, target))