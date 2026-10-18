class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        String cur = "";
        backtrack(res, cur, n, 0, 0);
        return res;
    }
    private void backtrack(List<String> res, String cur, int n, int l, int r) {
        if (l==n && r==n) {
            res.add(cur);
            return;
        }
        if (r>=l) {
            backtrack(res, cur+'(', n, l+1, r);
        } else {
            if (l < n) {
                backtrack(res, cur + '(', n, l+1, r);
                backtrack(res, cur + ')', n, l, r+1);
            } else {
                backtrack(res, cur + ')', n, l, r+1);
            }
        }
        
    }
}
