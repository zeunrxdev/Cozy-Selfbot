import discord
from discord.ext import commands
from colorama import Fore
import random
import requests
from collections import defaultdict
import os
import aiohttp
import asyncio
import re
import time

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True
bot = commands.Bot(command_prefix='$', intents=intents, self_bot=True)
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
reset = "\033[0m"  
pink = "\033[38;2;255;192;203m"
white = "\033[37m"
blue = "\033[34m"
black = "\033[30m"
light_green = "\033[92m" 
light_yellow = "\033[93m" 
light_magenta = "\033[95m" 
light_cyan = "\033[96m"  
light_red = "\033[91m"  
light_blue = "\033[94m"  
bot.remove_command('help')
autoreply_tasks = {}
status_changing_task = None
autogc_enabled = False
help_message = None
help_author = None
help_expiry = None
status_rotation_active = False
emoji_rotation_active = False
current_status = ""
current_emoji = ""
autoreplies = [
"# P R O P H E T   runs u"
]

www = Fore.WHITE
mkk = Fore.BLUE
b = Fore.BLACK
ggg = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX 
pps = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
qqq = Fore.MAGENTA
lbb = Fore.LIGHTBLUE_EX
mll = Fore.LIGHTBLUE_EX
mjj = Fore.RED
yyy = Fore.YELLOW
autoreact_users = {}
dreact_users = {}
main = f"""
{www}╔════════════════════════════════════════╗
{www}║            xblood Selfbot                ║
{www}╠════════════════════════════════════════╣
{www}║ Made by: {mjj}zenursxmurder.                         {www}║
{www}║ Version: {mjj}1.0                           {www}║
{www}║ recorded: {mjj} 11220009  {www}║
{www}║ Welcome: {mjj}{bot.user}                    {www}║
{www}╚════════════════════════════════════════╝
"""
TOKEN = "MTMzOTI2MDY2Njc3NDgxODg1Mw.GHzn9X.NWmYSCXjO6fowHHVesmskfJjFsslwv_wmr2hA0"
if not TOKEN:
    input("Token not found. Please provide a token.")
    exit()

@bot.event
async def on_ready():
    print(f"""
                                        {www}╔════════════════════════════════════════╗
                                        {www}║            xblood Selfbot              ║
                                        {www}╠════════════════════════════════════════╣
                                        {www}║                                   {www}║
                                        {www}║ Version: {mjj}1.0                 {www}║
                                        {www}║                                   {www}║
                                        {www}║ Welcome: {mjj}{bot.user}          {www}║
                                        {www}╚════════════════════════════════════════╝
""")
pages = [
    f"""```ansi
                        {www} 
                        {www}[1] {red}help         {black}- Shows this menu          {www}
                        {www}[2] {red}cls          {black}- Clears the display UI    {www}
                        {www}[3] {red}autoreact    {black}- React to a user's message{www}
                        {www}[4] {red}autoreactoff {black}- Stop auto-reacting      {www}
                        {www}[5] {red}dreact       {black}- Rotate react on messages{www}
                        {www}[6] {red}dreactoff    {black}- Stop alternating reactions{www}
                        {www}[7] {red}clearmsg     {black}- Clear your messages      {www}
                        {www}[8] {red}countdown    {black}- Start a countdown        {www}
                        {www}[9] {red}countdownoff {black}- Stop the countdown       {www}

    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ```""",
        f"""```ansi
                        {www}                     
                        {www}[10] {red}areply <user> {black}- Auto reply       {www}
                        {www}[11] {red}areplyoff     {black}- Stop auto reply   {www} 
                        {www}[12] {red}mimic <user>  {black}- Start a mimic        {www}
                        {www}[13] {red}rstatus      {black} - Rotate status       {www}
                        {www}[14] {red}stream       {black} - Rotate stream       {www}
                        {www}[15] {red}remoji     {black}   - Rotate emoji status        {www}
                        {www}[16] {red}streamoff     {black}- Stop stream        {www}
                        {www}[17] {red}stopemoji     {black}- Stop emoji rotation          {www}
                        {www}[18] {red}stopstatus    {black}-  Stop status rotation        {www}

    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────

        ```""",
        f"""```ansi
                        {www}     
                        {www}[19] {red}autonick    {black}- Force a nickname on a user{www}
                        {www}[20] {red}avatar      {black}- Get a user's avatar       {www}
                        {www}[21] {red}banner      {black}- Show a user's banner      {www}
                        {www}[22] {red}gcname      {black}- Spam a group name     {www}
                        {www}[23] {red}gcnameend   {black}- Stop spamming a group name     {www}
                        {www}[24] {red}gcfill      {black}- Add tokens to a group      {www}
                        {www}[25] {red}gcleave     {black}- Leave a group with tokens      {www}
                        {www}[26] {red}gcleaveall  {black}- Leave all groups with tokens      {www}

    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────

        ```""",
        f"""```ansi
                        {www}                     
                        {www}[27] {red}antigc             {black}- Group chat spam protection {www}
                        {www}[28] {red}typing <time>      {black}- Trigger typing {www}
                        {www}[29] {red}typingoff          {black}- Stop triggering typing {www}
                        {www}[30] {red}vcjoin stable <id> {black}- Join and stay in one voice channel {www}
                        {www}[31] {red}vcjoin rotate      {black}- Rotate through all available voice channels {www}
                        {www}[32] {red}vcjoin random      {black}- Randomly join voice channels {www}
                        {www}[33] {red}vcjoin list        {black}- List all available voice channels {www}
                        {www}[34] {red}vcjoin leave       {black}- Leave voice channel {www}
                        {www}[35] {red}vcjoin status      {black}- Show current VC status {www}

    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────

        ```""",
        f"""```ansi
                        {www}                  
                        {www}[36] {red}rotateguild               {black}- Rotate guilds        {www}
                        {www}[37] {red}rotateguild stop          {black}- Stop rotating guilds     {www}
                        {www}[38] {red}rotateguild delay         {black}- Stop rotating guilds with tags  {www} 
                        {www}[39] {red}rotateguild status        {black}- Check rotating status    {www}
                        {www}[40] {red}hypesquad <house>         {black}- Change HypeSquad house  {www}
                        {www}[41] {red}hypesquad off             {black}- Remove HypeSquad house  {www}
                        {www}[42] {red}forcepurge toggle <user>  {black}- Force purge user messages    {www}
                        {www}[43] {red}forcepurge off            {black}- Disable force purge user messages    {www}
                        {www}[44] {red}forcepurge list           {black}- List force purge user messages    {www}
                        {www}[45] {red}forcepurge clear          {black}- Clear all force purge user messages    {www}

    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
⠀⠀⠀⠀{magenta}
⣿⠲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                
⠀⣸⡏⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀ 
⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⡰⠋⢙⣿⣦⡀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣦⣮⣤⡀⣸⣿⣿⣿⣆⠀⠀⠀⠀  
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⣿⢟⣫⠟⠋⠀⠀⠀⠀ 
⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣷⣷⣿⡁⠀⠀⠀⠀⠀⠀  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢸⣿⣿⣧⣿⣿⣆⠙⢆⡀⠀⠀⠀⠀           
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣤⣿⣿⣿⡟⠹⣿⣿⣿⣿⣷⡀⠀  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣴⣿⣿⣿⣿⠏⢧⠀⠀  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠈⢳⡀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⢳  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣼⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠛⠻⠿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⠏⠀
```"""
    ]

@bot.command()
async def help(ctx, page: int = 1):
    global help_message, help_author, help_expiry, pages
    
    total_pages = len(pages)
    if 1 <= page <= total_pages:
        await ctx.send(f"``` xblood is welcoming you ```")
        message = await ctx.send(pages[page - 1] + f"```ansi\n              {www}Page {page}/{total_pages} - Type {red}p#{www} to navigate.                 Welcome [ {red}{bot.user}{www} ]        Made by [ @mwpv ]         ```")
        
        help_message = message
        help_author = ctx.author
        help_expiry = asyncio.get_event_loop().time() + 60  
        
        await asyncio.sleep(60)
        help_message = None
        help_author = None
        help_expiry = None
    else:
        await ctx.send(f"Invalid page number. Please choose a page between 1 and {total_pages}.", delete_after=10)

@bot.command()
async def hypesquad(ctx, house: str):
    house_ids = {
        "bravery": 1,
        "brilliance": 2,
        "balance": 3
    }

    headers = {
        "Authorization": bot.http.token, 
        "Content-Type": "application/json"
    }

    if house.lower() == "off":
        url = "https://discord.com/api/v9/hypesquad/online"
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, headers=headers) as response:
                if response.status == 204:
                    await ctx.send("```HypeSquad house removed.```")
                else:
                    error_message = await response.text()
                    await ctx.send(f"```Failed to remove HypeSquad house: {response.status} - {error_message}```")
        return

    house_id = house_ids.get(house.lower())
    if house_id is None:
        await ctx.send("```Invalid house. Choose from 'bravery', 'brilliance', 'balance', or 'off'.```")
        return

    payload = {"house_id": house_id}
    url = "https://discord.com/api/v9/hypesquad/online"

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status == 204:
                await ctx.send(f"```HypeSquad house changed to {house.capitalize()}.```")
            else:
                error_message = await response.text()
                await ctx.send(f"```Failed to change HypeSquad house: {response.status} - {error_message}```")

            
@bot.group(invoke_without_command=True)
async def rotateguild(ctx, delay: float = 2.0):
    global guild_rotation_task, guild_rotation_delay
    
    if guild_rotation_task and not guild_rotation_task.cancelled():
        await ctx.send("```tag rotation is already running```")
        return
        
    if delay < 1.0:
        await ctx.send("```tag must be at least 1 second```")
        return
        
    guild_rotation_delay = delay
    
    async def rotate_guilds():
        headers = {
            "authority": "canary.discord.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "authorization": bot.http.token,
            "content-type": "application/json",
            "origin": "https://canary.discord.com",
            "referer": "https://canary.discord.com/channels/@me",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI1MDgzNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }
        
        while True:
            try:
                async with aiohttp.ClientSession() as session:
                    valid_guild_ids = []
                    
                    async with session.get(
                        'https://canary.discord.com/api/v9/users/@me/guilds',
                        headers=headers
                    ) as guild_resp:
                        if guild_resp.status != 200:
                            await ctx.send("```Failed to fetch guilds```")
                            return
                        
                        guilds = await guild_resp.json()
                        
                        for guild in guilds:
                            test_payload = {
                                'identity_guild_id': guild['id'],
                                'identity_enabled': True
                            }
                            
                            async with session.put(
                                'https://canary.discord.com/api/v9/users/@me/clan',
                                headers=headers,
                                json=test_payload
                            ) as test_resp:
                                if test_resp.status == 200:
                                    valid_guild_ids.append(guild['id'])
                        
                        if not valid_guild_ids:
                            await ctx.send("```No guilds with valid clan badges found```")
                            return
                            
                        await ctx.send(f"```Found {len(valid_guild_ids)} guilds```")
                        
                        while True:
                            for guild_id in valid_guild_ids:
                                payload = {
                                    'identity_guild_id': guild_id,
                                    'identity_enabled': True
                                }
                                async with session.put(
                                    'https://canary.discord.com/api/v9/users/@me/clan',
                                    headers=headers,
                                    json=payload
                                ) as put_resp:
                                    if put_resp.status == 200:
                                        await asyncio.sleep(guild_rotation_delay)
                            
            except asyncio.CancelledError:
                raise
            except Exception as e:
                print(f"Error in guild rotation: {e}")
                await asyncio.sleep(5)
    
    guild_rotation_task = asyncio.create_task(rotate_guilds())
    await ctx.send(f"```Started guild rotation (Delay: {delay}s)```")

@rotateguild.command(name="stop")
async def rotateguild_stop(ctx):    
    global guild_rotation_task
    
    if guild_rotation_task and not guild_rotation_task.cancelled():
        guild_rotation_task.cancel()
        guild_rotation_task = None
        await ctx.send("```Stopped clan rotation```")
    else:
        await ctx.send("```Clan rotation is not running```")

@rotateguild.command(name="delay")
async def rotateguild_delay(ctx, delay: float):
    global guild_rotation_delay
    
    if delay < 1.0:
        await ctx.send("```Delay must be at least 1 second```")
        return
        
    guild_rotation_delay = delay
    await ctx.send(f"```Clan rotation delay set to {delay}s```")

@rotateguild.command(name="status")
async def rotateguild_status(ctx):
    status = "running" if (guild_rotation_task and not guild_rotation_task.cancelled()) else "stopped"
    await ctx.send(f"""```
Guild Rotation Status:
• Status: {status}
• Delay: {guild_rotation_delay}s
```""")
active_tokens = []  

typing_active = {}  

@bot.group(invoke_without_command=True)
async def vcjoin(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"""```ansi
{red}Voice Channel Commands:
{red}• {blue}vcjoin stable <channel_id> {black}- Join and stay in one voice channel
{red}• {blue}vcjoin rotate {black}- Rotate through all available voice channels
{red}• {blue}vcjoin random {black}- Randomly join voice channels
{red}• {blue}vcjoin list {black}- List all available voice channels
{red}• {blue}vcjoin leave {black}- Leave voice channel
{red}• {blue}vcjoin status {black}- Show current VC status```""")

@vcjoin.command(name="stable")
async def vc_stable(ctx, channel_id: int = None):
    if not channel_id:
        await ctx.send(f"```ansi\n{black}Please provide a voice channel ID```")
        return
        
    try:
        channel = bot.get_channel(channel_id)
        if not channel or not isinstance(channel, discord.VoiceChannel):
            await ctx.send(f"```ansi\n{black}Invalid voice channel ID```")
            return
            
        voice_client = ctx.guild.voice_client
        if voice_client:
            await voice_client.move_to(channel)
        else:
            await channel.connect()
            
        await ctx.send(f"```ansi\n{black}Connected to {black}{channel.name}```")
    except Exception as e:
        await ctx.send(f"```ansi\n{black}Error: {black}{str(e)}```")

@vcjoin.command(name="list")
async def vc_list(ctx):

    voice_channels = [channel for channel in ctx.guild.channels if isinstance(channel, discord.VoiceChannel)]
    if not voice_channels:
        await ctx.send(f"```ansi\n{black}No voice channels available```")
        return
        
    channel_list = "\n".join(f"{black}• {black}{channel.id}: {black}{channel.name}" for channel in voice_channels)
    await ctx.send(f"```ansi\n{black}Available Voice Channels:\n\n{channel_list}```")

@vcjoin.command(name="status")
async def vc_status(ctx):

    voice_client = ctx.guild.voice_client
    if voice_client and voice_client.channel:
        await ctx.send(f"""```ansi
{black}Current Voice Status:
{black}• {black}Connected to: {black}{voice_client.channel.name}
{black}• {black}Channel ID: {black}{voice_client.channel.id}
{black}• {black}Latency: {black}{round(voice_client.latency * 1000, 2)}ms```""")
    else:
        await ctx.send(f"```ansi\n{black}Not connected to any voice channel```")

@vcjoin.command(name="leave")
async def vc_leave(ctx):

    voice_client = ctx.guild.voice_client
    if voice_client:
        await voice_client.disconnect()
        await ctx.send(f"```ansi\n{black}Left voice channel```")
    else:
        await ctx.send(f"```ansi\n{black}Not in a voice channel```")

@vcjoin.command(name="rotate")
async def vc_rotate(ctx):

    voice_channels = [channel for channel in ctx.guild.channels if isinstance(channel, discord.VoiceChannel)]
    if not voice_channels:
        await ctx.send(f"```ansi\n{black}No voice channels available```")
        return
        
    rotate_active = True
    await ctx.send(f"```ansi\n{black}Starting voice channel rotation```")
    
    while rotate_active:
        for channel in voice_channels:
            try:
                voice_client = ctx.guild.voice_client
                if voice_client:
                    await voice_client.move_to(channel)
                else:
                    await channel.connect()
                    
                print(f"{text_color}Moved to channel: {highlight_color}{channel.name}")
                await asyncio.sleep(10)
                
                if not rotate_active:
                    break
                    
            except Exception as e:
                print(f"{accent_color}Error rotating to {channel.name}: {e}")
                continue


@bot.command()
async def typing(ctx, time: str, channel: discord.TextChannel = None):

    
    if channel is None:
        channel = ctx.channel

    total_seconds = 0


    try:
        if time.endswith('s'):
            total_seconds = int(time[:-1]) 
        elif time.endswith('m'):
            total_seconds = int(time[:-1]) * 60  
        elif time.endswith('h'):
            total_seconds = int(time[:-1]) * 3600  
        else:
            total_seconds = int(time)  
    except ValueError:
        await ctx.send("Please provide a valid time format (e.g., 5s, 2m, 1h).")
        return

   
    typing_active[channel.id] = True

    try:
        async with channel.typing():
            await ctx.send(f"```Triggered typing for {total_seconds}```")
            await asyncio.sleep(total_seconds)  
    except Exception as e:
        await ctx.send("```Failed to trigger typing```")
    finally:
        typing_active.pop(channel.id, None)

@bot.command()
async def typingoff(ctx, channel: discord.TextChannel = None):

    
    if channel is None:
        channel = ctx.channel

    if channel.id in typing_active:
        typing_active.pop(channel.id)  
        await ctx.send(f"```Stopped typing in {channel.name}.```")
    else:
        await ctx.send(f"```No typing session is active```")

@bot.command()
async def gcfill(ctx):
    tokens_file_path = 'token.txt'
    tokens = loads_tokens(tokens_file_path)

    if not tokens:
        await ctx.send("```No tokens found in the file. Please check the token file.```")
        return

    limited_tokens = tokens[:12]
    group_channel = ctx.channel

    async def add_token_to_gc(token):
        try:
            user_client = discord.Client(intents=intents)
            
            @user_client.event
            async def on_ready():
                try:
                    await group_channel.add_recipients(user_client.user)
                    print(f'Added {user_client.user} to the group chat')
                except Exception as e:
                    print(f"Error adding user with token {token[-4:]}: {e}")
                finally:
                    await user_client.close()

            await user_client.start(token, bot=False)
            
        except Exception as e:
            print(f"Failed to process token {token[-4:]}: {e}")

    tasks = [add_token_to_gc(token) for token in limited_tokens]
    await asyncio.gather(*tasks, return_exceptions=True)
    
    await ctx.send(f"```Attempted to add {len(limited_tokens)} tokens to the group chat```")

@bot.command()
async def gcleave(ctx):
    tokens_file_path = 'token.txt'
    tokens = loads_tokens(tokens_file_path)
    
    if not tokens:
        await ctx.send("```No tokens found in the file```")
        return
        
    channel_id = ctx.channel.id

    async def leave_gc(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        
        async with aiohttp.ClientSession() as session:
            try:
                url = f'https://discord.com/api/v9/channels/{channel_id}'
                async with session.delete(url, headers=headers) as response:
                    if response.status == 200:
                        print(f'Token {token[-4:]} left the group chat successfully')
                    elif response.status == 429:
                        retry_after = float((await response.json()).get('retry_after', 1))
                        print(f"Rate limited for token {token[-4:]}, waiting {retry_after}s")
                        await asyncio.sleep(retry_after)
                    else:
                        print(f"Error for token {token[-4:]}: Status {response.status}")
                        
            except Exception as e:
                print(f"Failed to process token {token[-4:]}: {e}")
            
            await asyncio.sleep(0.5) 

    tasks = [leave_gc(token) for token in tokens]
    await asyncio.gather(*tasks, return_exceptions=True)
    
    await ctx.send("```Attempted to make all tokens leave the group chat```")


@bot.command()
async def gcleaveall(ctx):
    tokens_file_path = 'token.txt'
    tokens = loads_tokens(tokens_file_path)
    
    if not tokens:
        await ctx.send("```No tokens found in the file```")
        return

    async def leave_all_gcs(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        left_count = 0
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get('https://discord.com/api/v9/users/@me/channels', headers=headers) as resp:
                    if resp.status == 200:
                        channels = await resp.json()
                        group_channels = [channel for channel in channels if channel.get('type') == 3]
                        
                        for channel in group_channels:
                            try:
                                channel_id = channel['id']
                                async with session.delete(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers) as leave_resp:
                                    if leave_resp.status == 200:
                                        left_count += 1
                                        print(f'Token {token[-4:]} left group chat {channel_id}')
                                    elif leave_resp.status == 429:
                                        retry_after = float((await leave_resp.json()).get('retry_after', 1))
                                        print(f"Rate limited for token {token[-4:]}, waiting {retry_after}s")
                                        await asyncio.sleep(retry_after)
                                    else:
                                        print(f"Error leaving GC {channel_id} for token {token[-4:]}: Status {leave_resp.status}")
                                
                                await asyncio.sleep(0.5)  
                                
                            except Exception as e:
                                print(f"Error processing channel for token {token[-4:]}: {e}")
                                continue
                                
                        return left_count
                    else:
                        print(f"Failed to get channels for token {token[-4:]}: Status {resp.status}")
                        return 0
                        
            except Exception as e:
                print(f"Failed to process token {token[-4:]}: {e}")
                return 0

    status_msg = await ctx.send("```Starting group chat leave operation...```")
    
    tasks = [leave_all_gcs(token) for token in tokens]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    total_left = sum(r for r in results if isinstance(r, int))
    
    await status_msg.edit(content=f"""```ansi
Group Chat Leave Operation Complete
Total tokens processed: {len(tokens)}
Total group chats left: {total_left}```""")


ugc_task = None
@bot.command()
async def gcname(ctx, user: discord.User):
    global ugc_task
    
    if ugc_task is not None:
        await ctx.send("```Group chat name changer is already running```")
        return
        
    if not isinstance(ctx.channel, discord.GroupChannel):
        await ctx.send("```This command can only be used in group chats.```")
        return

    async def name_changer():
        counter = 1
        unused_names = list(self_gcname)
        
        while True:
            try:
                if not unused_names:
                    unused_names = list(self_gcname)
                
                base_name = random.choice(unused_names)
                unused_names.remove(base_name)
                
                formatted_name = base_name.replace("{user}", user.name).replace("{UPuser}", user.name.upper())
                new_name = f"{formatted_name} {counter}"
                
                await ctx.channel._state.http.request(
                    discord.http.Route(
                        'PATCH',
                        '/channels/{channel_id}',
                        channel_id=ctx.channel.id
                    ),
                    json={'name': new_name}
                )
                
                await asyncio.sleep(0.1)
                counter += 1
                
            except discord.HTTPException as e:
                if e.code == 429:
                    retry_after = e.retry_after if hasattr(e, 'retry_after') else 1
                    await asyncio.sleep(retry_after)
                    continue
                else:
                    await ctx.send(f"```Error: {str(e)}```")
                    break
            except asyncio.CancelledError:
                break
            except Exception as e:
                await ctx.send(f"```Error: {str(e)}```")
                break

    ugc_task = asyncio.create_task(name_changer())
    await ctx.send("```Group chat name changer started```")

@bot.command()
async def gcnameend(ctx):
    global ugc_task
    
    if ugc_task is None:
        await ctx.send("```Group chat name changer is not currently running```")
        return
        
    ugc_task.cancel()
    ugc_task = None
    await ctx.send("```Group chat name changer stopped```")

@bot.command()
async def areply(ctx, user: discord.User):
    channel_id = ctx.channel.id

    await ctx.send(f"```Autoreply for {user.mention} has started.```")

    async def send_autoreply(message):
        while True:  
            try:
                random_reply = random.choice(autoreplies)
                await message.reply(random_reply)
                print(f"Successfully replied to {user.name}")
                break  
            except discord.errors.HTTPException as e:
                if e.status == 429:  
                    try:
                        response_data = await e.response.json()
                        retry_after = response_data.get('retry_after', 1)
                    except:
                        retry_after = 1 
                    print(f"Rate limited, waiting {retry_after} seconds...")
                    await asyncio.sleep(retry_after)
                else:
                    print(f"HTTP Error: {e}, retrying...")
                    await asyncio.sleep(1)
            except Exception as e:
                print(f"Error sending message: {e}, retrying...")
                await asyncio.sleep(1)

    async def reply_loop():
        def check(m):
            return m.author == user and m.channel == ctx.channel

        while True:
            try:
                message = await bot.wait_for('message', check=check)
                asyncio.create_task(send_autoreply(message))
                await asyncio.sleep(0.1)  
            except Exception as e:
                print(f"Error in reply loop: {e}")
                await asyncio.sleep(1)
                continue


    task = bot.loop.create_task(reply_loop())
    autoreply_tasks[(user.id, channel_id)] = task

@bot.command()
async def areplyoff(ctx):
    channel_id = ctx.channel.id
    tasks_to_stop = [key for key in autoreply_tasks.keys() if key[1] == channel_id]
    
    if tasks_to_stop:
        for user_id in tasks_to_stop:
            task = autoreply_tasks.pop(user_id)
            task.cancel()
        await ctx.send("```Autoreply has been stopped.```")
    else:
        await ctx.send("```No active autoreply tasks in this channel.```")


@bot.command()
async def mimic(ctx, user: discord.Member):
    if not hasattr(bot, 'mimic_tasks'):
        bot.mimic_tasks = {}
        
    if user.id in bot.mimic_tasks:
        bot.mimic_tasks[user.id].cancel()
        del bot.mimic_tasks[user.id]
        await ctx.send(f"```Stopped mimicking {user.name}```")
        return

    headers = {
        "authorization": bot.http.token,
        "content-type": "application/json"
    }

    last_message_id = None
    cached_messages = {}
    
    blocked_content = [
        "underage", "minor", "year old", "yo", "years old",
        "10", "11", "9", "8", "7", "6", "5", "4", "3", "1", "2",
        "12", "13", "14", "mute",
        "/kick", "/mute", ".kick", ".mute",
        "-kick", "-mute", "$kick", "ban",
        "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "self-bot", "self bot",
        "nsfw", "porn", "hentai", "nude", "nudes"
    ]

    async def mimic_task():
        nonlocal last_message_id
        
        while user.id in bot.mimic_tasks:
            try:
                params = {'after': last_message_id} if last_message_id else {'limit': 1}
                response = requests.get(
                    f"https://discord.com/api/v9/channels/{ctx.channel.id}/messages",
                    headers=headers,
                    params=params
                )
                
                if response.status_code == 200:
                    messages = response.json()
                    
                    for msg in reversed(messages):
                        if msg['author']['id'] == str(user.id):
                            content = msg.get('content', '').lower()
                            
                            if any(word in content for word in blocked_content):
                                continue
                            
                            content = msg.get('content', '')
                            
                            while content.startswith('.'):
                                content = content[1:].lstrip()  
                            
                            if not content:
                                continue
                                
                            if content[:3].count('.') > 1:
                                continue

                            if content.startswith(('!', '?', '-', '$', '/', '>', '<')):
                                continue
                            
                            if not content and msg.get('referenced_message'):
                                content = f"Reply to: {msg['referenced_message'].get('content', '[Content Hidden]')}"
                            elif not content and msg.get('mentions'):
                                content = f"Mentioned: {', '.join(m['username'] for m in msg['mentions'])}"
                            elif not content:
                                if msg.get('embeds'):
                                    embed = msg['embeds'][0]
                                    content = embed.get('description', embed.get('title', '[Embed]'))
                                elif msg.get('attachments'):
                                    content = '[' + ', '.join(a['filename'] for a in msg['attachments']) + ']'
                                else:
                                    continue
                                    
                            if any(word in content.lower() for word in blocked_content):
                                continue
                            
                            if msg['id'] not in cached_messages:
                                cached_messages[msg['id']] = True
                                
                                payload = {
                                    "content": content,
                                    "tts": False
                                }
                                
                                if msg.get('embeds'):
                                    payload['embeds'] = msg['embeds']
                                
                                requests.post(
                                    f"https://discord.com/api/v9/channels/{ctx.channel.id}/messages",
                                    headers=headers,
                                    json=payload
                                )
                                
                                await asyncio.sleep(0.5)
                            
                            last_message_id = msg['id']
                            
            except Exception as e:
                print(f"Mimic Error: {e}")
                
            await asyncio.sleep(1)

    task = bot.loop.create_task(mimic_task())
    bot.mimic_tasks[user.id] = task
    await ctx.send(f"```Started mimicking {user.name}```")
@bot.command()
async def autoreact(ctx, user: discord.User, emoji: str):
    autoreact_users[user.id] = emoji
    await ctx.send(f"```Now auto-reacting with {emoji} to {user.name}'s messages```")

@bot.command()
async def autoreactoff(ctx, user: discord.User):
    if user.id in autoreact_users:
        del autoreact_users[user.id]
        await ctx.send(f"```Stopped auto-reacting to {user.name}'s messages```")
    else:
        await ctx.send("```This user doesn't have autoreact enabled```")        

@bot.command()
async def dreact(ctx, user: discord.User, *emojis):
    if not emojis:
        await ctx.send("```Please provide at least one emoji```")
        return
        
    dreact_users[user.id] = [list(emojis), 0]  # [emojis_list   , and then current index cuz why not >.<]
    await ctx.send(f"```Now alternating reactions with {len(emojis)} emojis on {user.name}'s messages```")

@bot.command()
async def dreactoff(ctx, user: discord.User):
    if user.id in dreact_users:
        del dreact_users[user.id]
        await ctx.send(f"```Stopped reacting to {user.name}'s messages```")
    else:
        await ctx.send("```This user doesn't have dreact enabled```")   
@bot.command()
async def clearmsg(ctx, limit: int):
    
    await ctx.message.delete() 
    

    async for message in ctx.channel.history(limit=limit):
        if message.author == ctx.author:  
            try:
                await message.delete()
            except discord.HTTPException:
                print(f"Failed to delete message {message.id} due to a rate limit or permission issue.")
    

    await ctx.send(f"```Purged {limit} of your messages.```", delete_after=5)

countdown_active = False
@bot.command(name="countdown")
async def afkcheck(ctx, member: discord.Member, count: int):
    global countdown_active
    countdown_active = True  

    count = abs(count)

    for i in range(count, 0, -1):
        if not countdown_active:
            break

        countdown_message = f"{member.mention} **{i}**"

        await ctx.send(countdown_message)

        await asyncio.sleep(1)

    if countdown_active:
        await ctx.send(f"```ountdown complete.```")

countdown_active = False  


@bot.command(name="countdownoff")
async def afkoff(ctx):
    global countdown_active
    countdown_active = False
    await ctx.send(f"```the countdown has been stopped.```")


forced_nicknames = {}

@bot.command(name="autonick")
async def forcenick(ctx, action: str, member: discord.Member = None, *, nickname: str = None):
    global forced_nicknames

    if action == "toggle":
        if member is None or nickname is None:
            await ctx.send("```Please mention a user and provide a nickname.```")
            return

        if ctx.guild.me.guild_permissions.manage_nicknames:
            forced_nicknames[member.id] = nickname
            await member.edit(nick=nickname)
            await ctx.send(f"```{member.display_name}'s nickname has been set to '{nickname}'.```")
        else:
            await ctx.send("```I do not have permission to change nicknames.```")

    elif action == "list":
        if forced_nicknames:
            user_list = "\n".join([f"<@{user_id}>: '{name}'" for user_id, name in forced_nicknames.items()])
            await ctx.send(f"```Users with forced nicknames:\n{user_list}```")
        else:
            await ctx.send("No users have forced nicknames.")

    elif action == "clear":
        if member is None:
            forced_nicknames.clear()
            await ctx.send("```All forced nicknames have been cleared.```")
        else:
            if member.id in forced_nicknames:
                del forced_nicknames[member.id]
                await member.edit(nick=None)  
                await ctx.send(f"```{member.display_name}'s forced nickname has been removed.```")
            else:
                await ctx.send(f"```{member.display_name} does not have a forced nickname.```")
    else:
        await ctx.send("```Invalid action. Use `toggle`, `list`, or `clear`.```")
@bot.event
async def on_member_update(before, after):
    if before.nick != after.nick and after.id in forced_nicknames:
        forced_nickname = forced_nicknames[after.id]
        if after.nick != forced_nickname:  
            try:
                await after.edit(nick=forced_nickname)
                print(f"Nickname for {after.display_name} reset to forced nickname '{forced_nickname}'.")
            except discord.errors.Forbidden:
                print("Bot does not have permission to change nicknames.") 

@bot.command(name="banner")
async def userbanner(ctx, user: discord.User):
    headers = {
        "Authorization": bot.http.token,
        "Content-Type": "application/json"
    }
    
    url = f"https://discord.com/api/v9/users/{user.id}/profile"
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            banner_hash = data.get("user", {}).get("banner")
            
            if banner_hash:
                banner_format = "gif" if banner_hash.startswith("a_") else "png"
                banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_hash}.{banner_format}?size=1024"
                await ctx.send(f"```{user.display_name}'s banner:``` [Birth Sb]({banner_url})")
            else:
                await ctx.send(f"{user.mention} does not have a banner set.")
        else:
            await ctx.send(f"Failed to retrieve banner: {response.status_code} - {response.text}")
    
    except Exception as e:
        await ctx.send(f"An error occurred: {e}") 
@bot.command(aliases=['av', 'pfp'])
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author

    avatar_url = str(user.avatar_url_as(format='gif' if user.is_avatar_animated() else 'png'))

    await ctx.send(f"```{user.name}'s pfp```\n[xblood Sb]({avatar_url})")

async def change_status():
    await bot.wait_until_ready()
    while True:
        for status in statuses:
            await bot.change_presence(activity=discord.Streaming(name=status, url="https://www.twitch.tv/ex"))
            await asyncio.sleep(10) 





@bot.command()
async def stream(ctx, *, statuses_list: str):
    global status_changing_task
    global statuses
    
    statuses = statuses_list.split(',')
    statuses = [status.strip() for status in statuses]
    
    if status_changing_task:
        status_changing_task.cancel()
    
    status_changing_task = bot.loop.create_task(change_status())
    await ctx.send(f"```Set Status to {statuses_list}```")

@bot.command()
async def streamoff(ctx):
    global status_changing_task
    
    if status_changing_task:
        status_changing_task.cancel()
        status_changing_task = None
        await bot.change_presence(activity=None)  
        await ctx.send(f'status rotation stopped')
    else:
        await ctx.send(f'status rotation is not running')

@bot.command(name='rstatus')
async def rotate_status(ctx, *, statuses: str):
    global status_rotation_active, current_status, current_emoji
    await ctx.message.delete()
    
    status_list = [s.strip() for s in statuses.split(',')]
    
    if not status_list:
        await ctx.send("```Please separate statuses by commas.```", delete_after=3)
        return
    
    current_index = 0
    status_rotation_active = True
    
    async def update_status_emoji():
        json_data = {
            'custom_status': {
                'text': current_status,
                'emoji_name': current_emoji
            }
        }

        custom_emoji_match = re.match(r'<a?:(\w+):(\d+)>', current_emoji)
        if custom_emoji_match:
            name, emoji_id = custom_emoji_match.groups()
            json_data['custom_status']['emoji_name'] = name
            json_data['custom_status']['emoji_id'] = emoji_id
        else:
            json_data['custom_status']['emoji_name'] = current_emoji

        async with aiohttp.ClientSession() as session:
            try:
                async with session.patch(
                    'https://discord.com/api/v9/users/@me/settings',
                    headers={'Authorization': bot.http.token, 'Content-Type': 'application/json'},
                    json=json_data
                ) as resp:
                    await resp.read()
            finally:
                await session.close()

    await ctx.send(f"```Status rotation started```")
    
    try:
        while status_rotation_active:
            current_status = status_list[current_index]
            await update_status_emoji()
            await asyncio.sleep(8)
            current_index = (current_index + 1) % len(status_list)
                
    finally:
        current_status = ""
        await update_status_emoji()
        status_rotation_active = False

@bot.command(name='remoji')
async def rotate_emoji(ctx, *, emojis: str):
    global emoji_rotation_active, current_emoji, status_rotation_active
    await ctx.message.delete()
    
    emoji_list = [e.strip() for e in emojis.split(',')]
    
    if not emoji_list:
        await ctx.send("```Please separate emojis by commas.```", delete_after=3)
        return
    
    current_index = 0
    emoji_rotation_active = True
    
    async def update_status_emoji():
        json_data = {
            'custom_status': {
                'text': current_status,
                'emoji_name': current_emoji
            }
        }
        
        custom_emoji_match = re.match(r'<a?:(\w+):(\d+)>', current_emoji)
        if custom_emoji_match:
            name, emoji_id = custom_emoji_match.groups()
            json_data['custom_status']['emoji_name'] = name
            json_data['custom_status']['emoji_id'] = emoji_id
        else:
            json_data['custom_status']['emoji_name'] = current_emoji

        async with aiohttp.ClientSession() as session:
            try:
                async with session.patch(
                    'https://discord.com/api/v9/users/@me/settings',
                    headers={'Authorization': bot.http.token, 'Content-Type': 'application/json'},
                    json=json_data
                ) as resp:
                    await resp.read()
            finally:
                await session.close()

    await ctx.send(f"```Emoji rotation started```")
    
    try:
        while emoji_rotation_active:
            current_emoji = emoji_list[current_index]
            await update_status_emoji()
            await asyncio.sleep(8)
            current_index = (current_index + 1) % len(emoji_list)
                
    finally:
        current_emoji = ""
        await update_status_emoji()
        emoji_rotation_active = False

@bot.command(name='stopstatus')
async def stop_rotate_status(ctx):
    global status_rotation_active
    status_rotation_active = False
    await ctx.send("```Status rotation stopped.```", delete_after=3)

@bot.command(name='stopemoji')
async def stop_rotate_emoji(ctx):
    global emoji_rotation_active
    emoji_rotation_active = False
    await ctx.send("```Emoji rotation stopped.```", delete_after=3)

force_delete_users = defaultdict(bool)  


@bot.command(name="forcepurge")
async def forcepurge(ctx, action: str, member: discord.Member = None):
    if action.lower() == "toggle":
        if member is None:
            await ctx.send("```Please mention a user to toggle force delete.```")
            return
        force_delete_users[member.id] = not force_delete_users[member.id]
        status = "enabled" if force_delete_users[member.id] else "disabled"
        await ctx.send(f"```Auto-delete messages for {member.display_name} has been {status}.```")

    elif action.lower() == "list":

        enabled_users = [f"```<@{user_id}>```" for user_id, enabled in force_delete_users.items() if enabled]
        if enabled_users:
            await ctx.send("```Users with auto-delete enabled:\n```" + "\n".join(enabled_users))
        else:
            await ctx.send("```No users have auto-delete enabled.```")

    elif action.lower() == "clear":
        force_delete_users.clear()
        await ctx.send("```Cleared auto-delete settings for all users.```")

    else:
        await ctx.send("```Invalid action. Use `toggle`, `list`, or `clear`.```")


@bot.event
async def on_message(message):
    if message.author == bot.user and message.content.startswith('.'):
        return

    if help_message and message.author == help_author and help_expiry and help_expiry > asyncio.get_event_loop().time():
        content = message.content.lower()
        if content in ['p1', 'p2', 'p3', 'p4', 'p5']:
            page = int(content[1])
            if 1 <= page <= len(pages):
                await help_message.edit(content=pages[page - 1] + f"```ansi\n              {www}Page {page}/{len(pages)} - Type {red}p#{www} to navigate.                 {www}Welcome [ {red}{bot.user}{www} ]             Made by [ @mwpv ]         ```")
                try:
                    await message.delete()
                except:
                    pass

    for user_id, emoji in autoreact_users.items():
        if message.author.id == user_id:
            try:
                await message.add_reaction(emoji)
            except Exception as e:
                print(e)

    for user_id, data in dreact_users.items():
        if message.author.id == user_id:
            emojis = data[0]
            current_index = data[1]
            try:
                await message.add_reaction(emojis[current_index])
                data[1] = (current_index + 1) % len(emojis)
            except Exception as e:
                print(e)


    if force_delete_users[message.author.id]:
        try:
            await message.delete()
        except:
            pass

    await bot.process_commands(message)


gcspam_protection_enabled = False

@bot.command()
async def antigc(ctx):
    global gcspam_protection_enabled
    gcspam_protection_enabled = not gcspam_protection_enabled

    if gcspam_protection_enabled:
        await ctx.send(f"```ansi\nGroup chat spam protection is now {cyan}enabled.```")
    else:
        await ctx.send(f"```ansi\nGroup chat spam protection is now {red}disabled.```")

        
@bot.event
async def on_private_channel_create(channel):
    if gcspam_protection_enabled and isinstance(channel, discord.GroupChannel):
        try:
            headers = {
                'Authorization': bot.http.token,
                'Content-Type': 'application/json'
            }
            params = {
                'silent': 'true'
            }
            async with aiohttp.ClientSession() as session:
                async with session.delete(f'https://discord.com/api/v9/channels/{channel.id}', headers=headers, params=params) as resp:
                    if resp.status == 200:
                        print(f"left group chat silently: {channel.id}")
                    elif resp.status == 429:
                        retry_after = int(resp.headers.get("Retry-After", 1))
                        print(f"Rate limited. Retrying after {retry_after} seconds...")
                        await asyncio.sleep(retry_after)
                    else:
                        print(f"Failed to leave group chat. Status code: {resp.status}")
        except Exception as e:
            print(f"Error leaving group DM: {e}")

    if not autogc_enabled:
        return

    try:
        async for msg in channel.history(limit=1):
            if msg.author.id in gc_whitelist:
                return
    except:
        pass

@bot.command()
async def cls(ctx):
    os.system('cls')  
    print(main)
    await ctx.send(f"```Cleared Display UI```")

bot.run(TOKEN, bot=False)
