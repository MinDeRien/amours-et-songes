label scene2:
    window show
    show bg int_thesee_corr_pm with dissolve
    show LN LN at left:
        yalign 0.15
    show M BlushneutralSquirm at center:
        yalign 0.15
    l worryBase"Qu'y a-t-il mon amour? Pourquoi vos joues sont-elles si pâles? Pourquoi sur vous les roses se fanent-elles si vite?"
    show LN worryPout
    m BlushPainedOpen"Faute peut-être de pluie... qu'une averse de mes yeux pourrait leur prodiguer"
    show M BlushSadPout
    l worrySad"Hélas! D'après tout ce que j'ai pu lire ou entendre rapporter par la légende ou par l'histoire, le véritable amour n'eut jamais un cours paisible" 
    l worryTalk2"Mais tantôt la différence de naissance..."
    m BlushConScowl"Ô contrariété! être enchaîné à plus bas que soi"
    l worryTalk3"Tantôt la disparité d'âge..."
    m BlushConTalk"Malheur! Être fiancé à plus jeune que soi!"
    l worryBase"Tantôt il dépend du choix d'amis..."
    m BlushSadOpen"Ô enfer! choisir son amour par les yeux d'autrui"
    l worryOpen"Ou bien, s'il y eut parfait accord dans le choix, c'est la guerre, la mort ou la maladie qui venait l'assiéger"
    l worrySad"Rendant l'amour aussi rapide qu'un bruit, aussi léger qu'une ombre,fugace comme un rêve"
    show M BlushPainedFrown
    l worryTalk1"Bref comme l'éclair dans la nuit charbonneuse qui, dans un accès de fureur, dévoile ciel et terre"
    l worryTalk2"Mais avant qu'on ait pu dire: Regardez! Les mâchoires de la nuit l'ont englouti"
    l worryTalk3"Comme tout ce qui brille, vivement se brouille"
    m BlushPainedTalk"Si l'amour véritable est toujours contrarié, cela doit être un arrêt du destin"
    m BlushPainedOpen"Supportons donc cette épreuve avec patience, puisque c'est un mal habituel"
    m BlushSadTalk"Aussi inséparable de l'amour que les rêves, les soucis et les soupirs, les désirs et les pleurs qui forment le triste cortège de Désir"
    l worryEarnest"Sage pensée"
    
    show M BlushSadPout at center:
        yalign 0.15
    with ease
    show bg ext_thesee_pm with Dissolve(1.0)

    l resolve"Mais écoute-moi [m]. J'ai une tante veuve, douairière qui possède un gros revenu, et point d'enfants"
    show M BlushneutralTalk1
    l happySmile"Elle habite à sept lieues d'Athènes, et me considère comme son fils unique.\nLà-bas ma douce [m], je pourrai t'épouser, sans que la cruelle loi d'Athène puisse nous poursuivre"
    l blushFlirt"Donc si tu m'aimes, échappe-toi de la maison de ton père, demain, la nuit, et rends-toi dans la forêt à une lieue de la ville... Je t'y attendrai"
    m BlushConUwu"J'y serai, mon bon [l]! Je te le jure par l'arc le plus résistant de Cupidon, par sa plus rapide flèche à la pointe d'or, par l'innoncence des colombes de Vénus, par tout ce qui enchaîne les coeurs et attise les amours"
    m BlushSadUwu"Par le feu qui brûlait la reine de Carthage lorsqu'elle vit fuir le vaisseau du perfide Troyen, par tous les serments que jamais violèrent les hommes, plus nombreux que tous ceux que jamais firent les femmes"
    m BlushResolUwu"Oui, demain, en vérité, je te retrouverai en ce lui même où tu me donnes rendez-vous"
    l blushHbase"Tiens ta promesse, mon amour. Mais voici venir [h]"
    
    show LN LN at left: 
        yalign 0.15
        xalign -0.15
    show M BlushConSmile at left: 
        xalign 0.23
        yalign 0.15
    with ease
    "[h], amie d'enfance de [m], les rejoint"
    show H H at right: 
        yalign 0.15
        xalign 0.8
    with easeinright
    m neutralSmile"Dieu garde la belle [h]! Où allez-vous ainsi?"
    h BaseRaisedSadtalk "Belle, dites-vous? Belle est de trop. C'est vous la belle qu'aime [d].\nOh heureuse belle!"
    show LN happyBase
    show M neutralSquirm
    h BaseRaisedOpentalk"Vos yeux sont des étoiles polaires, et le doux gazouillis de votre voix est plus mélodieuse que l'alouette à l'oreille du berger, quand le blé est vert et que bourgeonnent les boutons d'aubépine"
    h BaseRaisedHappytalk"Les maladies sont contagieuses, ah! Que votre grâce ne l'est-elle, belle [m]! Comme je l'attrapperais avant de vous quitter!"
    show M neutralSquiggly
    h BaseNeutralOpentalk"Mon oreille attrapperait votre voix. Mon oeil, votre oeil.\nMa langue, la suave mélodie de votre langue."
    h BaseNeutralHappytalk"Si l'univers m'appartenait, je le donnerais tout entier - [d] excepté - pour être en vous changée." 
    show LN uwu
    h BlushBaseRaisedHappytalk"Apprenez-moi à vous ressembler, et par quelle magie vous gouvernez les battements de son coeur!"
    show LN happyBase
    show H BlushBaseRaisedDownturned
    m conPout"Je fronce les sourcils et malgré tout il m'aime."
    h BlushBaseNeutralHappytalk"Que vos sourcils enseignent cet art à mes sourires!"
    show H BlushBaseNeutralDownturned
    m conScowl"Je lui donne ma malédiction, qu'il me retourne en affection."
    h BaseNeutralOpentalk"Ah, puissent mes prières susciter pareille affection!"
    show H BaseNeutralDownturned
    m conOpen"Plus je le déteste, et plus il m'aime."
    h BaseRaisedSadtalk"Plus je l'aime, et plus il me déteste."
    show H BaseRaisedDownturned
    m sadOpen"Si il est fou, [h], ce n'est pas ma faute."
    show LN happySmile
    h BaseFrownSadtalk"Non. Seule votre beauté est fautive. Puissé-je commettre pareille faute!"
    show H BaseFrownDownturned
    m resolOpen"Consolez-vous, il ne verra plus mon visage. [l] et moi nous nous enfuyons d'ici. Athènes me semblait un paradis avant de connaître [l]"
    show H BaseRaisedNeutral
    m resolTalk"Ah, quel enchantement recèle mon amour pour qu'il ait fait du ciel un enfer!"
    show M neutralSmile
    l resolve"[h], nous allons vous dévoiler nos intentions." 
    show H BaseNeutralNeutral
    l happySmile"Demain soir, à l'heure où Phébé contemple son visage argenté dans le miroir des eaux et pare chaque brin d'herbe d'une perle liquide"
    l talk1"À ce moment propice à la fuite des amants, nous franchirons à la dérobée les portes d'Athènes"
    show H BaseRaisedNeutral
    show LN happyBase
    show bg ext_thesee_night with disShortest
    m neutralSmile"Et dans ce bois où souvent vous et moi nous aimions nous étendre sur un fragile tapis de primevères, vidant nos coeurs de leurs charmants secrets, nous nous retrouverons [l] et moi"
    m resolSmile"Et détournant nos regards d'Athènes, nous partirons en quête d'amis inconnus et de société nouvelle"
    show H BaseRaisedSlightsmile
    m sadTalk"Adieu, chère compagne de mes jeux, prie pour nous et qu'une chance favorable te donne ton [d]!"
    show M BlushConUwu at flip
    show LN uwu
    m BlushConUwu"Tiens parole, [l], jusqu'à demain à la nuit noire nos regards affamés doivent se priver de la nourriture des amoureux"
    l blushFlirt"Je tiendrai parole, mon [m]." 
    show H WideRaisedNeutral
    l uwu"Adieu, [h], que [d] raffole autant de vous que vous de lui!"
    show LN at flip
    hide LN LN with easeoutleft
    hide M M with easeoutleft
    "Il ne reste plus qu'[h], seule avec ses pensées"
    show H WideNeutralNeutral at center:
        yalign 0.15
    with ease
    h WideRaisedOpentalk"Commme certains sont plus heureux que d'autres! A Athènes, je passe pour être aussi belle qu'[m]. Mais à quoi bon, si [d] n'est pas de cet avis?"
    h WideRaisedSadtalk"Il ne veut pas admettre ce que tous reconnaissent, sauf lui... et tandis qu'il se fourvoie en languissant pour les yeux d'[m], moi je fais de même, en m'extasiant sur ses qualités"
    h WideNeutralSadtalk"L'amour a le pouvoir de conférer noblesse et beauté aux choses viles et ordinaires qui n'ont aucune valeur."
    h WideNeutralOpentalk"L'amour ne voit pas avec les yeux, mais avec l'âme.\nAussi représente-t-on aveugle le Cupidon ailé."
    h WideFrownOpentalk"Mais l'âme de l'amour n'a pas un grain de jugeote; des ailes, mais point d'yeux, c'est l'image même d'une étourderie galopante."
    h BaseRaisedSadtalk"On dit de l'amour que c'est un enfant, parce qu'il se trompe si souvent dans son choix"
    h BaseFrownOpentalk"Et comme les gamins espiègles qui jouent à se parjurer, le jeune Amour en tous lieux se parjure"
    h NarrowFrownOpentalk"Car avant de regarder les yeux d'[m], [d] jurait plus dru que grêle qu'il était à moi seule"
    h NarrowRaisedSadtalk"Mais dès qu'il sentit la chaleur d'[m], sa foi s'est dissoute, et sa grêle de serments s'est mise à fondre"
    show H NarrowRaisedDownturned
    menu:
        "Lui révéler la fuite des amants":
            show H BaseNeutralOpentalk
            jump scene2_ending
        "{choice_tag} Garder le secret d'[m]":
            jump alt1_scene1

    label scene2_ending:
        $ persistent.seconplaytext = True
        show bg ext_thesee_dark with dis
        h BaseNeutralOpentalk"Je vais lui révéler la fuite de la belle [m], pour qu'il la suive demain soir dans le bois. Si ma complicité me vaut sa reconnaissance, je l'aurai chèrement payée"
        h BlushBaseNeutralSadtalk"Mais en l'accompagnant là-bas, puis en revenant avec lui, je veux enrichir ma douleur"
        hide H BlushBaseRaisedNeutral with easeoutright
        window hide
        jump scene3