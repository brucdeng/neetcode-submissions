class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> vals = new ArrayList<>();
        backtrack(0, res, vals, nums, target, 0);
        return res;
    }
    private void backtrack(int curSum, List<List<Integer>> res, List<Integer> vals, int[] nums, int target, int start) {
        if (curSum == target) {
            res.add(new ArrayList<>(vals));
            return;
        }
        for (int i = start; i < nums.length; i++) {
            if (curSum + nums[i] <= target) {
                vals.add(nums[i]);
                backtrack(curSum+nums[i], res, vals, nums, target, i);
                vals.remove(vals.size() -1);
            }
        }
    }
}
