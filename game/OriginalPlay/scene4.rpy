label scene4:
    show oberon surprise
    o surprise"Mais qui vient là?" 
    show oberon at dh with ease
    o snarky "Étant invisible, je m'en vais surprendre leur entretien"
    hide oberon with easeoutbottom
    "[o] se cache. Entre [d], suivi par [h]"
    show DD DD at center:
        yalign 0.15
    show H H at left:
        yalign 0.15
    with easeinleft
    d BaseFrownOpen"Je ne t'aime pas, ne me poursuis donc pas. Où est [l], où est la belle [m]?"
    d WideFrownDown"Je tuerai l'un comme l'autre me tue"
    d WideFrownTalkscowl"Tu m'as dit qu'ils s'étaient enfuis vers ce bois, et me voilà aux abois dans ce bois, cherchant vainement mon [m]"
    d BaseFrownTalkscowl2"Vas-t'en, décampe, et cesse de me suivre!"
    show DD BaseFrownDown
    show H at left:
        xalign 0.15
        yalign 0.15
    with ease
    h BaseRaisedOpentalk"C'est vous qui m'attirez, aimant au coeur dur; et pourtant, que parlez-vous de tirer un fer pour me tuer?"
    show DD BlushBaseFrownSquirm
    h BaseRaisedSadtalk"Mon coeur est franc comme l'acier: que cesse votre pouvoir d'attraction, et je n'aurai plus le pouvoir de vous suivre"
    show H NarrowRaisedDownturned
    show DD at center:
        xalign 0.6
        yalign 0.15
    with ease
    d BlushBaseFrownOpen"Est-ce moi qui vous encourage, moi qui vous enjôle? Bien au contraire, je vous déclare tout net que je ne vous aime pas, que je ne peux vous aimer"
    show H at left:
        xalign 0.25
        yalign 0.15
    with ease
    show DD BaseFrownDown
    h BlushNarrowRaisedSadtalk "Et moi je vous en aime d'avantage. Je suis votre épagneul: plus vous me battrez, et plus je vous cajolerai"
    h BlushWideRaisedOpentalk"Traitez-moi seulement comme votre épagneul: repoussez-moi, frappez-moi, méprisez-moi, abandonnez-moi"
    show H BlushBaseRaisedHappytalk at left:
        xalign 0.3
    with ease
    h BlushBaseRaisedHappytalk "Mais laissez-moi au moins vous suivre, tout indigne que je suis"
    show H BlushNarrowRaisedHappytalk at left:
        xalign 0.35
    with ease
    h BlushNarrowRaisedHappytalk"Quelle plus humble place puis-je implorer dans votre amour - place que j'estime hautement, pourtant - que de me voir traitée par vous comme votre chien?"
    show DD at center:
        xalign 0.78
        yalign 0.15
    with ease
    show H BlushNarrowRaisedSquirm
    d NarrowFrownOpen"N'allume pas trop la haine que je te porte: rien que de te voir, ça me fait mal au coeur"
    show H WideRaisedSquirm at left:
        xalign 0.45
    with ease
    h WideRaisedSquirm "Et moi, ça me fait mal au coeur de ne pas vous voir"
    show DD NarrowFrownDown
    show DD at center:
        xalign 0.80
    with ease
    show H BlushWideRaisedDownturned
    d NarrowFrownTalkscowl"C'est pas trop compromette votre pudeur que de quitter la ville et vous livrer aux mains d'un homme qui ne vous aime pas"
    d NarrowFrownTalkscowl2"C'est trop faire confiance à la nuit propice, à cet endroit désert et de mauvais conseil pour le précieux trésor de votre virginité"
    show H at left:
        xalign 0.55
    with ease
    h BlushWideRaisedOpentalk"Votre vertu est ma sauvegarde: il ne fait plus nuit quand je vois votre visage, je ne crois donc pas me trouver dans la nuit"
    h BaseRaisedHappytalk"Et il y a dans ce bois quantité de monde, puisque vous êtes pour moi le monde entier"
    h BlushNarrowRaisedHappytalk"Qui pourrait dire que je suis seule, quand le monde entier est là qui me regarde?"
    show H BlushWideRaisedSlightsmile
    show DD at center:
        xalign 0.85
    with ease
    d NarrowFrownLaugh"Je vais m'enfuir loin de toi et me cacher dans les fourrés en t'abandonnant à la merci des bêtes féroces"
    show H BlushNarrowFrownSquirm
    show H at left:
        xalign 0.35
    with ease
    h NarrowFrownSadtalk"La bête la plus féroce n'a pas un coeur comme le votre!\nPartez quand vous voudrez, la légende sera renversée"
    h NarrowRaisedSadtalk"Apollon s'enfuit poursuivi par Daphné; la colombe court après le griffon,\nla biche inoffensive s'élance sur le tigre"
    h BaseNeutralSadtalk"Course vaine que celle où la lâcheté poursuit le courage qui se sauve"
    show H BaseNeutralSquirm
    show DD at center:
        xalign 0.65
    with ease
    d WideFrownTalkscowl"Je ne discuterai pas plus longtemps avec toi!" 
    show DD WideFrownOpen at center:
        xalign 0.90
        xzoom -1
    with ease
    show H BlushBaseFrownDownturned
    d NarrowFrownOpen"Laisse-moi partir, et si tu me suis, sois sûre que je te ferai outrage dans ce bois"
    hide DD with easeoutright
    show H at left:
        xalign 0.75
    with ease
    h BaseFrownSadtalk"Hé, ne me fais-tu pas outrage au temple, à la ville, à la campagne?\nFi, [d], vos offenses jettent l'opprobre sur mon sexe"
    show H at left:
        xalign 0.60
    with ease
    h NarrowRaisedOpentalk"Nous ne pouvons, comme les hommes, nous battre par amour"
    h NarrowRaisedSadtalk"Nous devons être courtisées, mais non pas courtiser nous-mêmes"

    menu:
        "Le suivre, quitte à en mourir":
            jump scene4_ending
        "{choice_tag} A quoi bon le suivre? Il ne m'aimera jamais":
            jump alt2_scene1
    
    label scene4_ending:
        h BlushBaseRaisedSadtalk"Je te suivrai, et je ferai un ciel de mon enfer en périssant de la main que j'adore"
        hide H with easeoutright

        show oberon oberon at center,dh with easeinbottom
        "[o], de sa cachette, regarde [h] s'éloigner"
        show oberon oberon at center with ease
        o sad "Au revoir, nymphe!"
        show puck puck at right, dh with easeinright
        o snarky "Avant qu'il ait quitté ce bosquet, c'est toi qui le fuiras et lui qui recherchera ton amour"
        jump scene5