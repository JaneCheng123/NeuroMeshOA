def minNum_subsequences(source: str, target: str) -> int:
    result = 1
    i, j = 0, 0
    
    while i < len(target):
        exist = False
        while j < len(source) and not exist:
            if source[j] == target[i]:
                exist = True
                i += 1
            j += 1

        if not exist:
            if j == len(source):
                result += 1
                j = 0
            if not target[i] in source:
                return -1
    return result

def valid_paraentheses(checking: str) -> str:
    lefts = []
    marks = [' '] * len(checking)

    for index in range(len(checking)):
        char = checking[index]
        if char == '(':
            lefts.append(index)
        elif char == ')':
            if lefts:
                lefts.pop()
            else:
                marks[index] = '?'

    for index in lefts:
        marks[index] = 'x'

    output = checking + '\n' + ''.join(marks)
    return output

# Test cases
print("Test Cases for Q1:")
print(minNum_subsequences("abc", "abcbc"))
print(minNum_subsequences("abc", "acdbc"))
print(minNum_subsequences("xyz", "xzyxz"))

print("Test Cases for Q2:")
print(valid_paraentheses("bge)))))))))"))
print(valid_paraentheses("((IIII))))))"))
print(valid_paraentheses("()()()()(uuu"))
print(valid_paraentheses("))))UUUU((()"))