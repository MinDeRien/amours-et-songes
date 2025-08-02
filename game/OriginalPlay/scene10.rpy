label scene10:
    scene bg forest_clearing_night3
    "[d] et [m] entrent dans la clairière"
    show M conPout at center with easeinright
    show DD BaseRaisedDown at right with easeinright
    d BaseRaisedTalkscowl"Ah, pourquoi repousser celui qui vous aime tant? Gardez vos paroles cruelles pour votre cruel ennemi"
    show DD BaseRaisedDown
    m conOpen"Je ne fais pour l'instant que te gronder. Mais je devrais te traiter plus mal car, j'en ai peur, tu m'as donné des raisons de te maudire"
    m conScowl"Si il est vrai que tu as tué [l] dans son sommeil, achève de sombrer dans l'abîme en me tuant aussi"
    m conTalk"Le soleil n'était pas plus fidèle au jour qu'il ne l'était à moi: eût-il abandonné [m] endormie?"
    show DD BaseRaisedSquirm
    m sadPout"Je croirais aussi bien qu'on peut percer le globe compact et que la lune, en traversant le centre, peut aller éclipser en plein midi son frère aux antipodes"
    m sadCry"Il faut que tu l'aies tué, cet air sinistre et criminel est bien celui d'un assassin"
    d BaseRaisedTalkscowl2"Non, d'un assassiné, je dois en avoir l'air, car j'ai le coeur percé par ton inflexible cruauté"
    d WideRaisedOpen"Et pourtant, toi, l'assassin, tu as l'air aussi radieuse et éclatante que Vénus, là-haut, dans sa sphère luisante"
    show DD WideRaisedSquirm
    m sadOpen"Quel rapport cela a-t-il avec mon [l]? Où est-il? Ah, mon bon [d], veux-tu me le rendre?"
    show DD WideFrownDown
    d WideFrownTalk"Je donnerais plutôt sa carcasse à ma meute"
    m neutralAngry"Arrière, chien, arrière, sale bête! Tu me fais franchir les bornes de la patience qui sied à une jeune fille!"
    show DD BaseFrownDown
    m neutralTalk1"Tu l'as donc tué? Cesse désormais d'appartenir au genre humain!"
    m painedTalk"Ah, dis la vérité, dis la vérité pour l'amour de moi. Aurais-tu osé le regarder quand il était éveillé? L'as-tu tué dans son sommeil?"
    show DD BaseFrownNeutral
    m nTalk"Ô courageux exploit! Un serpent, un vipère n'en feraient-ils autant?\nUne vipère l'a fait; oui, toi, serpent"
    show DD BaseNeutralNeutral
    m nScowl"Jamais vipère ne piqua avec une langue plus double que la tienne"
    show DD BaseRaisedNeutral
    d BaseRaisedOpen"Tu échauffes ta colère sur une méprise, je ne suis pas coupable d'avoir versé le sang de [l]. D'ailleurs il n'est pas mort, que je sache"
    show DD BaseRaisedNeutral
    m painedTalk"Dis-moi alors qu'il va bien, je t'en prie"
    d NarrowFrownLaugh"Et si je pouvais le dire, qu'obtiendrais-je en échange?"
    show DD NarrowFrownNeutral
    m resolAngry"Le privilège de ne plus jamais me revoir. Et sur ce, je vais fuir ta présence détestée; ne me revois plus, qu'il soit vivant ou mort"
    show DD NarrowNeutralNeutral
    hide M with easeoutleft
    "[m] se sauve"
    show DD BaseNeutralNeutral at center with ease
    d BaseNeutralDown"A quoi bon la suivre en cette humeur furieuse? Je vais rester ici un moment"
    d BaseRaisedTalkscowl2"Le poids du chagrin s'alourdit de la dette que le sommeil en banqueroute ne lui a pas payée"
    d BaseRaisedSquirm"Si j'attends ici un moment ses offres, peut-être va-t-il me donner un léger acompte"
    hide DD with easeoutbottom
    "[d] s'étend et s'endort"

    scene bg forest_clearing_night3

    "[o] et [p] sortent de leur cachette"
    show oberon angry at left 
    show puck worry at right 
    with easeinbottom
    o angry "Qu'as-tu fait? Tu t'es complètement trompé: tu as déposé le suc d'amour sur les yeux d'un loyal amant!"
    o sullen "Et l'infaillible résultat de ta méprise c'est d'égarer un coeur fidèle et non de guérir un inconstant"
    p worry "Cela confirme le destin qui veut que pour un homme qui tient parole, un million y manquent qui violent serment sur serment"
    o angry "Cours par le bois plus vite que le vent et retrouve-moi [h] d'Athènes." 
    o sad "Elle a le mal d'amour et le teint pâle, car les soupirs d'amour ruinent le jeune sang"
    o oberon "Trouve quelque artifice pour l'amener ici;\nAu moment où elle paraîtra, je charmerai les yeux de celui-ci"
    p worry "Je pars! Je pars! Voyez comme je pars!\nPlus vite que le dard que lance le Tartare!"
    hide puck with easeoutright
    "[p] file, vite, vite, vite..."

    show oberon at center,dh with ease
    "[o] administre le philtre à [d]"

    o happy "O fleur de nuance pourprée que Cupidon a transpercée"
    o oberon "Pénètre au fond de sa prunelle lorsqu'il contemplera sa belle"
    o open "Et qu'elle brille aussi splendide que Vénus dans l'azur limpide"
    o snarky "Mais toute proche, à ton réveil, mon remède aura fait merveille!"
    show oberon at left with ease
    "[p] réapparaît"
    show puck puck at right with easeinright
    p puck "Capitaine de nos lutins, voici [h] qui s'en vient.\nEt le garçon de ma méprise la déclare de bonne prise"
    p snarky "Allons-nous voir des coeurs en fête?\nMon Dieu! Que les mortels sont bêtes!"
    o surprise"Cachons-nous car [d] va se réveiller dans ce bruit"
    show puck at right,dh
    show oberon at left, dh
    with ease
    p happy "A deux pour une ils vont languir: spectacle unique pour en rire.\nVraiment, rien ne me plaît autant que ces absurdes contretemps!"
    hide oberon
    hide puck
    with easeoutbottom
    jump scene11