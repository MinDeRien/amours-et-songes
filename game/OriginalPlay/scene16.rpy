label scene16:
    # EPILOGUE PLAY
    show bg commercial_area_night_light with Dissolve(1.0)
    show puck puck at center with easeinbottom
    p "{i}If we shadows have offended, Think but this, and all is mended{/i}\n{size=-7}Si nous les ombres que nous sommes vous avons un peu outragés,\nDites-vous pour tout arranger{/size}"
    p happy"{i}That you have but slumbred here, While these visions did appear{/i}\n{size=-7}Que vous venez de faire un somme avec des rêves partagés{/size}"
    show puck at center:
        xalign 0.55
    with ease
    p puck"{i}And this weak and idle theme, no more yielding but a dream{/i}\n{size=-7}Ce thème faible et qui s'allonge n'a d'autre rendement qu'un songe{/size}"
    p worry"{i}Gentles, do not reprehend. If you pardon, we will mend{/i}\n{size=-7}Pardon, ne nous attrapez pas, nous ferons mieux une autre fois{/size}"
    show puck at center:
        xalign 0.45
    with ease
    p question"{i}And, as I am an honest Puck, If we have unearned luck{/i}\n{size=-7}Aussi vrai que Puck est mon nom, si cette chance nous avons{/size}"
    p awkward"{i}Now to 'scape the serpent's tongue, We will make amends, ere long:{/i}\n{size=-7}D'éviter vos coups de sifflet, vite nous nous amenderons{/size}" 
    p snarky"{i}Else the Puck a liar call.{/i}\n{size=-7}Ou Puck n'est qu'un menteur fieffé{/size}"
    show puck at center with ease
    p puck"{i}So, good night unto you all.{/i}\n{size=-7}Sur ce, à vous tous bonne nuit.{/size}"
    p happy"{i}Give me your hands, if we be friends:{/i}\n{size=-7}Que vos mains prennent leur essor si vraiment nous sommes amis{/size}"
    p puck"{i}And Robin shall restore amends.{/i}\n{size=-7}Robin réparera ses torts.{/size}"
    hide puck with easeoutbottom
    window hide
    show bg stage2 with Dissolve(2.0)
    centered "{size=128}{font=PlaywriteIN-Regular.ttf}Fin{/font}{/size}"
    pause 1.0
    return