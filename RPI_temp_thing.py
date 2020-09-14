#Dette er et program til RPI
import thingspeak
import time

channel_id = ****** # PUT CHANNEL ID HERE
write_key='***************' # PUT YOUR WRITE KEY HERE
read_key='***************' # PUT YOUR READ KEY HERE

def thermometer(channel):
                        
    try:
        #callableculate CPU temperature of Raspberry Pi in Degrees C
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        params= channel.update({'field1': temp})
        print(temp)
                #print response.status, response.reason

        read = channel.get({})
        print(read)
        
    except:
        print ("connection failed")
        
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        thermometer(channel)
        time.sleep(15)
