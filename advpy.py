#walrus 
#if(n:=len([1,2,3,4,5,6]))>3:
 #   print(f"this is walrus operator used in  and length of the n is {n} it is perfect ")
#declare type of varible exlipcit
#s: str="zadfg"
#n: int=1234
# print(f"{s}and {n}")

# #advanced type hints 

# from  typing import List,Tuple,Dict,Union
# num: List[int]=[1,2,3,4,5]
# names: Tuple[str,int]=(12,"zaid",32,"dfg")
# roomno: Dict[str,int]={"zaid":12,"rahil":13}
# print(num)
# print(names)
# print(roomno)

# def http_status(status):
#     match status:
#         case 200:
#             return "failed to connect"
#         case 300:
#             return "i can i will"
#         case 400:
#             return "do it"
#         case _:
#             return "assume always may not be true"
# print(http_status(300))


