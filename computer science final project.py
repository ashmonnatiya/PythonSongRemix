from music import*
import time

tick= AudioSample("tickkash.wav")
boom= AudioSample("boomcardi1.wav")
boom2= AudioSample("boomkash1.wav")
drums= AudioSample("drumsnelly1.wav")
snip= AudioSample("snipcardi1.wav")

samples = [tick,snip,boom,boom,drums,tick,snip,boom2,boom2,drums,tick,snip]
durations = [.2,.3,1.4,1.4,.5,.2,.3,.4,.4,.5,.2,.3]

for i in range(len(samples)):
   samples[i].play()
   time.sleep(durations[i])
   
