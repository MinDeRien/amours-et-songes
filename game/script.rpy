# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Variable persistente pour afficher une seule fois le texte de "ces choix dévient de la pièce"
default persistent.seconplaytext=False
define config.has_autosave = True
define config.autosave_on_choice = True


#helena
default helena_home = False

# import images PUCK
image puck happy = "images/puck/side puck happy.png"
image puck awkward ="images/puck/side puck awkward.png"
image puck puck = "images/puck/side puck.png"
image puck question = "images/puck/side puck question.png"
image puck snarky = "images/puck/side puck snarky.png"
image puck angry = "images/puck/side puck angry.png"
image puck worry = "images/puck/side puck worry.png"
#side images
image side puck happy = "images/puck/side puck happy.png"
image side puck awkward ="images/puck/side puck awkward.png"
image side puck = "images/puck/side puck.png"
image side puck question = "images/puck/side puck question.png"
image side puck snarky = "images/puck/side puck snarky.png"
image side puck angry = "images/puck/side puck angry.png"
image side puck worry = "images/puck/side puck worry.png"

# import images THESEE
image thesee thesee = "images/thesee/side thesee.png"
image thesee angry = "images/thesee/side thesee angry.png"
image thesee snarky="images/thesee/side thesee snarky.png"
image thesee surprise="images/thesee/side thesee surprise.png"
image thesee sad="images/thesee/side thesee sad.png"
# side images
image side thesee = "images/thesee/side thesee.png"
image side thesee angry = "images/thesee/side thesee angry.png"
image side thesee snarky="images/thesee/side thesee snarky.png"
image side thesee surprise="images/thesee/side thesee surprise.png"
image side thesee sad="images/thesee/side thesee sad.png"

# import images EGEE
image egee egee ="images/egee/side egee.png"
image egee angry ="images/egee/side egee angry.png"
image egee surprise="images/egee/side egee surprise.png"
image egee happy="images/egee/side egee happy.png"
image egee sad="images/egee/side egee sad.png"
image egee snarky="images/egee/side egee snarky.png"
# side images
image side egee ="images/egee/side egee.png"
image side egee angry ="images/egee/side egee angry.png"
image side egee surprise="images/egee/side egee surprise.png"
image side egee happy="images/egee/side egee happy.png"
image side egee sad="images/egee/side egee sad.png"
image side egee snarky="images/egee/side egee snarky.png"

# import images OBERON
image oberon oberon ="images/oberon/side oberon.png"
image oberon angry="images/oberon/side oberon angry.png"
image oberon happy="images/oberon/side oberon happy.png"
image oberon open="images/oberon/side oberon open.png"
image oberon sad="images/oberon/side oberon sad.png"
image oberon snarky="images/oberon/side oberon snarky.png"
image oberon sullen="images/oberon/side oberon sullen.png"
image oberon surprise="images/oberon/side oberon surprise.png"
# side images
image side oberon ="images/oberon/side oberon.png"
image side oberon angry="images/oberon/side oberon angry.png"
image side oberon happy="images/oberon/side oberon happy.png"
image side oberon open="images/oberon/side oberon open.png"
image side oberon sad="images/oberon/side oberon sad.png"
image side oberon snarky="images/oberon/side oberon snarky.png"
image side oberon sullen="images/oberon/side oberon sullen.png"
image side oberon surprise="images/oberon/side oberon surprise.png"

# PLACEHOLDER FOR OTHER ACTORS

image DD DD = "images/demeterius/DD/side DD base neutral neutral.png"
image side DD="images/demeterius/DD/side DD base neutral neutral.png"

image H H ="images/helena/side H base neutral neutral.png"
image side H="images/helena/side H base neutral neutral.png"




init:
    $ define.move_transitions("slowermove",0.8,subpixel="True")
    $ define.move_transitions("slowerease",0.8,subpixel="True")
    $ define.move_transitions("superslowermove", 1.2, subpixel="True")
    $ define.move_transitions("superslowerease", 1.2, subpixel="True")
    $ define.move_transitions("fastermove", 0.3, subpixel="True")
    $ define.move_transitions("fasterease",0.3, subpixel="True")
    $ define.move_transitions("superfastermove", 0.14, subpixel="True")
    $ define.move_transitions("superfasterease", 0.14, subpixel="True")
    $ define.move_transitions("omegafastermove", 0.2, subpixel="True")

# CAST AND CREW -- PERSONNAGES DU JEU
define m = Character('Hermia', color="#ee70d3ff", image="M")
define h = Character('Héléna', color="#48c0f0", image="H")

# BLOC LYSANDRE --- 3 états
define l = Character("Lysandre", color="#9922e9", image="LN")
define le = Character("Lysandre", color="#9922e9", image="LE")
define lc = Character("Lysandre", color="#9922e9", image="LC")

# BLOC DEMETRIUS --- 3 états
define d = Character("Démétrius", color="#f5d131", image="DD")
define de = Character("Démétrius", color="#f5d131", image="DE")
define dc = Character("Démétrius", color="#f5d131", image="DC")

define t = Character("Titania", color="#3be7a0")
define o = Character("Obéron", color="#227a17", image="oberon")
define p = Character("Puck", color="#c7c69a", image="puck")
define e = Character("Égée", color="#8e9622ff", image="egee")
define th = Character("Thésée", color="#d65454", image="thesee")

init: 
    transform flip: 
        xzoom -1.0
    transform default:
        yalign 0.15

define dis = { "master" : Dissolve(2.0) }
define disShorter = {"master": Dissolve(1.1)}
define disShortest = {"master": Dissolve(0.8)}

# Le jeu commence ici
label start:
    if persistent.seconplaytext:
        jump secondplaytext
    else: 
        jump firstplaytext
    
    label firstplaytext:
        'Les choix précédés de "{choice_tag}" ouvrent des chemins qui dévient du texte original'
        jump secondplaytext
    
    label secondplaytext:
        scene bg intro
        "Notre histoire commence il était une fois, à Athènes..."
        "Il était une fois, à Athènes, le noble [e] rend visite à [th], le Duc, pour obtenir de lui qu'il fasse entendre raison à sa fille, la belle [m]."
        "Celle-ci, fiancée à l'homme qu'il a choisi pour elle, refuse de l'épouser.\nElle lui préfère un autre, qu'elle aime." 
        "[e] est accompagné de sa fille, [m], du fiancé qu'il lui a choisi, [d], ainsi que de son amour, [l]"
        window show
        show bg int_thesee_day
        show M M at left:
            xalign 0.08
            yalign 0.15
        show egee egee at left:
            yalign 0.15
            xalign -0.12
        with slowereaseinleft
        e egee"Bonjour à vous, [th], notre illustre Duc!"
        show thesee thesee at right: 
            yalign 0.15 xzoom -1
            xalign 1.10
        with slowereaseinright
        th thesee"Merci mon bon [e]. Quelles nouvelles viens-tu m'annoncer?"
        e sad"Je viens plein de dépit porter plainte contre mon enfant, ma fille [m]"
        e egee"Approche, [d]"
        show DD DD at center:
            yalign 0.15
            xalign 0.55
        with easeinleft
        e happy"Mon noble seigneur, cet homme a mon consentement pour l'épouser"
        show DD BaseNeutralSlightsmile
        e sad"Approche, [l]"
        show LN LN at center:
            yalign 0.15
            xalign 0.30
        with easeinleft
        e angry"Et celui-ci a ensorcelé le coeur de mon enfant"
        show DD BaseFrownDown
        show LN worryOpen
        e surprise"Oui, toi, [l]. Tu as donné des vers à ma fille et échangé avec elle des gages d'amour"
        show M BlushConUwu
        e angry "Tu as chanté à sa fenêtre au clair de lune, d'une voix trompeuse, des vers d'amour trompeurs"
        show DD BaseFrownNeutral
        e sad"Par maints cadeaux tu t'es emparé de son imagination"
        show M BlushSadSquiggly
        e angry "Bracelets faits de tes cheveux, bagues, bijoux, parures, colifichets, bagatelles, bouquets, gourmandises, tout-puissants messagers de la tendre jeunesse"
        e snarky "Par tes ruses empressées tu as escamoté le coeur de ma fille et changé en aigreur rétive son obéissance qui m'est due"
        show LN scowl
        show M painedFrown
        e surprise"Et, mon gracieux duc, si tant est qu'ici même devant votre seigneurie elle ne consent pas à épouser [d]"
        show LN worryBase
        e angry"Je revendique, puis qu'elle m'appartient, l'ancien privilège d'Athènes de disposer d'elle"
        show DD BaseRaisedDown
        e snarky"Je la donne à ce gentilhomme, ou à la mort, comme notre loi l'a expressément prévu en pareil cas"
        show LN worrySad
        th surprise"Que dites-vous [m]? Ecoutez-moi, belle jeune fille. Votre père doit être pour vous comme un dieu qui a modelé votre beauté"
        show M painedSquirm
        th snarky"Oui, vraiment, vous n'êtes pour lui que cire où il marqua son empreinte et c'est en son pouvoir de conserver votre image ou d'en finir avec elle"
        show DD BaseNeutralNeutral
        th thesee "[d] est un digne gentilhomme"
        show LN uwu
        m painedOpen"[l] aussi."
        show M painedFrown
        th sad"Il l'est par lui-même, mais comme il n'est pas agréé par votre père, c'est l'autre qu'on doit tenir pour plus digne"
        m sadOpen"Je voudrais que mon père ne vit qu'avec mes yeux"
        show M resolPout
        th angry"C'est plutôt à vos yeux de voir avec son jugement"
        show DD BaseNeutralSlightsmile
        m resolBase"Je supplie Votre Grâce de me pardonner; je ne sais quelle force me rend si téméraire, ni comment ma modestie ose, en votre présence, plaider pour mes pensées"
        m resolTalk"Mais j'implore Votre Grâce de me dire ce qui peut m'arriver de pire si je refuse d'épouser [d]"
        show LN worryBase
        show M painedFrown
        th thesee "Ou la peine capitale, ou abjurer pour toujours la société des hommes"
        th sad "C'est pourquoi, belle [m], interrogez vos désirs, considérez votre jeunesse, posez la question à votre sang"
        show M painedSquirm
        th angry"Voyez si, refusant de vous soumettre au choix de votre père, vous pourrez supporter l'habit de nonne et être enfermée à jamais dans un cloître obscur"
        th sad "Rester toute votre vie vierge et nonne, psalmodiant des hymnes languissants à la froide et stérile lune"
        show M painedFrown
        th snarky "Trois fois bénies celles qui donnent ainsi leur sang pour supporter ce virginal pélerinage!"
        th sad "Mais plus heureuse sur terre est la rose distillée que celle qui s'étiole sur ses chastes épines et grandit, vit et meurt dans une solitude bénie"
        show egee sad
        show LN worrySad
        m resolBase"Je veux grandir ainsi, vivre et mourir ainsi monseigneur, plutôt que de céder mes virginales faveurs à l'autorité d'un mâitre dont mon âme refuse le joug imposé"
        show DD BaseRaisedDown
        th sad"Prenez le temps de réfléchir, et à la nouvelle lune, au jour qui doit sceller un lien d'éternel amour entre ma bien-aimée et moi" 
        show M sadPout
        th sad "Préparez-vous à mourir pour votre désobéissance, ou à épouser [d], ou enfin à faire voeu de chasteté sur l'autel de Diane"
        d BaseRaisedTalk"Cède, douce [m]. Et toi, [l], abandonne tes folles prétentions devant mon droit manifeste!"
        show DD BaseRaisedDown
        l scowl"Tu as l'amour de son père, [d]. Laisse-moi celui d'[m]."
        show DD BaseRaisedSquirm
        l snarky "Épouse-le!"
        show egee surprise
        show bg int_thesee_pm with disShorter
        e surprise"Méprisant [l]. Oui, il a mon affection. Et ce qui est à moi, mon affection le lui donnera"
        show LN resolve
        show M conSquirm
        e snarky"Or [m] est à moi, et je transfère à [d] tous les droits que j'ai sur elle"
        show DD BaseNeutralNeutral
        l talk1 "Monseigneur. Je suis d'aussi bonne naissance que lui, et non moins riche. Mon amour est plus grand que le sien; mon avenir aussi large et brillant, sinon davantage que celui de [d]"
        l talk2"Et ce qui importe plus que toutes ces vanités, je suis aimé de la belle [m]. Pourquoi donc ne ferais-je pas valoir mes droits? "
        show egee angry
        l angryTalk1"[d], et je le lui soutiendrai en face, a courtisé [h], la fille de Nedar. Il a gagné son coeur et la douce enfant s'est éprise de lui"
        show DD WideFrownDown
        show M sadSquirm
        l angryTalk2"Elle en radote, elle idolâtre cet homme taré et inconstant"
        th thesee"Je dois avouer que je l'avais entendu dire et j'avais l'intention d'en parler à [d]"
        show DD WideRaisedSquiggly
        show LN LN 
        show egee sad
        th snarky"Mais viens, [d], et toi aussi [e], j'ai des conseils à vous donner à tous deux en particulier"
        show DD BaseRaisedNeutral
        show LN worryBase
        show M sadPout
        th sad"Et quand à vous, belle [m], maîtrisez-vous de sorte que vos sentiments soient conformes à la volonté paternelle"
        th angry "Sinon, la loi d'Athènes, qu'il n'est pas en notre pouvoir de fléchir, vous condamne à mort ou au voeu de chasteté"
        show M conSquirm
        th thesee "[d] et [e], suivez-moi. Je veux vous employer à une certaine affaire concernant notre mariage et causer avec vous de quelque chose qui vous touche de près"
        show DD BaseNeutralNeutral
        e happy "Nous avons le devoir et le désir de vous suivre"
        show thesee thesee:
            xzoom 1

        "[th] sort, accompagné de [d] et [e]"
    
        hide thesee thesee with slowereaseoutright
        pause (0.8)
        hide DD DD with slowereaseoutright
        hide egee egee with slowereaseoutright

        show LN LN at left
        show M at center
        with ease

        "Les amoureux [l] et [m] se retrouvent seuls"
        jump scene2

