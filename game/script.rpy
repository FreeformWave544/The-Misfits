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

define n = Character("Narrator")
define a = Character("You")
define b = Character("Billey")
default BilleyAlive = True
default BilleyRun = False
default TuckedSisterIn = ""
default obedienceScore = 96.0
default misfit = False
define HC = False
define role = ""
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
    $ obedienceScore = 96.0
    $ a = Character(renpy.input("What is your name? ", length=20).strip() or "Alex")
    n "*BEEP BEEP*"
    n "{w=0.2}*BEEP BEEP*"
    n "Your 9 AM alarm beeped loudly."
    n "It was a day like all the others."
    n "Nothing observed to differ from the norm."
    show screen obedience
    a "*Sigh* Another 11 hour school day... {w=1.0}'optimal' knowledge retention they said..."
    a "Ha{w=0.2}.{w=0.2}.{w=0.2}. optimal for collecting data we know."
    jump misfitMeeting
    # jump presence

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
                n "You might want to slow down a bit...{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}"
            jump presence
        "Keep walking.":
            jump home
        "Turn a corner then make a run for it.":
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
                        n"Did you misread shout as shoot?"
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
                            jump BilleyRunning
                "Keep walking. {w=0.2}Any delay from your route will affect your obedience score.":
                    jump home
                "Walk towards him.":
                    a "Billey?"
                    $ change_obedience(-10)
                    jump BilleyRunning
        "Run.":
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
        for i in range(4):
            for p in random.sample(phrases, len(phrases)):
                renpy.say(str(glitch_name()), str(glitch_text(p)) + "{w=0.15}{nw}")
        for i in range(5):
            for p in random.sample(phrases, len(phrases)):
                renpy.say(str(glitch_name()), str(glitch_text(p)) + "{w=0.05}{nw}")
        for i in range(10):
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
    a "Just as long as we don't repeat what happened with your sister... y'know. Third try's not the charm."
    n "You two laugh in unison."
    n "The teacher then glares daggers at the pair of you."
    $ renpy.say("Teacher", "You two lovebirds. Not this again. One warning - and this is it.")
    $ renpy.say("Teacher", "You're always being observed after all. Behave the part.")
    $ change_obedience(-16)
    if obedienceScore > 80:
        a "Yes sir."
    else:
        menu:
            b "You gonna keep playing by their rules, [a.name] or are ya gonna stand up for yourself?"
            "Rules are rules.":
                $ change_obedience(15)
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
        n "You've been put fourth to show your skills and lead this project."
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
        b "So, what do you chose?"
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
    b "And here I thought you were a servant of the system. Guess you've proved my doubts to be nothing but that - doubts."

label homeAgain:
    pass
    # REMEMBER THIS!!

define w = Character("Processing Worker")
label endScreen:
    w "You've come here, to the ending screen, for some reason or another."
    w "Welcome."
    w "Now, let's take a look at what we've captured of you..."
    if not BilleyAlive:
        w "So... you deviated to kill your friend? Well done for killing a lead figure."
    if obedienceScore < 50:
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
    if not misfit and obedienceScore >= 90 and BilleyAlive:
        n "Your life was meaningless. You did nothing of value."
        n "I feel sorry for you. Actual pity."
    menu:
        "Restart Evaluation?":
            if misfit:
                w "For joining the misfits, you will wait here for a while to think of your actions."
                w "Don't worry, no matter how much you click, it won't be any quicker."
                python:
                    renpy.say(n, "".join("{color=#%06x}...\u200b{/color}{w=0.1}" % random.randint(0, 0xFFFFFF) for _ in range(max(0, int(200.0 - obedienceScore)))))
            if TuckedSisterIn == False:
                w "We're looping back. {w=0.5}Why didn't you tuck your sister in?"
                w "Is it some kind of personal vendetta (same name as one of my game - go play it on itch.io!) against your own sister?"
                w "If so, why? She never did anything good nor bad to you! All you see of her is her sleeping in this WHOLE visual novel!"
            jump start
        "Exit":
            return
