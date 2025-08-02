label scene3:
    scene bg forest_clearing_black with fade
    "Dans le bois,  [o], roi des elfes, se querelle avec sa bien-aimée, [t], reine des fées..."
    "[o], voulant prendre comme page un enfant sous la protection de [t], voit non seulement sa requête refusée, mais se retrouve en froid avec sa Reine"
    show bg forest_clearing_afternoon with Dissolve(0.8)
    "Leur dispute terminée, [o] cherche l'aide de [p], aussi appelé Robin bon diable, pour se venger de [t]"
    window show
    show oberon oberon at center:
        yalign 0.15
    with easeinleft
    show oberon angry
    show bg forest_clearing_day with disShorter
    o angry"... Tu ne sortiras pas de ce bois que je ne t'aie châtiée pour cet outrage!"
    o angry"Approche, mon gentil Puck"
    show oberon oberon
    show puck happy at right:
        yalign 0.15
    with easeinright
    o oberon"Te souviens-tu du jour où, assis sur la falaise, j'entendis une sirène perchée sur le dos d'un dauphin murmurer une chanson si suave et mélodieuse que le rude Océan en devint courtois"
    o happy"Et que les étoiles fixes bondirent éperdues hors de leur sphère pour mieux écouter la musique de cette fille de la mer?"
    p happy  "Je m'en souviens"
    o surprise"Au même instant je vis, mais tu ne pus le voir, Cupidon armé de pied en cap qui volait contre la froide lune et la terre"
    o open"Il prit pour cible une belle vestale qui trônait à l'Occident et décocha aussi vigoureusement sa flèche d'amour que s'il eût dû percer cent mille coeurs."
    o surprise"Mais je vis la flèche enflammée s'éteindre dans les chastes et humides rayons de la lune, et l'impériale prêtresse, le coeur intact, poursuivit son chemin et sa virginale rêverie"
    o happy"J'ai repéré cependant le point de chute de la flèche de Cupidon." 
    show oberon oberon
    show bg forest_clearing_afternoon with disShortest
    o oberon"Elle est tombée sur une petite fleur d'Occident, naguère d'un blanc de lait, désormais empourprée par cette blessure d'amour. Les jeunes filles l'appellent 'pensée d'amour'"
    show oberon snarky
    o snarky"Vas me cueillir cette fleur que je te montrai un jour. Son suc, déposé sur les paupières de l'homme ou de la femme endormis, les rend éperdument amoureux de la première créature vivant qu'ils aperçoivent"
    o oberon"Vas me chercher cette plante et sois de retour avant que la baleine ait pu nager une seule lieue."
    p happy"En quarante minutes j'enroulerai une ceinture autour de la terre"
    hide puck happy with easeoutright
    o oberon"Une fois muni de cette substance, je guette [t] endormie et verse la liqueur dans ses yeux."
    o snarky"Le premier être vivant qu'elle verra à son réveil, qu'il soit lion, ours, loup ou taureau, singe fureteur ou macaque affairé, elle le poursuivra dans un transport d'amour"
    show oberon open
    show bg forest_clearing_night2 with disShortest
    o open"Et, avant de délivrer sa vue de ce charme, comme je puis le faire par une autre plante, je l'obligerai à me céder son page"
    
    jump scene4