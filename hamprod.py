def hadamard_product(Hk, v):
  """
  This computes the matrix-vector product of a modified Hadamard matrix Hk and a vector v using the divide-and-conquer strategy.
  Time complexity: O(n log n)

  Args:
      Hk: A modified Hadamard matrix of size 2^k x 2^k.
      v: A column vector of size 2^k.

  Returns:
      The result of Hk * v as a column vector.
  """

  n = len(v)  # O(1) operation to get the vector length

  # Base case: when n is 1, no computation is needed, return the input vector directly.
  # Time complexity: O(1)
  if n == 1:
    return v

  # Recursive case: when n is greater than 1, divide the problem into halves.
  else:
    half_n = n // 2  # O(1) operation to find the half size

    # Split the input vector into two halves
    v1 = v[:half_n]  # Slicing operation, O(1)
    v2 = v[half_n:]  # Slicing operation, O(1)

    # Recursively compute the matrix-vector products for each half using the same function
    # Time complexity: 2 * T(n/2) (recursive calls)

    product1 = hadamard_product(Hk[:half_n, :half_n], v1)
    product2 = hadamard_product(Hk[half_n:, half_n:], v2)

    # Combine the results by stacking and subtracting elements based on the matrix structure
    # Time complexity: O(n) (concatenation and element-wise operations)
    return np.concatenate((product1 - product2, product2 - product1))

  # Example usage:
Hk = np.array([[1, 1, 1, 1],
              [-1, -1, -1, -1],
              [-1, -1, -1, -1],
              [1, 1, 1, 1]])
v = np.array([2, 3, 4, 5])

result = hadamard_product(Hk, v)
print(result)