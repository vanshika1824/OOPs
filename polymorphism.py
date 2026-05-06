#polymorphism
#overloading
'''class Solution:
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c):
        return a+b+c
    
s = Solution()
print(s.add(5,4))
#print(s.add(2,5,3))
'''
#overriding
class A:
    def start(self):
        print("A started....")

class B(A):
    def start(self):
        super().start()     #to get both we use super keyword
        print("B Started...")

if __name__ == "__main__":
    b=B()
    b.start()