def reverse(s):
    result = ""
    for ch in s:
        result = ch + result # result + ch 이렇게 하면 문자열 역순으로 안되고 그대로 출
    return result


def main():
    s = input("Enter a string : ").strip()
    print("The reversed string : ",reverse(s))

main()
