#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    
	    if n==1:return 0
	    if arr[0]==0:return -1
	    jump = 1
	    far = arr[0]
	    reach = arr[0]
	    
	    for i in range(1,n):
	        if i==n-1:
	            return jump
	        far =  max(far,i+arr[i])
	        reach-=1
	        if reach==0:
	            jump+=1
	            
	            if i>=far:
	                return -1
	            reach = far-i     
	   
"""	   TLE
       l,r = 0,0
	   jump = 0
	   
	   while r<(n-1):
	       far = 0
	       for i in range(l,r+1):
	           far = max(far,i+arr[i])
	       l = r+1
	       r = far
	       jump+=1
	   
	   return jump if jump>0 else -1 """   
	       
	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends