
class Math:
    
    @staticmethod
    def checkpalindrome(mystring):
        if mystring==mystring[::-1]:
            return True
        else:
            return False
    
print(Math.checkpalindrome('101'))
print(Math.checkpalindrome('dad'))
print(Math.checkpalindrome('man'))