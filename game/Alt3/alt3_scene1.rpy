label alt3_scene1:
    show puck puck at right,dh with ease
    "[p] regarde [l] dormir"
    show puck puck at right:
        yalign 0.15
    with ease
    p angry "Eh bien, rustaud, tu ne mérites de connaître ni l'amour, ni la joie" 
    p happy "Mais que cette fille à son réveil puisse te rendre la pareille"
    p snarky "Et moi parti, oublie-la. Je rejoins [o], mon roi"
    hide puck with easeoutright
    jump alt3_scene2

label alt3_scene2:
    show bg forest_black with Dissolve(1.0)
    window show
    "[p] s'en va, entrent [d] et [h]"
    show DD WideFrownDown at center:
        yalign 0.15
    show H BlushBaseRaisedSquirm at center:
        yalign 0.15
        xalign 0.75
    with easeinright
    h BlushBaseRaisedOpentalk"Arrête, cher [d], même si tu dois me tuer"
    show DD NarrowFrownTalkscowl at center:
        xalign 0.3
    with ease
    show H BlushBaseRaisedNeutral
    d NarrowFrownTalkscowl2"Va-t'en, je te l'ordonne et ne me hante plus!"
    show DD NarrowFrownNeutral
    show H BlushNarrowRaisedDownturned at center:
        xalign 0.65
    with ease
    show DD BaseFrownNeutral
    h BlushNarrowRaisedOpentalk"Oh je t'en prie, ne me laisse pas dans cette obscurité!"
    show H WideRaisedDownturned
    d WideFrownOpen"Reste ou prends garde! Je veux partir seul"
    show DD BaseFrownSquirm
    hide DD with easeoutleft
    show H NarrowRaisedDownturned at center:
        xalign 0.5
    with ease
    "[d] disparaît dans le bois"

    h NarrowRaisedSadtalk"Cette folle poursuite m'a fait perdre le souffle.\nPlus je le suppie et moins il me fait grâce"
    h NarrowRaisedOpentalk"Où qu'elle se trouve elle est heureuse, [m], avec ses yeux attirants et enchanteurs... Qu'est-ce qui les rend si brillants?"
    h WideRaisedSadtalk"Non pas des larmes amères, car mes yeux en sont bien plus souvent baignés que les siens"
    h WideRaisedOpentalk"Non je suis plus laide qu'une ourse... quel miroir trompeur m'a poussée à comparer mes yeux aux yeux étoilés d'[m]?"
        # rentre à Athènes // reste dans le bois
        # note que ce choix influence si héléna est témoin de la suite...
    show H NarrowRaisedSquirm
    menu: 
        "Vraiment, je ferais mieux de rentrer":
            $ helena_home = True
            "Le coeur lourd, [h] prend la direction d'Athènes"
            hide H with superslowereaseoutright
        "Mon coeur refuse de l'abandonner":
            $ helena_home = False
            "Suivant son coeur, [h] suit [d]. Discrètement, pour ne pas le fâcher."
            hide H with slowereaseoutleft

    jump alt3_scene3