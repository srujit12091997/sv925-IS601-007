a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    [print(i) for i in arr]
    a1_positive = [abs(x) for x in a1]
    a2_positive = [abs(x) for x in a2]
    a3_positive = [abs(x) for x in a3]
    a4_positive = [abs(float(x)) for x in a4]
    print(type(a1_positive))
    print(type(a2_positive))
    print(type(a3_positive))
    print(type(a4_positive))
    #result
    #print(type(result))
    print("\nPositive Output:\n")
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)