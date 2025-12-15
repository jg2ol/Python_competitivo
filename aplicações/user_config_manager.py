def add_setting(dic_config, item):
    key = item[0].lower()
    value = item[1].lower()
    if key in dic_config.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    dic_config[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dic_config, item):
    key = item[0].lower()
    value = item[1].lower()
    if key in dic_config.keys():
        dic_config[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dic_config, key):
    key = key.lower()
    if key in dic_config.keys():
        dic_config.pop(key)
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(dic_config):
    if dic_config == {}:
        return "No settings available."
    str_return = "Current User Settings:\n"
    for key, value in dic_config.items():
        str_return += f"{key.capitalize()}: {value}\n"
    return str_return

print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(update_setting({'theme': 'light'}, ('theme', 'dark')))
print(update_setting({'theme': 'light'}, ('volume', 'high')))
print(delete_setting({'theme': 'light'}, 'theme'))
print(delete_setting({"oi": "alo"}, "a"))
print(view_settings({}))
test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
print(view_settings(test_settings))
