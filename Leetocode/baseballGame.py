class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        Sum = 0

        for operation in operations:
            if operation[1:].isdigit() or operation.isdigit():
                records.append(int(operation))
            elif operation == 'C' and len(records)>=1:
                records.pop()
            elif operation == 'D' and len(records) >=1:
                records.append(records[-1]*2)
            elif operation == '+' and len(records) >=2:
                records.append(records[-2]+records[-1])
               
        return sum(records)