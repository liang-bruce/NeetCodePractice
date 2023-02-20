class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> complementMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;
            if (complementMap.containsKey(num)) {
                return new int[] {i, complementMap.get(num)};
            }
            complementMap.put(diff, i);
            System.out.println(complementMap);
        }
        return new int[] {};
    }
}