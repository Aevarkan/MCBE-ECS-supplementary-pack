import json
import os
import re

# Path and the scale value we want
folder_path = "./behavior_pack/entities"
default_scale_value = {"value": 1}

# Exceptions
exclusions = ['huntable_adult', 'unhuntable_adult']

exclusion_pattern = '|'.join(map(re.escape, exclusions))
# Can't get it to work though, but there's only 1 file

# Only need to manually edit salmon and hoglins
# Everything else should be fine

baby_pattern = re.compile(
    r'(?<!is_)_baby\b',
    re.IGNORECASE
)

# adult_pattern = re.compile(
#     rf'^(?!.*(?:{exclusion_pattern}))(?<!is_)_adult\b',
#     re.IGNORECASE
# )

adult_pattern = re.compile(
    r'(?<![^\s_])adult\b',
    re.IGNORECASE
)



def add_to_components(data):
    if "components" in data.get("minecraft:entity", {}):
        components = data["minecraft:entity"]["components"]
        if "minecraft:scale" not in components:
            components["minecraft:scale"] = default_scale_value
            print(f"Added 'minecraft:scale' to {filename}")

# Loop through each JSON file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        
        # Remove comments using regular expression first
        with open(file_path, 'r', encoding='utf-8') as file:
            json_content = file.read()
            json_content = re.sub(r'//.*', '', json_content)

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.loads(json_content)
        
        # Check if component_groups exists
        if "component_groups" in data.get("minecraft:entity", {}):
            component_groups = data["minecraft:entity"]["component_groups"]
            
            baby_groups = [group for group in component_groups if baby_pattern.search(group)]
            adult_groups = [group for group in component_groups if adult_pattern.search(group)]


            if baby_groups and adult_groups:
                for baby_group in baby_groups:
                    for adult_group in adult_groups:
                        # Check if "minecraft:scale" exists in baby group
                        if "minecraft:scale" in component_groups[baby_group]:
                            # Check if "minecraft:scale" doesn't exist in adult group
                            if "minecraft:scale" not in component_groups[adult_group]:
                                # Add "minecraft:scale" to adult group
                                component_groups[adult_group]["minecraft:scale"] = default_scale_value
                                print(f"Added 'minecraft:scale' to '{adult_group}' in {filename}")

            else:
                add_to_components(data)
            
            # Adds scale component for everything else
        else:
            if "components" in data.get("minecraft:entity", {}):
                components = data["minecraft:entity"]["components"]
                if "minecraft:scale" not in components:
                    components["minecraft:scale"] = default_scale_value
                    print(f"Added 'minecraft:scale' to {filename}")

        # Write the modified JSON back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

