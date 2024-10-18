# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this 
grey=1
blue=2
she=int(input("ask she is \n1.online \n2.offline\n-->"))
if she ==1:
    tick=int(input("which tick \n1.grey\n2.blue\n-->"))
    print("she is online")
    if tick==grey:
        print("ignoring ur mesg")
    elif tick==blue:
        print("seen ur msg")
elif she ==2:
    print("mesg sent")
    print("offline ")
else:
    print("mesg not sent")
