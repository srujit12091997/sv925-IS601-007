#UCID: SV925
#name: Srujit Varasala
a1 = [10.001, 11.591, 0.011, 5.991, 16.121, 0.131, 100.981, 1.001]
a2 = [1.99, 1.99, 0.99, 1.99, 0.99, 1.99, 0.99, 0.99]
a3 = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
a4 = [10.01, -12.22, 0.23, 19.20, -5.13, 3.12]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    total=round(sum(arr),2)

    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add necessary code here for sum; every number must have two decimal places shown (i.e., 0.10, 0.01, 0.00)
    print("\nThe total is {}\n".format(total))

print("Problem 2")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)