def Quadratic_Solver():

  A = input("Please say what A is: ")
  B = input("Please say what B is: ")
  C = input("Please say what C is: ")
  
  B_squared = int(B) * int(B)
  Four_AC = 4 * int(A) * int(C)
  Two_A = 2 * int(A)
  Minus_B = 0 - int(B)
  Solve_1 = B_squared - Four_AC
  import math
  Solve_2 = math.sqrt(Solve_1)

  Solve_3_Addition = Minus_B + Solve_2
  Solve_4_Addition = Solve_3_Addition / Two_A

  Solve_3_Subtraction = Minus_B - Solve_2
  Solve_4_Subtraction = Solve_3_Subtraction / Two_A

  print ("\n")

  if Solve_4_Addition == Solve_4_Subtraction:
    print (Solve_4_Addition)
  else:

    print (Solve_4_Addition)
    print ("or")
    print (Solve_4_Subtraction)

  print ("\n")


  Do_Again_Question = input("Press 1 and hit enter to go again: ")

  print ("\n")

  if Do_Again_Question == "1":
    Quadratic_Solver()


  
Quadratic_Solver()