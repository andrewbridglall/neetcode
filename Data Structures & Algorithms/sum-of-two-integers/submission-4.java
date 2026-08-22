class Solution {
    public int getSum(int a, int b) {
        // 32 bit integers have fixed size
        while (b != 0) {
            // calc carry
            int temp = (a & b) << 1;
            // calc bit value
            a = a ^ b;
            b = temp;
        }
        // return a
        return a;
    }
}
