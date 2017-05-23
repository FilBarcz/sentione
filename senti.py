def solution(S):
    N = len(S)
    ii= iter(range(0,N-1))
    if (N <=1):
        out=0
    else:
        out = 0
        for i in ii:
            if S[i]==S[i+1]:
                out= out+1
                k=2
                a=S[i]
                while(i+k<=N-1 and a==S[i+k]):
                    out= out+k
                    k=k+1
                c=1
                while( i-c>=0 and i+k-1+c<= N-1 and S[i-c]==S[i+k-1+c] and out<=100000000):
                    out = out + 1
                    c = c + 1
                for n in range(3,k+1):
                    next(ii, None)
            else:
                if (i!=N-2 and S[i]==S[i+2]) :
                    out = out + 1
                    k=1
                    while( i-k>=0 and i+k+2<= N-1 and S[i-k]==S[i+2+k] and out<=100000000):
                        out = out + 1
                        k = k + 1
            if out>=100000000:
                out=-1
                break
    return(out)