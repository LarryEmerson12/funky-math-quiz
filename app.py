fn = 0
sn = 0
ca = fn + sn
ua = 0
iq = 0
crazy = False

while iq != 100:
  print(f"your iq: {iq}")
  ua = int(input(f"what is the answer({fn}+{sn}+?): "))
  if ua == ca:
    print("correct")
    iq += 1
    fn += 1
    sn += 1
    ca = fn + sn
  elif ua == 100:
    if fn != 50:
      print("you spammed, get outta here...")
      iq = 100
      crazy = True
  else:
    print("wrong")
    iq -= 1

print("what!?")

if crazy == False:
  print("you passed the national stupid test")
else:
  print("you passed the national crazy test")