import discord; import os; import re; import random
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents); cat = 0
hello = ['haiii', 'hi hello nya~', 'mraow', 'hihihihiii hewoo', 'harro', 'ha-iiiiii', ':hai:', ':hai::iiiii::iiiii:', 'suppers', 'hewoooooooooooooo', 'heyo', '>w< hihi']
mraow = ['mraowwww', 'meeeoww', 'nyaaaa~', 'UwU', 'mrrrp mraow meowww', 'miumiumiumewowww', 'mrowwwww', 'mryaowww', 'mrpppp', '>w<', '^._.^', 'mlem']
@client.event
async def on_ready():
	print(f'hi oomfie is now up and running')
@client.event
async def on_message(message):
	global cat
	guild = message.author.guild
	terrarian = guild.get_role(1526562302340497469)
	gooner = guild.get_role(1527189062035705937)
	if message.author == client.user:
		return
	if message.content == "test":
		await message.channel.send("reply~")
	if "[nsfw]" in message.content.lower():
		await message.author.add_roles(gooner)	
	if message.content == ":3":
		cat += 1
		if cat >= 3:
			cat = 0
			await message.channel.send(":3")
	else:
		cat = 0
	if message.reference and message.reference.cached_message:
		ogmsg = message.reference.cached_message
		if (ogmsg.author == client.user) and re.search(r'\b((h+[aei]+(l+o+y+)*)|(w+s+p+)|(s+u+p+)|(y+o+))\b', message.content):
 			await message.reply(random.choice(hello))
		meow = r'\b((m+[yr]*[ea]+o*w+)|(m+r+p+)|(m+r+[iue]+u+)|n+y+a+)\b'
		if (ogmsg.author == client.user) and re.search(meow, message.content):
			await message.reply(random.choice(mraow))	
		if (ogmsg.author == client.user) and (re.fullmatch("hits you with (my|an?)? .+", message.content) or re.fullmatch("(?! a good .+$)^.+s you", message.content)):
			await message.reply(random.choices(['*dies*', '*cums*'], weights=[0.9, 0.1], k=1)[0])
		if (ogmsg.author == client.user) and message.content == "marco":
			await message.reply("polo")
		if (ogmsg.author == client.user) and re.fullmatch("(calls you a )?good .+", message.content):
			await message.reply(random.choice(['nyaaaa~', 'UwU', 'mrrrp mraow meowww', 'miumiumiumewowww', 'cums', 'ejects', 'ok bro', 'goons on you', 'cums on you']))
		if (ogmsg.author == client.user) and re.fullmatch("(cums [io]n you|goons [io]n you)", message.content):
			await message.reply(random.choices(['swallows', 'yummers', ':drooling_face:', 'licks', 'takes it in']))
	
	await message.author.add_roles(terrarian)	
async def on_member_join(member):
	id = member.id	
client.run(os.getenv("OOMFIE"))

