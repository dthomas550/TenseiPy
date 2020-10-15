import game_files.game_skills as game_skills
import game_files.game_items as game_items
import game_files.game_characters as game_characters
from .character_info import Info
from .character_inventory import Inventory
from .character_attributes import Attributes
from .character_combat import Combat
from .character_subordinates import Subordinates
from .character_map import Map


class Character(Info, Attributes, Inventory, Combat, Subordinates, Map):
    def __init__(self):
        # Main character attributes, inventory, skills, resistances, etc.
        self.starting_state = []
        self.friends = self.subordinates = {'Special S': {}, 'S': {}, 'Special A': {}, 'A+': {}, 'A': {},
                                            'A-': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'Other': {}}

        self.attributes = {'Manas': {},
                           'Ultimate Skill': {},'Unique Skill': {},'Special Skill': {},'Extra Skill': {},'Intrinsic Skill': {},
                           'Common Skill': {},'Daily Skill': {},'Composite Skill': {},'Resistance': {},'Attribute': {}}

        # Character inventory.
        self.inventory_capacity = 0  # Inventory capacity in percentage.
        self.inventory_capacity_add = 0  # Add to overall capacity when adding items to inventory.
        self.quantity = 0  # Item quantity in inventory.
        self.quantity_add = 1  # Usually items are added in batches, E.g. Hipokte Grass, Magical Ore.
        self.inventory = {'Items': {}, 'Materials': {}, 'Consumable': {},'Misc': {}}

        # Character information and data related variables.
        self.name = 'N/A'
        self.family_name = ''
        self.canon_name = 'N/A'  # Name from anime or manga storyline.
        self.title = 'N/A'  # E.g. True Dragon, Demon Lord.
        self.blessing = 'N/A'  # E.g. Storm Crest (from Veldora)>
        self.shared_blessing = 'N/A'
        self.species = 'N/A'
        self.rank = 'N/A'  # E.g. Catastrophe, Calamity.
        self.level = 1  # Same as rank just as integer.
        self.info_page = 'N/A'  # Info page for character.
        self.description = 'N/A'
        self.appearance = 'N/A'
        self.evolution = ''
        self.acquired_msg = ''
        self.is_alive = True

        # Combat variables.
        self.active_mobs = []  # Current mobs around you that you can interact or attack.
        self.targeted_mobs = []  # Targets that will be attacked with 'attack' command.

        # Map functionality.
        self.available_locations = []
        self.current_location = 'N/A'

        # Game variables.
        self.game_object_type = 'character'
        self.story_progress = [None]
        self.save_path = ''
        self.valid_save = None
        self.text_crawl = None
        self.show_ascii = True

    def set_start_state(self):
        """Adds corresponding starter attributes and items to character."""

        for i in self.starting_state:
            self.add_attribute(i, show_acquired_msg=False)

    def get_object(self, match, item_pool=[], new=False, stricter=True):
        """
        Can take in either a str or obj, then returns object (initialized if not already in inventory).

        Args:
            item_pool: List of game items to search against.
            new: If first time adding a new object to character.
            stricter: Find more of a exact match, still cane insensitive. For example, sometimes Sage will be returned instead of Great Sage.

        Returns:
            Corresponding object, will initialize if one hasn't been already in inventory.
            False: If inputted item cannot be used to find object.

        Usage:
            .get_object('great sage')
            .get_object('hipokte grass')
        """

        if new: item_pool = ([*game_items.Item.__subclasses__(), *game_skills.Skill.__subclasses__(), *game_characters.Character.__subclasses__()])

        if 'character' in self.game_object_type:
            item_pool.extend([*self.inventory_generator(), *self.attributes_generator()])

        for game_object in item_pool:
            if type(game_object) is str: continue

            if new:
                try: game_object = game_object()
                except: pass

            if stricter:
                if str(game_object) == str(match).lower().strip():
                    return game_object
            elif str(game_object) in str(match).lower():
                return game_object

            if new: del game_object

        return None

    def check_acquired(self, check_object):
        """
        Checks to see if character has object/attribute/item/etc.

        Args:
            check_object: Object to check if specified character has item, attribute, skill, etc.

        Returns:
            Boolean: If specified character has attribute or object.

        Usage:
            .check_acquired('resist poison')
        """

        if item := self.get_object(check_object):
            return item
        else: return False

    def __str__(self): return self.name.lower()
