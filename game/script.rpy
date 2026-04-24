init python:
    import random
    def change_obedience(amount=0):
        global obedienceScore
        obedienceScore += amount
        sign = "+" if amount > 0 else ""
        renpy.show_screen("obedience_popup", text=f"{sign}{amount} Obedience")
    def glitch_text(text):
        if random.random() < 0.3:
            return text.replace("—", "...—")
        if random.random() < 0.2:
            sentence = ""
            for letter in text:
                sentence += letter.upper() if random.random() >= 0.5 else letter.lower()
            return sentence
        return text
    def glitch_name():
        name = ""
        for i in range(5):
            if random.randint(1, 2) == 1:
                name += "."
            else:
                name += "?"
        return name

define m = Character("Maverick")
define n = Character("Narrator")
define a = Character("You")
define b = Character("Billey")
default BilleyAlive = True
default BilleyRun = False
default TuckedSisterIn = ""
default obedienceScore = 96.0
default misfit = False
default HC = False
default cat = False
default role = ""
screen obedience():
    frame:
        xalign 0.95
        yalign 0.05
        if obedienceScore > 90:
            text "Obedience Score: [obedienceScore]" color "#23f535"
        elif obedienceScore > 30:
            text "Obedience Score: [obedienceScore]" color "#cff523"
        elif obedienceScore > 10:
            text "Obedience Score: [obedienceScore]" color "#f52323"
        else:
            text "Obedience Score: [obedienceScore]" color "#CD1C18"

screen obedience_popup(text):
    frame:
        xalign 0.5
        yalign 0.2
        background None
        text text:
            size 40
            if "+" in text:
                color "#23f535"
            else:
                color "#f52323"
    timer 1.0 action Hide("obedience_popup")

label start:
    $ HC = False
    $ role = ""
    $ misfit = False
    $ BilleyAlive = True
    $ BilleyRun = False
    $ TuckedSisterIn = ""
    $ cat = False
    $ obedienceScore = 96.0
    $ a = Character(renpy.input("What is your name? ", length=20).strip() or "Alex")
    n "*BEEP BEEP*"
    n "{w=0.2}*BEEP BEEP*"
    n "Your 9 AM alarm beeped loudly."
    n "It was a day like all the others."
    n "Nothing observed to differ from the norm."
    show screen obedience
    a "*Sigh* Another 11-hour school day... {w=1.0}'optimal' knowledge retention they said..."
    a "Ha{w=0.2}.{w=0.2}.{w=0.2}. optimal for collecting data we know."
    n "You start walking to school, your sister assumably running late yet again."
    jump presence

default spins = 0
label presence:
    menu:
        n "You feel a strange presence behind you..."
        "Spin around.":
            $ spins += 1
            if spins >= 16:
                n "Shutting down...{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
                jump endScreen
            elif spins >= 15:
                n "You know what? Once more and we're shutting this all down."
                jump presence
            elif spins >= 12:
                n "Nope. No more. We're done here."
                jump presence
            n "You spin around, losing friction, and you start spinning 'round and 'round,"
            n "So much so that you've already exceeded your weekly spin levels. Any more and you'll get a fee."
            n "In fact, this movement is so, SO incredibly unproductive that I think I'll just give you a redo."
            $ change_obedience(-1)
            if spins >= 10:
                n "STOP. {w=1.0}NOW!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!"
            elif spins >= 5:
                n "And... you might want to slow down a bit...{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}"
            jump presence
        "Keep walking.":
            jump home
        "Turn a corner then make a run for it.":
            $ change_obedience(-50)
            n "You run and you run, yet you have a strange feeling of being followed."
            n "Until this feeling suddenly disappears and you realise you've been running for hours."
            n "You've run to an abandoned place with a big sign. \"KFC\""
            n "From what you read, it seems to be some 'fast-food' restaurant from back when schools were straying from trusting students to surveillance."
        "Turn around slowly and subtly.":
            n "As you turn around, you see Billey, out of school uniform, backing into an alley..."
            n "Seemingly trying to get specifically your attention."
            menu:
                n "Do you interact with your closest friend - Billey?"
                "Shout for him.":
                    a "Billey! What are you doing?"
                    $ change_obedience(-2)
                    menu:
                        n "Do you punish Billey as he is doing something he is not?"
                        "Yes.":
                            a "Bang goes the gun as the bullet goes flying towards Billey."
                            a "Flop goes the body of Billey as the bullet flies on through."
                            a "Shout to shoot, {w=0.7}word to wound, {w=0.7}life to death."
                            $ change_obedience(5)
                            a "An innocent life lost for what?"
                            $ BilleyAlive = False
                            jump home
                        "No.":
                            a "Billey! Talk to me!"
                            $ change_obedience(-10)
                            jump BilleyRunning
                "Keep walking. {w=0.2}Any delay from your route will affect your obedience score.":
                    jump home
                "Walk towards him.":
                    a "Billey?"
                    $ change_obedience(-10)
                    jump BilleyRunning
        "Run.":
            $ change_obedience(-20)
            n "You bump into a man who was trying to pry the microphone embedded in their clothes..."
            n "They were using a knife to do so..."
            n "A sharp pain spreads through your body, {w=2.0}and in your last breath, {w=2.0}you look down to see a knife {w=1.0}impaled into your chest."
            jump endScreen
    jump endScreen

label BilleyRunning:
    n "Billey started running away."
    $ BilleyRun = True
    menu:
        "Chase?"
        "Yes.":
            $ change_obedience(-5)
            "You run and run after him, but you lose track and end up returning home."
        "No.":
            "You decide to head home."
    jump home

label home:
    n "Now you're home,"
    n "You think over the events of today and can't help but think you missed something... {w=2.0}something important. {w=0.5}Very, {w=0.2}very important..."
    n "You head to your room, and see your little sister is already in bed."
    menu:
        n "Do you tuck your little sister in?"
        "Yes.":
            a "*Tucks her in.*"
            $ change_obedience(2)
            $ TuckedSisterIn = True
        "No.":
            n "Why? This small deed of good affects the story in no feasible way."
            n "Now your poor little sister will be freezing all night."
            n "How. {w=0.5}Dare. {w=0.5}You."
            $ change_obedience(-20)
            $ TuckedSisterIn = False
            n "But... since I'm the narrator, I can change that myself."
            n "*You tuck your sister in. {w=1.5}As if some mysterious force is making you. {w=1.0}You deeply regret not doing it yourself in the first place.*"
    n "As you fall asleep, you have the same 'off' feeling as before wash over you, fading you into unconsciousness..."
    n "The same words flow circles around your mind, over and over {w=3.0}and over and over{w=1.0} and over and over and over."
    python:
        phrases = ["Misfits—", "2 Nerds—", "3 Freaks—", "3 days—"]
        for i in range(3):
            for p in random.sample(phrases, len(phrases)):
                renpy.say(str(glitch_name()), str(glitch_text(p)) + "{w=0.3}{nw}")
        for i in range(3):
            for p in random.sample(phrases, len(phrases)):
                renpy.say(str(glitch_name()), str(glitch_text(p)) + "{w=0.15}{nw}")
        for i in range(4):
            for p in random.sample(phrases, len(phrases)):
                renpy.say(str(glitch_name()), str(glitch_text(p)) + "{w=0.05}{nw}")
        for i in range(5):
            for p in random.sample(phrases, len(phrases)):
                renpy.say(str(glitch_name()), str(glitch_text(p)) + "{w=0.001}{nw}")
        renpy.say("?..??", "3 days...{w=2.0}{nw}")
        renpy.say("?..??", "They strike.{w=3.0}{nw}")
    n "You gasp awake."
    a "It was only a dream... *sigh* an odd dream at that..."
    n "As you looked around, you saw your sister wasn't there..."
    a "How odd..."
    a "Is she early for school? ... That'd be a first."
    a "*Chuckles to yourself.*"
    n "On your way to school, you don't see your sister."
    n "When you get to school, you hand in your phone and go to your usual spot to meet up with Billey."
    n "He's not there."
    menu:
        "Search more for Billey?":
            $ change_obedience(-5)
            a "Billey?"
            n "You search for Billey, finding him climbing a tree."
            a "There you are, Billey."
            b "Oh, [a.name]! How are you?"
            n "You notice Billey trying to act casual on the tree."
            menu:
                "Good, you?":
                    b "Yeah... yeah... good... lesson? We need to get to lesson."
                    jump lesson1
                "What were you doing on the tree?":
                    menu:
                        b "Uhh... nothing?"
                        "Insist on it.":
                            b "Okay, okay... I was following a squirrel."
                            menu:
                                n "Believe him?"
                                "Yes.":
                                    pass
                                "No.":
                                    b "Ok. The truth? I was looking for a parcel."
                                    a "In a tree? Likely story."
                                    b "Believe me! It's the truth. Just as true as: We need to get to lesson now. Before we're late."
                                    b "Else your 'all so precious' obedience score will be tarnished!"
                                    a "Ha. But I bet your obedience score is so much worse than mine."
                                    b "No clue. I stopped checking it when I got my 15th reduction."
                                    jump lesson1
                        "Leave it be.":
                            pass
                    a "Okay. Let's get to lesson then."
                    jump lesson1
        "Head straight to lesson.":
            $ change_obedience(2)
            jump lesson1
    jump endScreen

label lesson1:
    n "At your first lesson..."
    n "You notice Billey still hasn't shown up."
    n "But he doesn't matter. Your lesson matters. Your obedience score matters. Focus on that. Nothing more."
    b "Sorry, sir, about being late..."
    menu:
        b "*Sits down next to you.*"
        "Why were you so late?":
            b "None... nothing to worry about... "
            b "Eh... {w=0.5}Probably..."
            b "I hope..."
            b "say, in 3 days, do you want to have a sleepover?"
            show text "3 Days." with dissolve
            a "3 days? I—Uh—"
            hide text "3 Days." with dissolve
    a "Sure... I guess..."
    a "Just as long as we don't repeat what happened with my sister... y'know. Third try's not the charm."
    n "You two laugh in unison."
    n "The teacher then glares daggers at the pair of you."
    $ renpy.say("Teacher", "You two lovebirds. Not this again. One warning - and this is it.")
    $ renpy.say("Teacher", "You're always being observed after all. Behave the part.")
    $ change_obedience(-16)
    if obedienceScore > 80:
        $ change_obedience(5)
        a "Yes sir."
    else:
        menu:
            b "You gonna keep playing by their rules, [a.name] or are ya gonna stand up for yourself?"
            "Rules are rules.":
                $ change_obedience(15)
                jump homeAgain
            "Stand up for myself? Hell yes.":
                $ change_obedience(-20)
                b "Say... how interested would you be, theoretically, in..."
                b "... in standing up against the whole system?"
                b "Stand against... them?"
                b "Theoretically, of course!"
                menu:
                    "I mean... sure. I guess.":
                        $ change_obedience(-10)
                        b "If you're certain then meet me in the janitor's closet after school."
                n "(After school.)"
                menu:
                    "Do you go to the closet with Billey?"
                    "Yes.":
                        n "Upon entering the closet, you see Billey, standing there ominously in the dark."
                        jump recruitment
                    "No.":
                        $ change_obedience(2)
                        jump homeAgain

label recruitment:
    a "Yes, Billey?"
    menu:
        b "Can I trust you?"
        "Yes.":
            b "Good."
        "No.":
            b "Haha. Ok, so."
    menu:
        b "Have you heard the rumours of the Misfits?"
        "Yes.":
            b "Splendid!"
        "No.":
            b "Ok. So the Misfits are, allegedly, an elite taskforce that has infiltrated the roots of society,"
            b "planting people - \"Masked\" - amongst us as teacher, janitors, students, and any role."
            b "They carry out protests, riots, data breaches of the government, some of the biggest ever DDoS attacks against surveillance systems,"
            b "all to try and rid us of all the surveillance that has plagued our world."
            a "Okay..."
    a "And... why do I need to know of the Misfits?"
    b "*Presses a strange device to your neck.*"
    b "Because I am one of them."
    a "You... what?!"
    b "I am a Misfit. I've been one for up on a year now. "
    a "And you... want me to join you?"
    b "Exactly."
    menu:
        "Deal.":
            $ change_obedience()
            b "Great. Then follow me."
            jump misfitMeeting
        "No.":
            b "You... you sure?"
            menu:
                "Yes.":
                    b "Then... we can't have you know..."
                    n "A sharp pain spreads through your body and, looking down, you see a gaping hole in your chest. That probably shouldn't be there."
                    jump endScreen
                "No.":
                    b "Then you're joining us. Good."
                    jump misfitMeeting
        "(Call out to nearby teacher to tell on Billey.)":
            a "Help! Misfit member!"
            $ renpy.say("Teacher", "(Rushes over.) Misfit member? This is serious. You sure?")
            a "Yes. Billey is a Misfit."
            $ renpy.say("Teacher", "(Muttering...) Always knew it... (Turns to [a.name].) Good work. *Takes Billey away.*")
            $ change_obedience(20)
            n "Day after day, you don't see Billey. The teachers say he had a 'permanent move to a more optimal area for him to learn'."
            n "They killed him. You're certain."
            n "In your distraught of losing your first and closest friend, you are unable to live with your guilt."
            jump endScreen

label misfitMeeting:
    $ misfit = True
    n "Billey leads you some distance, blindfolded, and takes it off after you hear the sound of a door closing behind you."
    b "[a.name]... this is where we hold our meetings."
    n "It is a small room, rusted table, tiny stools to sit on, meant for young kids,"
    a "This... is surprisingly pathetic for all I've heard of the Misfits."
    b "This is just our Merton base."
    b "Back where we started... it's a lot more put together."
    $ say("Misfit Nerd", "It's not meant to be flashy and impressive. {w=1.0}\nIt's meant to be hidden.")
    menu:
        n "Taken aback by their (slightly rude) abruptness, how do you respond?"
        "Oh. Sorry...":
            pass
        "Never asked it to be polished." if obedienceScore <= 50:
            a "Never asked it to be polished. Merely asked for seats that aren't microscopic stools."
            $ change_obedience(-2)
            b "[a.name], calm down! We're all Misfits here."
    n "A seemingly important Misfit at the head of the table speaks up."
    $ say("Important Misfit", "Enough bickering.")
    $ say("Important Misfit", "We need to plan our next course of action. Is newbie with us or not?")
    menu:
        "Yes.":
            pass
        "100%%":
            pass
        "Sure!":
            pass
        "Damn right.":
            n "Language, kiddo."
        "Bring it on.":
            $ say("Important Misfit", "Now that's the energy!")
        "Yas queen.":
            pass
        "Yessir.":
            pass
        "Say less.":
            pass
    b "*Squeals slightly in joy.* Perfect!"
    b "Well..."
    b "Well... welcome to the club!"
    b "Say, do you like computers?"
    menu:
        "Yes.":
            b "Perfect! Then you can be in our hacker sector. For short, we like to call it our \'Hack Club\'."
            $ HC = True
        "No.":
            b "Ah... oh well."
    n "After the meeting, you've all decided on hacking and taking down the school website - distract the IT team to get more time for other acts against surveillance."
    if HC:
        n "You've been put forth to show your skills and lead this project."
    b "Wait, wait wait wait!"
    b "[a.name], we need to assign you your role."
    b "We have the Geeks. {w=1.0}They find bypasses, exploits, vulnerabilities in the ruined system and do all the research and OSINT required."
    b "Then we have the Neeks. {w=1.0}Field agents who deal with on-the-job tech problems and hacking, specially trained in stealth."
    b "Next up, the Nerds. {w=1.0}Field operatives who do a majority of the strategic planning, sleight of hand, leading, and logical thinking."
    b "Finally, the Freaks. {w=1.0}Rough, strong operatives who might run protests, lead riots, or do a majority of the combat."
    b "And under the hood, the Masked deal with infiltration. They hide under the cover of the system, acting as teachers, students, janitors, or police! Any job needed to fit in and gather intelligence."
    b "My way of fixing the system has always been blowing up the medium into a million pieces and putting it back together in a beautiful sculpture."
    b "But that's just me."
    menu:
        b "So, what do you choose?"
        "Geek":
            $ role = "Geek"
        "Neek":
            $ role = "Neek"
        "Nerd":
            $ role = "Nerd"
        "Freak":
            $ role = "Freak"
        "Masked":
            $ role = "Masked"
    b "So... a [role] called out to you? How intriguing..."
    $ change_obedience(-5)
    b "And here I thought you were a servant of the system. Guess you've proved my doubts to be nothing but that - doubts."
    $ say("Important Misfit", "I'm nicknamed \'Maverick\' by the way.")
    m "I'm the leader of the UK Misfits."
    jump misfitDay

label misfitDay:
    n "You've been assigned to do whatever it takes it disable the security cameras in the bathroom during your 2nd lesson."
    n "First lesson flies by, but now you have lesson 2."
    menu:
        "Go to the bathroom.":
            jump bathroom
        "Go to lesson.":
            jump camerasLesson

label bathroom:
    n "In the bathroom, you see a security camera in the corner of the room with full view of most things."
    n "'To catch vandalism' they said..."
    a "*Mutters* Vandalise the anti-vandalism camera? Perfect."
    while True:
        menu:
            "Climb up on a toilet to reach the camera and give it a good smack.":
                n "You hurt your hand. Ouch."
            "Do the Macarena.":
                n "You try, but you fail it so horribly that everyone in the bathroom stares directly at you in horror, and the security camera sparks and dies, the AI in it overloading."
                jump misfitCamera
            "Throw a rock.":
                n "You see no rock."
            "Throw a brick.":
                n "You try and try to get a brick free, but cement is, believe it or not, quite very strong."
            "Grab a handful of water and throw it at the camera.":
                n "You try, but the water falls through the holes between your hands. Idiot."
            "Wrap your shirt around it.":
                n "You wrap your shirt around it, and walk out shirtless."
                n "But of course you wrapped it around every part but the actual camera part. Only the casing."
            "Use your phone to hack it.":
                n "You start downloading a program \"Hack Security Cameras - No Scam\""
                n "but, since you're in the school bathrooms, your signal is not very good and it takes 5 minutes to get 1%%"
                n "but in that time the teacher sent someone to find you, and they retrieve you from the bathroom."

label camerasLesson:
    n "As you enter lesson, it starts normal, you sit down and the teacher takes the register."
    n "Some bit into the lesson, you remember your goal."
    n "Bathroom. Security cameras. Misfits."
    menu:
        "Ask to go to the bathroom.":
            $ say("Teacher", "No. The lesson has just started.")
        "Do your work.":
            $ say("Teacher", "Well done on the good work, [a.name]")
    n "A couple minutes pass."
    menu:
        "Ask to go to the bathroom.":
            $ say("Teacher", "Are you desperate?")
            menu:
                "Yes.":
                    $ say("Teacher", "Okay, then. But just because you're a good kid.")
                "No.":
                    $ say("Teacher", "Eh, you know what? You're my favourite student. Off you go.")
            jump bathroom
        "Do your work.":
            n "A kid asks to go to the bathroom, but the teacher denies them, saying \"Only kids with [obedienceScore] or more can go mid-lesson. You know this.\""
            menu:
                "Ask to go to the bathroom.":
                    pass
                "Do your work.":
                    $ say("Teacher", "Such as [a.name]!")
                    menu:
                        "Ask to go to the bathroom.":
                            pass
            jump bathroom

label misfitCamera:
    b "Well done!"
    b "How'd it go?"
    menu:
        "Well.":
            b "That's good."
        "Interestingly...":
            b "Why? How did you disable the cameras?"
            a "I... failed at the Macarena..."
            b "Huh?! I— You— Wha—"
            b "You know what? I don't care!"
            b "Everyone in this establishment is mad!"
            b "That's just the chaotic way we do things here."
    b "Anyway, we've got a new job for you. Do you chose to accept?"
    menu:
        b "We need you to kill a kitten."
        "Yes. I... Accept.":
            b "Monster."
            b "But is it necessary. We need you to kill a kitten."
            b "The owner of such a pet fondly named it \"Safia\"."
            b "The owner's name being \"Soya\"."
            n "You get on a train as instructed, and after a bit of a travel, you reach a house."
            menu:
                "The door is locked."
                "Kick it down.":
                    pass
                "Pick the lock.":
                    pass
            n "You make quick work of the lock."
            n "As you enter the building, you see the kitten."
            n "Laying on its side, ribcage showing."
            n "It looks starved. Neglected. Lying awake, eyes wide, pupils dilated."
            n "Yet it stares blankly past you at the wall."
            n "It does not react as you approach."
            n "Nor as the door slams closed, loud enough to make you jump."
            n "It just lays there."
            n "And it looks so much like your sister when she was given alcohol for the first time."
            n "But to your credit, that was an accident."
            menu:
                "Do you kill it?"
                "Yes.":
                    n "No. I am the narrator and I have the power."
                    n "You're only here 'cause I let you be here."
                    n "Now... let. That. Cat. LIVE."
                "No.":
                    pass
            menu:
                "Do you take it home with you?"
                "Yes.":
                    n "KITTY! CAT! SO CUTE! AWEEE!!!"
                "No.":
                    n "You can't bear to leave it. You take it with you."
            $ cat = True
            n "You head back to your house."
            jump catHome
        "No.":
            b "Wrong choice."
            n "You feel a strange sensation growing inside you,"
            n "like you're being lifted from the ground, ascending..."
            n "then, all of a sudden, this sensation collapses in on itself, and a sheer pain - exploding inside of you."
            n "You collapse to the ground, coughing up blood. A bullet alongside that blood."
            jump endScreen

label catHome:
    n "At your house, you set the cat down."
    n "The cat lays there."
    n "You find it some food."
    n "You feed it."
    n "Its eyes finally lay to rest.{w=1.0} It sleeps."
    n "And, at long last. After a long, long day. You plop down in your bed..."
    n "And you rest. You put your troubled mind to ease..."
    n "..."
    n "......"
    n "Your sleep is sound save the deep growling growing suddenly inside you."
    n "It vibrates your whole body, and for a few seconds, your mind goes in full panic as you wake with a jolt."
    n "And you see the root cause."
    n "The cat - Safia - is sleeping right by your head. It was yawning awake."
    n "Your heart shatters at the thought that a human had to consciously neglect them."
    menu:
        "The cat look hungry again."
        "Give it some Tuna.":
            n "Mmmm! Fish..."
            n "Oh yeah, the cat."
        "Give it some dairy milk.":
            n "It immediately starts lapping it up."
        "Give it some oat milk.":
            n "It stares a few moments too long at this strange new liquid, but braves it and drinks some."
            n "Turns out it is slightly better than dairy milk with many environmental advantages."
    n "Very soon, Safia has devoured all you gave it, and seems satisfied."
    n "But very soon you realise something dire."
    n "You realise you've not much for the cat. Food you eat, the bed you sleep, but nothing specifically for it."
    n "No cat bed. No litter box. No cat food (kibble). No leash. Nothing."
    n "And very soon you regret your ignorance as you see fur scattered across your bed, milk spilt everywhere and a need for the cat to stretch its legs."
    n "But before you can care for that, you hear a knocking on the door."
    menu:
        b "[a.name]? You in there?"
        "Yep! Come in!":
            n "Billey sees the cat and stares you dead in the eyes."
        "*Hide Safia.*":
            b "[a.name]?"
            n "Billey uses the keys you gave them to open the door and sees the cat."
        "*Stay silent and still.*":
            n "Safia lets out a loud purr, nuzzling your leg."
            b "[a.name]... is that...?"
            n "Billey uses the keys you gave them to open the door and sees the cat."
            b "Yep..."
    menu:
        b "I thought I told you your mission was to kill the damned thing. Not make it a princess."
        "Sorry...":
            b "If you're sorry then you'll kill the cursed thing."
            b "Now."
            menu:
                "Ok...":
                    n "You grab a pen, stabbing it deep into the cat's heart."
                    n "It's eyes rolls to the back of its head... blood pours out of its chest, covering the pen, streaks of black from the ink."
                    n "You pull your hand away in shock, your hand covered in a mix of black and red."
                    n "You look up at Billey and without a second thought, you say..."
                    a "What next?"
                    b "Next you rid us of the sight of that body."
                    n "And mindlessly you drag the body away. Your conscious filled with guilt, pain, shock and fear. Your subconscious focused only on the task at hand."
                    $ cat = False
                "No!":
                    b "What did you just say?"
                    a "I. Said. No."
                    b "And I say yes."
                    a "Out of my house. Now.{w=1.0} Or else."
                    b "Or else what?"
                    a "Or else..."
                    b "Ha. Another empty threat. Weak as always."
                    n "Those words trigger something deep within you. Something that's been stirring for a while now."
                    n "You lash out. Barely conscious of what you're doing."
                    n "Knife to hand. Wait, no. Keys. Keys to Billey's throat..."
                    n "Digging deep. Drawing blood."
                    n "He resists. He fights back. He knees you in the chest. He gets free. He runs, throat bleeding."
                    n "You stare down at your blood soaked keys."
                    n "You stare down at your sinless sins."
        "Yet you always told me to ignore the system.":
            a "Yet you always told me to ignore the system. To rebel. And yet here I am doing that and you're ANGRY."
            a "Y'know, I think you're, more so than angry, hypocritical and narcissistic."
            a "You hate the confines of the system, yet you've created your own to overthrow the old."
            a "You want to replace one functioning system with another one that works."
            a "People don't like change. You'll feel resistance from the majority who are used to obedience scores."
            a "You're wrong in so many dimensions."
            b "You... you think us Misfits are just another system? Fools to play the game of humanity?"
            b "No! The Misfits are so much more than that!"
            a "So much more than what? What makes them so special?"
            b "Because... because we have a good cause—"
            a "We've all had causes we thought were good. Others begged to differ."
            a "The blunt truth is that you don't seek a better humanity."
            a "You seek control. Followers. A sense of power."
            b "No. I seek the truth—"
            a "The truth is that you've been neglected so long that you've forgotten what were once your core values."
            a "Equality."
            b "I still—!"
            a "Justice."
            b "That's different—"
            a "Kindness."
            b "I..."
            a "You've forgotten what it is to be kind. You've forgotten compassion, empathy. Joy and pain. Kindness and suffering."
            a "You know only what others done to wrong you."
            b "No!"
            n "In a fit of rage, Billey grabs out a gun, pointing it at you."
            b "Stop speaking. Your words are lies spat by a serpent of the devil."
            b "You want to manipulate me. Make me leave the Misfits, but you're wrong! I will stay strong!"
            b "I... I... I... I am in the right. Not you!"
            n "Billey runs out the front door. Runs and runs and runs."
    n "You know what you done is wrong."
    if cat:
        n "You know Billey now hates you."
        n "You know you've wronged him."
        n "You know he wronged you."
        n "But at least you have Safia. Safia, safe and sound. Soft and strong. Slowly and steadily adapting to the new environment."
    else:
        b "Good. Now you can follow orders we can continue."
    jump sister

label sister:
    n "The next day at school, you see Billey. He seems... different... and happy..."
    menu:
        b "Say... where is your sister at? I've not seen her in a while."
        "I... I can't say I entirely know...":
            b "But she's your sister."
            a "Yet an independent person from me."
            if cat:
                a "And it's 'bout time you understood that."
                a "We're not all pawns in your game to be played like junk mail."
                a "We're all human beings who live independent lives."
        "My sister? Right, where IS she?!":
            b "[a.name]..."
            b "I've got to tell you the truth..."
            a "Firstly, my sister. I need to know where she is!"
            b "That's the thing..."
            a "Go on...?"
    b "She has, for years, fought against us."
    b "You wonder why she seems to have endless friends to go out with at every time of day, but in reality, she is out searching for our hideouts."
    b "And yet she is a better fighter than any of us. She's taken down any attempt to shut her down, yet she never kills."
    n "You laugh audibly."
    a "She is not a fighter. I've had to protect her at school when she was about to get 'jumped' for the first time."
    a "So speak your lies no longer. I wish not to hear them."
    b "It's the truth. Despite what you think, your sister is a better actor than you think."
    b "And we need you to avoid her at all costs."
    $ renpy.show_screen("obedience_popup", "++Find your sister at all costs.++")
    jump endScreen

label homeAgain:
    n "The day passes."
    n "School tomorrow? Billey is gone."
    n "The day after? Still no sign of him. Nor of your sister."
    $ change_obedience(5)
    n "3rd day of this? You feel used to it. Day after day passes until you realise you've graduated."
    n "You're on a walk with your new dog."
    n "You take your dog on another walk. And another."
    $ change_obedience(2)
    n "5 years of taking your dog on a walk every two days."
    n "You're old now."
    $ change_obedience(1)
    n "Old and alone. The system taught you to prioritise work over relationships. You worked day in day out."
    n "..."
    n "You're dead now."
    n "Dead and unburied. You died peacefully yet alone. No one noticed. No one realised."
    n "..."
    n "Your rent's due now."
    n "Your landlord finds your rotten corpse on the floor of your living room."
    n "..."
    n "You're done now."
    n "Nothing for you in the land of the living nor dead."
    n "..."
    jump endScreen

define w = Character("Processing Worker")
label endScreen:
    w "You've come here, to the ending screen, for some reason or another."
    w "Welcome."
    w "Now, let's take a look at what we've captured of you..."
    if not BilleyAlive:
        w "So... you deviated to kill your friend? Well done for killing a lead figure."
    if obedienceScore < 0 and misfit:
        w "Uhh...—"
        n "What's?—"
        n "Both the worker and I disappear... I disappeared, how am I speaking? Eh, who cares."
        n "CONTINUITY ERRORS! YEAH!!"
        m "Now that we've got them gone..."
        m "[a.name], you were one of our best members, and we can't have you go just like that."
        m "So what we're gonna do is send you through time and space to join the Misfits in the Misfit HQ, 2031."
        m "The future so not to cause any problems in time."
        jump future
    elif obedienceScore < 50:
        w "You're a traitor of the worst kind."
        if misfit:
            w "AND you joined the Misfits."
            w "Sorry, but there's no coming back from this."
            w "Report to the incineration and replacement facility."
            n "Two armed guards march in and one holds a strange device to your throat, and you swiftly lose consciousness."
    elif obedienceScore < 90:
        w "Your obedience score is far below what we accept."
        w "Please report for refactoring."
    if misfit and obedienceScore >= 50:
        w "As a Misfit, you disrupted our works with your very existence."
        w "For this..."
        w "Report to the incineration and replacement facility."
        n "Two armed guards march in and one holds a strange device to your throat, and you swiftly lose consciousness."
    if obedienceScore > 100:
        w "Wow. Just wow. Your obedience score is higher than even mine."
        w "Wow... I'd applaud you, but I can't take my hand off this button else you'll fall to the incinerator..."
        w "But... you have to take my job."
        w "The person with the highest obedience has this job..."
        n "And with that, the worker takes the keys out of the machine, hand still on button, chucks them to you, and you two swap places."
        n "Never once was the button released. Although you are now the one pressing it."
        n "Then, as the worker is thanking you, your hand slips and the worker plummets."
        $ change_obedience(1)
        n "Day after day you work this job, thousands of people reviewed, and at least 18 a day."
        n "This is your life now. No one was ever able to topple your record."
        n "You've been working this job for who knows how long until, eventually, you see Billey."
        n "Billey is in his 90s. You're still the same age as when you last saw him."
        n "Turns out Billey was a key figure in the Misfits, but you're too overwhelmed by emotion to properly read it."
        n "Billey does not remember you."
        n "No one even noticed you were gone."
        n "The system just... let you fade out..."
    elif not misfit and obedienceScore >= 90 and BilleyAlive:
        n "Your life was meaningless. You did nothing of value."
        n "I feel sorry for you. Actual pity."
    menu:
        "Restart Evaluation?":
            if misfit:
                w "For joining the misfits, you will wait here for a while to think of your actions."
                w "Don't worry, no matter how much you click, it won't be any quicker."
                python:
                    renpy.say(n, "".join("{color=#%06x}...\u200b{/color}{w=0.1}" % random.randint(0, 0xFFFFFF) for _ in range(max(0, int(180.0 - obedienceScore)))))
            if TuckedSisterIn == False:
                w "We're looping back. {w=0.5}Why didn't you tuck your sister in?"
                w "Is it some kind of Personal Vendetta (same name as one of my game - go play it on itch.io!) against your own sister?"
                w "If so, why? She never did anything good nor bad to you! All you see of her is her sleeping in this WHOLE visual novel!"
            jump start
        "Exit":
            return

label future:
    n "You open your eyes."
    n "It is dark."
    n "It is quiet."
    n "And it smells like lavender?"
    n "Taking a look around, you see you're in a huge, luxurious mansion, yet no one in sight - it seems to be night time."
    menu:
        "Explore the current room.":
            n "There is a big TV on the wall, and a red couch, big enough for at least 10 people, placed in front of said TV."
            n "There is also a table in the middle of the room with chairs encapsulating it."
            n "And a grand piano off to the side."
        "Go through the nearest door - a soft pink, cosy door.":
            jump pinkRoom

label pinkRoom:
    n "Upon entering the room, you see it seems to be a child's play area, and from the various things scattered, you can deduce it to be targeted towards the stereotypical female."
    n "And a bed."
    n "A bed in the corner with a young child sleeping on it..."
    n "A violin laid against the bed."
    menu:
        "Hold the violin...":
            call violin
        "Leave it be.":
            pass
    n "The door creaks slightly before flying open, and a man marching in."
    $ say("Man", "You. What's your business here?")
    menu:
        "The Maverick sent me.":
            $ say("Man", "The...?")
            $ say("Man", "I'm the Maverick...")
            $ say("Man", "Wait... [a.name]?")
            a "Yes! That's me."
            m "And the Maverick is me."
        "Who are you?":
            $ say("Man", "I should not trust you, but I do.")
            m "I'm the Maverick. Now, who are you?"
            a "The Maverick! I'm [a.name]! Remember me?"
            m "I... yes, I do!"
    m "Since you left, the Misfits of the UK descended to chaos. The UK is ruined. I was forced to flee to here - the Capital of the Misfits and most surveillance-heavy country in the world."
    a "How... wait, is Billey okay?!"
    m "He's here in this very house... but he's fallen sick."
    a "Is... is he gonna survive?"
    m "Maybe."
    m "We've never seen anything like it."
    m "Even with our advanced technology and hard-working members, we've found nothing."
    m "Nothing whatsoever. Every time we think we're getting somewhere, it seems to mutate into a whole new virus, yet we have no evidence of change."
    a "Are you saying..."
    m "Yes..."
    a "That Billey can name this new virus how they want?!"
    m "*Chucles slightly.* Sadly no, documenting it would blow our cover."
    menu:
        "But... Billey could go to a public hospital? Get it documented? Get it named?":
            m "That would likely doom Billey to certain death. We will not allow that."
        "I... can I see him?":
            m "Not until we can find out how contagious this is."
    n "A few days pass and you learn the ins and outs of this new building, and settling into this new time."
    n "But as the days pass, [m.name] tells you of Billey's condition getting worse and worse and all their attempts at saving him to seemingly no avail."
    n "You're left helpless as you're told Billey passed, not having been able to see him since you got to this new time."
    n "Yet you can't help but feel a little relief."
    n "He was always treated as more than you. Always treated with respect. Always acknowledged."
    n "Yet you got ignored. Disrespected. Dehumanised."
    n "And now without him gone... you won't have people constantly and unfairly comparing you two..."
    n "Why should you be compared to someone with completely different passions, joys, and loves than you?"
    n "Two separate entities are not equatable."

label violin:
    n "The violin fits perfectly in your arms, and you feel an irresistible urge to play it..."
    n "But you resist. Obedience is the way. You put back the violin, and you continue on your way."