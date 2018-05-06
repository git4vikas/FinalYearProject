
from random import randint
print(str(randint(0, 9)))
with open("data1.json",'w') as f:
    f.write("""{ "data": [
  { "date":"2018-04-01" ,
    "Nitrogen" : 220,
    "Phosphorus" : 16,
    "Potassium" : 212,
    "location" : [
    13.03234, 
    77.59250]
  },
 """  )
    for i in list(range(30)):
        if i<2:
            pass
        if i>9:
            f.write(""" { "date":"2018-04-"""+str(i)+"""",
    "Nitrogen" : """+str(randint(210,256))+""",
    "Phosphorus" : """+str(randint(12,23))+""",
    "Potassium" : """+str(randint(218,260))+""",
    "location" : [
    13.03234, 
    77.59250]
  },
 """)
        elif (i%3 -1) ==0:
            f.write(""" { "date":"2018-04-0""" + str(i) + """",
    "Nitrogen" : """+str(randint(230,256))+""",
    "Phosphorus" : """+str(randint(12,22))+""",
    "Potassium" : """+str(randint(218,260))+""",
    "location" : [
    13.03253, 
    77.59237]
  },
 """)
        else:
            f.write(""" { "date":"2018-04-0""" + str(i) + """",
    "Nitrogen" : """ + str(randint(210, 256)) + """,
    "Phosphorus" : """ + str(randint(12, 22)) + """,
    "Potassium" : """ + str(randint(218, 260)) + """,
    "location" : [
    13.03285, 
    77.59274]
  },
 """)
    f.write(""" { "date":"2018-04-30"""+ """",
    "Nitrogen" : """ + str(randint(210, 256)) + """,
    "Phosphorus" : """ + str(randint(12, 22)) + """,
    "Potassium" : """ + str(randint(218, 260)) + """,
    "location" : [
    13.03285, 
    77.59274]
  }
 """+"]}")

