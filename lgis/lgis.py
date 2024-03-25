import logging
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) 

def lis(nums):
    if not nums:
        return []
    
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                # logging.debug("i: "+str(i)+" "+str(nums[i])+"  j: "+str(j)+" "+str(nums[j]))
                dp[i] = dp[j] + 1
                prev[i] = j
    logging.debug(dp)
    logging.debug(prev)
    max_length = max(dp)
    end_index = dp.index(max_length)
    
    result = []
    while end_index != -1:
        result.append(nums[end_index])
        end_index = prev[end_index]
    
    return result[::-1]

def lds(nums):
    if not nums:
        return []
    
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] < nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    max_length = max(dp)
    end_index = dp.index(max_length)
    
    result = []
    while end_index != -1:
        result.append(nums[end_index])
        end_index = prev[end_index]
    
    return result[::-1]

if __name__ == "__main__":

    filename = sys.argv[1]
    n = 0
    sequence = []
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        sequence = list(map(int, f.readline().strip().split()))

    resInc = lis(sequence)
    resDec = lds(sequence)
    
    logging.debug(resInc)
    logging.debug(resDec)

    
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, resInc)) + '\n')
        f.write(' '.join(map(str, resDec)) + '\n')