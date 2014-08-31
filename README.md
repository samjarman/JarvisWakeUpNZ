Jarvis WakeUp for NZ
==============

A Jarvis like wakeup for RaspberryPi. Pulls from Metservice API and then uses Google's TTS engine to say it to you. 

<iframe width="640" height="360" src="//www.youtube.com/embed/sXH2K2ZlrjQ?rel=0" frameborder="0" allowfullscreen></iframe>

Call it like `$ python wakeup.py christchurch`

Then add it as a cron job or whatever you like :)

I'm [@samjarman](http://www.twitter.com/samjarman) too.

#### Set up

Make sure you have audio configured on your RPi. 

`$ chmod u+x speech.sh`
`$ sudo apt-get install mpg123`

#### References
http://danfountain.com/2013/03/raspberry-pi-text-to-speech/
http://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)