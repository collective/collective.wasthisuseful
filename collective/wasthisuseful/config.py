"""Common configuration constants
"""

PROJECTNAME = 'collective.wasthisuseful'

STORAGE_KEY = 'usefulness'  # key for annotation storage of ratings
KEY_USEFUL = 'useful'  # see _createVote
KEY_COMMENT = 'comment'  # see _createVote
KEY_DATE = 'date'  # see _createVote
KEY_IP = 'ip_address'  # see _createVote

SETTINGS_KEY = 'usefulness_settings'  # key for rating settings
CHILDREN_ENABLED = 'children_enabled'  # are ratings enabled on children
ITEM_ENABLED = 'item_enabled'  # are ratings enabled on this item

FORM_FIELD_USEFUL = 'useful'  # equals form field in useful.pt
FORM_FIELD_COMMENT = 'comment'  # equals form field in useful.pt
