# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 원소들의 합을 반환하는 함수 list_sum(nums) 를 정의한다.
def list_sum(nums):
    total = 0
    for i in nums:
        total += i
    return total
# 함수를 호출해 결과를 출력한다.
print(list_sum(nums))