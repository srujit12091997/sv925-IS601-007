a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")

    # Convert all negative elements in the array to positive
    positive_arr = []
    for element in arr:
        if isinstance(element, str):
            positive_arr.append(abs(int(element)))
        else:
            positive_arr.append(abs(element))

    # Keep the output data type the same as the input data type
    if all(isinstance(x, int) for x in arr):
        positive_arr = [int(x) for x in positive_arr]
    elif all(isinstance(x, float) for x in arr):
        positive_arr = [float(x) for x in positive_arr]
    elif all(isinstance(x, str) for x in arr):
        positive_arr = [str(x) for x in positive_arr]

    # Print the positive output array
    print(positive_arr)

    # Print the type of the output data
    print("\nType of output data:", type(positive_arr[0]))


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)

