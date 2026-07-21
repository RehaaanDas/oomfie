import discord; import os; import re; import random
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents); cat = 0
hello = ['haiii', 'hi hello nya~', 'mraow', 'hihihihiii hewoo', 'harro', 'ha-iiiiii', ':hai:', ':hai::iiiii::iiiii:', 'suppers']
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
 			print("console log"); await message.reply(random.choice(hello))
	await message.author.add_roles(terrarian)	
async def on_member_join(member):
	id = member.id	
client.run(os.getenv("OOMFIE"))
