label scene5:
    p puck "..."
    o happy "Voyageur, tu es le bienvenu, as-tu la fleur?"
    show puck puck at right:
        yalign 0.15
    with ease
    p happy "Oui, la voici"
    o happy "Donne-la moi, je t'en prie"
    o oberon "Je connais un tertre où fleurit le thym sauvage... c'est là que [t] s'endort un moment la nuit."
    o snarky "J'enduirai ses yeux du suc de cette plante et lui insuflferai d'horribles caprices"
    o oberon "Prends-en un peu et va fouiller ce bosquet."
    o sad "Une charmante fille d'Athènes s'est éprise d'un jeune homme qui la dédaigne"
    o snarky "Frottes-en ses yeux, mais arrange-toi pour que le plus proche objet qui tombe sous son regard soit cette jeune fille"
    o oberon "Tu reconnaîtras l'homme à son habit d'Athénien."
    show oberon snarky
    show bg forest_clearing_black with dis
    o snarky "Aie bien soin qu'il devienne plus amoureux d'elle qu'elle ne l'est de lui, et viens me retrouver ici avant le premier chant du coq"
    p snarky "Soyez tranquille, monseigneur, votre serviteur y pourvoira"
    hide puck snarky with easeoutright
    hide oberon oberon with easeoutleft
    "Ainsi, [p] s'en va suivre les ordres de son maître.\nEt [o] presse la fleur sur les paupières de [t]"
    scene bg forest_black with Dissolve(1.0)
    jump scene6