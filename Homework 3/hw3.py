import numpy as np

if __name__ == "__main__":
    # Define matrix A
    A = [[1, -1, 1, -1], 
         [1, 1, 1, 1], 
         [1, -1.2, 1.44, -1.728],
         [1, 1.4, 1.96, 2.744],
         [1, 1.9, 3.61, 6.859]]
    
    # Convert A to a NumPy array
    A = np.array(A)
    
    # Compute the transpose of A
    AT = A.transpose()
    print("A^T is:")
    print(AT)
    
    # Compute the dot product of AT and A
    result = np.dot(AT, A)
    
    print("A^T * A is:")
    print(result)
    print('\n')

    try:
        # Compute the inverse of result
        result_inv = np.linalg.inv(result)
        print("The inverse of A^T * A is:")
        print(result_inv)
    except np.linalg.LinAlgError:
        print("The matrix A^T * A is not invertible.")
    print('\n')
    
    # Compute the dot product of result_inv and AT
    result_inv_AT = np.dot(result_inv, AT)
    print("The inverse of A^T * A multiplied by A^T is:")
    print(result_inv_AT)
    print('\n')
    
    # Define matrix T
    T = [[2, 3, -3, 0, -3],]
    
    # Convert T to a NumPy array
    T = np.array(T)
    
    # Compute the dot product of result_inv_AT and the transpose of T
    result_T = np.dot(result_inv_AT, T.transpose())
    print("The result of the multiplication of the inverse of A^T * A with A^T and T is:")
    print(result_T)