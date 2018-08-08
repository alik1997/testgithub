import random
import os
import sys

class a:
    def guess(self,n):
        v = random.randint(0, 100)
        while True:
          if(v==n):
              print("done")
              break
          elif(v<n):
                print("guess high comp")
                v=random.randint(v,100)
          else:
                print("guess low comp")
                v=random.randint(0,v)

d=int(input("enter no."))
j=a()
j.guess(d)
