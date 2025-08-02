label scene14:
    show bg plains_night with Dissolve(0.5)
    show bg plains_night_light with Dissolve(1.0)
    "Le jour se lève sur Athènes et sur les bois"
    show bg plains_afternoon with Dissolve(1.0)
    #transitions plan large lever de soleil
    "Le Duc [th] chasse, accompagné par Hippolyta, sa fiancée, et [e]"
    "Par le fruit du plus grand hasard, le groupe se retrouve à un endroit particulier de la forêt..."    
    show bg forest_afternoon 
    show M M at left:
        xalign 0.15
        yalign 2.18
    show LN LN at left: 
        xalign -0.15
        yalign 2.18
    show DC BaseNeutralNeutral at right: 
        xalign 1.15
        yalign 2.18
    show H H at right:
        xalign 0.95
        yalign 2.18
    with Dissolve(0.5)
    th thesee"... Jamais meute plus harmonieuse ne fut par le cor travaillée ni acclamée, en Crète, à Sparte ni en Thessalie"
    th "Jugez-en vous-même quand vous les entendrez"
    th surprise"Mais tout doux!"
    show M M at left:
        xalign 0.15
        yalign 2.0
    show LN LN at left: 
        xalign -0.15
        yalign 2.0
    show DC BaseNeutralNeutral at right: 
        xalign 1.15
        yalign 2.0
    show H H at right:
        xalign 0.95
        yalign 2.0
    with easeinbottom
    th "Que sont ces nymphes?"
    e surprise"Seigneur! C'est ma fille qui dort là!"
    e egee"Et voici [l]! Et voici [d]! Et voilà [h]!"
    e surprise"L'[h] du vieux Nédar"
    e happy"Je m'émerveille de les voir ici tous ensemble"
    th thesee"Nul doute qu'ils se levèrent de bonne heure pour célébrer les rites de Mai"
    th snarky"Et, connaissant nos intentions, ils s'en vinrent ici rendre honneur à notre cérémonie"
    th surprise"Mais, dites, [e], n'est-ce pas aujourd'hui qu'[m] doit faire connaître son choix?"
    e sad"Oui, monseigneur"
    th snarky"Allez donc dire aux chasseurs de les réveiller aux sons du cor"
    show M BlushConOpen at left,dh:
        xalign 0.15
    show LN LN at left,dh:
        xalign -0.15
    show DC BlushBaseRaisedNeutral at right,dh: 
        xalign 1.15
    show H BlushBaseRaisedNeutral at right,dh:
        xalign 0.95
    with omegafastermove
    "Bruits de cors et cris, et les amants se réveillent en sursaut"
    

    th thesee"Bonjour, les amis. La Saint-Valentin est passée"
    show DC BaseRaisedNeutral
    show H BaseRaisedNeutral
    with disShortest
    th "Ces oiseaux de bois, est-ce aujourd'hui seulement qu'ils décident à s'accoupler?"
    l blushFrown"Pardon, Monseigneur"
    th "Je vous en prie, vous tous, debout!"
    show M BlushConSquig at left:
        xalign 0.15
    show LN at left:
        xalign -0.15
    show DC at right:
        xalign 1.15
    show H at right:
        xalign 0.95
    with ease
    th snarky"Je sais que vous êtes tous deux rivaux et ennemis"
    th surprise"D'où vient en ce monde que cette gentille concorde qui fait que la haine est si loin de la jalousie qu'elle dort à côté de la haine sans craindre la trahison?"
    l worryEarnest"Monseigneur, je vous répondrai dans l'ahurissement d'un homme mi-endormi, mi réveillé"
    l worryOpen"Qui jure pour l'instant ne pas savoir comment il est venu ici"
    show H BaseNeutralNeutral
    l worryTalk1"Mais j'ai de plus en plus l'impression, moi qui voudrais dire toute la vérité, que les choses se sont passées ainsi"
    l resolve"Je suis venu ici avec [m]. Notre dessein était de nous éloigner d'Athènes et de nous mettre hors d'atteinte de la loi athénienne et de ses menaces"
    e surprise"Assez! Assez! Monseigneur nous en avons assez!"
    show LN frown
    e angry"Je réclame les rigueurs de la loi sur sa tête!"
    e snarky"Ils voulaient fuir, ils voulaient, [d], nous frustrer vous et moi!"
    show LN worryBase
    e angry"Vous de votre femme, et moi de mon accord, puisque je vous l'avais accordée pour épouse"
    show H BaseRaisedNeutral
    dc BaseRaisedSlightsmile"Monseigneur, la belle [h] m'avait fait part de leur fuite et de leur projet de venir ici dans ce bois"
    dc WideRaisedNeutral"Et ma fureur les avait suivis et l'amour de la belle [h] me suivait ici à son tour"
    show LN LN
    dc WideRaisedOpen"Mais, Monseigneur, j'ignore par quel sortilège... Car sortilège il y a!-" 
    dc BaseRaisedOpen"Mon amour pour [m] fondit comme de la neige et il m'apparaît maintenant comme un vain colifichet dont, enfant, j'eusse raffolé"
    show H NarrowNeutralUwu
    dc WideRaisedUwu"Et c'est la seule [m] qui est la foi, la vertu de mon coeur, l'objet et le délice de mes yeux"
    dc BlushNarrowNeutralUwu"C'est à elle, Seigneur, que j'étais fiancé avant de connaître [m]"
    show bg forest_day with disShortest
    dc NarrowNeutralUwu"C'est un aliment dont, malade, je ne voulais plus"
    show H NarrowRaisedNeutral
    dc BaseRaisedTalk"Mais la santé m'est revenue, ramenant avec soi mon goût naturel"
    dc WideRaisedSmile"Et maintenant je la désire, je la chéris, je languis après elle qui sera désormais ma seule vérité"
    show H BaseNeutralUwu
    show DC BaseNeutralUwu
    th surprise"Beaux amoureux, voilà une heureuse rencontre; mais nous n'en avais pas fini avec cette histoire"
    show M BlushPainedSmile
    th snarky"[e], je materai votre volonté et tantôt, au temple avec nous-mêmes, ces couples seront unis pour l'éternité"
    show DC BaseNeutralSmile
    
    #  RESOLUTION PLAY
    show M conSheep
    th thesee"Puisque le matin est déjà en lambeaux, nous annulerons nos projets de chasse"
    show M neutralSquiggly
    th "Et en route avec nous pour Athènes!"
    show M neutralSmile
    show H BaseRaisedUwu
    th "Trois plus trois!"
    th snarky"Nous célébrerons une fête en grand cérémonial. Venez, Hippolyta"
    show M M
    "Sortent [th], Hippolyta, [e], et leur suite"

    dc NarrowRaisedTalk"Ces choses semblent petites et indiscernables, comme de très lointaines montagnes qui s'effilochent en nuages"
    m BlushResolBase"Je crois les voir d'un oeil bigle qui dédouble tout devant lui"
    show DC NarrowRaisedUwu
    h BlushNarrowRaisedUwu"Moi aussi, et [d] fait figure pour moi d'un joyeau trouvé qui est à moi et n'est pas à moi"
    dc WideRaisedTalkscowl2"Êtes-vous bien sûrs que nous soyons éveillés? Il me semble que nous dormons encore, que nous rêvons"
    dc WideRaisedTalkscowl"Ne pensez-vous pas que le Duc était là et nous disait de le suivre?"
    show H NarrowRaisedSlightsmile
    m resolOpen"Oui, lui et mon père"
    show DC WideRaisedNeutral
    show M resolBase
    h BaseRaisedSlightsmile"Et Hippolyta"
    l happyBase"Et il nous dit, en effet, de le suivre au temple"
    dc WideRaisedUwu"Alors nous sommes bien réveillés. Suivons-le et, chemin faisant, nous nous raconterons nos rêves"
    hide DC
    hide M
    hide H 
    hide LN 
    with easeoutright
    show bg plains_day with Dissolve(1.0)
    jump scene15