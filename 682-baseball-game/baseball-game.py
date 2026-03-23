class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        
        for op in operations:
            if op == "C":
                total -= stack.pop()
            elif op == "D":
                val = 2 * stack[-1]
                stack.append(val)
                total += val
            elif op == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
                total += val
            else:
                val = int(op)
                stack.append(val)
                total += val
        
        return total