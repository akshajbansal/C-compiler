// Longest Common Subsequence --- Recursive method

int max(int a, int b) 
{ 
    return (a > b)? a : b; 
} 
  
/* Returns length of LCS for X[0..m-1], Y[0..n-1] */
int lcs( char *X, char *Y, int m, int n ) 
{ 
   if (m == 0 || n == 0) 
     return 0; 
   if (X[m-1] == Y[n-1]) 
     return 1 + lcs(X, Y, m-1, n-1); 
   else
     return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 
} 
  
/* Driver program to test above function */
int main() 
{ 
  char X[] = "AGGTAB"; 
  char Y[] = "GXTXAYB"; 
  
  int m = 6, n=7;
  
  int ans = lcs(X, Y, m, n);
  
  return 0; 
} 
