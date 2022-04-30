import us_sensor as us
import matplotlib.pyplot as plt
import sys
from twilio.rest import Client
sys.path.append ('./ir')
import  ir_detect as ir
sys.path.append ('./detection')
import detect
account_sid = 'AC054fc9ef48b9b5e98258bce5eca21cb4'
auth_token = '29e23fdae2616b513fd09503f3ebc93f'
client = Client(account_sid, auth_token)

def main():
    
    i = 1
    print ("System ON !!")
    while 1:
        D = {'animal':0 ,'cheetah':0,'leopard':0,'mammal':0,'wildlife':0,'elephant':0}
        ir.detect()
        print("Detecting...")
        D,count = detect.detect_animals(D)
        
        if (count):
            print (count)
            call = client.calls.create(
                      url='https://handler.twilio.com/twiml/EHee56782cafb80d205d3e817bf0514a71',
                     from_='+12015483755',
                     to='+917738809453'
                 )
            print(call.sid)
            if (i%2 == 0):
                plt.bar (D.keys(), D.values())
                plt.savefig ('visual.png')
            us.flee_animals ()
            
        else:
            print ("NO ANIMAL !!")

        i = i+1
if __name__ == "__main__":
    main()
