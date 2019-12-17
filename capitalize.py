para=input().split('.')
a=len(para)
for i in range(a):
    para[i]=para[i].strip().capitalize()

print('. '.join(para))