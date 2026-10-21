class Solution {
    public List<List<String>> partition(String s) {
        // add a letter or add 2 letters if palindrome or add 3 letters if palindrome...
        List<String> cur = new ArrayList<>();
        List<List<String>> res = new ArrayList<>();
        backtrack(s, 0, cur, res);
        return res;
    }
    private void backtrack(String s, int ind, List<String> cur, List<List<String>> res) {
        if (ind >= s.length()) {
            res.add(new ArrayList<>(cur));
            return;
        }
        for (int i = ind; i < s.length(); i++) {
            String temp = s.substring(ind, i+1);
            if (isPalindrome(temp)) {
                cur.add(temp);
                backtrack(s, ind+temp.length(), cur, res);
                cur.remove(cur.size()-1);
            }
        }
    }
    private boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l)!=s.charAt(r)) {
                return false;
            }
            l+=1;
            r-=1;
        }
        return true;
    }
}
