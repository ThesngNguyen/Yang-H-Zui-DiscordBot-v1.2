import discord
import random
import asyncio
from discord import client, Intents
from discord.ext import commands, tasks
from itertools import cycle

intents = Intents.default()
intents.members = True
client = discord.Client(intents = intents)
status = cycle(['Anh','Iêu', 'Em', 'Nắm'])

#Prefix của con bot
client = commands.Bot(command_prefix = '>', intents = intents)

#Kiểm tra Bot khởi động
@client.event
async def on_ready():
    change_status.start()
    # await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type = discord.ActivityType.watching, name = 'Pỏn Húp'))
    print('Bố mày sẵn sàng rồi!'.format(client))

#Loop Status Bot
@tasks.loop(seconds = 1)
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
    
    

client.run('OTE4NTQ5NDIzOTcyMzE1MTM2.YbI30A.ziBGvqMQjRvpohGUYzNpxHINN-k')