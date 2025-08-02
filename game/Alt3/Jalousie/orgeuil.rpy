label orgeuil:
    show bg forest_night_orgeuil with disShortest
    "[d] baisse les yeux"
    "Dans ce silence parfait, quelque chose se brise"
    "Une fissure dans sa poitrine, sèche, sans larmes"
    "Une main glacée étouffe son coeur, une jalousie acide, étouffante"
    "Pourquoi [l]? Pourquoi lui?"
    "Pourquoi celui qui n'a pas poursuivi, pas couru, pas supplié?"
    "Pourquoi ce garçon arrogant aurait ce que lui, [d] avait tant convoité?"
    "Ce qui lui revenait de droit?"
    "N'avait-il pas été approuvé par le père d'[m]?"
    "Elle était sienne, ça allait de soit"
    "Sans y penser, sa main trouva la poignée de son épée"
    "Une sensation familière, pleine de pouvoir, pleine de promesse"
    "[d] s'avança, muscles tendus, les nerfs à vif, le regard brûlant"
    "D'un geste net, il mis fin à [l], et fit couler son sang"
    "Un gémissement, un soupire, puis plus rien"
    "Il avait fait un cadavre de cet Athénien"
    "A ce moment-là, [m] s'éveilla. Vit la scène. Hurla. Pleura"
    "Et se rua vers [l]"
    "[d] la saisit par le bras"
    "La souleva comme une chose, un objet à reprendre"
    "A ramener à Athènes, même contre son gré"
    "Elle se débattit, le frappa, le supplia"
    "Mais il la traîna, insensible à ses pleurs"
    "Loin de son [l], loin de la forêt."
    "Pour [d] c'était clair: elle était à lui, désormais"
    "Qu'elle le veuille ou non, un jour elle l'aimerait"
    if helena_home:
        jump orgeuil_epilogue
    else:
        jump helena_orgeuil_epilogue
    
label helena_orgeuil_epilogue:
    "[h] vit tout, cachée dérrière un arbre"
    "Elle vit [d] approcher, lame à la main, et sentit son coeur se glacer"
    "Elle vit [l] mourir sans comprendre, et [m] hurler de douleur, pleurer, supplier"
    "Et elle vit [d] l'emporter, comme le jouet brisé qu'il ne savait pas aimer"
    "Elle ne fit rien. Paralysée. Ecrasée par l'horreur. Par l'impuissance. Par la douleur."
    "Quand le silence revint, emportant les larmes d'[m], [h] ne pleura pas"
    "Elle offrit une prière pour [l]"
    "Lui ferma les yeux"
    "Et elle marcha. Longtemps. Loin"
    "Pour oublier. Pour survivre"
    show bg lysander_death_afternoon with disShorter
    "[h] ne rentra pas à Athènes. Elle resta dans les bois\nEnterra [l] dans un endroit paisible"
    "Sous une pierre marquée d'un coeur, pour celui d'[m]\nQui était mort aussi, cette nuit-là"
    show bg lysander_death_night_light with disShortest
    "Elle n'avertit personne. Ne dénonça rien. A quoi bon?\nAucune force au monde ne pouvait réunir les amants"
    jump orgeuil_ending_helena

label orgeuil_epilogue:
    show bg plains_afternoon
    "A athènes, [d] fit croire à tous que [l] s'était enfui"
    "Et que [m] avait choisi de revenir avec lui"
    "Pour l'épouser, obéissant à son père, [e]"
    "Personne ne pouvait demander à [m] ce qu'il en était. [m] ne parlait plus."
    "Pour expliquer son mutisme, [d] disait qu'elle avait perdu sa voix"
    "En voyant [l], le lâche, s'enfuir dans les bois"
    show bg reception_room_afternoon with disShortest
    "Dans la maison de [d], [m] errait, muette et pâle"
    "Comme une ombre, enchaînée à la vie, malgré elle, malgré ses cris"
    "Elle s'était retirée de la société. Même [h] ne la voyait plus"
    "[d] quant à lui brillait encore, toujours plus forts"
    "A tous les grands dîners il était là, en grande compagnie"
    show bg reception_room_night_light with disShorter
    "Un homme aimé. Respecté. Remarqué"
    "Et même si sur lui tous les regards se portaient"
    "Personne ne voulait voir le monstre qu'il était."
    jump orgeuil_ending