#Geminids
#imports
import random
import time
#pausing
def wait (t):
    #time.sleep(0)
    time.sleep(t)
#ellipsis
def ellipsis():
    for i in range (3):
        print (".", end  ="", flush = True)
        time.sleep(1.33)
#header
def header (text):
    wait (2)
    print ("---\n\n%s\n\n---\n" % (text))
    wait (2)
#choice function
def choice(flavour, opt1, opt2, cq1, cq2):
    inval = True
    print (flavour)
    print()
    wait(1)
    print ("1. " + opt1)
    print ("2. " + opt2)
    while inval:
        cin = int(input ("> ")) #input from user
        if cin == 1:
            inval = False
        if cin ==2:
            inval = False
        #print ("INVALID")
    print()
    if cin == 1:
        print (cq1)
    elif cin == 2:
        print (cq2)
    print ()
#vars
gender, name, gOpp = "", "", ""

inv = []

#Opening Scene
print ("* GEMINIDS *")
print ("An interactive short story, in 3 parts.")
print ("To play this game, just type the number before the option and press <ENTER>\n")
wait(1)
name = input("What is your name, stranger? Press <Enter> to confirm:\t")
#name = "yes"
print ("And your gender?\n1: Female\n2: Male\n")
gIn = int(input(">: "))
#if (int(gIn) != 1 & int(gIn) != 2):
    #gIn = random.randint(1,2)
#Gender init()
if gIn == 1:
    gender = "Female"
    gOpp = "Male"
    gPro = "he"
    gpPro = "his"
    gPro2 = "him"
#    print ("gPRO SET")
elif gIn == 2:
    gender = "Male"
    gOpp = "Female"
    gPro = "she" #pronoun
    gpPro = "her" #possesive
    gPro2 = "her"
#    print ("gPRO SET")
#print (gOpp)

print ("%s, are you ready to start?\t" % (name)) 
print ("\n1: Yes\n2: No\n")
tIn = input(">: ")
while (int(tIn) != 1):
    tIn = input(">: ")


#prologue
header ("PROLOGUE")
print ("“I prefer to remain unenlightened, to better appreciate the dark.\n― Erin Morgenstern, The Night Circus")
print ()
wait (1)
print ("Some things are better not understood...")
print ("Like the crackle of a bright fire,")
wait(1.5)
print ("\tthe pale glimmer of moonlight reflected off an icy pond,")
wait(1.5)
print ("\t\tor the pervasive quiet that follows a heavy snowfall.")
wait(1.5)

#part 1
header ("PART I")
print ("\"Three minutes!\" %s says, %s voice muffled by the think scarf %s wears around %s face." % (gPro, gpPro, gPro, gpPro))
wait (1.5)
print ("It is December %s, %s." %(random.randint(4,17),time.strftime("%Y")))
wait (1.5)
print ("The brightest day of the Geminid meteor shower.")
wait (2.2)
print ("\nYou meander with %s to a lookout, a long way up a winding, twilit path." % (gPro2))

choice ("The forest surrounds you, but it is lit by many small lights, \nnew LEDs that someone has put to illuminate the way.", "You look at the lights...", "You look to your left...", "They are of many colours, a red like candycane or a blue like ice.\n\nSomeone has evidently taken a lot of care in arranging them.\n", "%s is grinning at you, or at least you think so. It's hard to tell beneath the heavy scarf.\n%s eyes sparkle, dancing with reflected starlight." % (gPro.capitalize(),gpPro.capitalize()))
wait (2)
print ("The path is not long. During the day, it is a pleasant walk to the lookout.\nAt night, especially on this night, it becomes alive, a portal to a world of glinting ice and brilliant snow.\n")
wait (3)
print ("The steps are ancient, made out of old wooden planks held together with rusted nails.\nDespite that, someone has cleared them of ice recently.")
wait (1)
header ("PART II")
wait (1)
choice ("It's not far to the lookout.", "\"Race you to the top!\"", "Walk, slowly.", "You take off in a sprint, laughting, making your way upwards quickly. %s is not far behind you, in quick pursuit. You wonder what will happen when %s catches up with you."% (gPro.capitalize(),gPro), "You stretch out the time you have. You smile at %s, and %s smiles back. You both dance your way up, towards the stars. Even so, the time passes by so quickly, already turning into a memory." % (gPro2, gPro))
wait (3)
print ("You are finally at the lookout, designated by a soliditary lamp.\nYou think it's an old gaslamp, because the shadows it throws grow dimmer, and then brighter again.\n")
wait (2)
print ("Snow falls, dampening the air. A silence falls, though it is not one of boredom or awkwardness.")
print ("It is a comfortable silence, charged with excitement.")
wait (1.8)
print("You feel electricity flaring between you.")
wait (2)
choice ("Even though the silence is light, you suddenly remember you wanted to say something.", "\"How long 'til it starts?\"","What are you thinking?", "%s glances down, at %s watch. It glows with reflected light, a reminder of the time that remains.\n\"One minute.\", %s replies, almost whispering." % (gPro.capitalize(), gpPro, gPro), "\"... I wish we had more time. I can't believe I'm out here tonight.\" %s replies, almost in a whisper. You agree." % (gPro))
wait (2)
for i in  reversed(range (61)):
    print (i, end = " ")
    if i == 50:
        print ("The sky is an indigo, like ink, ", end  ="")
    if i == 45: 
        print ("the crimson and blood-orange of the day already gone, ", end  ="")
    if i == 40: 
        print ("beyond the horizon.", end  ="")
    if i == 35:
        print ("The echoes of the day have long since faded to silence.", end  ="")
    if i == 30:
        print ("Still, you like feel there is not enough time.", end  ="")
    if i == 20:
        print ("You have come all this way to see the Geminids.", end  ="")
    if i == 10:
        print ("So why are you still looking back?", end  ="")
    print ()
    time.sleep (1)
header ("PART III")
print ("The first of the storm of cosmic debris comes into existence,\njust beyond the glowing arc of the horizon.")
print ("It is a bolt of lancing fire, bisecting the darkness into separate fragments of black canvas.")    
wait (2)
print ("Dozens of trails follow, each a different shade of starlight.\nThe darkness is now no longer so complete.")
wait (2)
choice ("The gaslight flares suddenly bright, casting the snow around your feet in golden light.", "You do nothing.", "You move closer.", "Still frozen in awe, you stay still, lost in the falling stars.\nYou forget that you are not alone.", "It takes what seems like an hour, but you slowly turn, shifting your weight towards %s.\nYou catch the faint scent of lilac, and an inexplicable force draws you yet closer." %(gPro2))
wait (3)
print ("The world slows to a halt. Even the falling snow seems to stand still.")
ellipsis()
choice ("", "You watch the snow fall, quietly. The world falls into stasis.","You lean forwards to kiss %s." % (gPro2),'You think that maybe, if you concentrate hard enough, you can stretch out the night forever.\nYou do not move, not until the snow has stopped falling and the stars have dissolved again into the breaking dawn.','%s smiles shyly at you, and starts to say something when you kiss %s.\nFor a half-second, you feel %s hesitate, but then %s kisses you back.\nYou forget where you are. You forget how to breathe.\nThe air seems to disappear, the world around you flaring into brilliant light.\nThe rest you don\'t remember.' % (gPro.capitalize(),gPro2, gPro2,gPro))
wait (4)
header ("EPILOGUE")
#END
print ("Some things are better not understood...")
wait(1.5)
print ("Like the patterns of dancing flames")
wait(1.5)
print ("\tthe closeness of watching the sky, together,")
wait(1.5)
print ("\t\tor the pervasive quiet that follows a bright starfall.")
wait(4)
print ("Thanks for playing my game.\n~wintermut3")