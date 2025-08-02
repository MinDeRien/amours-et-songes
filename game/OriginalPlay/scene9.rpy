label scene9:
    scene bg forest_clearing_night3 with fade
    "Dans leur clairière, [o] et [p] s'entretiennent"
    window show
    show oberon snarky at left:
        yalign 0.15
    show puck happy at right: 
        yalign 0.15
    with easeinbottom
    o snarky"Je me demande si [t] s'est réveillée et ce qui tout d'abord s'est offert à sa vue, qu'elle doit aimer à la folie"
    p happy "Ma maîtresse est tombée amoureuse d'un monstre"
    p awkward "Des acteurs venus d'Athènes ont choisi ce bois pour y répéter leur pièce.\nIls prétendent jouer la tragique histoire de Thisbé et Pyrame"
    p happy "Mais c'est leur jeu, la tragédie, je ne pouvais pas les laisser continuer ainsi."
    p snarky "Aussi ais-je fixé sur un acteur la caboche d'un âne"
    p happy"L'idiot a constaté sa transformation avec grands cris, si bien que ses compagnons ont fuit d'épouvante"
    p snarky"A ce moment-là, [t] s'est réveillée pour aussitôt s'amouracher d'un âne"
    o happy"Cela se présente encore mieux que je n'aurais pu l'imaginer! Mais as-tu humecté les yeux de l'Athénien avec le philtre d'amour, comme je t'en avais chargé?"
    p happy "C'est aussi affaire réglée: Je l'ai surpris dans son sommeil, l'Athénienne à son côté, en sorte qu'il devra forcément la voir à son réveil"
    "Un bruit se fait entendre, non loin. Des gens approchent"
    show oberon surprise at left,dh
    show puck worry at right,dh
    with ease
    o surprise "Ne bouge pas; voici notre Athénien"
    p worry "C'est bien la femme, mais non pas l'homme"
    "[o] et [p] se fondent dans les ombres..."
    hide oberon 
    hide puck
    with easeoutbottom
    jump scene10