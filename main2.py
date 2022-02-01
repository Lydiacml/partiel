
def polynome1(x):
    try :
        type(x)=='char'
        return ((x*x*x)-(1.5*(x*x))-(6*x)+5)
    except TypeError as e:
        print("attention, la valeur inséré est une chaine de caractère : ",x)
        

def polynome2(x):
        if(x<0):
            raise Exception("attention la valeur inséré est un nombre négatif : ",x)
        else:
            return ((x*x*x)-(1.5*(x*x))-(6*x)+5)

polynome2(-5)

def polynome3(x):
        if(type(x)=='complex'):
            raise Exception("attention, la valeur inséré est un nombre complex : ",x)
        else:
            return ((x*x*x)-(1.5*(x*x))-(6*x)+5)

def polynome4(x):
        if(x<0.005):
            raise Exception("attention la valeur inséré est trop petit : ",x)
        else:
            return ((x*x*x)-(1.5*(x*x))-(6*x)+5)


def polynome5(x):
        if(x>999999):
            raise Exception("attention la valeur inséré est un trop grand : ",x)
        else:
            return ((x*x*x)-(1.5*(x*x))-(6*x)+5)