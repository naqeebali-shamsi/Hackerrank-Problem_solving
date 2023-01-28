def findSubstring(s):
    max_length = 0
    result_str = "None"
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_str = s[i:j+1]
            if sub_str == sub_str[::-1]:
                if len(sub_str) > max_length:
                    max_length = len(sub_str)
                    result_str = sub_str
    if len(sub_str) <= 1:
        return "None"
    return result_str


def main():
    inputStr = str(input())
    result = findSubstring(inputStr)
    print(result)


if __name__ == "__main__":
    main()