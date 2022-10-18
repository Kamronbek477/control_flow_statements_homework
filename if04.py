def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    
    if a>0:
        x1=1
    if a<0:
        x1=0
    if b>0:
        x2=1
    if b<0:
        x2=0
    if c>0:
        x3=1
    if c<0:
        x3=0
    return x1+x2+x3
print(main(-19,-9,6))
 
