"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
"""


"""
In the set() function, in each call, we store a value at (key, timestamp) location, which takes O(L)O(L)O(L) time to hash the string.
Thus, for MMM calls overall it will take, O(M⋅L)O(M \cdot L)O(M⋅L) time.

In the get() function, we will find correct key in our map, which can take O(L⋅logM)O(L \cdot logM)O(L⋅logM) time and then use binary search on that bucket which can have at most M elements, which takes O(logM)O(logM)O(logM) time.
peekitem in python will also take O(logN)O(logN)O(logN) time to get the value, but the upper bound remains the same.
Thus, for NNN calls overall it will take, $O(N \cdot (L \cdot logM + logM))$ time.
##############
In the set() function, in each call we store one value string of length L, which takes O(L)O(L)O(L) space.
Thus, for MMM calls we may store MMM unique values, so overall it may take O(M⋅L)

In the get() function, we are not using any additional space.
Thus, for all NNN calls it is a constant space operation. The space for output is not considered the space use.

"""

class TimeMap:

    def __init__(self):
        self.dict={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append([value,timestamp])
        else:
            self.dict[key]=[[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        values=[]
        if key in self.dict:
            values=self.dict[key]
        else:
            return ""
        
        start=0
        end = len(values)-1
        actual = ""
        while(start<=end):
            mid=(start+end)//2
            if values[mid][1]==timestamp:
                return values[mid][0]
            elif values[mid][1]<timestamp:
                actual=values[mid][0]
                start=mid+1
            else:
                end=mid-1
        return actual
