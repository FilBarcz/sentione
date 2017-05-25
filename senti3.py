def solution(S):
    N = len(S)
    ii= iter(range(0,N-1))
    if (N <=1):
        out=0
    else:
        out = 0
        for i in ii:
            if S[i]==S[i+1]:# looking for polindromes of size 2
                out= out+1 # if we find one we add 1 to our score
                k=2 
                a=S[i]
                while(i+k<=N-1 and a==S[i+k]): # algorithm is least efficient when there is a lot of the same characters next to each other so we try this special code to deal with the situation
                    out= out+k #k stands for the number of letters than are the same in a row and we can derive this iteratrive formula by considering change in number of polindromes when we add extra character
                    k=k+1
                c=1
                while( i-c>=0 and i+k-1+c<= N-1 and S[i-c]==S[i+k-1+c] and out<=100000000): #once we get at least two same characters in the row we can create another polindrme by adding same character at the beginning and at the end of it 
                    out = out + 1
                    c = c + 1
                for n in range(3,k+1): #if we have just two characters in the row nothing happens here, once we have three or more we need to skip to the last one (of the sequence of same ones) as all polindromes with combinations of intermediate characters were already considered in algorithm before. It is also worth noting that we are sure that the next character is not same so we do not need to worry about it not going through code above
                    next(ii, None)
            else:
                if (i!=N-2 and S[i]==S[i+2]) : #second most basic class of polindromes would be those of size 3 
                    out = out + 1
                    k=3 #we will stick with k denoting size but this time we are worried about substrings of the form 'abababab' as they would be second worst case scenario for algorithm, we can note that substrings of the form 'abcabc' are not very problematic as there is no polindromes in them
                    a=S[i]
                    b=S[i+1]
                    k1=1
                    k2=2
                    while(i+k<=N-1 and b==S[i+k]): #here formula comes from the fact that if we have interchanging characters say a and b then iteratevly adding 'a' will increase number of polindromes by 1 for each length of already contained in substring polindromes and add one extra which will be longer from previous (same with b)
                        out=out+k1
                        k=k+1
                        k1=k1+1
                        if(i+k<=N-1 and a==S[i+k]):
                            out=k2+out
                            k2=k2+1
                            k=k+1
                        else:
                            break
                    c=1
                    while( i-c>=0 and i+c+k-1<= N-1 and S[i-c]==S[i+k-1+c] and out<=100000000):
                        out = out + 1
                        c = c + 1
                    for n in range(3,k+1): #here we are skipping to second last of our 'abab' substring as the next loop we want to start with last one to check if following term is not 'b'
                        next(ii, None)
            if out>=100000000:
                out=-1
                break
    return(out)