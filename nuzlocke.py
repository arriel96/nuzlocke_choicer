import random

violet = ['Larvitar', 'Pupitar', 'Tyranitar', 'Drifloon', 'Drifblim', 'Stunky', 'Skuntank', 'Deino', 'Zweilous', 'Hydreigon', 'Skrelp', 'Dragalge', 'Oranguro', 'Stonjourner', 'Great Tusk', 'Brute Bonnet', 'Sandy Shocks', 'Scream Tail', 'Flutter Mane', 'Slither Wing', 'Roaring Moon', 'Armarouge', 'Koraidon']
scarlet = ['Misdreavus', 'Gulpin', 'Swalot', 'Bagon', 'Shelgon', 'Salamence', 'Mismagius', 'Clauncher', 'Clawitzer', 'Passimian', 'Dreepy', 'Drakloak', 'Dragapult', 'Eiscue', 'Iron Treads', 'Iron Moth', 'Iron Hands', 'Iron Jugulis', 'Iron Thorns', 'Iron Bundle', 'Iron Valiant', 'Ceruledge', 'Miraidon']

#version = violet
#version = scarlet


repeat = []
region01 = 'Poco Path 01'
pokemon01 = ['Fletchling', 'Hoppip', 'Lechonk', 'Pawmi', 'Scatterbug', 'Tarountula', 'Yungoos']

pokemon01 = list(set(pokemon01) - set(version))

x=random.randint(0,(len(pokemon01)-1))
print(region01)
print(pokemon01[x])

repeat.append(pokemon01[x])

region02 = 'Inlet Grotto 02'
pokemon02 = ['Yungoos','Houndour','Diglet']

pokemon02 = list(set(pokemon02) - set(repeat))
pokemon02 = list(set(pokemon02) - set(version))

x=random.randint(0,(len(pokemon02)-1))
print(region02)
print(pokemon02[x])

repeat.append(pokemon02[x])

region03 = 'East Paldean Sea 03'
pokemon03 = ['Bruxish', 'Clauncher', 'Mareanie', 'Toxapex']

pokemon03 = list(set(pokemon03) - set(repeat))
pokemon03 = list(set(pokemon03) - set(version))

x=random.randint(0,(len(pokemon03)-1))
print(region03)
print(pokemon03[x])

repeat.append(pokemon03[x])




region04 = 'West Paldean Sea 04'
pokemon04 = ['Buizel', 'Floatzel', 'Wingull', 'Pelipper', 'Magikarp', 'Gyarados', 'Barraskewda', 'Kilowattrel', 'Bombirdier', 'Finizen', 'Orthworm', 'Shellder', 'Cloyster', 'Qwilfish', 'Luvdisc', 'Finneon', 'Lumineon', 'Bruxish', 'Skrelp', 'Clauncher', 'Tynamo', 'Eelektrik', 'Froslass', 'Veluza']

pokemon04 = list(set(pokemon04) - set(repeat))
pokemon04 = list(set(pokemon04) - set(version))

x=random.randint(0,(len(pokemon04)-1))
print(region04)
print(pokemon04[x])

repeat.append(pokemon04[x])

region05 = 'North Paldean Sea 05'
pokemon05 = ['Floatzel', 'Pelipper', 'Gyarados', 'Barraskewda', 'Kilowattrel', 'Finizen', 'Orthworm', 'Eiscue (Ice Face)', 'Shellder', 'Cloyster', 'Qwilfish', 'Finneon', 'Lumineon', 'Alomomola', 'Skrelp', 'Dragalge', 'Clauncher', 'Clawitzer', 'Tynamo', 'Eelektrik', 'Bergmite', 'Avalugg']

pokemon05 = list(set(pokemon05) - set(repeat))
pokemon05 = list(set(pokemon05) - set(version))

x=random.randint(0,(len(pokemon05)-1))
print(region05)
print(pokemon05[x])

repeat.append(pokemon05[x])


region06 = 'South Province (Area One) 06'
pokemon06=['Oinkologne', 'Tarountula', 'Spidops', 'Hoppip', 'Fletchling', 'Pawmi', 'Houndour', 'Scatterbug', 'Spewpa', 'Surskit', 'Paldean Wooper', 'Ralts', 'Fidough', 'Dachsbun', 'Oricorio (Pom-Pom Style)', 'Wingull', 'Pelipper', 'Charcadet', 'Deerling', 'Sawsbuck', 'Toedscool']

pokemon06 = list(set(pokemon06) - set(repeat))
pokemon06 = list(set(pokemon06) - set(version))

x=random.randint(0,(len(pokemon06)-1))
print(region06)
print(pokemon06[x])

repeat.append(pokemon06[x])

region07 = 'South Province (Area Two) 07'
pokemon07 = ['Azurill', 'Bonsly', 'Buizel', 'Chewtle', 'Combee', 'Diglett', 'Fidough', 'Fletchling', 'Happiny', 'Hoppip', 'Igglybuff', 'Jigglypuff', 'Kricketot', 'Magikarp', 'Makuhita', 'Mareep', 'Maschiff', 'Nacli', 'Pichu', 'Pikachu', 'Psyduck', 'Rockruff', 'Skwovet', 'Smoliv', 'Starly', 'Sunkern']

pokemon07 = list(set(pokemon07) - set(repeat))
pokemon07 = list(set(pokemon07) - set(version))

x=random.randint(0,(len(pokemon07)-1))
print(region07)
print(pokemon07[x])

repeat.append(pokemon07[x])

region08 = 'South Province (Area Three) 08'
pokemon08 = ['Bronzor', 'Charcadet', 'Drowzee', 'Dunsparce', 'Growlithe', 'Gulpin', 'Happiny', 'Klawf', 'Makuhita', 'Murkrow', 'Nacli', 'Nymble', 'Oricorio (Baile Style)', 'Pawmi', 'Rookidee', 'Shinx', 'Skiddo', 'Spoink', 'Squawkabilly', 'Tinkatink', 'Yungoos' ]

pokemon08 = list(set(pokemon08) - set(repeat))
pokemon08 = list(set(pokemon08) - set(version))

x=random.randint(0,(len(pokemon08)-1))
print(region08)
print(pokemon08[x])

repeat.append(pokemon08[x])

region09 = 'South Province (Area Four) 09'
pokemon09= ['Buizel', 'Deerling', 'Dunsparce', 'Fletchinder', 'Goomy', 'Houndour', 'Lechonk', 'Makuhita', 'Marill', 'Maschiff', 'Murkrow (Night only)', 'Nacli', 'Pachirisu', 'Pawmi', 'Pawmo', 'Phanpy', 'Psyduck', 'Riolu', 'Scyther', 'Starly', 'Tadbulb', 'Tarountula', 'Toxel', 'Wooper (Paldean form)' ]

pokemon09 = list(set(pokemon09) - set(repeat))
pokemon09 = list(set(pokemon09) - set(version))

x=random.randint(0,(len(pokemon09)-1))
print(region09)
print(pokemon09[x])

repeat.append(pokemon09[x])

region10 = 'South Province (Area Five) 10'
pokemon10=['Lechonk', 'Oinkologne', 'Tarountula', 'Spidops', 'Skiploom', 'Fletchinder', 'Pawmo', 'Yungoos', 'Gumshoos', 'Spewpa', 'Rookidee', 'Corvisquire', 'Surskit', 'Masquerain', 'Buizel', 'Paldean Wooper', 'Clodsire', 'Psyduck', 'Chewtle', 'Chewtle', 'Drednaw', 'Gastly', 'Slakoth', 'Vigoroth', 'Bounsweet', 'Rockruff', 'Luxio', 'Shroomish', 'Misdreavus', 'Makuhita', 'Nacli', 'Magikarp', 'Arrokuda', 'Basculin', 'Drifloon', 'Flabebe', 'Floette', 'Axew', 'Fraxure', 'Mankey', 'Charcadet', 'Barboach', 'Tadbulb', 'Goomy', 'Croagunk', 'Toxicroak', 'Deerling', 'Sawsbuck', 'Pachirisu', 'Stantler', 'Teddiursa', 'Zangoose', 'Seviper', 'Swablu', 'Skiddo', 'Litleo', 'Pyroar', 'Stunky', 'Murkrow', 'Toedscool', 'Fomantis', 'Lurantis', 'Flittle', 'Mudbray', 'Bagon', 'Wiglett', 'Dreepy', 'Larvitar', 'Pincurchin', 'Sandygast', 'Palossand', 'Slowpoke', 'Shellos', 'Gastrodon', 'Froslass', 'Pawniard']

pokemon10 = list(set(pokemon10) - set(repeat))
pokemon10 = list(set(pokemon10) - set(version))

x=random.randint(0,(len(pokemon10)-1))
print(region10)
print(pokemon10[x])

repeat.append(pokemon10[x])

region11 = 'South Province (Area Six) 11'
pokemon11 = ['Lokix', 'Jumpluff', 'Pawmo', 'Yungoos', 'Gumshoos', 'Greedent', 'Sunflora', 'Vivillon', 'Vespiquen', 'Chansey', 'Buizel', 'Floatzel', 'Clodsire', 'Psyduck', 'Drednaw', 'Gallade', 'Fidough', 'Dachsbun', 'Arboliva', 'Lycanroc (Midday Form)', 'Flaaffy', 'Ampharos', 'Petilil', 'Lilligant', 'Misdreavus', 'Mismagius', 'Hariyama', 'Salandit', 'Salazzle', 'Donphan', 'Copperajah', 'Gible', 'Gabite', 'Naclstack', 'Arrokuda', 'Barraskewda', 'Drifblim', 'Floette', 'Diglett', 'Dugtrio', 'Bronzong', 'Meditite', 'Medicham', 'Lucario', 'Whiscash', 'Goomy', 'Wattrel', 'Umbreon', 'Sylveon', 'Toxel', 'Toxtricity', 'Altaria', 'Skiddo', 'Murkrow', 'Honchkrow', 'Gothorita', 'Gothitelle', 'Sinistea', 'Scovillain', 'Flittle', 'Espathra', 'Mudbray', 'Mudsdale', 'Shelgon', 'Hattrem', 'Bombirdier', 'Sableye', 'Banette', 'Glimmet', 'Houndstone', 'Larvitar', 'Pupitar', 'Shellos', 'Gastrodon', 'Tynamo', 'Eelektrik', 'Dratini', 'Rufflet', 'Deino', 'Gimmighoul']

pokemon11 = list(set(pokemon11) - set(repeat))
pokemon11 = list(set(pokemon11) - set(version))

x=random.randint(0,(len(pokemon11)-1))
print(region11)
print(pokemon11[x])

repeat.append(pokemon11[x])

region12 = 'East Province (Area One) 12'
pokemon12 = ['Corvisquire', 'Deerling', 'Dunsparce', 'Gulpin', 'Hoppip', 'Komala', 'Lechonk', 'Litleo', 'Murkrow (Night only)', 'Oinkologne', 'Pikachu', 'Rookidee', 'Shroodle', 'Shuppet (Night only)', 'Spidops', 'Squawkabilly', 'Steenee', 'Tadbulb', 'Tandemaus', 'Tauros (Paldean form)', 'Teddiursa', 'Tarountula', 'Venonat']

pokemon12 = list(set(pokemon12) - set(repeat))
pokemon12 = list(set(pokemon12) - set(version))

x=random.randint(0,(len(pokemon12)-1))
print(region12)
print(pokemon12[x])

repeat.append(pokemon12[x])

region13 = 'East Province (Area Two) 13'
pokemon13 =['Buizel', 'Chewtle', 'Crabrawler', 'Cyclizar', 'Deerling', 'Finizen', 'Gyarados', 'Magikarp', 'Magnemite', 'Makuhita', 'Mareanie', 'Marill', 'Murkrow (Night only)', 'Nacli', 'Oinkologne', 'Pawmi', 'Pincurchin', 'Psyduck', 'Rookidee', 'Sandygast', 'Slowpoke', 'Tadbulb', 'Tauros (Paldean form)', 'Wattrel', 'Wiglett']

pokemon13 = list(set(pokemon13) - set(repeat))
pokemon13 = list(set(pokemon13) - set(version))

x=random.randint(0,(len(pokemon13)-1))
print(region13)
print(pokemon13[x])

repeat.append(pokemon13[x])

region14 = 'East Province (Area Three) 14'
pokemon14=['Lokix', 'Pawmo', 'Yungoos', 'Gumshoos', 'Rookidee', 'Corvisquire', 'Buizel', 'Floatzel', 'Clodsire', 'Psyduck', 'Chewtle', 'Chewtle', 'Drednaw', 'Gastly', 'Fidough', 'Dachsbun', 'Rolycoly', 'Carkol', 'Squawkabilly', 'Makuhita', 'Hariyama', 'Salandit', 'Cufant', 'Nacli', 'Magikarp', 'Arrokuda', 'Barraskewda', 'Basculin', 'Meowth', 'Drifloon', 'Drifblim', 'Diglett', 'Dugtrio', 'Torkoal', 'Charcadet', 'Barboach', 'Tadbulb', 'Goomy', 'Voltorb', 'Electrode', 'Magnemite', 'Growlithe', 'Skiddo', 'Murkrow', 'Gothita', 'Sinistea', 'Bramblin', 'Toedscool', 'Silicobra', 'Mudsdale', 'Varoom', 'Revavroom', 'Orthworm', 'Sableye', 'Shuppet', 'Dreepy', 'Glimmet', 'Larvitar', 'Pawniard', 'Gimmighoul (Chest Form)']

pokemon14 = list(set(pokemon14) - set(repeat))
pokemon14 = list(set(pokemon14) - set(version))

x=random.randint(0,(len(pokemon14)-1))
print(region14)
print(pokemon14[x])

repeat.append(pokemon14[x])

region15 = 'West Province (Area One) 15'
pokemon15 = ['Nymble', 'Yungoos', 'Combee', 'Happiny', 'Buizel', 'Floatzel', 'Psyduck', 'Chewtle', 'Gastly', 'Rockruff', 'Petilil', 'Lilligant', 'Misdreavus', 'Makuhita', 'Crabrawler', 'Salandit', 'Phanpy', 'Gible', 'Nacli', 'Wingull', 'Pelipper', 'Magikarp', 'Arrokuda', 'Basculin', 'Drifloon', 'Flabebe', 'Diglett', 'Numel', 'Bronzor', 'Mankey', 'Charcadet', 'Tadbulb', 'Wattrel', 'Swablu', 'Skiddo', 'Capsakid', 'Flittle', 'Mudbray', 'Wiglett', 'Bombirdier', 'Sableye', 'Falinks', 'Larvitar', 'Tynamo', 'Eelektrik', 'Rufflet', 'Gimmighoul (Chest Form)']

pokemon15 = list(set(pokemon15) - set(repeat))
pokemon15 = list(set(pokemon15) - set(version))

x=random.randint(0,(len(pokemon15)-1))
print(region15)
print(pokemon15[x])

repeat.append(pokemon15[x])

region16 = 'West Province (Area Two) 16'
pokemon16 = ['Arrokuda', 'Buizel', 'Crabrawler', 'Cyclizar', 'Deerling', 'Diglett', 'Ditto', 'Donphan', 'Dunsparce', 'Finizen', 'Flaaffy', 'Floatzel', 'Gible', 'Girafarig', 'Grimer', 'Gyarados', 'Kilowattrel', 'Kirlia', 'Magikarp', 'Makuhita', 'Maschiff', 'Meditite', 'Meowth', 'Murkrow (Night only)', 'Nacli', 'Noibat', 'Oinkologne', 'Pawmi', 'Phanpy', 'Pincurchin', 'Psyduck', 'Salandit', 'Sandygast', 'Shellos', 'Skiddo', 'Slowpoke', 'Tandemaus', 'Tauros (Paldean form)', 'Wattrel', 'Wiglett', 'Wingull', 'Wugtrio']

pokemon16 = list(set(pokemon16) - set(repeat))
pokemon16 = list(set(pokemon16) - set(version))

x=random.randint(0,(len(pokemon16)-1))
print(region16)
print(pokemon16[x])

repeat.append(pokemon16[x])

region17 = 'West Province (Area Three) 17'
pokemon17 = ['Lechonk', 'Oinkologne', 'Tarountula', 'Spidops', 'Lokix', 'Jumpluff', 'Fletchinder', 'Pawmo', 'Gumshoos', 'Greedent', 'Chansey', 'Azumarill', 'Floatzel', 'Clodsire', 'Psyduck', 'Drednaw', 'Jigglypuff', 'Gallade', 'Pikachu', 'Fidough', 'Dachsbun', 'Vigoroth', 'Arboliva', 'Sudowoodo', 'Starly', 'Staravia', 'Staraptor', 'Petilil', 'Lilligant', 'Shroomish', 'Breloom', 'Applin', 'Misdreavus', 'Hariyama', 'Nacli', 'Magikarp', 'Arrokuda', 'Barraskewda', 'Basculin', 'Meowth', 'Persian', 'Drifloon', 'Drifblim', 'Bronzong', 'Primeape', 'Charcadet', 'Barboach', 'Whiscash', 'Tadbulb', 'Goomy', 'Eevee', 'Sylveon', 'Maschiff', 'Mabosstiff', 'Dedenne', 'Pachirisu', 'Shroodle', 'Foongus', 'Voltorb', 'Electrode', 'Ditto', 'Skiddo', 'Gogoat', 'Zorua', 'Zoroark', 'Murkrow', 'Toedscool', 'Tropius', 'Pineco', 'Scyther', 'Espathra', 'Mudbray', 'Mudsdale', 'Hatenna', 'Bombirdier', 'Sableye', 'Dreepy', 'Greavard', 'Komala', 'Snom', 'Glalie', 'Rufflet', 'Deino', 'Gimmighoul (Chest Form)']

pokemon17 = list(set(pokemon17) - set(repeat))
pokemon17 = list(set(pokemon17) - set(version))

x=random.randint(0,(len(pokemon17)-1))
print(region17)
print(pokemon17[x])

repeat.append(pokemon17[x])

region18 = 'North Province (Area One) 18'
pokemon18 = ['Lokix', 'Jumpluff', 'Pawmo', 'Greedent', 'Kricketune', 'Vivillon', 'Vespiquen', 'Chansey', 'Blissey', 'Floatzel', 'Golduck', 'Wigglytuff', 'Gallade', 'Haunter', 'Arboliva', 'Lycanroc (Midday Form)', 'Lycanroc (Dusk Form)', 'Ampharos', 'Applin', 'Grumpig', 'Mismagius', 'Salazzle', 'Copperajah', 'Naclstack', 'Barraskewda', 'Drifblim', 'Floette', 'Bronzong', 'Axew', 'Fraxure', 'Primeape', 'Lucario', 'Barboach', 'Whiscash', 'Umbreon', 'Ursaring', 'Altaria', 'Gogoat', 'Sneasel', 'Weavile', 'Honchkrow', 'Indeedee', 'Brambleghast', 'Fomantis', 'Lurantis', 'Scovillain', 'Venonat', 'Venomoth', 'Espathra', 'Mudsdale', 'Tinkatuff', 'Wugtrio', 'Revavroom', 'Hawlucha', 'Noibat', 'Noivern', 'Drakloak', 'Greavard', 'Houndstone', 'Eiscue (Ice Face)', 'Pincurchin', 'Shellos', 'Gastrodon', 'Shellder', 'Alomomola', 'Dratini', 'Delibird', 'Cubchoo', 'Snorunt', 'Cetoddle', 'Cetitan', 'Rufflet', 'Braviary', 'Deino', 'Zweilous', 'Arctibax', 'Gimmighoul (Chest Form)']

pokemon18 = list(set(pokemon18) - set(repeat))
pokemon18 = list(set(pokemon18) - set(version))

x=random.randint(0,(len(pokemon18)-1))
print(region18)
print(pokemon18[x])

repeat.append(pokemon18[x])

region19 = 'North Province (Area Two) 19'
pokemon19 = ['Spidops', 'Lokix', 'Jumpluff', 'Houndoom', 'Kricketot', 'Vivillon', 'Vespiquen', 'Chansey', 'Blissey', 'Floatzel', 'Clodsire', 'Arboliva', 'Luxray', 'Grumpig', 'Mismagius', 'Hariyama', 'Copperajah', 'Gabite', 'Naclstack', 'Floette', 'Dugtrio', 'Camerupt', 'Bronzong', 'Primeape', 'Lucario', 'Foongus', 'Amoonguss', 'Arcanine', 'Ursaring', 'Gogoat', 'Honchkrow', 'Indeedee', 'Fomantis', 'Lurantis', 'Venonat', 'Venomoth', 'Scyther', 'Heracross', 'Espathra', 'Tinkatuff', 'Sableye', 'Falinks', 'Hawlucha', 'Noibat', 'Noivern', 'Drakloak', 'Glimmet', 'Houndstone', 'Oranguru', 'Passimian', 'Dratini', 'Rufflet', 'Braviary', 'Bisharp', 'Deino', 'Zweilous']

pokemon19 = list(set(pokemon19) - set(repeat))
pokemon19 = list(set(pokemon19) - set(version))

x=random.randint(0,(len(pokemon19)-1))
print(region19)
print(pokemon19[x])

repeat.append(pokemon19[x])

region20 = 'North Province (Area Three) 20'
pokemon20 = ['Jumpluff', 'Pawmo', 'Gumshoos', 'Sunflora', 'Vivillon', 'Combee', 'Vespiquen', 'Chansey', 'Blissey', 'Floatzel', 'Golduck', 'Dolliv', 'Petilil', 'Lilligant', 'Copperajah', 'Naclstack', 'Magikarp', 'Barraskewda', 'Floette', 'Florges', 'Bellibolt', 'Umbreon', 'Dedenne', 'Gogoat', 'Fomantis', 'Lurantis', 'Wugtrio', 'Sableye', 'Hawlucha', 'Drakloak', 'Greavard', 'Houndstone', 'Eiscue (Ice Face)', 'Pincurchin', 'Alomomola', 'Delibird', 'Cubchoo', 'Beartic', 'Cetoddle', 'Rufflet', 'Deino', 'Arctibax']

pokemon20 = list(set(pokemon20) - set(repeat))
pokemon20 = list(set(pokemon20) - set(version))

x=random.randint(0,(len(pokemon20)-1))
print(region20)
print(pokemon20[x])

repeat.append(pokemon20[x])

region21 = 'Asado Desert 21'
pokemon21 = ['Lokix', 'Pawmo', 'Yungoos', 'Gumshoos', 'Combee', 'Chansey', 'Gastly', 'Rockruff', 'Makuhita', 'Phanpy', 'Donphan', 'Floette', 'Bronzor', 'Charcadet', 'Murkrow', 'Bramblin', 'Toedscool', 'Capsakid', 'Cacnea', 'Rellor', 'Flittle', 'Hippopotas', 'Sandile', 'Silicobra', 'Mudbray', 'Larvesta', 'Tinkatink', 'Orthworm', 'Falinks', 'Stonjourner']

pokemon21 = list(set(pokemon21) - set(repeat))
pokemon21 = list(set(pokemon21) - set(version))

x=random.randint(0,(len(pokemon21)-1))
print(region21)
print(pokemon21[x])

repeat.append(pokemon21[x])

region22 = 'Tagtree Thicket 22'
pokemon22 = ['Lechonk', 'Oinkologne', 'Tarountula', 'Spidops', 'Pawmo', 'Gumshoos', 'Greedent', 'Sunflora', 'Clodsire', 'Dolliv', 'Arboliva', 'Lycanroc (Midday Form)', 'Applin', 'Misdreavus', 'Dugtrio', 'Charcadet', 'Barboach', 'Whiscash', 'Bellibolt', 'Goomy', 'Shroodle', 'Grafaiai', 'Foongus', 'Gogoat', 'Zorua', 'Zoroark', 'Murkrow', 'Mimikyu', 'Fomantis', 'Lurantis', 'Scovillain', 'Venonat', 'Venomoth', 'Pineco', 'Flittle', 'Espathra', 'Silicobra', 'Hattrem', 'Impidimp', 'Morgrem', 'Orthworm', 'Oranguru', 'Passimian', 'Komala', 'Larvitar', 'Snom', 'Rufflet', 'Pawniard']

pokemon22 = list(set(pokemon22) - set(repeat))
pokemon22 = list(set(pokemon22) - set(version))

x=random.randint(0,(len(pokemon22)-1))
print(region22)
print(pokemon22[x])

repeat.append(pokemon22[x])

region23 = 'Casseroya Lake 23'
pokemon23 = ['Oinkologne', 'Tarountula', 'Spidops', 'Azumarill', 'Golduck', 'Drednaw', 'Raichu', 'Vigoroth', 'Slaking', 'Arboliva', 'Sudowoodo', 'Starly', 'Staravia', 'Staraptor', 'Petilil', 'Lilligant', 'Mismagius', 'Copperajah', 'Naclstack', 'Pelipper', 'Swalot', 'Bronzong', 'Sliggoo', 'Croagunk', 'Toxicroak', 'Mabosstiff', 'Amoonguss', 'Altaria', 'Gogoat', 'Skuntank', 'Zoroark', 'Honchkrow', 'Brambleghast', 'Toedscool', 'Toedscruel', 'Tropius', 'Lurantis', 'Scovillain', 'Venomoth', 'Forretress', 'Scyther', 'Heracross', 'Flittle', 'Hawlucha', 'Drakloak', 'Houndstone', 'Oranguru', 'Passimian', 'Palossand', 'Slowpoke', 'Slowbro', 'Gastrodon', 'Flamigo', 'Dratini', 'Dragonair', 'Frosmoth', 'Cetitan', 'Veluza', 'Dondozo', 'Tatsugiri']

pokemon23 = list(set(pokemon23) - set(repeat))
pokemon23 = list(set(pokemon23) - set(version))

x=random.randint(0,(len(pokemon23)-1))
print(region23)
print(pokemon23[x])

repeat.append(pokemon23[x])

region24 = 'Glaseado Mountain 24'
pokemon24 = ['Pawmo', 'Vespiquen', 'Chansey', 'Clodsire', 'Psyduck', 'Kirlia', 'Gardevoir', 'Gallade', 'Haunter', 'Vigoroth', 'Lycanroc (Midday Form)', 'Grumpig', 'Misdreavus', 'Mismagius', 'Crabrawler', 'Crabominable', 'Salandit', 'Copperajah', 'Gabite', 'Naclstack', 'Barraskewda', 'Drifloon', 'Drifblim', 'Dugtrio', 'Bronzong', 'Axew', 'Fraxure', 'Whiscash', 'Goomy', 'Vaporeon', 'Flareon', 'Espeon', 'Umbreon', 'Glaceon', 'Magneton', 'Ursaring', 'Gogoat', 'Litleo', 'Pyroar', 'Sneasel', 'Murkrow', 'Honchkrow', 'Gothita', 'Mimikyu', 'Klefki', 'Toedscool', 'Fomantis', 'Lurantis', 'Flittle', 'Espathra', 'Mudbray', 'Mudsdale', 'Tinkatuff', 'Hattrem', 'Wugtrio', 'Revavroom', 'Sableye', 'Banette', 'Hawlucha', 'Drakloak', 'Glimmet', 'Greavard', 'Houndstone', 'Larvitar', 'Pincurchin', 'Snom', 'Frosmoth', 'Snover', 'Delibird', 'Cubchoo', 'Beartic', 'Snorunt', 'Cryogonal', 'Cetoddle', 'Cetitan', 'Bergmite', 'Avalugg', 'Rufflet', 'Zweilous', 'Frigibax']

pokemon24 = list(set(pokemon24) - set(repeat))
pokemon24 = list(set(pokemon24) - set(version))

x=random.randint(0,(len(pokemon24)-1))
print(region24)
print(pokemon24[x])

repeat.append(pokemon24[x])

region25 = 'The Great Crater of Paldea 25'
pokemon25 = ['Jumpluff', 'Talonflame', 'Corviknight', 'Masquerain', 'Hypno', 'Lycanroc (Midnight Form)', 'Donphan', 'Garganacl', 'Camerupt', 'Medicham', 'Bellibolt', 'Dunsparce', 'Girafarig', 'Farigiraf', 'Swablu', 'Sneasel', 'Weavile', 'Venomoth', 'Volcarona', 'Glimmora', 'Flamigo', 'Braviary', 'Bisharp', 'Great Tusk', 'Scream Tail', 'Brute Bonnet', 'Flutter Mane', 'Slither Wing', 'Sandy Shocks', 'Iron Treads', 'Iron Bundle', 'Iron Hands', 'Iron Jugulis', 'Iron Moth', 'Iron Thorns', 'Roaring Moon', 'Iron Valiant']

pokemon25 = list(set(pokemon25) - set(repeat))
pokemon25 = list(set(pokemon25) - set(version))

x=random.randint(0,(len(pokemon25)-1))
print(region25)
print(pokemon25[x])

repeat.append(pokemon25[x])


