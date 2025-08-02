label scene7:
    show bg forest_helena with Dissolve(1.0)
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
    show H BaseRaisedSquirm at center:
        yalign 0.15
        xalign 0.65
    with ease
    h WideNeutralOpentalk"Mais qui est là?"
    show H WideRaisedNeutral at right, dh with ease
    h WideRaisedSadtalk"[l]! Etendu sur le sol." 
    h WideNeutralOpentalk"Est-il mort ou endormi?\nJe ne vois ni sang, ni blessure..."
    show H WideNeutralNeutral at center:
        xalign 0.65
    with ease
    h BaseNeutralHappytalk"Si tu es en vie, [l], réveille-toi mon bon ami!"
    show H BaseNeutralNeutral
    jump scene8