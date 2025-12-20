# Q12 (Filter): filter() use karke ek list me se sirf Even numbers ko alag karo


li =[2,3,4,5,6,7,8,9]
resut = list(filter(lambda x: x%2==0 ,li))
print(resut)



nums = [-3,-1,0,2,5]
res = list(filter(lambda x: x>0,nums))
print(res)
