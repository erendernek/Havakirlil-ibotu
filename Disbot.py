import discord
from discord.ext import commands
import os 
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')





@bot.command()
async def info(ctx):
    await ctx.send(f'Ben, hava kirliliği botuyum. Size bununla ilgili bilgi verbilirim.\n Bir vidyo isterseniz vid \n Hava kirliliği nedir: a\n Hava kirliliğini nasıl önleyebiliriz: b\n Hava kirliliği ile ilgili bilgiler: c')


@bot.command()
async def c(ctx):
    await ctx.send("""12.yy ve 13. yy’larda hava kirliliği İngiltere gibi gelişmiş ülkelerin büyük kentlerinde oluşmaya başlamıştır.\n
1288 yılında fosil yakıt tüketiminin aşırı artması nedeniyle İngiltere Kraliçesi Elanor akciğer rahatsılığı nedeniyle Buckingham Sarayını terk etmek zorunda kalmaştır. İlk defa o tarihte hava kirliliğinden sağlık sorunu rapor edilmiştir.\n Orta çağda kömür yakılmasının artması nedeniyle halkta sağlık sorunları oluşmaya başlamıştır.
1306 yılında Kral Edwart ısı kaynaklı kömür yakımını büyük kentlerde yasaklamıştır. \n
18.yy ve 19.yy da endüstri devrimi ve maden çıkartmanın yaygınlışması ile Almanya Ruhr vadisi, Amerika Cupper hill, İngiltere Themes nehri civarı o dönemin yoğun hava kirliliği olan yerleriydi.\n
20.yy ortalarına doğru hava kirliliği kendini iyiden iyiye hissettirmeye başladı.\n
1970'li yıllara gelindğinde ise hava kirliliği iyiden iyiye kentlerde insan sağlığı ve çevreyi tehtit etmeye başladı.\n
1972 yılında Stokholm konferansında temiz hava eylam planı yapıldı.""")


@bot.command()
async def vid(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=Wd0FzQTDM90')




@bot.command()
async def a(ctx):
    await ctx.send(f'Hava kirliliği, atmosferde zararlı veya istenmeyen maddelerin yoğunlaşmasıdır. Bu maddeler genellikle endüstriyel faaliyetler, araç emisyonları, tarım ve diğer insan etkinlikleri tarafından atmosfere salınır. Hava kirliliği insan sağlığına zarar verebilir, çevre kirliliğine ve iklim değişikliğine katkıda bulunabilir.')



@bot.command()
async def b(ctx):
    await ctx.send("""Hava kirliliğini önlemek için alınabilecek tedbirler

Sanayi tesislerinin bacalarına filtre takılması sağlanmalı, ayrıca sanayi kuruluşları yer seçimi düzenli yapılmalı,\n
Evleri ısıtmak için yüksek kalorili kömürler kullanılmalı, her yıl bacalar ve soba boruları temizlenmeli,\n
Pencere, kapı ve çatıların izolasyonuna önem verilmeli,\n
Kullanılan sobaların TSE belgeli olmasına dikkat edilmeli,\n
Doğalgaz kullanımı yaygınlaştırılarak, özendirilmeli,\n
Kalorisi düşük olan ve havayı daha çok kirleten kaçak kömür kullanımı engellenmeli,\n
Kalorifer ve doğalgaz kazanlarının periyodik olarak bakımı yapılmalı,\n
Kalorifercilerin ateşçi kurslarına katılımı sağlanmalı,\n
Yeni yerleşim yerlerinde merkezi ısıtma sistemleri kullanılmalı,\n
Toplu taşıma araçları yaygınlaştırılmalı,\n
Sanayi tesisleri kurulurken yeşil alanlar artırılmalı, planlanmalı, sanayi atıklarının yeterince filtre edilmeden havaya verilmesi önlenmeli,\n
Kentlerde arabaların egzozlarından kaynaklanan kirliliğin azaltılması için önlemler alınmalıdır. Bu kirleticiler kış aylarında ozon oluşmasına neden olduğu için canlıların solunumunu güçleştirir.\n
İnsanlar toplu taşımacılığa özendirilmeli, yakıt olarak kullanılan doğal gazın toplu ulaşım araçlarında kullanılması yaygınlaştırılmalı ,\n
Ormanların tahribatı önlenmeli, ağaçlandırma çalışmalarına hız verilmeli,ağaçlar kesilmemelidir\n
Kloroflorokarbon gibi maddelerin etkileri ile ozon tabakası zarar görmektedir. Bu maddelerin yerine kullanılabilecek kimyasallar araştırılmalıdır.\n
""")


bot.run("Token")
