name = input("Name :")
section = input("Section: ")
prelim = float(input("Prelim: "))
if prelim  <40 or prelim >100:
    print("Please enter between 41-100")
else: 
  midterms = float(input("Midterms: "))
  if midterms  <40 or midterms >100:
    print("Please enter between 41-100")
  else: 
    finals = float(input("Finals: "))
    if finals  < 40 or finals >100:

       print("Please enter between 41-100")
    else:

        average = round((prelim*0.3333)+(midterms*0.3333)+(finals*0.3333))
        print (average) 
        roundoff = round(average)
    
    if  roundoff >= 99:
        print("GPA: 1.00")
    if    roundoff >= 96 and roundoff <= 98:
        print ("GPA: 1.25")
    if    roundoff >= 93 and roundoff <= 95:
        print ("GPA: 1.50")
    if    roundoff >= 92 and roundoff <= 90:
        print ("GPA: 1.75")
    if    roundoff >= 87 and roundoff <= 89:
        print ("GPA: 2.00")
    if    roundoff >= 86 and roundoff <= 84:
        print ("GPA: 2.25")
    if    roundoff >= 83 and roundoff <= 81:
        print ("GPA: 2.50")
    if   roundoff >= 80 and roundoff <= 78:
        print ("GPA: 2.75")
    if   roundoff >= 77 and roundoff <= 75:
        print ("GPA: 3.00")
    if roundoff < 75:
        print ("GPA: 5.00")
        



