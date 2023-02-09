def main():
    ##################################################
    # Comlete your code here
    ##################################################
   #input 
   numM= int((input())) #input() returns string value. Need to change it to INT value. 
   # num= int(numM)
   numF= int(input())
   
   #calculation 
   #total =numM +numF
   percM = numM / (numM + numF ) *100 
   percF = numF / (numM+ numF) *100

   #output 
   print ('Total ', numM + numF)
   print ('Number of males and females' ,numM, numF)
  # print ( f ' Percentage of males and females : {percM : 2f} {percF : 2F }) 
#pass




if __name__ == '__main__':
    main()
