from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Helpers import get_option_value

    if category_name == "ORB01":
       return get_option_value(multiworld, player, "player_access") >= 1
    if category_name == "ORB02":
        return get_option_value(multiworld, player, "player_access") >= 2
    if category_name == "ORB03":
        return get_option_value(multiworld, player, "player_access") >= 3
    if category_name == "ORB04":
        return get_option_value(multiworld, player, "player_access") >= 4
    if category_name == "ORB05":
        return get_option_value(multiworld, player, "player_access") >= 5
    if category_name == "ORB06":
        return get_option_value(multiworld, player, "player_access") >= 6
    if category_name == "ORB07":
        return get_option_value(multiworld, player, "player_access") >= 7
    if category_name == "ORB08":
        return get_option_value(multiworld, player, "player_access") >= 8
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
