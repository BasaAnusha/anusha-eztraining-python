def LCS(i,j):
     if(A[i]=='\0'or B[j]=='\0'):
         return 0
     elif (A[i]==B[j]):
         return  1+LCS(i+1,j+1)
     else:
         return LCS(LCS(i+1,j),LCS(i,j+1))
        
