from plone.app.contentrules.handlers import execute_rules

def usefulness_rated(event):
    execute_rules(event)
