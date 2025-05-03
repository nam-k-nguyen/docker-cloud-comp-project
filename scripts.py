import re
import socket
from collections import Counter

def count_words(path, split_contractions=False):
    text = open(path, encoding='utf-8').read().lower()
    if split_contractions:
        text = text.replace("'", " ").replace("’", " ")
    words = re.findall(r"\b\w+\b", text)
    return Counter(words)

ctr1 = count_words("IF-1.txt")
ctr2 = count_words("AlwaysRememberUsThisWay-1.txt", split_contractions=True)

total1 = sum(ctr1.values())
total2 = sum(ctr2.values())
grand_total = total1 + total2

top3_if = ctr1.most_common(3)
top3_ar = ctr2.most_common(3)

ip_addr = socket.gethostbyname(socket.gethostname())

out_path = "output/result.txt"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(f"Word count IF-1.txt: {total1}\n")
    f.write(f"Word count AlwaysRememberUsThisWay-1.txt: {total2}\n")
    f.write(f"Grand total words: {grand_total}\n\n")
    f.write("Top 3 in IF-1.txt:\n")
    for word, cnt in top3_if:
        f.write(f"  {word}: {cnt}\n")
    f.write("\nTop 3 in AlwaysRememberUsThisWay-1.txt:\n")
    for word, cnt in top3_ar:
        f.write(f"  {word}: {cnt}\n")
    f.write(f"\nContainer IP: {ip_addr}\n")

print(open(out_path, encoding="utf-8").read())
