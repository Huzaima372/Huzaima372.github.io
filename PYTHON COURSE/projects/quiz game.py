l1 = ["a",'b','c']
l2 = ['1','2','3']
balance = 0
l1_len = len(l1)
for i in  range(0,l1_len):
    print(l1[i])
    a = str(input("Enter your answer= "))
    if a == l2[i] :
      balance += 10
      print("your answer is correct and balance = ",balance)
    else:
      balance -=10
      print("your answer is wronge correct = " ,l2[i] ,"and balance = ",balance)
    
