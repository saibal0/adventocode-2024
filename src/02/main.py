import csv 
import sys

def check(row):
    '''
    Pseudo Code:
    Check Increasing or Decreasing of list
    Check if absolute of current vs previous row is greater than=1 and less than=3
    '''
    flag=1
    if sorted(row)==row or sorted(row,reverse=True)==row:
        for var in range(len(row)-1):
            if not 1<=abs(row[var]-row[var+1])<=3:
                flag = 0
                break
    else:
        flag=0
    return flag

def count(reader_object):
    counter,counter1=0,0
    for row in reader_object:
        row=list(map(int,row))

        #Answer 1: 
        counter+=check(row)
        #Answer 2:
        #Remove element from each row and check if it holds good.
        safe=False
        for var in range(len(row)):
            if check(row[:var]+row[var+1:]):
                safe=True
        if safe:
            counter1+=1
    
    return counter,counter1

def run(file):   
    with open(file, 'r') as csvfile:
        reader_object=csv.reader(csvfile, delimiter=' ')
        counter,counter1=count(reader_object)
    print("01. Answer: {}".format(counter))
    print("02. Answer: {}".format(counter1))    

if __name__ == '__main__':
    
    file=sys.argv[1]
    run(file)