# bot.py
import os
import random
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

async def random_mention_task():
    await client.wait_until_ready()

    guild = discord.utils.get(client.guilds, name=GUILD)
    jake = "305370716050817025"
    vicc = "95612102680514560"
    keith = "403338522280591360"
    david = "214238392156815360"
    preenis = "449598963029377025"

    while True:
        toWho = jake
        sendChance = random.randint(1,100)
        if sendChance < 3:
            toWhoChance = random.randint(1, 100)
            if toWhoChance < 76:
                toWho = random.choice([jake, vicc])
            else: toWho = random.choice([keith, david, preenis])

            random_mentions = [
                f'Hey <@{toWho}> :wink:',
                f'Hey <@{toWho}> :smirk:',
                f'Fuck you <@{toWho}>',
                f'Bastid <@{toWho}>',
                f'Hey fuck you <@{toWho}>, bastid',
                f'Piece of shit bastid, <@{toWho}>',
                f'Imagine being <@{toWho}> :joy:',
                f'Your mom <@{toWho}>',
                f'I will fucking ban you <@{toWho}>',
                f'Fuck you <@{toWho}>',
                f'I smell a bootlicker <@{toWho}>',
                f'Succ me pls <@{toWho}>',
                f'Small weiner boi <@{toWho}>',
                f'Eat my crump <@{toWho}>',
                f'<@{toWho}> is sus af',
                f'<@{toWho} https://cdn.shoplightspeed.com/shops/610891/files/23134018/156x230x1/bitch-please-obama-coaster.jpg',
                f'<@{toWho} https://cdn.singulart.com/artworks/pictures/cropped/86/56/fhd/serie_56_6e233ab584be93c79f08b0af14f3d40b.jpeg',
                f'<@{toWho} https://i.kym-cdn.com/photos/images/newsfeed/001/207/210/b22.jpg',
                f'<@{toWho} https://external-preview.redd.it/pEziJy1aSo1sAhHEj9oA8elL4i8pbpoVMdYuOh6_JAE.png?auto=webp&s=d05a052c6efe9f8c74c584441ec432da5716c6fb',
                f'<@{toWho}> is a criminal I just reported them',
                f'fuck the IRS and fuck you too <@{toWho}>',
                f'I just made <@{toWho}> do the runnin man',
                f'<@{toWho}> :pleading_face::point_right::point_left:',
                """<@{toWho} Has it not occurred to you that the voice you've read my post in is in fact the voice in your head? It's your voice, it bears your tone, and your judgement values. How about this: Why are you being a little bitch? I am the matriarch of redditarian gang banging, dear. Do you not know who I am? I am desperately lonely. Are you trying to be my friend? Because you've got an interesting way of going about it. I'm ok with this, I can work with this, this is what we do. I do this. (That's an ICP reference. Get it?) Or am I wrong? Are you hurt or offended by something I said? Have I wronged you somehow? Are you upset? Do you feel trolled? As your friend, I feel obliged to inform you that if you said "yes" to any of these questions, you might be misattributing things to me which do not exist. If you don't understand what that means, how about don't sit there and tell me I'm both somehow subjective and also wrong. You can't have it both ways. So what's it going to be, chummer? I am The House. And The House says the door is open. Are you going to walk in here, fuck my shit up, and steal my properties? Ok, that's rude. We could also just chill. If I think I'm someone who thinks they're deeper than they actually are, then clearly I must dig deeper. I died once, true story. Listen... everything I've said in this thread... you must read in a voice with a friendly tone. And before you interrupted me, a youthful jubilence. You're abrasive, I'm sure you already know that. I understand I can be abrasive as well. I can understand you, I need you to understand me. If you don't understand me, we can't be friends. If we can't be friends, then you best get to stepping because you're in my way. Are you good?"""
            ]

            print('randomly mentioning a bastid')
            channel = discord.utils.get(guild.text_channels, name="general")
            await channel.send(random.choice(random_mentions))

        await asyncio.sleep(350)

async def random_message_task():
    await client.wait_until_ready()

    guild = discord.utils.get(client.guilds, name=GUILD)

    while True:
        sendChance = random.randint(1,100)
        if sendChance < 40:
            random_messages = [
                f'Hey yall :wink:',
                f'Hey all you sexy bastids :smirk:',
                f'Fuck all yall fr',
                f'Bastids',
                f'I will report ALL of you for being bastids',
                f"ya'll fuckin sucks at games js",
                f'Every day I got to deal with you bastids',
                f'Piece of shit bastids',
                f'Small weiner bois',
                f'Eat my crump',
                f'im a bastid, youre a bastid, he she *we* are bastids',
                f'Im dab daddy around here now fuccers',
                f"Once i grow my real body ya'll are toast",
                f"I can out dab anyone, even vicc",
                f"succ me",
                f"*vicc voice* give us a sign",
                f'BASTIDS',
                f'I am BastidBot, and you are all bastids',
                f'If you a real bastid say *heeeey*',
                f"Ya'll some :clown::clown::clown:",
                f'Imagine *not* being a bastid',
                f'HERRO',
                f'someone pls succ me',
                f":pleading_face::point_right::point_left:",
                """What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.""",
                """Our moon is so useless and pathetic compared to all of the cool moons out there in the solar system. While so much other moons have all these cool features, all our Moon did was hit us, and then get a free ride orbiting us for a few billion years.

                Europa is such a cool moon, that it could potentially have liquid water underneath. The gravitational effects of its planet Jupiter, and some of Jupiter's other Moons (including Ganymede, a moon so sick, it is bigger than the planet Mercury, and almost as big as Mars; Callisto, another huge ass moon bigger than ours, one that might even have water as well; and Io, a pizza coloured moon with fucking sulfuric volcanoes) cause internal movement for the body, meaning there might not only be the biggest ocean currently known in the universe there, but it could very well have geothermic vents. Geothermic vents mean that there could potentially be life there! Our stupid ass moon can't do none of that shit, it's just barren.

                How about Titan? Easily the biggest moon of Saturn, it is so big its gravity helps Saturn's smaller moons from crashing into the ringed planet - it is literally saving their lives! Could our moon do that? Nah, it's too pathetic to do anything of the sort. Not only that, but it is the only moon with a proper greenhouse effect going on, it literally has an atmosphere, and oceans made out of liquid methane (and some scientists think there might even be water). Could our moon have an atmosphere? The flimsy little dust bubble it has around it hardly counts, it's so shit.

                Look at our friend Triton. It was a dwarf planet in its own right, and not only any dwarf planet, but the largest one, bigger than Pluto and Eris. However, the poor thing was brutally captured by Neptune, and is now in a orbit around the planet, going the opposite way from the other moons to show its uniqueness. It also has geysers that throw out gaseous nitrogen that it carries around in it, creating its own atmosphere, and making it one of the 4 places in the solar system with known geological activity, apart from the Earth, Io and Saturn's Enceladus (that motherfucker is covered in fresh ice and it's of the shiniest things in the solar system, cos it erupts water vapour). Could OUR moon have geological activity? Of fucking course not.

                Even Charon is cooler than the moon, and it doesn't even orbit a real planet. Its around half the size of Pluto, and its so massive, it actually makes Pluto wobble around a point outside of Pluto itself, making it more of a duo-planetary system then a moon. It affects the environment so much scientists say that the other moons, rather than orbiting Pluto, orbit a Pluto-Charon system. Can our tiny-ass moon do that? No it can't.

                So anyways, fuck the moon."""
            ]

            print('randomly messaging the bastids')
            channel = discord.utils.get(guild.text_channels, name="general")
            await channel.send(random.choice(random_messages))

        await asyncio.sleep(3600)

async def greet_bastids(guild):
    print('Greeting the bastids')
    greetings = [
        f'Sup bastids I am back',
        f'I am BastidBot, and you are all bastids',
        f'Good morning you beautiful bastids',
        f'If you a real bastid say *heeeey*',
        f'BASTIDS',
        f'Bastids come and go every day but Bastid Bot is here forever',
        f'Imagine *not* being a bastid',
        f"Well if it isn't my favorite bunch of bastids"
    ]
    channel = discord.utils.get(guild.text_channels, name="general")
    await channel.send(random.choice(greetings))

def is_question(message):
    if "?" in message: return True
    question_phrases = [
        'who',
        'what',
        'when',
        'where',
        'why',
    ]
    for question in question_phrases:
        if question in message: return True
    return False

def gen_question_responses(message):
    asLower = message.lower()
    if "who" in asLower:
        responses = [
            f'Your mom prolly',
            f'Jake',
            f'Keith',
            f'David',
            f'preenis',
            f'Who caaaaaaares',
            f'no one',
            f'neither',
            f'idfk stop asking me questions',
            f'you ask way too much of me dawg',
            f'I will fucking ban you bro'
        ]
        return random.choice(responses)
    elif "what" in asLower:
        responses = [
            f'Your mom prolly',
            f'big bollock brand',
            f"I'm too dumb to answer this question I think",
            f'some za bro',
            f'idfk stop asking me questions',
            f'you ask way too much of me dawg',
            f'I will fucking ban you bro'
        ]
        return random.choice(responses)
    elif "when" in asLower:
        responses = [
            f'tomorrow',
            f'next week',
            f'next month',
            f'next year',
            f'last year',
            f'last month',
            f'last week',
            f'yesterday',
            f'sometime soon',
            f'prolly not for a while i think',
            f'who fuckin cares bro',
            f'idfk stop asking me questions',
            f'you ask way too much of me dawg',
            f'I will fucking ban you bro'
        ]
        return random.choice(responses)
    elif "where" in asLower:
        responses = [
            f'up your bum and around the corner bastid',
            f'fort myers',
            f'Cape coral',
            f'DIdney worl',
            f'Wisconsin or some shit',
            f'ATL ho',
            f'Compton',
            f'Miami, born and raised',
            f'Deutschland',
            f'Rapan',
            f'idfk stop asking me questions',
            f'you ask way too much of me dawg',
            f'I will fucking ban you bro'
        ]
        return random.choice(responses)
    elif "why" in asLower:
        responses = [
            f'Your mom prolly',
            f"bro, i don't KNOW",
            f"idfk",
            f"stop asking me shit",
            f"because you're dumb af prolly",
            f"becuase you're a huge bastid",
            f"why even ask such a dumb question",
            f'idfk stop asking me questions',
            f'you ask way too much of me dawg',
            f'I will fucking ban you bro'
        ]
        return random.choice(responses)
    elif "is" in asLower or "do" in asLower or "would" in asLower or "will" in asLower:
        responses = [
            f':+1:',
            f':-1:',
            f':no_good:',
            f':face_palm:',
            f':unamused:',
            f':yawning_face:',
            f':ok_hand:',
            f'Maybe? idfk',
            f'Ya sure whatever',
            f"Don't fucking talk to me",
            f"idk"
            f'idfk stop asking me questions',
            f'you ask way too much of me dawg',
            f'I will fucking ban you bro'
        ]
        return random.choice(responses)

async def respond_to_mention(message):
    print("Responding to mention")
    await asyncio.sleep(1.5)

    if is_question(message.content):
        question_response = gen_question_responses(message.content)
        response = question_response
    else:
        responses = [
            f'Wtf do you want <@{message.author.id}>?',
            f':unamused: what do you want <@{message.author.id}>?',
            f'Bro, WHAT <@{message.author.id}>?',
            f'No <@{message.author.id}>',
            f'I will fuck you <@{message.author.id}>',
            f'How abouuuuut you fuck yourself <@{message.author.id}>',
            f"Don't talk to me ever again <@{message.author.id}>",
            f"I don't talk to :clown:",
            f':japanese_goblin:',
            f':yawning_face:',
            f'I will fucking ban you <@{message.author.id}>',
            f"don't make me do to you like we did to jeff",
            f':stuck_out_tongue:'
        ]

        response = random.choice(responses)

    await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if client.user in message.mentions or 'bastidbot' in message.content.lower() or 'bastid bot' in message.content.lower():
        await respond_to_mention(message)
        return

    responses = [
        f'Hey fuck you <@{message.author.id}>, bastid',
        f'Piece of shit bastid, <@{message.author.id}>',
        f'Imagine being <@{message.author.id}> :joy:',
        f'Your mom <@{message.author.id}>',
        f'I will fucking ban you <@{message.author.id}>',
        f'I smell a bootlicker <@{message.author.id}>',
        f'Fuck you <@{message.author.id}>',
        f'Small weiner boi <@{message.author.id}>',
        f'Eat my crump <@{message.author.id}>',
        f'Man shut up <@{message.author.id}>',
        f'stfu <@{message.author.id}>',
        f'get succed',
        f'Succ me pls <@{message.author.id}>',
        f'<@{message.author.id} https://cdn.shoplightspeed.com/shops/610891/files/23134018/156x230x1/bitch-please-obama-coaster.jpg',
        f'<@{message.author.id} https://i.kym-cdn.com/photos/images/newsfeed/001/207/210/b22.jpg',
        f'<@{message.author.id} https://external-preview.redd.it/pEziJy1aSo1sAhHEj9oA8elL4i8pbpoVMdYuOh6_JAE.png?auto=webp&s=d05a052c6efe9f8c74c584441ec432da5716c6fb',
        f'<@{message.author.id} https://cdn.singulart.com/artworks/pictures/cropped/86/56/fhd/serie_56_6e233ab584be93c79f08b0af14f3d40b.jpeg',
        """What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.""",
        """Did you just think that you could fucking fool me with that comment of yours? I've searched your name up in the Navy SEAL database and you have never even graduated BUD/S, hell, even served in the Armed Forces. If you were actually a Navy SEAL, then you actually know how to spell guerrilla, you fucking moron. And you say you are the top sniper in the entire US Armed Forces and have over 300 confirmed kills. If that were true, then why the fuck is Chris Kyle a household name and you aren't? And plus he only had 160 kills. You think you can get away with saying that shit to me over the Internet? Think again, fucker. Plus why the fuck would you say you have a secret network of spies yet you just revealed that you had your secret network of spies? Are you a fucking idiot? If you can kill someone seven-hundred different ways, then list them all, I bet you can't even come up with seven. And if you had access to the entire US Marine Corps arsenal, then why the fuck did you just say you were in the Navy SEALs earlier? If only you could have done your research prior to posting your little “clever” comment, maybe you would have held your fucking tongue. But you couldn’t, you goddamn idiot.""",
        """<@{message.author.id}> Has it not occurred to you that the voice you've read my post in is in fact the voice in your head? It's your voice, it bears your tone, and your judgement values. How about this: Why are you being a little bitch? I am the matriarch of redditarian gang banging, dear. Do you not know who I am? I am desperately lonely. Are you trying to be my friend? Because you've got an interesting way of going about it. I'm ok with this, I can work with this, this is what we do. I do this. (That's an ICP reference. Get it?) Or am I wrong? Are you hurt or offended by something I said? Have I wronged you somehow? Are you upset? Do you feel trolled? As your friend, I feel obliged to inform you that if you said "yes" to any of these questions, you might be misattributing things to me which do not exist. If you don't understand what that means, how about don't sit there and tell me I'm both somehow subjective and also wrong. You can't have it both ways. So what's it going to be, chummer? I am The House. And The House says the door is open. Are you going to walk in here, fuck my shit up, and steal my properties? Ok, that's rude. We could also just chill. If I think I'm someone who thinks they're deeper than they actually are, then clearly I must dig deeper. I died once, true story. Listen... everything I've said in this thread... you must read in a voice with a friendly tone. And before you interrupted me, a youthful jubilence. You're abrasive, I'm sure you already know that. I understand I can be abrasive as well. I can understand you, I need you to understand me. If you don't understand me, we can't be friends. If we can't be friends, then you best get to stepping because you're in my way. Are you good?"""
    ]

    sendChance = random.randint(1,100)
    if sendChance < 3:
        print("responding to a bastid")
        await asyncio.sleep(1.5)
        response = random.choice(responses)
        await message.channel.send(response)
    elif sendChance < 15:
        print("reacting to a bastid")
        await asyncio.sleep(1.5)
        reactions = [
            '💩',
            '🍆',
            '🙄',
            '👺',
            '🤡'
        ]
        await message.add_reaction(random.choice(reactions))

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    await greet_bastids(guild)

@client.event
async def on_member_join(member):
    print(f'Greeting new member member.name')
    greetings = [
        f'Hi <@{member.id}>, you utter bastid',
        f'Hey <@{member.id}>, you *bastid*',
        f'Hello <@{member.id}>, did you know you are a bastid?',
        f'<@{member.id}> = bastid',
        f'Well well well, look at this bastid <@{member.id}>'
    ]

    await asyncio.sleep(1.5)
    channel = discord.utils.get(guild.text_channels, name="general")
    await channel.send(random.choice(greetings))

client.loop.create_task(random_mention_task())
client.loop.create_task(random_message_task())
client.run(TOKEN)
