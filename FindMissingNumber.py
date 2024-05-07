def find_missing_integer(A, binaryNum = ""):
    #check that if we find the missing binary number
    if (binaryNum not in A) and (len(binaryNum) == len(A[0])):
        print("missing: "+binaryNum)
    else:
        #we make different combination
        if len(binaryNum) < len(A[0]):
            find_missing_integer(A, binaryNum + "1")
            find_missing_integer(A, binaryNum + "0")
    return

A = ["000", "001", "010", "011", "101", "110", "111"]
find_missing_integer(A, "")