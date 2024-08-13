card = [i for i in range(1,21)]
for i in range(10):
    ai,bi = map(int,input().split())
    card = card[:ai-1]+card[ai-1:bi][::-1]+card[bi:]
print(" ".join(map(str,card)))
