import random

def exclude_minimal_triforce_hunt(weight_dict, random_settings):
    """ If triforce hunt is enabled, reroll the item pool excluding minimal. """
    weights = weight_dict['item_pool_value']
    if 'minimal' in weights.keys() and random_settings['triforce_hunt'] == "true":
        weights.pop('minimal')
    random_settings['item_pool_value'] = random.choices(list(weights.keys()), weights=list(weights.values()))[0]

def exclude_ice_trap_misery(weight_dict, random_settings):
    """ If the damage multiplier is quad or OHKO, exclude ice trap onslaught and mayhem. """
    weights = weight_dict['junk_ice_traps']
    if 'mayhem' in weights.keys() and random_settings['damage_multiplier'] in ['quadruple', 'ohko']:
        weights.pop('mayhem')
    if 'onslaught' in weights.keys() and random_settings['damage_multiplier'] in ['quadruple', 'ohko']:
        weights.pop('onslaught')
    random_settings['junk_ice_traps'] = random.choices(list(weights.keys()), weights=list(weights.values()))[0]

def disable_fortresskeys_independence(random_settings):
    """ Set shuffle_fortresskeys to match shuffle_smallkeys. """
    if random_settings['shuffle_smallkeys'] in ['remove', 'vanilla', 'dungeon']:
        random_settings['shuffle_fortresskeys'] = 'vanilla'
    else:
        random_settings['shuffle_fortresskeys'] = random_settings['shuffle_smallkeys']

def include_40_50_skulls(random_settings):
    """ If Tokensanity is rolled, include 40 and 50 skulls check. """
    if random_settings['tokensanity'] in ['off']:
        random_settings['disabled_locations'].extend(["Kak 40 Gold Skulltula Reward",
        "Kak 50 Gold Skulltula Reward"])

def max_triforce_pieces(random_settings):
    if random_settings['triforce_hunt'] == "true":
        if random_settings['item_pool_value'] == "balanced":
            Max_pieces = 44
            if random_settings["shuffle_cows"] == "true":
                Max_pieces += 8
            if random_settings["shuffle_scrubs"] != "off":
                Max_pieces += 21
            if random_settings["shopsanity"] != "off" and random_settings["shopsanity"] != "0" and random_settings["shopsanity"] != "random":
                if random_settings["shopsanity"] == "1":
                    Max_pieces += 3
                elif random_settings["shopsanity"] == "2":
                    Max_pieces += 8
                elif random_settings["shopsanity"] == "3":
                    Max_pieces += 14
                elif random_settings["shopsanity"] == "4":
                    Max_pieces += 19
            if random_settings["shuffle_mapcompass"] == "remove" or random_settings["shuffle_mapcompass"] == "startwith":
                Max_pieces += 14
            if random_settings["shuffle_smallkeys"] == "remove":
                Max_pieces += 29
            if random_settings["shuffle_bosskeys"] == "remove":
                Max_pieces += 4
            if random_settings['triforce_goal_per_world'] > Max_pieces:
                random_settings['triforce_goal_per_world'] = Max_pieces      
        
