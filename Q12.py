'''Use the walrus operator in a list comprehension to store lengths of words from ["python", "rocks", "ai"] in a list while filtering out words shorter than 4 characters'''
# def lenght(x):
#     if len(x)<4:
#         return True
#     else:
#         return False
    


W=["pyhton","rock","ai"]


length=[n for w in W if(n:=len(w))>4]
print(length)
# new=list(filter(lenght,W))
# print(new)

