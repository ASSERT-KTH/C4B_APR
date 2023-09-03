import re
print("YES" if re.sub(r"(l){2,}", "ll", re.sub(r"(h|e|o)\1+", r'\1', re.sub(r"[^h|e|l|o]", "", str(input())))) == "hello" else "NO")