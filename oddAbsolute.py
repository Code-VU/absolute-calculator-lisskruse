def calculateAbsolute():
    
    # This first line is provided for you
    def absoluteValue(num):
        if(num<0):
            return (-num)
        else:
            return (num)


    in_num  = input("Enter a number: ")
    if(in_num>21):
        print ("Result:",2*absoluteValue(in_num-21))
    else:
        print ("Result:",absoluteValue(in_num-21)) 
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculateAbsolute()