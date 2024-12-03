import sys
import re

def check(row):
    '''
    Pseudo Code:
    If it contains don't() flag is False
    If it contains do flag is True
    else if flag is true perform multiplication and add them together.
    '''
    sum=0
    flag=True
    if row:
        for var in row:
            if var[0]=="don't()":
                flag=False
            if var[0]=='do()':
                flag=True
            if flag and var[0].startswith('mul') :
                    sum+=(int(var[1]) * int(var[2]))
    return sum

def count(reader_object):
    #Answer 1: 
    '''
    Check only for regex expression containing mul(a,b) where a and b are digits
    '''
    m=re.findall(r"(mul\((\d+),(\d+)\))", reader_object)
    counter=check(m)
    #Answer 2:
    '''
    Check only for regex expression containing mul(a,b) where a and b are digits 
    and do() and don't() to remove incorrect records.
    '''
    m=re.findall(r"(mul\((\d+),(\d+)\)|don't\(\)|do\(\))", reader_object)
    counter1=check(m)
    return counter,counter1

def run(file):   
    with open(file, 'r') as f:
        reader_object=f.read()
        counter,counter1=count(reader_object)
    print("01. Answer: {}".format(counter))
    print("02. Answer: {}".format(counter1))    

if __name__ == '__main__':
    
    file=sys.argv[1]
    run(file)