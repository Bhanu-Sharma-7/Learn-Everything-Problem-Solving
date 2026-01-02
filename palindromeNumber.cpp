class Solution {
public:
    bool isPalindrome(int x) {
        // Special cases:
        // 1. x < 0: Negative numbers are not palindromes.
        // 2. x % 10 == 0: Numbers ending in 0 (except 0) are not palindromes.
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int revertedNumber = 0;
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }

        // When the length is odd, we can get rid of the middle digit by revertedNumber/10
        // For example, for 121: 
        // x = 1, revertedNumber = 12. 
        // 1 == 12/10 is true.
        return x == revertedNumber || x == revertedNumber / 10;
    }
};