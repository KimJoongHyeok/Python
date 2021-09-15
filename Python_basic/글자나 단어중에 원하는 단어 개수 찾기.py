def count(s,ch):
    count = 0
    for c in s:
        if ch == c:
            count += 1

    return count

def main():
    s = input("Enter a string : ").strip() # strip = 공백을 없앰
    ch = input("Enter a character : ").strip()

    print(count(s,ch))
    
main()
