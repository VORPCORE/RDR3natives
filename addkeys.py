import json
import os

def add_keys_to_json_files(directory):
    # Iterate through all namespace directories
    for namespace in os.listdir(directory):
        namespace_path = os.path.join(directory, namespace)
        if os.path.isdir(namespace_path):
            # Iterate through all JSON files in the namespace directory
            for filename in os.listdir(namespace_path):
                file_path = os.path.join(namespace_path, filename)
                if file_path.endswith('.json'):
                    # Read the JSON content
                    with open(file_path, 'r') as file:
                        data = json.load(file)

                    # Add the new keys to each JSON object if they do not exist
                    for key, content in data.items():
                        if "examples" not in content:
                            content["examples"] = []
                        if "apiset" not in content:
                            content["apiset"] = ""

                    # Write the updated content back to the file
                    with open(file_path, 'w') as file:
                        json.dump(data, file, indent=4)
                    print(f'Updated file: {file_path}')

# Specify the directory containing the namespaces
directory = 'namespaces'
add_keys_to_json_files(directory)