#%%
import pokebase as pb
import polars as pl

def get_pokedex_data():
    data = []
    # All Pokemon forms at the time of making this script is 10277. 
    # This (likely) includes all mega forms, and regional forms
    all_pokemon_forms = 151 
    for i in range(1,all_pokemon_forms): # adjust when new forms and Pokemon are released
        p = pb.pokemon(i)
        stats = {s.stat.name: s.base_stat for s in p.stats}
        row = {
            "id":p.id
            , "name": p.name
            , "type_1": p.types[0].type.name
            , 'type_2': p.types[1].type.name if len(p.types) > 1 else None
            , 'hp': stats['hp']
            , 'attack': stats['attack']
            , 'defense': stats['defense']
            , 'sp_attack': stats['special-attack']
            , 'sp_defense': stats['special-defense']
            , 'speed': stats['speed']
            , 'stat_total': sum(stats.values())
        }
        data.append(row)
        print(f'{p.id} {p.name} has been added.')
    return pl.DataFrame(data=data)


#%%
# 
all_pkmn_kanto = get_pokedex_data()

#%%
all_pkmn_kanto.tail(10)