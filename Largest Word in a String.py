s=input() 
words=s.split() 
max_len=0 
max_word="" 
for word in words:
    if len(word)>max_len:
        max_len=len(word)
        max_word=word 
print(max_word)
