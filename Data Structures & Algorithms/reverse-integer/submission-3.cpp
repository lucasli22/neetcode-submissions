class Solution {
public:
    int reverse(int x) {
        int sign = 1;
        if (x < 0) {
            sign = -1;
            if (x == INT_MIN) return 0;
            x *= -1;
        }
        
        int ans = 0;
        while (x >= 1) {
            int digit = x % 10;
            if (ans > INT_MAX / 10 || (ans == INT_MAX / 10 && digit > 7)) return 0;
            ans *= 10;
            ans += digit;
            x /= 10;
        }

        return ans * sign;
    
          
    }

};