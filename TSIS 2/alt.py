class Solution:
    def largestAltitude(self, gain: [int]) -> int:
        max_altitude = 0
        cur_altitude = 0
        for i in gain:
            cur_altitude += i
            if cur_altitude > max_altitude:
                max_altitude = cur_altitude
        return max_altitude