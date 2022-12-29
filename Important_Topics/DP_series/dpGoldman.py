"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
"""

def find (nums):
    """
    k hunxa vanda kheri, euta dictionary hunxa, tesma hamile number rakhxum. Aba array iterate garne, hamilai ta pairs of 60 chahiyeko xa
    so pahile modulus linxum, sablai 0-59 ko range ma rakhna lai. Ani hami tyo number ko compliment linxum (60-number). Aba tyo dicxtionary
    ma xa vane, jati ota xa teti ota sanga pair banxa. so, count ma add gardinxum aba xaena vane tala jane ani tyo modulo lai dictionary ma 
    rakhdene
    0 ko lagi chai compliment garna mildena so teslai xuttai case ma rakhne. kinaki 60-0 60 hunxa hamile sab ko modulo leyera 60 lai ne 0
    banayisakem. value ta 0-59 xa ne ta
    """
    dict={}
    count=0
    for i in nums:
        modulo = i%60
        if modulo==0:
            if modulo in dict:
                count+=dict[modulo]
        else:
            if 60-modulo in dict:
                count+=dict[60-modulo]
        if modulo in dict:
            dict[modulo]+=1
        else:
            dict[modulo]=1
    return count
print(find([60,60,60,60,60]))



