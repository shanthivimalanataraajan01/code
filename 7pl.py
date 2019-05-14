#ms
n= input()
print(''.join([n[a:a+2][::-1] for a in range(0, len(n), 2) ]))
