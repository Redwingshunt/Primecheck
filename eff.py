def isPrime(n):
    if ((n!= 1)  and(n == 2 or n == 3)):
        return True
    i =5
    while(i*i <= n):
        if(n%i==0 or n%(i+2)==0):
            return False
        i +=6
    return False







if __name__ == "__main__":

   try :
     set_1 = int(input('give the number\t'))
     if(set_1 %1 == 0):
        print('is prime') if isPrime(set_1) else print('false') #invocation of  the function//

   except TypeError and ValueError as e:
       print("not a valid input")
       print("this stupid error {}". format(e) )
