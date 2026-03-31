class Solution {
public:
    int maxArea(vector<int>& heights) {
        int res = 0;
        int i = 0;
        int l = heights.size() - 1;

        while (i < l) {
            // Area = Width * height of the shorter wall
            int width = l - i;
            int current_height = min(heights[i], heights[l]);
            res = max(res, width * current_height);

            // Move the pointer pointing to the shorter wall inward
            if (heights[i] < heights[l]) {
                i++;
            } else {
                l--;
            }
        }
        return res;
    }
};
