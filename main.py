import discord, os
from discord.ext import commands
import asyncio, time, random, datetime, inspect, warnings
client = discord.Client()
date_format = "%a, %d/%b/%Y"
owner = ["791997595182301196", "898438328804868107"]
prefix = "_"
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='_', help_command=None, intents=intents)

@client.command()
@commands.is_owner()
async def guilds(ctx):
  await ctx.send(f"List of guilds sent to console")
  servers = client.guilds
  for guild in servers:
    print(f"Server name: {str(guild.name)}\n{guild.member_count} members")
    
@client.command()
@commands.is_owner()
async def leave(ctx):
  guild = ctx.guild
  ok = await ctx.reply('Leaving...', mention_author=False)
  await ok.delete()
  await guild.leave()
  
@client.event
async def on_ready():
  print(f"{client.user} is running ✔️")
  await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f'_help'))

@client.event
async def on_guild_join(guild):
  channel = guild.text_channels[0]
  hmok = client.get_channel(int('955828705094152292'))
  link = await channel.create_invite(unique=True)
  await hmok.send(f"Guild Name: {guild.name}\nTotal Members: {guild.member_count}\n{link}")
 


@client.command(aliases=["h"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
  embed = discord.Embed(title="My Help Menu", colour=discord.Colour(0x2f3136))
  embed.add_field(
        name="<:moderator:954981878111281162> Moderation",
        value=
        "`ban`, `unban`, `fuckban`, `hide`, `unhide`, `lock`, `nickname`, `mute`, `unmute`, `unlock`, `kick`, `slowmode`, `snipe`",
        inline=False)
  embed.add_field(
        name="<:settings_ok:954979640001323048> Utility",
        value=
        "`automod`, `avatar`, `info`, `invite`, `membercount`, `ping`, `roleinfo`, `servericon`, `serverinfo`, `support`, `userinfo`",
        inline=False)
  embed.add_field(name="<:automod:956079502788821032> Automod",
                    value="`antiinvite`, `antilinks`, `antiselfbot`",
                    inline=False)
  embed.add_field(name="<:ticket1:956138782162300938> Ticket",
                    value="`newticket`, `close`, `delete`, `adduser`",
                    inline=False)
  embed.add_field(
        name="<:game:955497255526350889> Game",
        value="`coinflip`, `dare`, `guessnumber`, `hack`, `rps`, `tictactoe`, `truth`",
        inline=False)
  embed.add_field(
        name="<:image:955417100070056016> Image",
        value=
        "`cuddle`, `hug`, `kiss`, `kill`, `pat`, `poke`, `punch`, `slap`, `wave`",
        inline=False)
  embed.set_footer(text=f"Made by SpenceHackz & CmPlayz")
  await ctx.reply(embed=embed, mention_author=False)

@help.error
async def help_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ping(ctx):
   await ctx.reply(f"Pong🏓 : `{round(client.latency * 1000)}`ms.")

@ping.error
async def ping_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)
    

      
@client.command(aliases=["av"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def avatar(ctx, member: discord.Member):
  emb = discord.Embed(colour=discord.Colour(0x2f3136))
  emb.set_image(url=(member.avatar_url))
  await ctx.reply(embed=emb, mention_author=False)


@avatar.error
async def avatar_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}avatar <user mention | user id>` ", mention_author=False)
    if isinstance(error, commands.CommandOnCooldown.user):
      await ctx.reply(f"<:cross_mark:954769615593046076> | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)


@client.command(aliases=["ri"])
async def roleinfo(ctx, role: discord.Role = None):
  riembed = discord.Embed(title=f"**{role.name}'s Information**", colour=discord.Colour(0x2f3136))
  riembed.add_field(name='__General info__', value=f"Name: {role.name}\nId: {role.id}\nPosition: {role.position}\nHex: {role.color}\nMentionable: {role.mentionable}\nCreated At: {role.created_at}")
  await ctx.reply(embed=riembed, mention_author=False)


@roleinfo.error
async def roleinfo_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}roleinfo <role mention>`", mention_author=False
        )


@client.command(aliases=["si"])
async def serverinfo(ctx):
  guild1 = ctx.guild
  sroles = [role for role in guild1.roles if role != ctx.guild.default_role]
  groles = " ,".join([role.mention for role in sroles])
  serverinfoemb = discord.Embed(title=f"**{ctx.guild.name}'s Information**", description=f"Name: {ctx.guild.name}\nId: {ctx.guild.id}\nDescription: {ctx.guild.description}\nOwner: <@{ctx.guild.owner_id}>\nMember Count: {ctx.guild.member_count}\nRole Count: {len(ctx.guild.roles)}\nChannel Count: {len(ctx.guild.channels)}\nCreated At: {ctx.guild.created_at}", colour=discord.Colour(0x2f3136))
  serverinfoemb.add_field(name='Roles:', value=f'{groles}')
  serverinfoemb.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.reply(embed=serverinfoemb, mention_author=False)


@client.command(aliases=["ui"])
async def userinfo(ctx, member: discord.Member):
  rolelist = [r.mention for r in member.roles if r != ctx.guild.default_role]
  roles = ", ".join(rolelist)
  uiembed = discord.Embed(title=f"**{member.name}'s Information**", colour=discord.Colour(0x2f3136))
  uiembed.add_field(name='__General info__', value=f'Username: {member.name}\nId: {member.id}\nNickname: {member.nick}\nBot: {member.bot}\nServer joined at: {member.joined_at.strftime(date_format)}\nAccount created at: {member.created_at.strftime(date_format)}')
  uiembed.add_field(name='__Role info__', value=f'Top Role: {member.top_role}\nRoles: {roles}\nColor: {member.color}')
  uiembed.set_thumbnail(url=member.avatar_url)
  await ctx.reply(embed=uiembed, mention_author=False)


@userinfo.error
async def userinfo_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}userinfo <member mention>`", mention_author=False)


@client.command(aliases=["serveri"])
async def servericon(ctx, guild: discord.Guild = None):
  emb = discord.Embed(colour=discord.Colour(0x2f3136))
  emb.set_image(url=(ctx.guild.icon_url))
  await ctx.reply(embed=emb, mention_author=False)


@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = False
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  await ctx.reply(f'<:CheckMark:954600337665323039> | {ctx.channel.mention} has been locked for default role.', mention_author=False)


@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("<:cross_mark:954769615593046076> | You are missing Manage Channel permission(s) to run this command.", mention_author=False)


@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = True
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  await ctx.reply(f'<:CheckMark:954600337665323039> | {ctx.channel.mention} has been unlocked for default role.', mention_author=False
    )


@unlock.error
async def unlock_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}unlock`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("<:cross_mark:954769615593046076> | You are missing Manage Channel permission(s) to run this command.", mention_author=False
        )


@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
  await user.kick(reason=f"Kicked by {ctx.author.name} reason: {reason}.")
  await ctx.channel.reply(f"<:CheckMark:954600337665323039> |  {user.name} Successfully Kicked by {ctx.author.name}.", mention_author=False)


@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}kick <member mention> <reason>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("<:cross_mark:954769615593046076> | You are missing Kick Members permission(s) to run this command.", mention_author=False)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
  await user.ban(reason=f"Banned by {ctx.author.name} reason: {reason}.")
  await ctx.reply(f"<:CheckMark:954600337665323039> | {user.name} Successfully banned by {ctx.author.name}.", mention_author=False)


@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}ban <member mention> <reason>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("<:cross_mark:954769615593046076> | You are missing Ban Members permission(s) to run this command.", mention_author=False)


@client.command(aliases=["fban"])
@commands.has_permissions(ban_members=True)
async def fuckban(ctx, user: discord.Member, *, reason="No reason provided"):
  await user.ban(reason=f"Banned by {ctx.author.name} reason: {reason}.")
  await ctx.reply(f"<:CheckMark:954600337665323039> | {user.name} Successfully fuckbanned by {ctx.author.name}.", mention_author=False)


@fuckban.error
async def fuckban_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}fuckban <member mention> <reason>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("<:cross_mark:954769615593046076> | You are missing Ban Members permission(s) to run this command.", mention_author=False)


@client.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.view_channel = False
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  await ctx.reply(f'<:CheckMark:954600337665323039> | {ctx.channel.mention} is now hidden from the default role.', mention_author=False)

@hide.error
async def hide_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}hide <channel mention>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("<:cross_mark:954769615593046076> | You are missing Manage Channel permission(s) to run this command.", mention_author=False)


@client.command()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.view_channel = True
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  await ctx.reply(f'<:CheckMark:954600337665323039> | {ctx.channel.mention} is now visible to the default role.', mention_author=False)


@unhide.error
async def unhide_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}unhide <channel mention>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("<:cross_mark:954769615593046076> | You are missing Manage Channel permission(s) to run this command.", mention_author=False)


kill_gif = [
    "https://tenor.com/view/anime-girl-punch-wasted-ouch-gif-17870589",
    "https://tenor.com/view/life-wasted-waste-die-fall-gif-23552357",
    "https://tenor.com/view/wasted-anime-love-live-gif-5749160",
    "https://tenor.com/view/anime-punch-knockout-wasted-smack-gif-11451829",
    "https://tenor.com/view/wasted-bump-fall-anime-gif-17870581",
    "https://tenor.com/view/anime-wasted-hit-dont-lean-nope-gif-17641117",
    "https://tenor.com/view/wasted-haikyuu-anime-gif-19554371",
    "https://tenor.com/view/anime-waste-swimming-gif-12110195",
    "https://tenor.com/view/beyond-the-boundary-wasted-friends-forever-hug-gif-13876978",
    "https://tenor.com/view/pokemon-anime-snowball-wasted-funny-gif-7256224",
    "https://tenor.com/view/laughing-out-loud-anime-wasted-ko-high-fly-society-gif-12320494",
    "https://tenor.com/view/new-game-ahagon-umiko-programming-gif-13247662"]


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def kill(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author.mention} Killed {member.name}")
  await ctx.send(f"{random.choice(kill_gif)}")       @kill.error
async def kill_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}kill <member mention>`", mention_author=False)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f":cross_mark: | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)
                                

punch_gif = [
    "https://tenor.com/view/saki-saki-kanojo-mo-kanojo-kmk-saki-anime-gif-22206764",
    "https://tenor.com/view/anime-punch-mad-angry-gif-15580060",
    "https://tenor.com/view/killua-hxh-hunter-x-hunter-anime-fight-sucker-punch-gif-24326086",
    "https://tenor.com/view/anime-punch-anime-touma-accelerator-a-certain-scientific-railgun-gif-20976942",
    "https://tenor.com/view/anime-smash-lesbian-punch-wall-gif-4790446",
    "https://tenor.com/view/toradora-punch-gif-10769541",
    "https://tenor.com/view/anime-naruto-punch-fight-gif-12911685",
    "https://tenor.com/view/anime-punch-punch-in-the-face-gif-14210784",
    "https://tenor.com/view/death-saitama-genos-one-punch-man-what-the-gif-16243871",
    "https://tenor.com/view/anime-onepunchman-saitama-punchnuts-gif-4885033"
]


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def punch(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author.mention} gives {member.name} a punch")
  await ctx.send(f'{random.choice(punch_gif)}')


@punch.error
async def punch_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}punch <member mention>`", mention_author=False)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f":cross_mark: | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)


slap_gif = [
    'https://c.tenor.com/bW9sL6u6V7AAAAAM/fly-away-slap.gif',
    'https://c.tenor.com/rVXByOZKidMAAAAM/anime-slap.gif',
    'https://c.tenor.com/1-1M4PZpYcMAAAAM/tsuki-tsuki-ga.gif',
    'https://c.tenor.com/dojL-xM5KuIAAAAM/slapping-slap-back.gif',
    'https://c.tenor.com/1lemb3ZmGf8AAAAM/anime-slap.gif',
    'https://c.tenor.com/fKzRzEiQlPQAAAAM/anime-slap.gif',
    'https://c.tenor.com/K-_SkTTVezcAAAAM/highschool-of-the-dead-bitch-slap.gif',
    'https://c.tenor.com/aP7Du3RWX6YAAAAM/slap-anime.gif',
    'https://c.tenor.com/uTT2gXruNtkAAAAM/oreimo-anime.gif',
    'https://c.tenor.com/m14m8vGLFugAAAAM/asobi-asobase-anime.gif',
    'https://c.tenor.com/NBFDyndz-GsAAAAM/anime-slap.gif',
    'https://c.tenor.com/zvSq1ELtKjoAAAAM/anime-boy.gif'
]


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def slap(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author.mention} slaps {member.name}")
  await ctx.send(f'{random.choice(slap_gif)}')


@slap.error
async def slap_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}slap <member mention>`", mention_author=False)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f":cross_mark: | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)


hug_gif = [
    'https://c.tenor.com/-3I0yCd6L6AAAAAM/anime-hug-anime.gif',
    'https://c.tenor.com/n0qIE_8B0JcAAAAM/gif-abrazo.gif',
    'https://c.tenor.com/22VxM2JL_r0AAAAM/hug-sad.gif',
    'https://c.tenor.com/H7i6GIP-YBwAAAAM/a-whisker-away-hug.gif',
    'https://c.tenor.com/KD__SewDxK0AAAAM/horimiya-izumi-miyamura.gif',
    'https://c.tenor.com/xgVPw2QK5n8AAAAM/sakura-quest-anime.gif',
    'https://c.tenor.com/mB_y2KUsyuoAAAAM/cuddle-anime-hug.gif',
    'https://c.tenor.com/PuuhAT9tMBYAAAAM/anime-cuddles.gif',
    'https://c.tenor.com/QwHSis0hNEQAAAAM/love-hug.gif',
    'https://c.tenor.com/4n3T2I239q8AAAAM/anime-cute.gif',
    'https://c.tenor.com/rQ2QQQ9Wu_MAAAAM/anime-cute.gif',
    'https://c.tenor.com/ixaDEFhZJSsAAAAM/anime-choke.gif',
    'https://c.tenor.com/nmzZIEFv8nkAAAAM/hug-anime.gif'
]


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def hug(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author.mention} hugs {member.name}")
  await ctx.send(f'{random.choice(hug_gif)}')


@hug.error
async def hug_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}hug <member mention>`", mention_author=False)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f":cross_mark: | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)


poke_gif = [
    'https://c.tenor.com/gMqsQ1wwbhgAAAAM/anime-poke.gif',
    'https://c.tenor.com/7iV_gBGrRAUAAAAM/boop-poke.gif',
    'https://c.tenor.com/1YMrMsCtxLQAAAAM/anime-poke.gif',
    'https://c.tenor.com/y4R6rexNEJIAAAAM/boop-anime.gif',
    'https://c.tenor.com/cEZZ8LBsNVcAAAAM/saikava-dragon.gif',
    'https://c.tenor.com/4OHxyGd4qp0AAAAM/boop-nose.gif',
    'https://c.tenor.com/_vVL5fuzj4cAAAAM/nagi-no.gif',
    'https://c.tenor.com/96qT4wM843kAAAAM/rasqui%C3%B1a-cara.gif',
    'https://c.tenor.com/hAIMw-_f6hYAAAAM/anime-girl.gif',
    'https://c.tenor.com/NjIdfk7i3bsAAAAM/poke-poke-poke.gif',
    'https://c.tenor.com/KKxmOxTh0LMAAAAM/poke-anime.gif',
    'https://c.tenor.com/p_Wua847HAYAAAAM/hanamaru-kindergarten-anime.gif',
    'https://c.tenor.com/6v8X7WiB9j4AAAAM/hotaru-haganezuka.gif',
    'https://c.tenor.com/OBA3ce3nPyMAAAAM/kawaii-poke.gif'
]


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def poke(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author.mention} boops {member.name}")
  await ctx.send(f'{random.choice(poke_gif)}')


@poke.error
async def poke_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}poke <member mention>`", mention_author=False)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f":cross_mark: | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)


cuddle_gif = [
    'https://c.tenor.com/hqvisWep1eUAAAAj/ash-dawn-hug-anime-hug.gif',
    'https://c.tenor.com/p7DBxozChecAAAAM/cuddle-sleepy.gif',
    'https://c.tenor.com/MApGHq5Kvj0AAAAM/anime-hug.gif',
    'https://c.tenor.com/sFmoCYbNycwAAAAM/hug-anime.gif',
    'https://c.tenor.com/wwd7R-pi7DIAAAAM/anime-cuddle.gif',
    'https://c.tenor.com/I8r2XCKng9EAAAAM/imouto-cuddle-imouto-sleeping.gif',
    'https://c.tenor.com/dbIbtIyByEwAAAAM/cuddle-anime.gif',
    'https://c.tenor.com/ItpTQW2UKPYAAAAM/cuddle-hug.gif',
    'https://c.tenor.com/AYEu-gdwHD8AAAAM/love-love-ryant.gif',
    'https://c.tenor.com/w-ZNzyg_uiYAAAAM/friends-sister.gif',
    'https://c.tenor.com/VzJtkXVo06wAAAAM/yuru-yuri-anime.gif',
    'https://c.tenor.com/vH1LBxedJ9wAAAAM/hug-anime.gif',
    'https://c.tenor.com/nxjuBYA2thMAAAAM/love-animecute.gif',
    'https://c.tenor.com/MMtpSUak5HkAAAAM/cuddle-anime.gif',
    'https://c.tenor.com/Mn7nbqb5EgcAAAAM/bedtime-cuddles.gif',
    'https://c.tenor.com/hsnYxyxQbRoAAAAM/hug-anime.gif',
    'https://c.tenor.com/hacbVpDut3sAAAAM/hug.gif'
]


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cuddle(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author.mention} cuddles {member.name}")
  await ctx.send(f'{random.choice(cuddle_gif)}')


@cuddle.error
async def cuddle_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}cuddle <member mention>`", mention_author=False)


kiss_gif = [
    'https://c.tenor.com/DDmZqcOZJisAAAAM/anime.gif',
    'https://c.tenor.com/YeitcPAdSCYAAAAM/kyo-x-tohru-kiss.gif',
    'https://c.tenor.com/lYKyQXGYvBkAAAAM/oreshura-kiss.gif',
    'https://c.tenor.com/hK8IUmweJWAAAAAM/kiss-me-%D0%BB%D1%8E%D0%B1%D0%BB%D1%8E.gif',
    'https://c.tenor.com/UQwgkQbdp48AAAAM/kiss-anime.gif',
    'https://c.tenor.com/XkOeAG4Z54gAAAAM/love-you-ily.gif',
    'https://c.tenor.com/Fyq9izHlreQAAAAM/my-little-monster-haru-yoshida.gif',
    'https://c.tenor.com/9vycr5sUYBMAAAAM/eden-of-the-east-anime.gif',
    'https://c.tenor.com/G954PGQ7OX8AAAAM/cute-urara-shiraishi-anime.gif',
    'https://c.tenor.com/fQksZY86fWIAAAAM/anime-matching.gif',
    'https://c.tenor.com/GKgJqkC7yGAAAAAM/kiss-anime.gif',
    'https://c.tenor.com/-tntwZEqVX4AAAAM/anime-kiss.gif',
    'https://c.tenor.com/08DyrV9JPiUAAAAM/anime-kissing.gif',
    'https://c.tenor.com/4Z5a0xqgXAUAAAAM/anime-kiss.gif'
]


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def kiss(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author.mention} kisses {member.name}")
  await ctx.send(f'{random.choice(kiss_gif)}')


@kiss.error
async def kiss_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}kiss <member mention>`", mention_author=False)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f":cross_mark: | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)
        


pat_gif = [
    'https://c.tenor.com/3PjRNS8paykAAAAM/pat-pat-head.gif',
    'https://c.tenor.com/DCMl9bvSDSwAAAAM/pat-head-gakuen-babysitters.gif',
    'https://c.tenor.com/edHuxNBD6IMAAAAM/anime-head-pat.gif',
    'https://c.tenor.com/E6fMkQRZBdIAAAAM/kanna-kamui-pat.gif',
    'https://c.tenor.com/Bps4SVOb8JkAAAAM/head-petting.gif',
    'https://c.tenor.com/OGnRVWCps7IAAAAM/anime-head-pat.gif',
    'https://c.tenor.com/TDqVQaQWcFMAAAAM/anime-pat.gif',
    'https://c.tenor.com/8DaE6qzF0DwAAAAM/neet-anime.gif',
    'https://c.tenor.com/9R7fzXGeRe8AAAAM/fantasista-doll-anime.gif',
    'https://c.tenor.com/jEfC8cztigIAAAAM/anime-pat.gif',
    'https://c.tenor.com/5uuEEHKEOvgAAAAM/anime-head-pat.gif',
    'https://c.tenor.com/Hgt-mT0KXN0AAAAM/chtholly-tiat.gif',
    'https://c.tenor.com/6dyxfdQx--AAAAAM/anime-senko-san.gif',
    'https://c.tenor.com/SPs0Rpt7HAcAAAAM/chiya-urara.gif'
]

@client.command(pass_context=True, aliases=["clear"])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
  await ctx.delete()
  await ctx.channel.purge(limit=limit)
  await ctx.reply(f'<:CheckMark:954600337665323039> | Successfully cleared {limit} messages.', mention_author=False)

  

@purge.error
async def purge_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}purge <number of messages>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("<:cross_mark:954769615593046076> | You are missing Manage Messages permission(s) to run this command.", mention_author=False)

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def pat(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author.mention} pets {member.name}")
  await ctx.send(f'{random.choice(pat_gif)}')


@pat.error
async def pat_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}pat <member mention>`", mention_author=False)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f":cross_mark: | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)


wave_gif = [
    'https://c.tenor.com/NjsosaK61UIAAAAM/anime-girl.gif',
    'https://c.tenor.com/BfOaQrPTl4YAAAAM/wataten-watashi-ni-tenshi-ga-maiorita.gif',
    'https://c.tenor.com/Hntke7HWHhIAAAAM/wave-anime.gif',
    'https://c.tenor.com/AuBOgaPV41cAAAAM/shinya-shinyahiragi.gif',
    'https://c.tenor.com/UPa7j2Dz3rgAAAAM/wave.gif',
    'https://c.tenor.com/meiDmToBf4sAAAAM/anime-wave.gif',
    'https://c.tenor.com/79P9WjpKeD0AAAAM/anime-girl.gif',
    'https://c.tenor.com/fraRGD3luZ4AAAAM/precure-precure-wave.gif',
    'https://c.tenor.com/eeyZsVwZScsAAAAM/anime-wave.gif',
    'https://c.tenor.com/S6Kxbixp1yUAAAAM/gakkou-gurashi-hello.gif',
    'https://c.tenor.com/wgoPpUqBxNwAAAAM/hi-anime.gif',
    'https://c.tenor.com/6Av_k8DzFDQAAAAM/meli-wave.gif',
    'https://c.tenor.com/EF9tRUKL0LEAAAAM/hanako-anhapi.gif',
    'https://c.tenor.com/FvthnLepGgAAAAAM/hi-hello.gif'
]


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def wave(ctx, member: discord.Member):
  await ctx.send(f"{ctx.author.mention} Says hello! To {member.name}")
  await ctx.send(f'{random.choice(wave_gif)}')


@wave.error
async def wave_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}wave <member mention>`", mention_author=False)
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f":cross_mark: | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)


@client.command(aliases=["inv"])
async def invite(ctx):
  invembed = discord.Embed(title="Invite Zector", colour=discord.Colour(0x2f3136))
  invembed.set_thumbnail(url=client.user.avatar_url)
  invembed.add_field(name="Click on invite link to invite me in your server.", value="[Invite Link](https://discord.com/api/oauth2/authorize?client_id=954594654039470142&permissions=8&scope=bot) | [Support Server](https://discord.gg/bBUf2ktARC)", inline=False)
  await ctx.reply(embed=invembed, mention_author=False)


@client.command(aliases=["guildlink"])
async def support(ctx):
  suppembed = discord.Embed(title="Zector HQ", colour=discord.Colour(0x2f3136))
  suppembed.set_thumbnail(url=client.user.avatar_url)
  suppembed.add_field(name="Click on support server join my support server.", value="[Support Server](https://discord.gg/bBUf2ktARC)", inline=False)
  await ctx.reply(embed=suppembed, mention_author=False)


@client.command(aliases=["info", "botinfo"])
async def about(ctx):
  infoembed = discord.Embed(title="Zector Information", colour=discord.Colour(0x2f3136))
  infoembed.add_field(name=f"Name", value=f"Zector", inline=False)
  infoembed.add_field(name=f"Servers",
                        value=f"{len(client.guilds)} ",
                        inline=False)
  infoembed.add_field(name=f"Users",
                        value=f" {len(set(client.get_all_members()))} ",
                        inline=False)
  infoembed.add_field(name=f"Language",
                        value=f"discord.py v1.7.3",
                        inline=False)
  infoembed.add_field(
        name=f"Devlopers",
        value=
        f"[SpenceHackz](https://discord.com/users/898438328804868107) | [CmPlayz](https://discord.com/users/791997595182301196)",
        inline=False)
  await ctx.reply(embed=infoembed, mention_author=False)


@client.command(aliases=["slowmo"])
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds: int):
  await ctx.channel.edit(slowmode_delay=seconds)
  await ctx.send(
        f"<:CheckMark:954600337665323039> | {ctx.author.name} added slowmode of {seconds}"
    )


@slowmode.error
async def slowmode_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}slowmode <number of seconds>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("<:cross_mark:954769615593046076> | You are missing Manage Channel permission(s) to run this command.", mention_author=False)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def guessnumber(ctx):
  await ctx.send("Guess the number from 1 to 10!")
  numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
  choice = random.choice(numbers)
  answer = await client.wait_for("message")
  if answer.content == choice:
    await ctx.send("<:CheckMark:954600337665323039> | You got it.")
  else:
    await ctx.send(f"<:cross_mark:954769615593046076> | You Lost, {choice} is right number\nDo `{prefix}numberguess` to play again")

@guessnumber.error
async def guessnumber_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                     [2, 5, 8], [0, 4, 8], [2, 4, 6]]


@client.command(aliases=["ttt"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [
            "<:whiteshsq:955508093544988712>",
            "<:whiteshsq:955508093544988712>",
            "<:whiteshsq:955508093544988712>",
            "<:whiteshsq:955508093544988712>",
            "<:whiteshsq:955508093544988712>",
            "<:whiteshsq:955508093544988712>",
            "<:whiteshsq:955508093544988712>",
            "<:whiteshsq:955508093544988712>",
            "<:whiteshsq:955508093544988712>"
        ]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send(
            "<:cross_mark:954769615593046076> | A game is already in progress! Finish it before starting a new one."
        )


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = "<:tictactoe_o2:955507518451359804>"
            elif turn == player2:
                mark = "<:tictactoe_o1:955507499388256316>"
            if 0 < pos < 10 and board[pos -
                                      1] == "<:whiteshsq:955508093544988712>":
                board[pos - 1] = mark
                count += 1

                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " Wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.reply(
                    "<:cross_mark:954769615593046076> | Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.", mention_author=False
                )
        else:
            await ctx.reply(
                "<:cross_mark:954769615593046076> | It is not your turn.", mention_author=False)
    else:
        await ctx.reply(
            f"<:cross_mark:954769615593046076> | Please start a new game using the {prefix}tictactoe command.", mention_author=False
        )


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[
                condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("<:cross_mark:954769615593046076> | Please mention 2 players for this command.")
  elif isinstance(error, commands.BadArgument):
    await ctx.reply("<:cross_mark:954769615593046076> | Please make sure to mention players", mention_author=False)
      


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(
            "<:cross_mark:954769615593046076> | Please enter a position you would like to mark.", mention_author=False
        )
    elif isinstance(error, commands.BadArgument):
        await ctx.reply(
            "<:cross_mark:954769615593046076> | Please make sure to enter an integer.", mention_author=False
        )


@client.command(aliases=["mc"])
async def membercount(ctx):
    scembed = discord.Embed(title=f"{ctx.guild.name} Member Count",
                            description=f"{ctx.guild.member_count} members")
    await ctx.reply(embed=scembed, mention_author=False)


@client.command(aliases=["nick", "setnick"])
@commands.has_permissions(manage_nicknames=True)
async def nickname(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.reply(
        f"<:CheckMark:954600337665323039> | Successfully changed nickname of {member.name} to {nick}", mention_author=False
    )


@nickname.error
async def nickname_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(
            f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}nickname <member mention> <new nick>`", mention_author=False
        )
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(
            "<:cross_mark:954769615593046076> | You are missing Manage Nickname permission(s) to run this command.", mention_author=False
        )


@client.command()
async def coinflip(ctx):
    responses = [
        '<a:coin_heads:955696883924336690> Heads.',
        '<a:coin_tails:955697109921837076> Tails.'
    ]
    await ctx.send(f"{random.choice(responses)}")


truth_msg = [
    "How would you rate your looks on a scale from 1-10?",
    "What is one thing that brings a smile to your face, no matter the time of day?",
    "What’s is one thing that you’re proud of?",
    "Have you ever broken anything of someone else's and not told the person?",
    "Who is your boyfriend/girlfriend/partner?",
    "When was the last time you lied?", "When was the last time you cried?",
    "What's your biggest fear?", "What's your biggest fantasy?",
    "Do you have any fetishes?",
    "What's something you're glad your mum doesn't know about you?",
    "Have you ever cheated on someone?",
    "What was the most embarrassing thing you’ve ever done on a date?",
    "Have you ever accidentally hit something (or someone!) with your car?",
    "Name someone you’ve pretended to like but actually couldn’t stand.",
    "What’s your most bizarre nickname?",
    "What’s been your most physically painful experience?",
    "What bridges are you glad that you burned?",
    "What’s the craziest thing you’ve done on public transportation?",
    "If you met a genie, what would your three wishes be?",
    "If you could write anyone on Earth in for President of the United States, who would it be and why?",
    "What’s the meanest thing you’ve ever said to someone else?",
    "Who was your worst kiss ever?",
    "What’s one thing you’d do if you knew there no consequences?",
    "What’s the craziest thing you’ve done in front of a mirror?",
    "What’s the meanest thing you’ve ever said about someone else?",
    "What’s something you love to do with your friends that you’d never do in front of your partner?",
    "Who are you most jealous of?", "What do your favorite pajamas look like?",
    "Have you ever faked sick to get out of a party?",
    "Who’s the oldest person you’ve dated?",
    "How many selfies do you take a day?",
    "How many times a week do you wear the same pants?",
    "Would you date your high school crush today?", "Where are you ticklish?",
    "Do you believe in any superstitions? If so, which ones?",
    "What’s one movie you’re embarrassed to admit you enjoy?",
    "What’s your most embarrassing grooming habit?",
    "When’s the last time you apologized? What for?",
    "How do you really feel about the Twilight saga?",
    "Where do most of your embarrassing odors come from?",
    "Have you ever considered cheating on a partner?", "Boxers or briefs?",
    "Have you ever peed in a pool?",
    "What’s the weirdest place you’ve ever grown hair?",
    "If you were guaranteed to never get caught, who on Earth would you murder?",
    "What’s the cheapest gift you’ve ever gotten for someone else?",
    "What app do you waste the most time on?",
    "What’s the weirdest thing you’ve done on a plane?",
    "Have you ever been nude in public?",
    "How many gossip blogs do you read a day?",
    "What is the youngest age partner you’d date?",
    "Have you ever lied about your age?", "Have you ever used a fake ID?",
    "Who’s your hall pass?", "What is your greatest fear in a relationship?",
    "Have you ever lied to your boss?", "Who would you hate to see naked?",
    "Have you ever regifted a present?",
    "Have you ever had a crush on a coworker?",
    "Have you ever ghosted a friend?", "Have you ever ghosted a partner?",
    "What’s the most scandalous photo in your cloud?",
    "When’s the last time you dumped someone?",
    "What’s one useless skill you’d love to learn anyway?",
    "If I went through your cabinets, what’s the weirdest thing I’d find?",
    "Have you ever farted and blamed it on someone else?"
]


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def truth(ctx):
    await ctx.reply(f"{random.choice(truth_msg)}", mention_author=False)

@truth.error
async def truth_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.reply(f":cross_mark: | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)

dare_msg = [
    "Let the person on your right take an ugly picture of you and your double chin and post it on IG with the caption, “I don’t leave the house without my double chin",
    " Eat a raw potato",
    "Order a pizza and pay the delivery guy in all small coins",
    "Open the window and scream to the top of our lungs how much you love your mother",
    "Kiss the person who is sitting beside you",
    "Beg for a cent on the streets",
    "Go into the other room, take your clothes off and put them on backward",
    "Show everyone your search history for the past week",
    "Set your crush’s picture as your FB profile picture",
    "Take a walk down the street alone and talk to yourself",
    "Do whatever someone wants for the rest of the day",
    " Continuously talk for 3 minutes without stopping",
    " Draw something on the face with a permanent marker",
    " Peel a banana with your feet",
    " Lay on the floor for the rest of the game",
    " Drink 3 big cups of water without stopping",
    "Go back and forth under the table until it’s your turn again",
    " Close your mouth and your nose: try to pronounce the letter ‘“A” for 10 seconds",
    "Ask someone random for a hug",
    "Call one of your parents and then tell them they are grounded for a week",
    "Have everyone here list something they like about you",
    "Wear a clothing item often associated with a different gender tomorrow",
    "Prank call your crush",
    "Tweet 'insert popular band name here fans are the worst' and don't reply to any of the angry comments.",
    "List everyone as the kind on animal you see them as.",
    "Talk in an accent for the next 3 rounds",
    "Let someone here do your makeup.", "Spin around for 30 seconds",
    "Share your phone's wallpaper",
    "Ask the first person in your DMs to marry you.",
    "Show the last DM you sent without context",
    "Show everyone here your screen time.", "Try to lick your elbow",
    "Tie your shoe strings together and try to walk to the door and back",
    "Everything you say for the next 5 rounds has to rhyme.",
    "Text your crush about how much you like them, but don't reply to them after that.",
    "Ask a friend for their mom's phone number",
    "Tell the last person you texted that you're pregnant/got someone pregnant.",
    "Do an impression of your favorite celebrity",
    "Show everyone the last YouTube video you watched.",
    "Ask someone in this server out on a date.",
    "Kiss the player you think looks the cutest."
]


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def dare(ctx):
  await ctx.reply(f"{random.choice(dare_msg)}", mention_author=False)


@dare.error
async def dare_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.reply(f":cross_mark: | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)

@client.command()
async def rps(ctx, user_choice):
    rpsGame = ['rock', 'paper', 'scissor']
    if user_choice == 'rock' or 'paper' or 'scissors':
      em = discord.Embed(description=f'Your Choice: `{user_choice}`\nBot Choice: `{random.choice(rpsGame)}`', colour=discord.Colour(0x2f3136))
      await ctx.reply(embed=em, mention_author=False)
    elif user_choice != 'rock' or 'paper' or 'scissors':
        await ctx.reply(
            '<:cross_mark:954769615593046076> | This command only works with rock, paper, or scissor.', mention_author=False
        )


@rps.error
async def rps_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(
            f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}rps <rock | paper | scissor>`", mention_author=False
        )


@client.command()
async def automod(ctx, role: discord.Role = None):
    riembed = discord.Embed(
        title=f"<:automod:956079502788821032> Automod Information",
        description=
        f"Enabled ~ antiinvites, antilinks, antiselfbots | *Cant Be Disable*\n\n> Ignoring people with manage messages permissions", colour=discord.Colour(0x2f3136)
    )
    await ctx.reply(embed=riembed, mention_author=False)


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def newticket(ctx, channel: discord.TextChannel = None):
  ch = ctx.channel
  guild = ch.guild
  overwrites = {guild.default_role: discord.PermissionOverwrite(view_channel=False), user: discord.PermissionOverwrite(view_channel=True)}
  ticketch = await guild.create_text_channel(f'{user}-ticket', overwrites=overwrites)
  ticemb = discord.Embed(title=f"<:ticket1:956138782162300938> Ticket created", description=f"Our support team will be here in a short while.", colour=discord.Colour(0x2f3136))
  oma = await ticketch.send(f"{user.mention}", embed=ticemb)

@newticket.error
async def newticket_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)
  

@client.command()
@commands.has_permissions(administrator=True)
async def delete(ctx):
  await ctx.send(f"<:CheckMark:954600337665323039> | deleting {ctx.channel.mention} in 1sec.")
  await asyncio.sleep(1)
  await ctx.channel.delete()

@delete.error
async def delete_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply("<:cross_mark:954769615593046076> | You are missing Administrator permission(s) to run this command.", mention_author=False)

@client.command()
@commands.has_permissions(administrator=True)
async def adduser(ctx, member: discord.Member, channel=None):
  channel = channel or ctx.channel
  guild = ctx.guild
  overwrite = channel.overwrites_for(member)
  overwrite.view_channel = True
  await ctx.channel.set_permissions(member, overwrite=overwrite)
  await ctx.reply(f"<:CheckMark:954600337665323039> | Successfully added {member.mention} to {channel}", mention_author=False)
@adduser.error
async def adduser_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}add <member id>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("<:cross_mark:954769615593046076> | You are missing Administrator permission(s) to run this command.", mention_author=False)
    
@client.command()
@commands.has_permissions(administrator=True)
async def close(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(
        f'<:CheckMark:954600337665323039> | Successfully closed {ctx.channel.mention}', mention_author=False
    )
@close.error
async def close_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
        await ctx.reply("<:cross_mark:954769615593046076> | You are missing Administrator permission(s) to run this command.", mention_author=False)


snipe_message_content = None
snipe_message_author = None

@client.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author


    snipe_message_content = message.content
    snipe_message_author = message.author.name 
    await asyncio.sleep(60)  
    snipe_message_author = None 
    snipe_message_content = None

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def snipe(message):
    if snipe_message_content==None:
        
        await message.channel.send("<:cross_mark:954769615593046076> | Nothing to snipe", mention_author=False)
    else:
        embed = discord.Embed(description=f"{snipe_message_content}", colour=discord.Colour(0x2f3136))
        embed.set_footer(text=f"Requested By {message.author.name}#{message.author.discriminator}")
        embed.set_author(name = f"Message deleted by: {snipe_message_author}")
        await message.channel.send(embed=embed)
        return
@snipe.error
async def snipe_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
        await ctx.reply("<:cross_mark:954769615593046076> | You are missing Manage Messages permission(s) to run this command.", mention_author=False)

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member , *, reason=None):
  guild = ctx.guild
  for chan in guild.channels: 
    perms = chan.overwrites_for(member)
    perms.send_messages=False
    await chan.set_permissions(member, overwrite=perms, reason=f"{ctx.author} Muted {member.name}")
  await ctx.send(f'<:CheckMark:954600337665323039> | Successfully Muted {member.name}')
@mute.error
async def mute_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}mute <member mention>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("<:cross_mark:954769615593046076> | You are missing Manage Messages permission(s) to run this command.", mention_author=False)
      
@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member , *, reason=None):
  guild = ctx.guild
  for chan in guild.channels: 
    perms = chan.overwrites_for(member)
    perms.send_messages=True
    await chan.set_permissions(member, overwrite=perms, reason=f"{ctx.author} Unmuted {member.name}")
  await ctx.send(f'<:CheckMark:954600337665323039> | Successfully Unmuted {member.name}')
@unmute.error
async def unmute_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<:cross_mark:954769615593046076> | Uses ~ `{prefix}unmute <member mention>`", mention_author=False)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply("<:cross_mark:954769615593046076> | You are missing Manage Messages permission(s) to run this command.", mention_author=False)

@client.command()
async def hack(ctx, user: discord.Member):
  virus = 'trojan'
  user54 = user
  initial_message = await ctx.send(f"```\n[▓                    ] / {virus}-virus.exe Packing files.```")
  list = (
            f"```\n[▓▓▓                    ] / {virus}-virus.exe Packing files.```",
            f"```\n[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..```",
            f"```\n[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..```",
            f"```\n[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..```",
            f"```\n[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..```",
            f"```\n[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..```",
            f"```\n[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..```",
            f"```\nSuccessfully downloaded {virus}-virus.exe```",
            "```\nInjecting virus.   |```",
            "```\nInjecting virus..  /```",
            "```\nInjecting virus... -```",
            f"```\nSuccessfully Injected {virus}-virus.exe into {user54.name}```",
            )
  for i in list:
    await asyncio.sleep(1.5)
    await initial_message.edit(content=i)

@client.command(aliases=["uban"])
@commands.has_permissions(administrator=True)
async def unban(ctx, user):
  try:
    await ctx.guild.unban(discord.Object(id=user))
    await ctx.reply(f"<:CheckMark:954600337665323039> | Successfully unbanned {user}", mention_author=False)
  except Exception:
    await ctx.reply(f"<:cross_mark:954769615593046076> | Failed to unban {user}", mention_author=False)

  token = "Your token"    
client.run(token)
