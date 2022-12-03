import discord
import random
import json
import os
import asyncio
from discord import client, Intents, Game
from discord.ext import commands, tasks
from discord.ext.commands import bot
from discord.ext.commands import has_permissions
from itertools import cycle
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

players = {}
queues = {}
intents = Intents.default()
intents.members = True
client = discord.Client(intents = intents)
status = cycle(['Em','Thấy', 'Gì', 'Trong', 'Mắt', 'Kẻ', 'Si', 'Tình'])
os.chdir("C:\\Users\\Admin\\Desktop\\Dev\\DisBot")




#Prefix của con bot
client = commands.Bot(command_prefix = '/', intents = intents)
client.remove_command("help")

#Kiểm tra Bot khởi động
@client.event
async def on_ready():
    change_status.start()
    # await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = 'Pỏn Húp'))
    print('Bố mày sẵn sàng rồi!'.format(client))

#Loop Status Bot
@tasks.loop(seconds = 2)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

#Kiểm tra ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Mạng nhà mày như con cặc lõ vậy, tầm {round(client.latency * 1000)}ms ? ')
    
#User vô room hoặc out#

#User vô server
@client.event
async def on_member_join(member):
    guild = client.get_guild(779648839728627713)
    channel = guild.get_channel(779648840235352118)
    await channel.send(f'Á địt mẹ thằng lồn {member.mention} đến với miền đất hứa !!')
    await member.send(f'Đến địa bàn {guild.name} thì {member.name} coi chùng tao !!')

#User bị tự rời máy chủ
@client.event
async def on_member_leave(member):
    guild = client.get_guild(779648839728627713)
    channel = guild.get_channel(779648840235352118)
    await channel.send(f'Thằng ngu {member.mention} bị chửi tự ái quá nên tự động rời miền đất hứa rồi :)) ')
    
#User bị kick khỏi máy chủ
@client.command()
async def cutmemaydi(ctx, member : discord.Member, *, reason = None):
    guild = client.get_guild(779648839728627713)
    channel = guild.get_channel(779648840235352118)
    await member.kick(reason = reason)
    await channel.send(f'Lồn {member.mention} quá trát nên tao cho nó cúc luôn, khỏi cám ơn !! ')
    
#User bay màu vĩnh viễn khỏi máy chủ
@client.command()
async def baymau(ctx, member : discord.Member, *, reason = None):
    guild = client.get_guild(779648839728627713)
    channel = guild.get_channel(779648840235352118)
    await member.ban(reason = reason)
    await channel.send(f'Thằng óc buồi {member.mention} đừng để tao gặp lại nha! ')

#Sủi tin nhắn
@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    
#Quotes yang hồ
@client.command(pass_content = True)
async def trietly(ctx):
    responses = ['Trước mặt em , anh là thằng hai lúa. Sau lưng em , anh là chúa giang hồ.',
                 'Đường tao đi có quý nhân phù hộ , việc tao làm có quỷ dữ bảo kê.',
                 'Chốn ăn chơi tôi xin vắng mặt, bạn hoạn nạn nhấc máy gọi tôi.',
                 'Vuốt tóc lên anh là Giang Hồ, thả tóc xuống anh làm bồ của em.',
                 'Kẻ đào hoa ngồi yên tình cũng tới, kẻ lụy tình gặp tình nào tình ấy tan.',
                 'Kẻ không tiền nói hay cũng thành dở, người có tiền thở nhẹ cũng thành thơ.',
                 'Quá khứ của em anh không kịp tham dự, nhưng tương lai của em nhất định anh sẽ đi cùng',
                 'Gọi nhau 2 tiếng "Bạn Bè" đến lúc có bồ bỏ mẹ anh em ? ',
                 'Chim thiếu ăn chim tìm con sâu, tớ thiếu cậu tớ sầu con tim :<',
                 '"Anh Thích Em" nó gọi là câu đơn, "Em ghét anh" nó gọi là cơn đau...',
                 'Có tiền đời đẹp như mơ , không tiền tình bỏ bạn lơ chẳng nhìn.',
                 'Bạn ơi trái đất hình cầu , bồ tui bạn gạ tét đầu như chơi.',
                 'Vì tri kỷ ta có thể bán mạng , đừng vì tiền tỷ mà bán mạng anh em.',
                 'Ráng đi học sau này làm bác sĩ , khám lòng người xem giả tạo tới đâu.',
                 'Cầm được con dao nó là bản năng , dám chém hay không nó là bản lĩnh.',
                 'Không mong gì nhiều chỉ mong sau này, anh em gặp lại và ngồi cùng nhau.',
                 'Vật chất xa hoa anh không có , yêu xe thương xế thì theo anh.',
                 'Thương cha mẹ anh giảm ga về số , nghĩ về em anh đá số tăng ga.',
                 'Con xe làm cho anh phong độ , cây kim số chỉ hướng mộ anh nằm.',
                 'Anh em tao nghèo nhưng sống tình cảm , bọn mày giàu chắc gì sống chết có nhau ?',
                 'Anh giúp tôi lúc khó, đến lúc có tôi nào dám quên ơn.',
                 'Đừng dùng đồng tiền để mua ân tình từ tao , sẵn lòng cho không nếu mày sống được!',
                 'Gia đình tôi kinh tế hạn hẹp, vì thế chữ nghèo nó đè bẹp chữ yêu...',
                 'Có tiền mới có được lòng , thời này ai lấy nghĩa tình cho không.',
                 'Tuy không sang nhưng chưa bao giờ chơi xấu , hoàn cảnh nghèo nên đành chôn giấu mọi tình yêu.',
                 'Lắc lắc quay quay anh bay trong Nonstop , đắng đắng cay cay anh say trong trò đời.',
                 'Tôi không giàu để mua được "Tình Bạn" , nhưng cũng chẳng nghèo để bán rẻ "Tình Anh Em".',
                 'Ngàn lời anh nói không bằng làn khói ôtô.',
                 'Cao sang quyền quý lắm kẻ theo , bần hàn cơ cực họ chê nghèo...']
    await ctx.send(f'{random.choice(responses)}')
    
#Boolean queue
def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
             
    
#Play nhạc cho Bot
@client.command()
async def play(ctx, url):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    YDL_OPTIONS = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1', 'options': '-reconnect_delay_max 5' '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Đưa tao cái mike rô !!')
#Bot đang chạy nhạc sẽ kh queue hàng chờ đc ( chưa code tới :)) //Update
    else:
        await ctx.send("Bố mày đang on da mic rồi đjt mẹ m >: (")
        return
    
def start_playing(self, voice_client, player):
    self.queue[0] = player
    i = 0
    while i < len(self.queue):
        try:
            voice_client.play(self.queue[i], after = lambda e: print('Error!!'))
        except:
            pass
        i += 1

@client.command()
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_clients_in(server)
    player = await voice_client.create_ytdl_player(url) 
    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await client.say('Hàng chờ nhạc : ')

#Tiếp tục nhạc
@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if not voice.is_playing():
        voice.resume()
        await ctx.send('Tao hát tiếp đjt mẹ mày luôn nha!!')
    else:
        await ctx.send('Có nhạc đâu mà hát thằng lồn ?')


#Tạm dừng nhạc
@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send('Giải lao lấy hơi cái đã !!')


#Dừng nhạc ( Kết thúc nhạc )
@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Cặc, dí buồi hát nữa !!')
       
#Kiểm tra số dư tài khoản 
@client.command()    
async def bal(ctx):
    await open_account(ctx.author) 
    user = ctx.author
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["Tiền Mặt"]
    bank_amt = users[str(user.id)]["Ngân Hàng"]
    em = discord.Embed(title = f"Tài khoản của {ctx.author.name}", color = discord.Color.red())     
    em.add_field(name = "Tiền Mặt", value = wallet_amt)
    em.add_field(name = "Ngân Hàng", value = bank_amt)
    await ctx.send(embed = em)
    
async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Tiền Mặt"] = 0
        users[str(user.id)]["Ngân Hàng"] = 0
    with open("bankbal.json","w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("bankbal.json","r") as f:
        users = json.load(f)
    return users

#Cào loto lụm lúa ( Update Gambling sau này )
@client.command()
async def loto(ctx):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    earn = random.randrange(1000,500000)
    await ctx.send(f"Tiền trên trời rơi xuống {earn} Việt Nam Đồng")
    users[str(user.id)]["Tiền Mặt"] += earn
    with open("bankbal.json","w") as f:
        json.dump(users,f) 

        
#Custom khung commands
@client.command()
async def help(ctx):
    user = ctx.message.author
    embed = discord.Embed(title = "Trợ Giúp Bot", description = "Toàn bộ lệnh của Bot", color = discord.Color.red())
    embed.set_author(name = ctx.message.guild.name, icon_url = ctx.message.guild.icon_url)
    embed.add_field(name = "Ping", value = "Kiểm tra độ trễ Ping mạng nội bộ")
    embed.add_field(name = "cax" , value = "abc ")
    embed.add_field(name = "play" , value = "Phát nhạc trong voice channel.")
    embed.add_field(name = "queue" , value = "Xem danh sách hàng chờ nhạc.")
    await ctx.send(embed = embed)
    
# @client.command()
# async def time():
#     user = ctx.message.authenticators(discord.Member):
        
@client.command()
async def oantuxi(ctx, message):
    answer = message.lower()
    choices = ["scissors", "rocks", "paper"]
    computers_answer = random.choice(choices)
    if answer not in choices:
        await ctx.send("Biết chơi không ba ? ")
    else:
        if computers_answer == answer:
            await ctx.send("Huề rồi mày ơi !!")
        if computers_answer == "rocks":
            if answer == "paper":
                await ctx.send(f"Bố mày ra Búa. Thua chịu, chơi lại mày !")
        if computers_answer == "paper":
            if answer == "rocks":
                await ctx.send(f"Bố mày ra Bao. Bố mày thắng rồi , thằng ngu :)))")
        if computers_answer == "scissors":
            if answer == "rocks":
                await ctx.send(f"Bố mày ra Kéo. Thua chịu, chơi lại mày !")
        if computers_answer == "rocks":
            if answer == "scissors":
                await ctx.send(f"Bố mày ra Búa. Bố mày thắng rồi , thằng ngu :)))")
        if computers_answer == "paper":
            if answer == "scissors":
                await ctx.send(f"Bố mày ra Bao. Thua chịu, chơi lại mày !")
        if computers_answer == "scissors":
            if answer == "paper":
                await ctx.send(f"Bố mày ra Kéo. Bố mày thắng rồi , thằng ngu :)))")
                

    

        

    
                
 
client.run('OTE4NTQ5NDIzOTcyMzE1MTM2.GiCRKo.Md_1FNBruzvMruGD8l-NYI-hOwAaG1Gpw7preg')

# Fix bug queue
# Add xác nhận tuổi video

