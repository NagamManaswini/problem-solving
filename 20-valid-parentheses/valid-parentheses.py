class Solution:
    def isValid(self, s: str) -> bool:
        x=[]
        for i in s:
            if i in "[({":
                x.append(i)
            else:
                if not x:
                    return False
                top=x.pop()
                if (i==")" and top!="(") or (i=="]" and top!="[") or (i=="}" and top!="{"):
                    return False
        return len(x)==0
        
        