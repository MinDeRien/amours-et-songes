label scene11:
    scene bg forest_clearing_night3
    "[o] et [p] se cachent à nouveau, entre [h] suivie de [l]" 

    show H BaseFrownSquirm at center
    show LE LE at left
    with easeinleft
    le worryPout"Pourquoi vous figurer que c'est par moquerie que je vous fais la cour?\nMépris et moquerie ne s'accompagnent jamais de larmes"
    le worryOpen"Et voyez, je pleure en protestant de mon amour. Et de telles protestations d'amour, nées dans les larmes, témoignent dès leur naissance de leur sincérité"
    show H NarrowFrownSquirm
    le worrySquirm"Comment peuvent-elles vous apparaître comme du mépris quand elles portent le sceau authentique de la bonne foi?"
    h NarrowFrownSadtalk"Vous poussez toujours plus avant votre perfidie.\nQuand la foi tue la foi, oh, l'infernale guerre sainte!"
    h BaseRaisedOpentalk"Ces protestations d'amour sont pour [m]. Voulez-vous donc l'abandonner?"
    show LE worryOpen
    h NarrowRaisedSadtalk"Pesez des serments avec des serments, et vous pèserez le néant"
    show LE worrySquirm
    h NarrowNeutralSadtalk"Vos serments à elle et à moi, mis sur les deux plateaux d'une balance, auront le même poids"
    h WideFrownDownturned"Aussi légers que des fables"
    le worryPout"Je n'avais pas ma raison quand je lui jurais mon amour"
    h BaseFrownSadtalk"Non, ma foi, et vous ne l'avez pas d'avantage maintenant que vous l'abandonnez"
    show H NarrowNeutralDownturned
    le angerFrown"[d] l'aime et il ne vous aime pas"
    "[d] se réveille"
    show DE BlushNarrowRaisedLaugh at right with easeinbottom
    hide LE
    show LC mFrown at left
    de BlushNarrowRaisedTalk"Ô [h], déesse, nymphe, parfaite, divine!"
    show H NarrowRaisedSquirm
    de BlushNarrowRaisedTalkscowl2"A quoi pourrais-je comparer tes yeux, mon amour?\nLe cristal n'est que de la boue"
    show LC mPout
    de BlushWideNeutralSquiggly"Comme elles sont mûres et tentantes tes lèvres, ces deux cerises amoureuses l'une de l'autre!"
    show H NarrowFrownDownturned
    de BlushWideRaisedLaugh"Quand tu lèves la main, la pure et blanche neige glacée des cîmes du Taurus tourne au noir de corbeau comme la balaye le vent d'Est"
    show LC mSquirm
    d BlushWideRaisedUwu"Ah, laisse-moi déposer un baiser sur cette souveraine blancheur virginale, ce sceau de la félicité!"
    h BaseRaisedOpentalk"Ô rage! Ô douleur! Je vois que vous vous êtes tous concertés pour vous jouer de moi"
    h NarrowRaisedDownturned"Si vous étiez honnêtes et courtois, vous ne me feriez pas un tel affront"
    show DE WideRaisedGiddy
    h WideRaisedSquirm"Ne pouvez-vous me haïr, comme je sais que vous le faites, sans vous liguer aussi du fond de l'âme pour me railler?"
    h WideRaisedOpentalk"Si vous étiez des hommes comme vous en avez l'apparence, vous n'en useriez pas ainsi avec une noble dame"
    show DE WideRaisedSquirm
    h WideRaisedSadtalk"Me faire des serments, me jurer votre amour et renchérir sur mes attraits, quand je suis sûre que vous me détestez de tout votre coeur"
    show LC wFrown
    h BaseFrownSadtalk"Vous êtes tous deux rivaux pour [m] et vous rivalisez maintenant pour vous moquer d'[h]"
    h NarrowFrownOpentalk"Joli exploit, héroïque entreprise que de faire venir les larmes aux yeux d'une pauvre fille, avec vos railleries!"
    show DE WideRaisedDown
    h BaseRaisedSquirm"Nul homme de noble race ne voudrait ainsi offenser une jeune fille et ne pousserait à bout une pauvre âme, rien que pour s'amuser"
    lc fScowl"Ne soyez pas méchant, [d]: vous savez bien que je sais que vous aimez [m]"
    show DE WideFrownSquirm
    lc wOpen"Et ici même, avec la meilleure volonté de tout mon coeur, je vous cède tous mes droits à l'amour d'[m]" 
    show H NarrowFrownSquirm
    lc nSmirk"Tandis que vous me léguerez ceux que vous avez sur [h], que j'aime et aimerai jusqu'à ma mort"
    h NarrowFrownSadtalk"Jamais railleurs ne gaspillèrent aussi vainement leur éloquence"
    show DC WideFrownSquirm at right
    hide DE
    show H NarrowRaisedDownturned
    dc BaseFrownTalkscowl2"Garde ton [m], [l], je n'en veux pas.\nSi je l'ai jamais aimée, mon amour s'est envolé"
    show LC fSquirm
    dc BaseRaisedTalk"Mon coeur a voyagé vers elle comme en visite, mais il est maintenant de retour à la maison, chez [h], pour y rester"
    lc mFrown"Ce n'est pas vrai, [h]"
    dc WideRaisedTalkscowl"Ne calomnie pas une foi que tu ignores ou bien tu risques de le payer cher"
    show DC at right:
        xalign 0.90
    with ease
    dc NarrowRaisedLaugh"Regarde, voici venir ton amour"
    show M sadOpen at right:
        xalign 1.21
    with easeinright
    show H BaseRaisedDownturned
    dc NarrowFrownGiddy"C'est elle, ta bien-aimée"
    show LC fBase
    "Hermia rentre et, voyant [l], court à lui"
    show M at left:
        xalign 0.3
    with ease
    show H at center:
        xalign 0.65
    with ease
    m sadTalk"La nuit noire qui prive la vue de son pouvoir, rend l'oreille plus prompte à saisir. Elle affaiblit la vue mais procure à l'ouïe un double dédommagement"
    show DC NarrowNeutralSlightsmile at right with ease
    m sadBase"Ce ne sont pas mes yeux qui t'ont trouvé, [l], mais mon oreille que je remercie de m'avoir guidée vers ta voix"
    show LC fBase at left:
        xalign -0.1
    with ease
    m sadPout"Mais pourquoi m'as-tu quittée si méchamment?"
    lc "Pourquoi serait-il resté, celui que l'amour pressait de partir?"
    show M at left:
        xalign 0.2
    with ease
    m conOpen"Quel amour pouvait presser [l] de s'éloigner de moi?"
    lc mDeranged"L'amour de [l] qui ne lui permettait pas d'attendre..."
    lc hDrool"Belle [h]! Qui rend la nuit plus dorée que ne font là-haut toutes ces paillettes de feu et ces yeux de lumière!"
    show H NarrowRaisedSquirm
    lc mCry"Pourquoi me cherches-tu?"
    lc mTeeth"Ne pouvais-tu comprendre que c'est la haine que je te porte qui m'a fait te quitter ainsi?"
    show H WideRaisedDownturned
    m conScowl"C'est impossible! Vous ne pensez pas ce que vous dites."
    h WideFrownDownturned"Voyez, elle aussi est du complot"
    h WideFrownOpentalk"Je vois bien maintenant qu'ils se sont mis tous les trois d'accord pour jouer à mes dépens cette comédie perfide"
    show H at center:
        xalign 0.55
    with ease
    h WideFrownHappytalk"Méchante [m], fille très ingrate, conspirez-vous, êtes vous liguée avec ces hommes pour me harceler de cette odieuse moquerie?"
    h WideRaisedSadtalk"Ainsi, tous les secrets que nous avons partagés, nos serments fraternels, les heures passées ensemble, alors que nous maudissions le temps au pas pressé qui nous séparait..."
    show LC mSmirk
    h WideRaisedHappytalk"Ah, tout cela est donc oublié? Notre amitié des jours d'école, notre innocence enfantine?"
    show H at center:
        xalign 0.49
    with ease
    h WideRaisedOpentalk"Comme deux habiles fées, [m], nous avons créé avec nos aiguilles la même fleur, au même canevas, assises sur le même coussin, gazouillant à l'unisson la même chanson"
    h BaseRaisedSadtalk"Comme si nos mains, nos flancs, nos voix, nos âmes eussent été confondus"
    show M conPout
    h BaseRaisedSquirm"Nous avons grandi ensemble comme deux cerises jumelles qui semblent séparées, mais sont unies entre elles, deux charmantes baies modelées sur la même tige"
    show LC mFrown
    h BaseRaisedSquirm"Deux corps en apparence mais avec un seul coeur... Même blason portant même écusson, couronnées d'un même cimier et obéissant à un seul seigneur"
    h BaseRaisedSadtalk"Et tu voudrais briser cette vieille amitié en te joignant à ces hommes pour narguer ta pauvre amie?"
    show DC BaseNeutralDown
    h BaseFrownOpentalk"Ce n'est pas amical, ce n'est pas digne d'une jeune fille..."
    h BaseFrownSquirm"Et quoique je sois seule à ressentir l'injure, tout notre sexe est avec moi pour vous la reprocher"
    m conSquirm"Vos paroles me confondent. Je ne vous raille pas"
    m conPout"C'est plutôt vous qui avez l'air de me railler"
    show LC fScowl
    h WideRaisedSadtalk"N'avez-vous pas par moquerie entraîné [l] à me poursuivre et à vanter mes yeux et mon visage?"
    h WideRaisedDownturned"Et engagé [d] votre soupirant (qui tout à l'heure me repoussait du pied!)"
    h WideRaisedOpentalk"A m'appeler déesse, nymphe, divine et rare, précieuse et céleste?"
    h NarrowRaisedSquirm"Pourquoi dit-il cela alors qu'il me déteste?"
    show DC BaseNeutralNeutral
    h NarrowRaisedOpentalk"Et pourquoi [l] rejette-t-il ton amour -qui pèse si lourd dans son coeur- pour m'offrir sa tendresse (par exemple!)"
    show LC fSquirm
    h NarrowRaisedSadtalk"Si ce n'est pas vous qui l'y poussez? S'il n'a pas votre approbation?"
    h NarrowRaisedDownturned"Et si je ne suis pas aussi favorisée que vous, aussi heureuse et pavoisée d'amour"
    show DC BaseRaisedDown
    h NarrowNeutralSadtalk"Mais au contraire, si j'ai le malheur d'aimer sans retour"
    h BaseRaisedSadtalk"Vous devriez me plaindre... et non me mépriser"
    show H BaseRaisedSquirm
    m conOpen"Je ne comprends pas ce que vous voulez dire"
    show H at center: 
        xalign 0.47
    with ease
    h WideFrownDownturned"Oui c'est cela, continuez, prenez votre mine navrée et faites-moi des grimaces quand j'ai le dos tourné"
    show LC wPout
    h WideFrownHappytalk"Faites-vous des clins d'oeil, poussez votre bonne plaisanterie jusqu'au bout, ce jeu bien combiné mérite une chronique!"
    h WideFrownOpentalk"Si vous aviez un peu de pitié, de délicatesse ou seulement de civilité, vous ne me feriez pas jouer cette farce!"
    show H at center:
        xalign 0.58
    with fasterease
    h WideRaisedSquirm"Mais adieu, tout cela est un peu de ma faute"
    show DC NarrowNeutralSquirm
    show LC wOpen
    h NarrowRaisedDownturned"La mort ou l'absence y remédieront promptement"
    show LE BlushHFlirtCreep at left:
        xalign -0.1
    hide LC
    le BlushHFlirtCreep"Reste, douce [h]. Entends ma défense"
    show LE at left: 
        xalign 0.021
    with ease
    le BlushHGiddy"Ma belle [h], mon amour, ma vie, mon âme!"
    show LC hWobble at left:
        xalign 0.021
    hide LE
    h NarrowFrownSquirm"Ah, parfait"
    show LC fBase
    show M at left:
        xalign 0.3
    show LC at left:
        xalign 0.016
    with ease
    show DC NarrowFrownDown
    m painedTalk"Ne te moque pas d'elle ainsi, mon chéri"
    show M at left: 
        xalign 0.25
    show LC at left:
        xalign -0.01
    with ease
    dc BaseFrownOpen"Si elle ne peut te fléchir par ses prières, moi je peux t'y contraindre"
    lc fScowl"Tu ne peux pas plus me contraindre qu'elle ne peut me fléchir; Tes menaces n'ont pas plus de force que tes faibles prières"
    show DC WideFrownDown
    show LE BlushHFlirt at left:
        xalign -0.01
    hide LC
    le BlushHFlirt"Je t'aime, [h], sur ma vie je t'aime"
    le BlushHFlirtCreep"Sur cette vie que je donnerais pour toi, je jure de prouver qu'il ment, celui qui dit que je ne t'aime pas"
    dc WideFrownOpen "Je dis que je t'aime plus qu'il ne saurait."
    show LC mTeeth at left:
        xalign -0.01
    hide LE
    show H NarrowFrownDownturned
    lc mTeeth"Si tu le dis, suis-moi et prouve-le, toi aussi"
    show LC at left: 
        xalign 0.01
    with ease
    dc WideFrownLaugh"Vite, allons"
    show M at left: 
        xalign 0.26
    with ease
    m painedTalk"[l], à quoi rime tout ceci?"
    show DC WideFrownSquirm
    show M at left:
        xalign 0.0
    show LC at left: 
        xalign 0.26
    with fasterease
    lc mFrown"Arrière, toi, Éthiopienne"
    dc NarrowFrownLaugh"Fais semblant de te dégager, fais comme si tu allais me suivre, mais tu ne viendras pas"
    dc BaseFrownLaugh"Vas-t'en, tu n'es qu'un lâche!"
    show M at left:
        xalign -0.1
    show LC at left: 
        xalign 0.27
    with ease
    show DC BaseNeutralSquirm
    lc mTeeth"Cesse donc de m'agripper, chienne, teigne!"
    lc mDrool"Lâche prise, sâle bête, ou je m'en vais te jeter loin de moi comme un serpent."
    show H NarrowFrownSquirm
    m sadTalk"Pourquoi êtes-vous si grossier, quel est ce changement, mon tendre amour?"
    show LC at left: 
        xalign 0.22
    with ease
    lc mOpen"Moi, ton amour?"
    show M at left: 
        xalign -0.15
    show LC at left: 
        xalign 0.21
    with fasterease
    lc mTalk1"Vas-t'en, Tartare, moricaude, va-t'en!"
    show M at left: 
        xalign -0.18
    show LC at left: 
        xalign 0.20
    with fasterease
    lc mTalk2"Au diable, médecine répugnante, au diable, vomitif dégoûtant!"
    m sadSquirm"Vous ne plaisantez pas?"
    show DC NarrowFrownDown
    h NarrowFrownHappytalk"Oui, bien sûr et vous aussi."
    show H NarrowFrownDownturned
    show LC at left: 
        xalign 0.25
    with ease
    lc mFrown"[d], je tiendrai parole."
    dc BaseNeutralDown"Je voudrais un papier de votre main, car je vois bien qu'une faible main suffit à vous retenir."
    dc NarrowFrownOpen"Je ne crois pas en votre parole."
    lc wFrown"Eh quoi, tu voudrais que je la blesse, que je la batte, que je la tue?"
    show DC NarrowFrownDown
    lc wOpen"Bien que je la haïsse, je ne puis lui faire du mal."
    m sadOpen"Quel plus grand mal pouvez-vous me faire que de me haïr?"
    m sadCry"Me haïr, mais pourquoi?"
    m sadOpen"Hélas, quelle révélation, mon amour!"
    show M painedOpen at left: 
        xalign -0.1
    with ease
    m painedOpen"Ne suis-je pas [m], n'êtes-vous pas [l]?"
    m painedTalk"Je suis aussi belle maintenant que je l'étais tantôt"
    m painedFrown"Vous m'aimiez hier soir; mais vous m'avez quittée depuis."
    show DC BaseFrownSquirm
    m painedOpen"M'avez-vous donc quittée"
    m painedSquirm"- Oh, les dieux m'en préservent! -"
    m painedTalk"Quittée pour de bon?"
    show H NarrowNeutralSquirm
    lc fScowl"Oui, sur me vie, et j'aurais souhaité ne jamais te revoir"
    lc fOpen"Ainsi, n'aie plus d'espoir, d'incertitude, de doute\nSois-en convaincue, car rien n'est plus vrai"
    show DC NarrowFrownSquirm
    lc fSmirk"Ce n'est nullement une plaisanterie:\nJ'aime [h] et je te hais"
    m sadOpen"Pauvre de moi!"
    show LC behind M
    show M sadCry at left: 
        xalign 0.04
    with ease
    m sadCry"Oh, vous, ensorceleuse, chenille, voleuse d'amour qui, à la faveur de la nuit, êtes venue dérober le coeur de mon bien-aimé!"
    h NarrowNeutralHappytalk"Ma foi c'est admirable"
    h NarrowRaisedHappytalk"N'avez-vous aucune modestie? Aucune pudeur de jeune fille?"
    show DC BaseNeutralDown
    h BaseRaisedHappytalk"Pas un semblant de honte?!"
    h WideRaisedOpentalk"Quoi, voulez-vous arracher des paroles véhémentes à ma douce langue?"
    h WideFrownOpentalk"Fi! Fi! Petite marionnette hypocrite!"
    show M at left: 
        xalign 0.03
    with ease
    show H WideFrownDownturned
    m nFrown"Moi, marionette?"
    m nTalk"Pourquoi?"
    m nYell"Ah, voilà le fin mot; Je saisis maintenant"
    show H BaseFrownDownturned
    m nScowl"Elle aura fait quelque comparaison entre nos deux tailles, elle a poussé sa stature et fait valoir sa taille"
    m nMean"Et du haut de son personnage, elle a fait sa conquête, ma foi!"
    show M at left: 
        xalign 0.045
    with ease
    m nCruel"Avez-vous grimpé si haut dans son estime parce que je suis si petite et si ratatinée?"
    show M at left: 
        xalign 0.06
    with fasterease
    show H BaseNeutralDownturned
    m nScowl"Ose dire que je suis petite, toi, mât de cocagne bariolé"
    show M at left: 
        xalign 0.1
    with fasterease
    show H BaseRaisedDownturned
    m nYell"Allons, dis-le que je suis petite!"
    show M at left: 
        xalign 0.45
    with fasterease
    show H at center: 
        xalign 1.25
    with fasterease
    show H WideRaisedSquirm
    m nMean"Je ne suis tout de même pas si petite que mes ongles ne puissent atteindre tes yeux!"
    show H at right: 
        xalign 1.28
    show M at center:
        xalign 0.50
    with ease
    h WideRaisedSadtalk"De grâce messieurs! Bien que vous vous moquiez de moi, empêchez-la de me blesser!"
    show DC BaseRaisedDown
    h WideRaisedOpentalk"Je n'ai jamais été méchante; Je n'ai aucun don de mégère"
    h WideRaisedDownturned"Je suis une vraie fillette pour la couardise; Ne la laissez pas me frapper!"
    show M wideScowl
    h WideRaisedSadtalk"Vous pourriez croire peut-être que je peux lui tenir tête parc qu'elle est un peu plus petite que moi-"
    show M at center: 
        xalign 0.55
    with ease
    m wideScowl"Plus petite, vous l'entendez, elle y revient"
    show DC behind H
    show H WideRaisedSquirm at right: 
        xalign 1.26
    with ease
    h WideRaisedHappytalk"Ma bonne [m], ne soyez pas si cruelle envers moi"
    h BaseRaisedHappytalk"Je vous ai toujours aimée, [m], je n'ai jamais trahi vos secrets, je ne vous ai jamais fait de mal"
    h BaseRaisedOpentalk"Mon seul tort est que, par amour pour [d], je lui ai dévoilé votre fuite dans ce bois"
    show H at right: 
        xalign 1.20
    with ease
    h BaseNeutralHappytalk"Il vous a suivie, je l'ai suivi par amour"
    h BaseFrownSadtalk"Mais il m'a repoussée en me menanaçant de me frapper, de me piétiner et même de me tuer"
    show DC BaseNeutralSquirm
    h WideRaisedOpentalk"Et maintenant si vous me laissez partir tranquille, je rentrerai à Athènes, en emportant avec moi ma folie et je ne chercherai plus à vous suivre"
    h WideRaisedHappytalk"Laissez-moi partir, vous voyez comme je suis simple et docile"
    show H WideRaisedDownturned
    show M wideSnarky at center: 
        xalign 0.60
    with ease
    m wideSnarky"Eh bien, allez-vous-en, qui vous retient?"
    show DC BaseNeutralNeutral
    h BlushNarrowRaisedDownturned"Un coeur insensé, que je laisse dérrière moi"
    m resolOpen"Avec qui? Avec [l]?"
    show H at right: 
        xalign 1.25
    with ease
    show M behind LC
    show DC BaseRaisedSlightsmile
    h BlushNarrowRaisedOpentalk"Avec [d]"
    show LC at center: 
        xalign 0.38
    with ease
    show H NarrowRaisedDownturned
    lc wBase"Ne crains rien, [h], elle ne te fera pas de mal."
    show DC BaseFrownDown
    show H behind DD
    show DC at right: 
        xalign 0.90
    with ease
    dc BaseFrownOpen"Non, monsieur, elle n'en fera rien, quand bien même tu prendrais son parti"
    show DC BaseFrownDown
    h BaseRaisedOpentalk"Oh mais c'est qu'elle est rusée et méchante, quand elle est en colère"
    h BaseRaisedHappytalk"C'était une vraie renarde à l'école"
    show LC wFrown
    h NarrowFrownOpentalk"Elle a beau être petite, elle est féroce!"
    show H NarrowFrownDownturned
    m nTalk'Encore "petite". Toujours "petite" et "ratatinée"!'
    m conScowl"Souffrirez-vous qu'elle se moque ainsi de moi?"
    show M at center: 
        xalign 0.70
    with fasterease
    show H NarrowRaisedSquirm
    m wideScowl"Laissez-moi l'approcher!"
    show LC at center: 
        xalign 0.65
    with superfasterease
    show M at left: 
        xalign 0.05
    with fasterease
    show LC at center: 
        xalign 0.50
    with ease
    lc mDeranged"Vas-t'en, naine, avorton fait de chiendent où l'en s'empêtre, gland de chêne, grain de chapelet!"
    dc WideRaisedLaugh"Vous vous mettez trop en peine pour qui dédaigne vos services"
    dc WideFrownTalkscowl2"Laissez-la tranquille"
    show H BaseRaisedSquirm
    dc WideFrownTalkscowl"Ne t'occupe plus d'[h], ne prends pas son parti"
    dc NarrowFrownTalkscowl2"Car si tu essaies seulement de lui témoigner le moindre semblant d'amour, tu le payeras cher"
    show LC at center: 
        xalign 0.55
    with ease
    show H at right: 
        xalign 1.10
    with ease
    show H BaseRaisedDownturned
    lc fSquirm"Elle ne me retient plus; Suis-moi maintenant si tu l'oses, et voyons qui de nous deux a le plus de droits sur [h]"
    show LC behind DD
    show DC at center: 
        xalign 0.78
    with ease
    dc WideRaisedLaugh"Moi, te suivre!"
    show DC BaseFrownLaugh at flip
    dc BaseFrownSquiggly"Non, nous irons ensemble et côte à côte"
    hide LC
    hide DC
    with easeoutright
    "[l] et [d] sortent"
    show H WideRaisedSquirm
    m nYell"Voyez, madame, tout ce remue-ménage est de votre faute."
    show H at right: 
        xalign 1.20
    with slowerease
    m nTalk"Non, ne vous échappez pas"
    show H WideNeutralDownturned at right: 
        xalign 0.92
    with ease
    h WideNeutralSadtalk"Je ne me fierai pas à vous et ne resterai pas davantage en votre maudite compagnie"
    h BaseNeutralHappytalk"Si vos mains sont plus promptes à la lutte, j'ai de plus longues jambes pour m'enfuir"
    show H BaseNeutralSquirm
    hide H with fastereaseoutright
    "[h] se sauve"

    m sadOpen"Je suis abasourdie et ne sais que dire"
    show M sadSquirm
    hide M with superslowereaseoutleft
    "[m] sort lentement"
    jump scene12