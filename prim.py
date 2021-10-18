def prime(n):
    '''
      Aratati daca un numar este prim sau nu
      param: un numar intreg
      return:True daca e prim si False daca nu este prim
    '''
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                print(n,"nu este prim")
            else:
                print(n,"n este prim")


def test_is_prime():
    assert is_prime(21) is False
    assert is_prime(2) is True
    assert is_prime(13) is True
    assert is_prime(26) is False
    assert is_prime(156) is False


numar= int(input("Dati un numar:"))
if is_prime(numar):
    print(numarul este prim)
else:
    print ("numarul nu este prim")