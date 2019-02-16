class Solution {
public:
    /*
     * @param reader: An instance of ArrayReader.
     * @param target: An integer
     * @return: An integer which is the first index of target.
     */
    int searchBigSortedArray(ArrayReader * reader, int target) {
        // write your code here
        if (reader->get(0) == target) return 0; // corner case
        long idx = 1;
        while(reader->get(idx) < target) {
            idx *= 2;
        }
        long left = idx / 2;
        long right = idx;
        while (left + 1 < right) {
            long mid = left + (right - left) / 2;
            if (reader->get(mid) < target) {
                left = mid;
            } else {
                right = mid;
            }
        }
        if (reader->get(left) == target) return left;
        if (reader->get(right) == target) return right;
        return -1;
    }
};
