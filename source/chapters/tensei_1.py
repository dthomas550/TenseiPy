# Import all game_functions' funcs for easy access.
from game_files.game_functions import *
# Import the next chapter to continue to.
from chapters.tensei_2 import ch2_goblin_encounter
from game_maps.game_location import cave_actions
from game_maps.game_location import *
from random import randint

def ch1_cave(rimuru):
    class wake_up:
        __location = 'Sealed Cave'

        def __init__(self):
            rimuru.set_start_state()
            idots()
            print()
            siprint("<< Confirmation Complete. Constructing body that does not require blood... >>\n")
            siprint("<< Confirmation Complete. Acquiring skill: [Predator]... >>")
            rimuru.add_attribute('Predator', top_newline=False)
            siprint("<< Confirmation Complete. Acquiring: Extra Skill [Sage]... >>")
            rimuru.add_attribute('Sage', top_newline=False)
            rimuru.upgrade_attribute('Sage', 'Great Sage')
            print()
            siprint("It's so dark? Where is this? What happened?")
            siprint("I remembered now. I got stabbed!")
            siprint("Was I saved? Can I move? Should I try to say something?")

            # Because I am a dick. There is a 1 in 1,000 chance that you will wake up and just instantly die! kek!
            if get_random(1, 1_000, 666):
                siprint("\nWAIT! WAIT WHAT'S THAT AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
                siprint("SOMETHING IS EATING MEEEEEEEEEEEEEEEEEEEEEEEEEE!!!!!!!!!!!!!!!")
                print("\n\nYou died before you could even do anything, what bad luck you have!")
                print("Watch out for [Evil Centipedes] on your next reincarnation little slime! hehehehee....")
                game_over()

            # Show user HUD and playable actions.
            game_action(self)

        class move:
            __subs = ['feel', 'touch']
            def __init__(self):
                siprint("Where are my arms, I can't feel them!")
                siprint("Did I just move? I can't see anything, can't hear, can't even smell anything...")
                siprint("What is this thing? It feels like I'm 'absorbing' something.")
                siprint("This body? Am I even human anymore!?!?!")

        class speak:
            __subs = ['try to speak', 'try speaking', 'try to talk', 'try talking', 'talk', 'say something', 'try to say something', 'yell', 'try to yell', 'try yelling', 'say something', 'try saying something', 'use mouth']
            def __init__(self):
                siprint("I can't seem to speak, wait.....")
                siprint("I CAN'T FEEL MY MOUTH!")
                siprint("I. Can't. Feel. ANYTHING! I should check the rest of my body!")

        class _inspect_body(cave_actions):
            __subs = ['examine', 'examine body', 'examine self', 'examine myself', 'inspect', 'check body', 'inspect my body', 'feel body', 'feel', 'feel around', 'move around', 'check', 'check if human']
            def __init__(self):
                siprint("What is that feeling? Is....is that grass?! It feels like it's dissolving...")
                iprint("\n< Hint: Try to 'eat grass' or 'eat ore', see what happens.")
                game_action(self)

            class eat_grass:
                __subs = cave_actions.eat_grass.__subs
                def __init__(self):
                    rimuru.add_inventory('hipokte grass')
                    learn_about_skills()

            class eat_ore:
                __subs = cave_actions.eat_ore.__subs
                def __init__(self):
                    rimuru.add_inventory('magic ore')
                    siprint("What is this hard feeling stuff?")
                    siprint("<< Information, analysis shows this is the raw form of [Magisteel]. Can be used for crafting weapons, armor, and more. >>")
                    siprint("Ok, might be useful in the future. Guess I should get as much as I can")
                    learn_about_skills()

            class puyo:
                __subs = ['squish', 'bounce']

                def __init__(self):
                    sprint("Puuuuuuuuuuuuyooooooooooo!")

            class _explore:
                __subs = move_on_subs

                def __init__(self):
                    siprint("More grass... Woooo!")
                    learn_about_skills()

    class learn_about_skills(cave_actions):
        def __init__(self):
            show_art('slime')
            print(game_art.rimuru_art.died)
            idots(3, 8)
            siprint("Dissolving and absorbing, this streamlined elastic feeling body....")
            siprint("It looks like I have been stabbed, died and reincarnated as a slime!")
            siprint("\nIt's been a long time since I have accepted myself a slime. I am getting use to this body.")
            siprint("I don't need sleep or food. I can't feel heat nor cold. Even after bumping into rocks I'll quickly regenerate.\n")
            if rimuru.check_acquired('hipokte grass') or rimuru.check_acquired('magic ore'):
                self.where_did_it_go()
            else:
                siprint("All I can do is fumble around in the dark and eat what I find... I'M SO BORED!")
            game_action(self)

        class eat_grass:
            __subs = cave_actions.eat_grass.__subs
            def __init__(self):
                if not rimuru.check_acquired('hipokte grass'):
                    rimuru.add_inventory('hipokte grass')
                    learn_about_skills.where_did_it_go()
                else:
                    rimuru.add_inventory('hipokte grass')

        class _hfunc_craft_full_potion:
            def __init__(self):
                if rimuru.check_acquired('full potion'):
                    siprint("I have a feeling these will come in handy.")

        class _keep_exploring:
            __subs = move_on_subs + ['fumble around', 'keep fumbling', 'fumble', 'more fumbling', 'fumble more']
            def __init__(self):
                siprint("It's just... very lonely here. Wherever here is. I've been eating grass just to pass the time.")
                siprint("There seems to be always some grass to eat, the occasional magic ore, and more to explore!")
                siprint("But lets keep moving!")
                in_water()

        class what_are_skills:
            __subs = ['what are skills?', 'skills?', 'tell me more about skills', 'what are these skills?']
            def __init__(self):
                siprint("<< Answer, when growth is recognized by the world, occasionally one will obtain a [Skill]. >>")
                siprint("What an interesting world! It's nice to have someone to talk to, even if it is a one way with a skill.")

        class what_is_predator:
            __subs = ['predator?', 'what is predator?', 'what is this predator?', 'what is this predator skill?', 'predator huh', 'tell me more about predator', 'tell me more about predator']
            def __init__(self):
                siprint("<< Answer, unique skill [Predator] allows one to 'eat' targets, store said targets in skill's stomach, or isolate as hazardous material.")
                siprint("<< Also, after successful analysis on a monster one can use mimicry to replicate appearance, and use replaceable abilities from target. >>")
                iprint("\n< Hint: Try 'info predator' to get more information. >")

        class what_is_great_sage:
            __subs = ['what is this great sage?', 'what is great sage?', 'great sage?', 'tell me more about great sage', 'what are you', 'tell me more about you', 'tell me more about yourself great sage', 'tell me more about yourself']
            def __init__(self):
                siprint("<< Answer, my function is to assist my master (you) to the best of my abilities. >>")
                siprint("<< Information, basic functions I am able to perform is: Analysis, skill control and manipulation, crafting, and more. >>")
                iprint("\n< Hint: Use 'info great sage' to get more information. >")

                if rimuru.check_acquired('hipokte grass'):
                    iprint("< Hint: Try 'info hipokte grass'. Then try 'craft full potion' command. >")

        class where_did_it_go:
            __subs = ['where did the grass go?', 'where did that all go?', 'hey where did that go?', "where's the grass?", "where's the grass now?", 'where is the grass?', 'where is the grass now?', 'where did it go?']
            def __init__(self):
                siprint("Where do that stuff I eat up go?")
                siprint("<< Answer, they are stored inside the Unique Skill [Predator]'s stomach sack. >>")
                siprint("Whoa! Who's that?")
                siprint("I think I heard this voice before. Who, or what, are you?")
                siprint("<< Answer, this is the Unique Skill [Great Sage], the ability has adapted to best assist you. >>")
                siprint("Skills and predator? huh... Wonder what those are.")
                siprint("\n.... Or should I just forget about that and just move on?")

    class in_water:
        __location = "Under water?"

        def __init__(self):
            print(game_art.rimuru_art.fall_in_water)
            siprint("I'M GOING TO DIE... AGAIN!")
            siprint("SHIT! I've finally reincarnated and I'm already going to die!")
            siprint("O'Great sage how painful thy death will be? Am I really going to suffocate to death?!?!")
            siprint("<< Information, A slime's body does not require oxygen to survive. >>")
            siprint("Huh.... I'm not feeling any pain. But what am I going to do now?\n")
            idots()
            siprint("I thought of something... I could suck up some of water then I can and expel it at a high pressure...")
            game_action(self)

        class stay_in_water:
            __subs = wait_subs + ['stay in water', 'wait in water']

            def __init__(self):
                idots(5)

        class eat_water:
            __subs = ['intake water', 'suck water', 'suck up water', 'suck in water', 'suck up some water', 'intake some water', 'suck water up', 'eat more water', 'predate more water', 'suck up more water']
            def __init__(self):
                rimuru.add_inventory('water')
                rimuru.add_attribute('Hydraulic Propulsion', show_acquired_msg=False)
                siprint("Alright, now lets try this out.")

        class try_getting_out:
            __subs = ['spew water', 'eject water', 'vomit water', 'try getting out', 'try to get out', 'swim', 'swim up', 'swim out', 'try swimming', 'leave water', 'try to swim', 'find a way out', 'get out', 'use water to propel', 'propel with water', 'expel water to propel', 'expel', 'expel water', 'expel the water']
            def __init__(self):
                if rimuru.check_acquired('hydraulic propulsion'):
                    siprint("Let's see if I can get out now.")
                    rimuru.use_skill('hydraulic propulsion')
                    find_veldora()
                else:
                    siprint("It's really hard to move in water, I need to find some way out!")

        class _hfunc_use_skill:
            __subs = ['use hydraulic propulsion', 'use new skill', 'use skill']
            def __init__(self):
                if rimuru.check_acquired('hydraulic propulsion'):
                    rimuru.use_skill('hydraulic propulsion')
                    find_veldora()

        class hfunc_grab_sword:
            __subs = ['look for treasure', 'look for things', 'search for things', 'search for treasure', 'grab sword', 'get sword', 'eat sword', 'predate sword', 'find treasure', 'grab treasure', 'eat treasure', 'predate treasure']
            def __init__(self):
                #rimuru.add_inventory('magisteel sword')
                siprint("HEY! Look! It feels like a sword! Wonder if it's any good?")
                siprint("<< Answer, analysis of sword shows it contains a magisteel core. This sword is above average. >>")
                siprint("Would you look at that, that might come in handy later on. But I'm still stuck down here!")
                in_water.hfunc_grab_sword.__subs = []  # Only able to grab sword once.

    class find_veldora(cave_actions):
        __location = "Sealed Cave"

        def __init__(self):
            siprint("Ouch! I hit something, but at least it seems like I'm back on land.")
            siprint("<< Notice, New skill [Hydraulic Propulsion] acquired. >>")
            siprint("Oh cool, I wonder what else I can do with this skill.")
            sprint("~ Can you hear me small one. ~")
            siprint("I almost pissed myself, if I could that is. Who's that speaking to me!? It can't be [Great Sage] could it?")
            siprint("This is the first conversation I'm having since reincarnating. According to [Great Sage] I've been in this cave for about 90 days!")
            siprint("Should I be friendly? But how do I even reply?. It's not like I have a mouth to speak with.")
            sprint("~ Hey can you just reply? ~")
            game_action(self)

        class hello:
            __subs = ['hi', 'reply', 'reply hi', 'reply with hi', 'repy with hello', "who's there?", 'who is there?', 'who is that?', 'somebody there?', "who's out there?", "is somebody there?", 'who is that speaking?', 'hello?', 'hello there!', "who's that speaking?", "who's that talking?"]
            def __init__(self):
                sprint("~ Keep following my voice small one. ~")

        class great_sage:
            __subs = ['that you great sage?', 'is that you great sage?', 'was that you great sage?', 'was it great sage?', 'great sage?']
            def __init__(self):
                siprint("<< Information, negative, that was not me. I am detecting incoming telepathy, source unknown. >>")
                siprint("Maybe I can try to following it if I keep moving, it seems to be getting stronger.")

        class _follow_voice:
            __subs = ['follow the voice', 'locate the voice', 'try locating the voice', 'try locating voice', 'try finding the voce', 'try following the voice', 'seek out voice', 'seek voice', 'follow strange voice', 'seek strange voice', 'follow']
            def __init__(self):
                siprint("I hit something, but it's not a rock. And what is this aura that I'm feeling? Could it be?")
                found_veldora()

        class _leave:
            __subs = move_on_subs
            def __init__(self):
                sprint("~ Hey, are you just going to keep ignoring me? ~")
                sprint("...")
                sprint("~ Wait where are you going? ~")
                sprint("You seem pretty suspicious...")
                sprint("~ Nooooo.... I'm not suspicious at all.l.l.. ~")
                tempest_serpent_encounter()

        class shut_it:
            __subs = ["shut it you baldy!", "screw you baldy!", 'shut up baldy!', 'shut up!', 'shut it!']
            def __init__(self):
                sprint("~ BALDY, HAHAHA, SEEMS LIKE YOU HAVE A DEATH WISH!!! ~")
                sprint("I'M SORRY!")
                sprint("I'm sorry! I didn't think you could hear me!")
                sprint("~ Come closer small one. ~")
                siprint('uh.... Should I follow the voice?')

    class found_veldora(cave_actions):
        def __init__(self):
            sprint("Hello? I never expected to speak with anyone other than my skill, since I can't see or hear.")
            sprint("~ It's a kind of telepathy. hmmmm..... Alright... fine, I'll help you see. Just don't be scared when you see my true form.")
            sprint("~ There is something called [Magic Perception], it allows you to perceive the surrounding magic essence. ~")
            sprint("What's this magic essence?...")
            siprint("<< Answer, this world is covered with magic essence for example, the body of a slime can move because it absorbs magic essence from it's surroundings. >>")
            sprint("~ With this skill you will be able to 'see', 'hear' and much more! ~")
            sprint("Eh... this feels really complicated. It won't hurt to try though... Will it???")
            siprint("<< Suggestion, in order to organize large amount of information, would you like to activate linking with [Great Sage] and [Magic Perception]. >>")
            game_action(self)

        class _use_magic_perception(cave_actions):
            __subs = ['try magic perception', 'try using magic perception', 'activate magic perception', 'yes', 'yes please!', 'yes do it', 'activate', 'activate it!', 'yes, activate it']
            def __init__(self):
                idots(3)
                show_art('magic perception')
                sprint("Like this?")
                rimuru.add_attribute('Magic Perception')
                sprint("I can see. I CAN SEE!")
                sprint("~ Seems like you did it. You learn quickly small one. ~")
                sprint("Yes, thank you!")
                sprint("~ Shall I formally introduce myself now? ~")
                game_action(self)

            class _yes:
                __subs = ['sure', 'why not', 'go ahead']
                def __init__(self):
                    sprint("My name is Storm Dragon Veldora! ~")
                    show_art('cave veldora')
                    sprint("~ I am one of the four True Dragons of this world. ~")
                    sprint("HOLY SHIT, you're a real dragon!")
                    sprint("~ Didn't I tell you not to get scared. ~")
                    friend_veldora()

            class _no:
                __subs = ['no!', 'nah', "let's move on", "don't", 'skip', 'skip it']
                def __init__(self):
                    sprint("~ Alright fine, I won't. Hmmmmph ~")
                    friend_veldora()

        class no:
            __subs = no_subs
            def __init__(self):
                sprint("~ Welllll? I'm waiting..... ~")
                siprint("<< Notice, activate linking? >>")

        class _leave:
            __subs = move_on_subs + ['no, leave', 'leave', 'leave him', 'leave dragon', 'escape']
            def __init__(self):
                sprint("Wait where are you going small one! Weren't we getting somewhere......")
                sprint("Hello? Hellooooooooooo?!")
                sprint("FINE! I don't need you anyways!")

    class friend_veldora(cave_actions):
        def __init__(self):
            sprint("Hmmmm, now what?")
            siprint("Should I try make a friend? Or just leave, there's something supsicious about him...")
            game_action(self)

        class _leave:
            __subs = move_on_subs
            def __init__(self):
                sprint("I guess I'll be heading out now.")
                sprint("Really, so soon. But we just started!")
                sprint("Stay, please, we have so much to talk abo.o.o...")
                siprint("Phew, I think I lost him.\n")
                tempest_serpent_encounter()

        class _friend_dragon(cave_actions):
            __subs = ['befriend dragon', 'ask to become friends', 'want to be friends?', 'wanna be friends?', 'become friends', 'friend', 'friend him', 'ask to be friends', 'make friend']
            def __init__(self):
                sprint("Okay... sooo, you want to be friends?")
                sprint("HAHAHA, WHAT?! A mere slime wants to be friends with the great Storm Dragon Veldora!?")
                sprint("Wellll... If you don't want to, that's fine too.")
                sprint("Now hold on, who said we can't!")
                sprint("I guess it can't be helped.")
                sprint("Great. Now I guess I should look this seal heh?")
                siprint("Wonder how he got imporisoned in the first place.....")
                game_action(self)

            class _look_at_seal(cave_actions):
                __subs = ['analyse seal', 'analyse prison', 'check seal', 'check prison', 'scan seal', 'scan prison', 'check out seal', 'check out prison']
                def __init__(self):
                    rimuru.add_attribute('mimic')
                    global veldora
                    veldora = mobs.Veldora_Tempest()
                    siprint("[Great Sage]?")
                    siprint("<< Answer, analysis shows it's impossible to destroy [Infinity Prison] using any physical attacks. >>")
                    siprint("<< Notice, possible solution may be...")
                    sprint("Hey, don't ignore me.")
                    sprint("It might be possible if we both analyze [Infinity Prison] inside and out")
                    sprint("My skills were sealed away as well, I can't use analyze.")
                    sprint("If you give me the information [Great Sage] can analyze your side as well")
                    sprint("Won't that take a long time? Didn't you say something about going out to find other reincarnates?")
                    sprint("I have a suggestion! How about you get in my belly!")
                    sprint("hahaha")
                    sprint("ku hahaha")
                    sprint("HAHAHAHAHAHAHA")
                    siprint("Ummmm, did he just use the 3 stage laugh?!?")
                    sprint("My life is in your hands.")
                    sprint("Wow how trusting of you.")
                    sprint("Well... The alternative is to stay in this cave for the rest of my lonely time.")
                    sprint("Before that, let me give you a name, and you think of a name for both of us.")
                    sprint("Like a family name? hmmmmm...")
                    family_name = str(input("\nFamily Name > "))
                    veldora.family_name = family_name

                    rimuru.family_name = family_name
                    rimuru.divineProtection = 'Storm Crest'
                    siprint("< Acquired: Storm Crest Divine Protection >\n")
                    rimuru.update_ranking(8)

                    sprint(f"Hmmmmmm... How about {family_name}")
                    sprint("That name is AWESOME!")
                    siprint("He actually likes it?")
                    sprint(f"From now on I will be Veldora {family_name}")
                    sprint("And as for you...")
                    rimuru.name = str(input("\nName > "))
                    sprint(f"How about {rimuru.name}!")

                    sprint("Until we meet again small one!")
                    siprint("<< Use Unique skill [Predator]? >>")
                    game_action(self)

                class eat_grass:
                    __subs = cave_actions.eat_grass.__subs
                    def __init__(self):
                        rimuru.add_inventory('hipokte grass')
                        sprint("Hey what are you doing there? Focus on me... ME!")

                class _eat_veldora:
                    __subs = all_yes_subs + ['predate veldora', 'eat dragon', 'eat the dragon', 'predate dragon']
                    def __init__(self):
                        veldora.update_info()
                        rimuru.add_inventory(veldora)
                        rimuru.add_mimic(veldora)
                        siprint("\n<< Notice, start analyzing Unique Skill [Infinity Prison]? >>")
                        game_action(self)

                    class _start_analysis:
                        __subs = all_yes_subs + ['start it!', 'yes start it please!', 'yes start it!']
                        def __init__(self):
                            siprint("Yes! Please take care of it [Great Sage].")
                            rimuru.update_status('veldora', 'Analyzing')
                            siprint("< Analysis Started >")
                            siprint("I hope you get out quickly Veldora!")
                            tempest_serpent_encounter()

                    class ignore:
                        __subs = no_subs + ['do not start analysis', "don't start analysis", 'cancel analysis', "don't start", 'ignore him', 'leave it', 'leave him', 'trap him', "don't help him", 'do not help him']
                        def __init__(self):
                            siprint("You know what, no. I think I'll just leave that for now. Hehehe...")

                    class _move_on:
                        __subs = move_on_subs + ['ignore him, lets move on']
                        def __init__(self):
                            siprint("ehehhh... Veldora is gonna be pissed that I didn't immediately start, will he think I betrayed him...")
                            tempest_serpent_encounter()

                class ask_about_seal:
                    __subs = ['so how did you get here anyways?', 'ask about seal?', 'ask about his story?', 'how did you get imprisoned?', 'how did you get here?', 'who did this to you?']
                    def __init__(self):
                        sprint("Will you see, that's kind of a long story. Not one to be told here.")

            class _leave_veldora(cave_actions):
                __subs = move_on_subs + ['leave veldora', 'leave friend', 'abandon veldora', 'abandon him', 'abandon friend']
                def __init__(self):
                    siprint("OK, I go now.")
                    siprint("WAIT! WHAAAAAT!")
                    siprint("I we were friends :(.......")
                    siprint("Please come back friend!")
                    sprint("I got to go! Bye!")
                    tempest_serpent_encounter()

    class tempest_serpent_encounter:
        __location = 'Sealed Cave'
        def __init__(self):
            mobs_new(['tempest serpent', 'giant bat', 'black spider', 'evil centipede'])
            siprint("I've been looking for the cave exit for a bit now.... This cave is so big! Or am I just small?")
            siprint("<< Answer, you are just small. >>")
            siprint("Oh, thanks for that.")
            siprint("* But before long some monsters started taking a interest in the small slime. *\n")
            siprint("What is that? it looks like a big snake!")
            siprint("<< Answer, this is a [Tempest Serpent]. >>")
            siprint("Still, it's not as scary as Veldora. I should be able to handle it.")
            siprint("However, I don't think I have any ways to attack or damage it if it's hostile. Hmmmmmm. I wonder...")
            siprint("\n< Hint: Try 'target tempest serpent'. Then try 'attack water blade' or 'attack water bullet'. >")
            game_action(self)

        class sneak_away:
            __subs = ['sneak out', 'try sneaking out', 'try to sneak out', 'try escaping', 'try to sneak away', 'try sneaking away', 'try sneaking out', 'try slipping out', 'try to slip away', 'try to slip out', 'slip away']
            def __init__(self):
                siprint("Crap! It noticed me, no sneaking out now!")

        class _hfunc_predate:
            __subs = ['eat']
            def __init__(self):
                if rimuru.check_acquired('sense heat source'):
                    siprint("< HINT: Try [Sense Heat Source] to detect foes using the 'use' command, or use 'nearby'. 'help' for more info. >")

        class _move_on:
            __subs = move_on_subs
            def __init__(self):
                if mobs_cleared():
                    at_cave_exit()
                else:
                    siprint("I still sense some enemies around.")
                    if rimuru.check_acquired('sense heat source'):
                        siprint("Oh yeah! I have that new [Sense Heat Source] skill, that might be useful.")
                        siprint("\n< Hint: Try 'nearby' or 'use sense heat source' to locate nearby mobs. >")
                        siprint("< Hint: Then use 'target' and 'attack' on them, also try 'help' if lost.")


        class _attack_water_bullet:
            __subs = ['learn water bullet', 'learn fast water attack', 'learn water attack']
            def __init__(self):
                rimuru.add_attribute('water bullet')
                rimuru.attack('water bullet')
                siprint("Nice, it worked. After learning [Hydraulic Propulsion], I was thinking I could use water as an attack too.")
                siprint("Now I have a way to attack.\n")
                tempest_serpent_encounter.hfunc_attack()

        class _attack_water_blade:
            __subs = ['learn water blade', 'learn slashing water attack', 'learn water attack']
            def __init__(self):
                rimuru.add_attribute('water blade')
                rimuru.attack('water blade')
                siprint("Hey, it worked. Since I already have [Hydraulic Propulsion], I was thinking I could use super high pressure water as a blade attack also.")
                siprint("Lets try it out!")
                tempest_serpent_encounter.hfunc_attack()

        class hfunc_attack:
            def __init__(self):
                if not mob_status('tempest serpent'):
                    siprint("Wow, what a powerful attack. I should probably use that only when needed.")
                    siprint("<< Suggestion, Use Unique Skill [Predator]. >>")
                    siprint("Oh...? What will that do?")
                    siprint("<< Answer, after predation, information and target's skills may be obtained through analysis. >>")
                    siprint("\n< Hint: Try 'eat' or 'predate' to use predation. >")
                    siprint("\nWait, are those bats over there?")
                    siprint("<< Answer, they are commonly known as [Giant Bat]. >>")
                    siprint("And it seems like there's some other small monsters dwelling in here aswell.")
                    siprint("Should I clear them out before they notice me? Or try sneaking out.")

                if mobs_cleared():
                    at_cave_exit()

    class at_cave_exit:
        def __init__(self):
            siprint("Finally! Found the exit. Wow, that's a pretty big door. How am I going to open that?")
            siprint("Water attack? No, that'll probably be overkill. Wait somethings happening.")
            siprint("Wait! They look like people! Three of them. What are they doing here?")
            siprint("I should wait and sneak out when they leave.")
            sprint("Phew, it's finally open, even the keyhole was rusted.")
            sprint("It is over 300 years old, and nobody is maintaining it. I doubt there's a real dragon in here.")
            sprint("Still reckless of the guildmaster to send us to investigate.")
            siprint("How can I understand them?")
            siprint("<< Answer, [Magic Perception] converts sound waves to comprehensible sentences which I interpret for you. >>")
            siprint("<< Also, sound waves can also be used to communicate your thoughts. >>")
            sprint("I shouldn't show, they'll probably get scared and attack me")
            game_action(self)

        class _sneak_out:
            subs = ['wait', 'sneak out', 'wait to sneak out', 'wait to slip out', 'try to slip out', 'sneak away', 'sneak out after them', 'wait to sneak away', 'sneak past']
            def __init__(self):
                siprint("Finally! I'm out of that cave. Where now to though?")
                continue_to(ch2_goblin_encounter)

        class _say_hi:
            def __init__(self):
                sprint("HELLO THERE!")
                sprint("AHHHHHHHHHHHHHH MONSTER.")
                sprint("KILL IT. KILL IT.")
                sprint("KILL IT!!!!")
                sprint("WAIT, Wait. I'm not a bad slime slurrrr.....")
                siprint("* The adventurers attacked and killed the little slime monster before he could say anything else. *")

                if rimuru.check_acquired('veldora'):
                    siprint("* After the little slime died. All of his stomach contents spewed outwards. *")
                    siprint("* Unfortunately, this particular little slime had somehow absorbed a whole dragon! *")
                    siprint("* Now with the three low-level adventurers swiftly flattened by such a massive object. They Have failed there simple mission. *")
                    sprint("What is this? Where is that little slime? Hello.... Friend?")
                    sprint("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

                game_over()

        class _attack:
            __subs = []
            def __init__(self):
                game_over()

    wake_up()
