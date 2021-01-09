import os, sys, time, pickle
import game_files.game_art as game_art
import game_files.game_characters as mobs

# I'm not exactly sure what actions will be taken in debug_mode, but so far it does get to the end of a chapter.
rimuru = None
fast_mode = False


# start_game.py will load game save if user has one, if not it'll create one.
# Then pass that into update_character which will update the rimuru variable to be used here.
def update_rimuru(rimuru_object):
    global rimuru
    rimuru = rimuru_object
    return rimuru

def set_fast_mode():
    global fast_mode
    rimuru.text_crawl = rimuru.show_ascii = False
    fast_mode = True

def action_menu(level=None, remove=False):
    """
    Updates player's location, Shows HUD, takes user input and runs corresponding actions.


    Args:
        level: Current story progress class object.

    Usage:
        > inv
        > stats
        > attack tempest serpent with water blade
    """

    rimuru.update_location(rimuru.get_location_variable(level))  # Updates player's location.

    actions = []
    for action in dir(level):  # Gets subclass functions.
        if '__' in action: continue  # Filters out unwanted variables and functions.
        actions.append(action)

    if remove: del actions[actions.index(remove)]  # Removes action so player can't take it.

    # ========== HUD
    print()
    if rimuru.targeted_mobs:
        # Adds (Dead) status to corresponding
        targets = ', '.join([(f'{mob[1]}({mob[0].name})' if mob[0].is_alive else f'X-{mob[1]}({mob[0].name})') for mob in rimuru.targeted_mobs])
        print(f'\nTarget: {targets}')

    # Formats actions available to user. Replaces _ with spaces and adds commas when needed.
    actions_for_hud = ' '.join([f"({action.replace('_', ' ').strip()})" for action in actions])
    print(f"Actions: {actions_for_hud}")

    # ========== Debug Mode
    # Runs first available action that will progress the storyline.
    if fast_mode:
        for action in actions:
            if action[0] == '_':
                user_input = action.replace('_', ' ').strip()
    else:
        user_input = input("\n> ").lower()
        print()

    # Separates user input into command and command arguments.
    split_user_input = user_input.split(' ')
    command, parameters = split_user_input[0], ' '.join(split_user_input[1:])
    character = rimuru

    level_actions = {
        'target': rimuru.set_targets,
        'mimic': rimuru.use_mimic, 'predate': rimuru.predate_targets,
        'stats': rimuru.show_attributes, 'inv': rimuru.show_inventory, 'info': rimuru.show_info, 'craft': rimuru.craft_item,
        'map': rimuru.get_map,
        'help': show_help, 'exit': game_exit, 'textcrawl': game_text_crawl
    }
    if 'attack' in command:
        if rimuru.attack(parameters):
            user_input = 'attack'  # Runs correlating function if attack was successful, if not it'll just loop.
    elif 'use' in command:
        rimuru.use_skill(parameters, character)
    elif 'location' in command:
        rimuru.get_location()
    elif 'nearby' in command:
        rimuru.use_skill('sense heat source', character)

    # Passes in user inputted arguments as parameters and runs corresponding action.
    for action_string, action in level_actions.items():
        if action_string in command:
            action(parameters)

    loop = True
    for action in actions:
        if action.replace('_', ' ').strip() in user_input:
            if action[0] == '_':
                loop = False  # Checks if action will progress storyline.
            eval(f"level.{action}()")

    if loop: action_menu(level)


#                    ========== Level Functions ==========
def game_conditions(value, new_value=None):
    if new_value:
        rimuru.conditional_data[value] = new_value
        return rimuru.conditional_data[value]

    if value in rimuru.conditional_data:
        return rimuru.conditional_data[value]
    else:
        return False

def new_active_mob(add_mobs):
    """
    Add new mob to current level, and able to set name at creation.

    Args:
        add_mobs: Adds mob objects to active_mobs list.

    Usage:
        new_active_mob(['tempest serpent'])
        new_active_mob(['tempest serpent', 'giant bat'])
        new_active_mob(['10* goblin', 'goblin: Goblin Chief'])
        new_active_mob(['50* goblin: Goblinas'])
    """

    for new_mob in add_mobs:
        amount = 1
        if '*' in new_mob:
            amount, new_mob = new_mob.split('*')  # Add multiple of same mob, e.g. ['5 * goblin']
            try:
                amount = int(amount)
            except:
                pass

        if ':' in new_mob:
            new_mob, new_name = new_mob.split(':')  # Sets mob name when creating new Character object, e.g. ['goblin name: Goblin Chief']
        else:
            new_name = None

        if mob_object := rimuru.get_object(new_mob, new=True):
            if new_name:
                mob_object.name = new_name.strip()

            rimuru.active_mobs.append([mob_object, amount])

def mob_status(target):
    """
    Returns whether mob in active_mobs list is is_alive.

    Args:
        target: Target to check is_alive status.

    Usage:
        mob_status('tempest serpent')
    """

    for i in rimuru.active_mobs:
        if target.lower() in i[0].get_name():
            return i[0].is_alive

def cleared_all_mobs():
    """
    Checks if mobs on current level are all dead.

    Returns:
        boolean: If all mobs in active_mobs are dead.

    Usage:
        if cleared_all_mobs():
    """

    for mob in rimuru.active_mobs:
        if mob[0].is_alive:
            return False
    else:
        return True

def reset_mobs():
    """Resets active_mobs and targeted_mobs list."""

    rimuru.active_mobs.clear()
    rimuru.targeted_mobs.clear()

def next_location(next_location):
    """
    Asks if

    Args:
        next_location: Next chapter to play.
    """

    rimuru.current_location_object = next_location
    game_save()
    try:
        next_location(rimuru)
    except:
        print("    < Error Loading Next Location >")


#                    ========== Extra ==========
def tbc():
    """ To Be Continued message.."""

    print("\n    < ---IN PREOGRESS--- >\n")
    input("Press Enter to exit > ")

def game_text_crawl(arg):
    """
    Updates and gets status for text_crawl.

    Args:
        arg: Enable or disable text crawl.

    Usage:
        > textcrawl
        > textcrawl enable
        > textcrawl 0

    """

    if arg in ['true', 'enable', '1'] or rimuru.text_crawl is True:
        rimuru.text_crawl = True
        print("    < Text Crawl Active >\n")
    elif arg in ['false', 'disable', '0'] or rimuru.text_crawl is False:
        rimuru.text_crawl = False
        print("\n    < Text Crawl Deactivated >\n")

def show_art(art):
    """
    Prints out ASCII art line by line or all at once dependding on text_crawl boolean.

    Args:
        art: Name of variable that is located in game_art.py file. The functions will replace spaces with _ if needed.
    """

    if rimuru.show_ascii is False: return False

    # Gets corresponding variable from within game_art.py file.
    art = eval(f"game_art.{art.lower().strip().replace(' ', '_')}")
    if rimuru.text_crawl:
        for line in art.split('\n'):
            time.sleep(0.05)
            print(line)
    else:
        print(art)


#                    ========== Game Saves ==========
def game_exit(*args):
    """Saves game using pickle, then exits."""

    game_save()
    exit(0)

def game_save(level=None):
    """Pickels Rimuru_Tempest object."""

    if level: rimuru.current_location_object = level
    rimuru.valid_save = True
    pickle.dump(rimuru, open(rimuru.save_path, 'wb'))
    print("\n    < Game Saved >\n")

def game_load(path):
    """
    Load game save.

    Args:
        path: Path of game save.

    Returns:
        Loaded game save object.
    """
    global rimuru

    # Tries loading game. If can't, creates new Rimuru_Tempest object which contains all game data that will be picked.
    try:
        rimuru = pickle.load(open(path, 'rb'))
    except:
        rimuru = mobs.Rimuru_Tempest()
        rimuru.save_path = path

        import chapters.tensei_1 as tensei1
        rimuru.current_location_object = tensei1.Chapter1

    if rimuru.valid_save is False:
        os.remove(rimuru.save_path)
        game_load(path)

    return rimuru

def game_over():
    """Deletes pickle save file."""

    rimuru.valid_save = False  # So you can't use copies of game save.
    os.remove(rimuru.save_path)
    print("\n    < GAME OVER >\n")
    exit(0)


#                    ========== Game Functions ==========
def ssprint(message):
    """Print tabbed in message."""

    if message[0] == '\n': print()
    print('    ', end='')
    sprint(message.strip())

def sprint(message):
    """
    Text crawling. Slowly print out text to console.

    Args:
        message: Message to delay.
    """

    if rimuru.text_crawl:
        message_length = len(message)

        if message_length > 200:
            total_time = 0.1
        elif message_length > 50:
            total_time = 4.5
        elif message_length > 25:
            total_time = 3.5
        elif message_length > 10:
            total_time = 2.5
        else:
            total_time = 2.5

        # Prints letter by letter, resulted speed depends on string length.
        sleep_time = total_time / message_length
        for letter in message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(sleep_time)
        print()

    else:
        print(message)  # Print all lines instantly.

def show_start_banner(rimuru):
    """Show game title, tips, and player stats/inv."""

    print(f"""
    ----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------

    NOTE: 
    - Some basic commands: info, stats, inv, save, and  help for more.
    - Fullscreen recommended.
    """)

    if rimuru.valid_save is True:
        print("\n    < Save Loaded >\n")

def show_help(*args):
    """Shows help page."""

    print("""
    Command Required_Parameter [Optional_Parameter]
    
    Commands:
        inv                         -- Show inventory.
        stats [TARGET]              -- Show yours skills and resistances. E.g. 'stats tempest serpent'
        info TARGET                 -- Show info on skill, item or character. E.g. 'info great sage, 'info hipokte grass', 'info tempest serpent'
        target TARGET(S)            -- Target mobs, target multiple by separating with comma ','. E.g. 'target tempest serpent', 'target tempest serpent, black spider'
        attack with SKILL	        -- Attack targeted_mobs. E.g. 'attack with water blade', 'attack water bullet'
        use SKILL                   -- Use a skill. E.g. 'use sense heat source'
        craft ITEM                  -- Craft items if have necessary ingredients. E.g. 'craft full potion'
                                         NOTE: Some items are crafted in batches, suggest reading the item's info page for the recipe and more.
        textcrawl <on|off>          -- Enable or disable text crawl effect.
        help                        -- Show this help page.
        exit                        -- Exits after save.

    Abilities:
        mimic TARGET                -- Mimics appearance of of predated. E.g. 'mimic tempest serpent'
          - info mimic              -- Shows available mimicries.
          - mimic reset             -- Resets mimic (Back to slime).
        predate                     -- Predate target(s). Can only predate mobs that are targeted_mobs and dead.
        nearby                      -- Once acquired the [sense heat source] skill, you can use nearby instead of typing 'use sense heat source' every time.
                                         

    Game Dialogue:
        ~Message~                   -- Telepathy, thought communication.
        *Message*                   -- Story context.
        < Message >                 -- Game info, acquisition, game help, etc.
        << Message >>               -- Great Sage (Raphael, Ciel).
        <<< Message >>>             -- Voice of the World.

    Level/Ranking:
       Level      Rank         Risk
        11.     Special S   Catastrophe
        10.     S           Disaster
        9.      Special A   Calamity
        8.      A+          Tragedy
        7.      A           Hazard
        6.      A-          Danger
        5.      B           Pro
        4.      C           Advance
        3.      D           Intermediate
        2.      E           Beginner
        1.      F           Novice
    """)
