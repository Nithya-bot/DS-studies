#strip removes unwanted spaces or newline characters from the start/end.

S=input().strip()

even_chars=S[0::2]
odd_chars=S[1::2]

print(even_chars, odd_chars)
