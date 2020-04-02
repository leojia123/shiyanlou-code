a = 0 ## start from 1
while a <= 99:
    a = a+1
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7:  #if the number is 7's beishu
        continue
    #elif a % 10 == 7: # if it contains 7 in the last position
      #  continue
    #elif a // 10 == 7: # if it contains 7 in the first piston
        #continue
    else:
        print(a)
    #a = a +1
