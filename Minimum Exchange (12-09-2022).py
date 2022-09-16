def MinimumExchange(self, matrix):
		# Code here
		count1, count2, a, b = 0, 0, 0, 0
    #counts number of A's - a
    #counts number of B's - b
    #count1 & count2 are the 2 types of pattern counter
    #we return the minimum of both the types
		for i in range(n):
		    for j in range(m):
		        if ((i+j) % 2 == 0):
		            if matrix[i][j] != "A":
		                count1 += 1
		                b += 1
		            else:
		                count2 += 1
		                a += 1
		        else:
		            if matrix[i][j] != "B":
		                count1 += 1
		                a += 1
		            else:
		                count2 += 1
		                b += 1
    count1 //= 2
		count2 //= 2
		if a == b:
		    answer = min(count1, count2)
		elif a > b:
		    answer = count1
		else:
		    answer = count2
		return answer
