class Solution {
    public boolean exist(char[][] board, String word) {
        boolean[][] used = new boolean[board.length][board[0].length];
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (backtrack(board, 0, word, used, r, c)) {
                    return true;
                }
            }
        }
        return false;
    }
    private boolean backtrack(char[][] board, int index, String word, boolean[][] used, int r, int c) {
        
        if (used[r][c] || board[r][c] != word.charAt(index)) {
            return false;
        }
        if (index==word.length()-1) {
            return true;
        }
        used[r][c] = true;
        int[][] rc = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int[] x : rc) {
            int tempr = r + x[0];
            int tempc = c + x[1];
            if (tempr >= 0 && tempr < board.length && tempc >=0 && tempc < board[0].length) {
                if (backtrack(board, index+1, word, used, tempr, tempc)) {
                    used[r][c] = false;
                    return true;
                }
            }
        }
        used[r][c] = false;
        return false;
    }
}
