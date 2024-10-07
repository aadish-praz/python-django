# [1,2,3,4,5] => [1,4,9,16,25]

# def square(*args):
#     for i in args:
#         i=i**2
#     return i
        
        
# result=square([1,2,3,4,5])
# print(result)

def square_numbers(numbers):
    return [x**2 for x in numbers]

# Example usage
input_list = [1, 2, 3, 4, 5]
squared_list = square_numbers(input_list)
print(squared_list) 
    

# # result=square(1,2,3,4,5)
# print(square(1,2,3,4,5))

#[1,2,3,4,5,6,7,8,9,10]=[2,4,6,8,10]

def evens(*args):
    for i in args:
        if i%2==0:
            return i
        else:
            continue
    return i

    
result=evens(1,2,3,4,5,6,7,8,9,10)
print(result)


# [1,2,3,4,5] = 15

# def addition(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum

# result=addition(1,2,3,4,5)
# print(result)

        
