label scene15:
    # WEDDING PLAY
    show bg church_day with Dissolve(1.0)
    "Ainsi, nos amoureux se retrouvent au temple..."
    
    show LN LN at left, lh:
        xalign -0.21
    show M BlushneutralUwu at left, lh:
        xalign -0.08
    show DC BaseRaisedSlightsmile at left, lh:
        xalign 0.27
    show H behind M
    show DC behind H
    show H BaseNeutralSlightsmile at left, lh:
        xalign 0.12
    with easeinleft
    show DC BlushNarrowRaisedSlightsmile
    show LN blushFlirt
    th snarky"Voici venir les amoureux, pleins de bonheur et de gaieté!"
    show DC BaseRaisedSmile
    show H BaseRaisedUwu
    show LN happySmile
    th thesee"Soyez joyeux, gentils amis, que l'allégresse et la fraîcheur des jours d'amour accompagnent vos coeurs"
    show M M
    show bg church_afternoon with disShortest
    "Ainsi, après cérémonies, célébrations et représentations, nos amoureux furent mariés"
    hide M 
    hide DC 
    hide LN
    hide H 
    with easeoutleft
    "Dans les chants et les rires, les rires et les danses, les danses et les jeux"
    "A qui aura su observer, ce détail n'aura pas échappé"
    show bg church_night_light with disShorter
    "Au départ des invités un petit lutin, oreilles dressées"
    "Se fraie un chemin - Caché, caché!"
    "Pour nous chuchoter cet épilogue bien mérité"
    jump scene16