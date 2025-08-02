label colere:
    show bg forest_night_rage with disShortest
    "[d] baisse les yeux. Le monde est couvert d'un voile rouge"
    "Et des tambours de tonnent dans ses oreilles"
    "{i}Je tuerai l'un comme l'autre me tue{/i}"
    "{i}Je tuerai l'un comme l'autre me tue{/i}"
    "{i}Je tuerai l'un comme l'autre me tue{/i}"
    "A chaque battement de son coeur, ses mots lui reviennent en tête"
    "{i}Je tuerai l'un comme l'autre me tue{/i}"
    "{i}Je tuerai l'un comme l'autre me tue{/i}"
    "{i}Je tuerai l'un comme l'autre me tue{/i}"
    "Pourquoi s'arrêter à un seul?"
    "{i}Je tuerai l'un comme l'autre me tue{/i}"
    "{i}Je tuerai l'un comme l'autre me tue{/i}"
    "JE TUERAI LES DEUX!"
    "[d] était presque surpris de trouver son épée dans sa main"
    "Mais le fer agissait comme par lui-même"
    "En un bond, il porta [d] auprès de [l]"
    "En un geste, il s'enfonça dans son coeur"
    "En un instant, [l] n'était plus"
    "Mais ce n'était pas assez"
    "Les tambours sonnaient toujours"
    "Alors [d] se retourna, pour trouver [m]"
    "Elle s'était réveillée, mais ne semblait pas comprendre"
    "L'horreur qui se trouvait devant elle"
    "Pas un cri. Pas un pleur. Seulement le vide"
    "Puis [m] comprit. Elle ne sortirait jamais de ces bois"
    "Son [l] n'était plus là, [d] le lui avait arraché"
    "Son seul espoir était de mourir à ses côtés"
    "Elle vit l'éclat de la lame. Et la sentit percer son flanc"
    "Une fois. Deux fois. Trois fois."
    "Entre chaque coup, [m] pleurait en rampant"
    "Vers son amour, son [l], son amant"
    "Et là, quand il était enfin à portée de bras"
    "L'épée de [d] la transperça"
    "Puis vinrent les coups de pied"
    "Les cris"
    "Le noir"
    "[m] était partie, elle aussi"
    if helena_home:
        jump colere_epilogue
    else:
        jump colere_helena_epilogue

label colere_epilogue:
    show bg plains_afternoon with disShorter
    "[d] disparut"
    "Personne ne sut ce qu'il advint de lui"
    "Certains disaient qu'il avait tenté de partir à la recherche d'[m], et qu'il s'était perdu en chemin"
    "D'autres, que son échec l'avait conduit à se jeter dans le fleuve"
    show bg dungeon_entrance_afternoon with disShorter
    "Et d'autres encore disaient qu'ils l'avaient vu, à peine reconnaissable, à moitié fou"
    "Errer dans la forêt"
    "Parlant à des ombres"
    "Mais ceux qui pensaient l'avoir vu n'avaient pas osé l'approcher"
    "Et à Athènes, pesonne ne cherchait vraiment à savoir"
    show bg dungeon_entrance_night_light with disShorter
    "Quant aux bois, ils gardèrent leur secret"
    "Comme ils gardèrent leurs morts"
    jump colere_ending

label colere_helena_epilogue:
    "Transie d'horreur, [h] vit la rage de [d] le porter"
    "Dans sa folie meurtrière"
    "Elle ne pouvait plus respirer. Elle ne pouvait pas pleurer"
    "Elle ne pouvait rien faire"
    "Pas même fermer les yeux pour bloquer de son regard"
    "L'horreur et le carnage qui prenait place dans le noir"
    "Que ce fut fini, et que [d] partit, hagard, couvert de sang"
    "S'enfoncer dans la forêt, de plus en plus profondément"
    "Dans la mystérieuse lumière rouge qui baignait les amants"
    "Elle s'approcha lentement"
    "Elle toucha les mains de [m]. Le front de [l]"
    "Les arrangeant comme elle pouvait, l'un contre l'autre"
    "En une dernière étreinte, éternelle"
    "Elle offrit pour eux une prière"
    "Une poignée de terre"
    show bg plains_afternoon with disShortest
    "Puis elle rentra"
    "[h] n'avait plus de coeur à briser"
    "Il était resté dans la forêt, avec les amants, à leurs côtés"
    "[h] ne parla jamais. Elle ne pouvait plus parler"
    show bg tombe_afternoon with disShortest
    "De ses mains, elle grava une stèle, qu'elle porta à l'orée de la forêt"
    "Pas de noms. Pas de date."
    "Une simple pierre, avec deux coeurs entrelacés"
    "Elle venait s'y asseoir, parfois"
    "Elle y restait, longtemps, en silence"
    show bg tombe_night_light with disShortest
    "Elle n'attendait plus rien"
    "Elle n'avait plus que le regret"
    "D'avoir exposé les amants et leur secret"
    jump colere_hermia_ending
