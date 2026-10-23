

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    result = []

    if not nums or k <= 0 or k > len(nums):
        return result

    for i in range(len(nums) - k + 1):
        maximum = nums[i]

        for j in range(i + 1, i + k):
            if nums[j] > maximum:
                maximum = nums[j]

        result.append(maximum)

    return result
