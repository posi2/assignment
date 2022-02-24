def factorial(n) :
    res = 1
     
    # Calculate value of [1*(2)*---*
    #(n-k+1)] / [k*(k-1)*---*1]
    for i in range(1, n + 1):
        res *= i
    return res
 
def binomialCoeff(n, k):
 
    res = 1
 
    # Since C(n, k) = C(n, n-k)
    if (k > n - k):
        k = n - k
 
    # Calculate value of [n*(n-1)*---*(n-k+1)] /
    # [k*(k-1)*---*1]
    for i in range(k):
     
        res *= (n - i)
        res //= (i + 1)
     
    return res
 
# A Binomial coefficient based function to
# find nth catalan number in O(n) time
def catalan(n):
 
    # Calculate value of 2nCn
    c = binomialCoeff(2 * n, n)
 
    # return 2nCn/(n+1)
    return c // (n + 1)
 

def countBST(n):
 
    # find nth catalan number
    count = catalan(n)
 
    return count
 
if __name__ == '__main__':

    a = input("Given BST")
 
    n = len(a)
 
    # find count of BST and binary
    # trees with n nodes
    count1 = countBST(n)
 
    # print count of BST and binary trees with n nodes
    print("Count of BST with", n, "nodes is", count1)
 
