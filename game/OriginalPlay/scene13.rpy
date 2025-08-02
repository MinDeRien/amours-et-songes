label scene13:
    show bg forest_clearing_black with Dissolve(1.0)
    hide oberon with easeoutbottom
    "Sur les ordres de son maître, [p] épuise [l] et [d] en les semant l'un après l'autre dans la forêt"
    "Imitant leurs voix, [p] les fait courir, encore et encore, en quête de celui que l'autre cherche à tuer"
    show bg forest_black with Dissolve(0.5)
    "Après un temps, les rivaux, exténués, sont perdus dans le noir..."
    show LC fBase at center with easeinleft
    lc fBase"Il va devant moi en me défiant toujours, mais quand j'arrive là où il m'appelle, il est parti"
    show LC at right with ease
    lc fOpen"Le manant a le pied beaucoup plus agile que moi, je le suis rapidement, mais il s'enfuit encore plus vite"
    show LC at left with ease
    lc wPout"Et me voici engagé dans un chemin noir et raboteux. Je vais me reposer ici."
    show LC at dh with ease
    lc wBase"Viens, toi, aimable jour, car dès que tu m'auras montré ta lueur grise, je trouverai [d] et me vengerai de cet affront"
    hide LC with easeoutbottom
    "[l] s'endort. Entre [d]. Dans le noir, il ne voit pas [l]"

    show DC BaseFrownDown at right with easeinright
    dc BaseFrownTalkscowl"Tu me le paieras cher si jamais j'aperçois ton visage au jour!"
    dc WideRaisedDown"La fatigue m'oblige à mesurer de toute ma longueur ce lit glacé"
    show DC at dh with ease
    dc BaseFrownOpen"Mais attends-toi à recevoir ma visite à l'approche du jour"
    show DC BaseFrownDown
    hide DC with easeoutbottom
    "[d] s'étend et s'endort"
    "[h] Rentre, tâtonnant dans le noir"
    show H WideRaisedDownturned at center with easeinleft
    h BaseRaisedOpentalk"Ô accablante nuit; Ô morne et longue nuit; Abrège tes heures!"
    show H at right with ease
    h NarrowRaisedOpentalk"Que la lumière de l'Orient me réconforte pour qu'au jour je regagne Athènes, loin de ceux qui détestent ma triste compagnie"
    show H at dh with ease
    h BaseRaisedSadtalk"Et toi, sommeil, qui parfois ferme l'oeil à le douleur, viens m'enlever un instant à moi-même"
    hide H with easeoutbottom
    "[h] s'endort, non loin de [d]"

    show puck puck at center with easeinleft
    "Rentre [p]"
    
    p question"Trois seulement? Une de plus pour qu'il n'y ait pas de surplus!"
    p worry"Elle s'en vient triste et geignarde"
    p snarky"Cupidon est un beau fripon"
    p happy"Qui ôte aux femmes la raison"
    hide puck with easeoutbottom
    "[m] entre"
    show M sadPout at left with easeinleft
    m sadPout"Jamais si fatiguée, jamais si malheureuse"
    m sadCry"Trempée par la rosée, déchirée par les ronces, je ne puis me traîner ni avancer d'un pas"
    m sadTalk"Mes jambes ne peuvent suivre le train de mes désirs"
    show M at dh with ease
    m sadOpen"Je vais me reposer ici jusqu'au lever du jour"
    m conSquirm"Que les dieux protègent [l] si ils veulent se battre!"
    hide M with easeoutbottom
    "[m] s'étend et s'endort non loin de [l]"

    show puck puck at center with easeinbottom
    
    p question"Sur le sol dors profond"
    show puck at left, dh with ease
    p happy"Moi, l'aède, j'ai remède"
    p snarky"Pour ton oeil en grand deuil"

    "[p] exprime le suc d'une herbe sur les yeux de [l]"
    show puck at left with ease
    p snarky"Lorsque tu te réveilleras, sache que pour ta grande joie"
    p happy"L'oeil de la belle trouveras, qui la première te troubla"
    p puck"Et le proverbe bien connu: A chaque homme selon son dû"
    p snarky"Montrera le bout de l'oreille à ton réveil"
    p puck"Jacques aura sa Jacqueline, le fermier aura sa divine jument"
    p happy"Tout sera mieux qu'avant au pays des amants"

    "[p] s'éclipse de la scène, laissant les quatre dormir..."
    hide puck with easeoutleft
    jump scene14