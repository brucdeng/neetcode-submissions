class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(res, cur, nums, used);
        return res;
    }

    private void backtrack(List<List<Integer>> res, List<Integer> cur, int[] nums, boolean[] used) {
        if (cur.size()==nums.length) {
            res.add(new ArrayList<>(cur));
            return;
        }
        for (int i = 0; i <nums.length; i++) {
            if (!used[i]) {
                cur.add(nums[i]);
                used[i] = true;
                backtrack(res, cur, nums, used);
                cur.remove(cur.size()-1);
                used[i] = false;
            }

        }
    } 
}
