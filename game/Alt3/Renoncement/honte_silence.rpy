label honte_silence:
    "Il contemple les amants encore un moment"
    "Puis il recule. Un pas. Un autre."
    "Il ne leur laisse ni mot, ni trace"
    "Même pas un son pour troubler leur sommeil"
    "[d] l'a enfin compris: [m] ne lui appartient pas"
    "Et l'amour, ça ne se vole pas"
    "Lui qui voulait posséder, conquérir, abandonner"
    "Il l'avait compris, à présent: il ne savait pas aimer"
    "Tout ce qu'il lui restait à faire, c'était de rentrer"
    if helena_home:
        jump honte_silence_epilogue
    else:
        jump honte_silence_helena

label honte_silence_helena:
    "[d] ne le savait pas, mais [h] l'avait suivi dans les bois"
    "Sans oser se montrer, elle avait pu l'observer"
    "Elle avait vu [d] s'arrêter, figé, face aux amants endormis"
    "Et elle avait retenu son souffle, n'osant pas faire de bruit"
    "Elle s'attendait à des éclats, une crise, et pire encore"
    "Mais elle ne vit rien de tout ça"
    "Elle le vit reculer, lentement"
    "Puis sans un mot, tourner les talons"
    "Elle ne dit rien. Elle ne le suivit pas."
    "Peut-être était-ce de le voir ainsi, à contempler [l] et [m]"
    "Peut-être était-ce la lumière étrange qui lui avait ouvert les yeux"
    "Mais pour la première fois, elle le vit, le vit vraiment"
    "Elle le vit comme un homme, et pas comme une obsession"
    show bg plains_day with disShortest
    "De retour à Athènes, [h] garda pour elle ce qu'elle avait vu"
    "Son amie était partie, mais elle la cherchait du regard, parfois, dans la rue"
    show bg alley_day with disShortest
    "Et un jour, en faisant son marché, c'est [d] que son oeil finit par trouver"
    "Il la regarda aussi. Sans arrogance. Sans amertume. Sans défense"
    "Elle lui sourit, lentement, prudemment"
    "Et il baissa les yeux, presque timidement"
    show bg alley_afternoon with disShortest
    "Puis elle poursuivit sa route avec une pensée"
    "Elle ne l'aimait plus. Elle ne l'avait peut-être jamais aimé"
    jump honte_silence_helena_ending

label honte_silence_epilogue:
    show bg plains_day with disShortest
    "[d] rentra à Athènes sans trahir les amants, sans récit"
    "Il reprit le cours de sa vie, mais sans faire de bruit"
    show bg guild_day with disShortest
    "Un retour à la normale, oui, en partie..."
    "Mais à une différence près:\nQuand on parlait d'amour, [d] se taisait"
    "Lui qui voyait les femmes comme objets à conquérir"
    "Avait compris qu'il les utilisait comme jouets pour nourir"
    "Son envie de posséder, de plaire, puis de fuir"
    "Vers une nouvelle conquète, puis une autre, puis une autre"
    show bg guild_afternoon with disShortest
    "Mais il n'y en aurait plus d'autres, il l'avait décidé"
    "Tant qu'il ne saurait pas à aimer, les femmes, c'était terminé"
    "Une promesse qu'il s'était en forêt, durant une nuit d'été"
    "Jusqu'à la fin de sa vie, elle ne fut jamais brisée"
    jump honte_silence_ending
