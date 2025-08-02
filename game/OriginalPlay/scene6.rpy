label scene6:
    "Dans le bois, [l] et [m] sont épuisés et perdus..."
    show bg forest_night with Dissolve(1.0)
    window show
    show LN LN at center:
        yalign 0.15
        xalign 0.6
    show M sadSquirm at left:
        yalign 0.15
        xalign 0.2
    with easeinleft
    l worryOpen"Vous défaillez mon bel amour, à force d'errer dans ce bois"
    l worryEarnest"A vrai dire, je ne retrouve plus notre chemin"
    l worryBase"Voulez-vous, [m], que nous nous reposions en attendant le jour réconfortant?"
    m conOpen"Oui, [l]. Cherchez un endroit où vous étendre...\nMoi, je reposerai ma tête sur ce tertre"
    show LN LN at center:
        yalign 0.15
        xalign 0.40
    with ease
    l happyBase"Qu'un même gazon nous serve d'oreiller;\nUn seul coeur, un seul lit; deux âmes et même foi"
    show M BlushSadSquirm at left:
        xalign 0.18
    with ease
    m BlushSadTalk"Non, mon bon [l], ne vous allongez pas si près de moi;\nEcartez-vous encore un peu, pour l'amour de moi"
    l worryEarnest"Oh, chère, comprenez ma pensée innocente;\nL'amour doit être l'interprète du langage amoureux"
    l blushFlirt"Je voulais dire que mon coeur est si bien lié au vôtre que tous les deux n'en font qu'un; ce sont deux âmes enchaînées par serment, deux âmes et même foi"
    l blushFrown"Ne me refusez donc pas une place où m'allonger à vôtre côté;\nA m'étendre ainsi, [m], je n'en suis pas moins tendre."
    m BlushSadSquiggly"[l] joue sur les mots fort joliment. Maudits soient mon orgueil et mes manières si j'ai jamais douté de mon tendre [l]"
    m BlushConTalk"Mais, gentil ami, par amour de moi et par courtoisie, allonge-toi un peu plus loin, comme le veut l'humaine pudeur"
    show M BlushResolBase at left:
        xalign -0.01
    with ease
    m BlushConSquig"Il convient de mettre quelque distance entre un vertueux jeune homme et une jeune fille"
    m BlushConUwu"Ecarte-toi donc et bonne nuit, tendre ami; puisse ton amour durer aussi longtemps que ta précieuse vie"
    show LN blushSmirkN at center:
        xalign 0.60
        yalign 0.15
    with ease
    l blushSmirkN"Et je réponds: ainsi soit-il à une si charmante prière. Que je cesse de vivre si je cesse detre loyal"
    show LN blushSmirkH at center:
        xalign 1.15
        yalign 0.15
    with ease
    l blushSmirkH"Voici mon lit: que le sommeil t'accorde son plus profond repos"
    m BlushResolUwu"Qu'une moitié de ce souhait aille fermer les yeux de qui l'a exprimé"
    hide LN blushSmirkH
    hide M M 
    with slowereaseoutbottom

    show bg forest_sleep with Dissolve(1.0)
    window show
    "[m] et [l] s'endorment. [p] entre"
    show puck awkward at center:
        yalign 0.15
    with easeinright
    p awkward "J'ai couru la forêt en vain, sans rencontrer un Athénien sur les yeux de qui éprouver l'amoureux pouvoir de ma fleur"
    p question "Nuit, silence..." 
    show puck happy at right, dh with ease
    p happy "Mais je le tiens! Il porte un habit d'Athénien!"
    p angry "C'est bien lui qui envoya paître cette Athénienne dit mon maître"
    show puck worry at center,dh with ease
    p worry "Et la voici dormant profond dans cette boue, tout de son long"
    p puck "Ame jolie qui ne voulut s'allonger près d'un malautru"
    menu:
        "Suivre les ordres d'[o]":
            jump scene6_ending
        "{choice_tag} Désobéir":
            jump alt3_scene1
    label scene6_ending:
        show puck puck at right,dh with ease
        "[p] humecte de la fleur les paupières de [l]"
        show puck puck at right:
            yalign 0.15
        with ease
        p angry "Eh bien, rustaud, sur tes deux yeux j'étale un charme impérieux." 
        p happy "Et que l'amour à ton réveil de tes yeux chasse le sommeil"
        p snarky "Et moi parti, réveille-toi. Je rejoins [o], mon roi"
        hide puck with easeoutright
        jump scene7