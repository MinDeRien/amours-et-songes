label honte_reveil:
    "[d] observe longtemps les amants endormis"
    "Rassemblant son courage dans le calme de la nuit"
    "Le troublant d'une voix douce, son tout premier bruit"
    "Un \"Réveillez-vous\" murmuré juste assez pour les éveiller"
    "[m] ouvre les yeux en premier. Suivie de [l], sur ses gardes, effrayé"
    "[d] lève les mains pour les rassurer: \"Je ne suis pas venu pour vous séparer\""
    "\"J'ai compris. Elle ne m'aime pas. Elle ne m'a jamais aimé\""
    "\"Et ici même, dans cette forêt, je renonce au droit qu'on m'avait donné sur elle\""
    "\"Rentrez  Athènes. Vivez votre amour.\""
    "\"J'aviserai votre père et le Duc. Je ne m'interposerai plus\""
    "Ainsi, [d] quitta la forêt, et sa lumière étrange"
    if helena_home:
        jump honte_reveil_epilogue
    else:
        jump honte_reveil_helena
label honte_reveil_helena: 
    "[h], qui l'avait suivi, l'observait depuis l'ombre, sans faire le moindre bruit"
    "A le voir face aux amants, [h] craignait une explosion, de la rage, du sang"
    "Mais au lieu de tout ça, d'une voix douce, [d] les réveilla"
    "Elle entendit ses mots, livrés sans amertume"
    "Pour ses amis, ils étaient la promesse d'une vie"
    "Et pour elle, à ce moment-là, un mystère opéra"
    "Etait-ce de le voir ainsi? Ou cette étrange lumière, qui éclairait la nuit?"
    "Les fils invisibles qui liaient son coeur à [d] s'étaient rompus"
    "Plus une once d'amertume, et pas de rancune. Mais pas d'amour, non plus"
    "Le constat constaté, [h] se hâta de rentrer"
    "Car bientôt, elle le savait, elle aurait raison de célébrer"
    jump honte_reveil_epilogue 

label honte_reveil_epilogue:
    "[d] rentra à Athènes, et tint sa promesse sitôt arrivé"
    "Libérant [m] de ses choix imposés"
    "[d], le cloître, ou la mort... de l'histoire ancienne"
    "Rentrée avec [l], elle pouvait enfin être sienne"
    "Ainsi donc à Athènes, de nouvelles noces furent célébrées"
    "Plus modestes que celles du Duc, mais si souvent rêvées"
    "[h] y assista, larmes de joies au premier rang"
    "[d], même invité, choisit d'en être absent"
    "Lui qui aimait la conquête, avant de rentrer"
    "Ne poursuivit plus jamais aucune femme, il se l'était juré"
    "Pas tant qu'il n'aurait pas appris à aimer"
    show bg big_house_day with disShortest
    "Et quant à [l] et [m], pour toujours sous leur toit"
    show bg big_house_afternoon with disShorter
    "Régnèrent la tendresse, l'amour et la joie" 
    jump honte_reveil_ending