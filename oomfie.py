import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

cat = 0

@client.event
async def on_ready():
	print(f'oomfie is now up and running')

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

	await message.author.add_roles(terrarian)	

async def on_member_join(member):
	id = member.id	
client.run('MTUyNjkzMjIxMDE1Njk2NjAyOA.GzdR2K.2yRhtoGoDckB62pHmc80905GAygKuUoluht5WY')
