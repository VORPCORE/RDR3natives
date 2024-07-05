import json
import os
import jsonschema

def merge_json_namespaces(output_file, schema_file):
    input_dir = 'namespaces'
    if not os.path.exists(input_dir):
        print(f"Input directory {input_dir} does not exist")
        return

    merged_data = {}

    for namespace in sorted(os.listdir(input_dir)):
        namespace_path = os.path.join(input_dir, namespace)
        if os.path.isdir(namespace_path):
            namespace_data = {}
            files = sorted(os.listdir(namespace_path))
            
            for file in files:
                file_path = os.path.join(namespace_path, file)
                with open(file_path, 'r') as infile:
                    data = json.load(infile)
                    namespace_data.update(data)
            
            merged_data[namespace] = namespace_data

    with open(schema_file, 'r') as file:
        schema = json.load(file)

    try:
        jsonschema.validate(instance=merged_data, schema=schema)
        print("Merged JSON is valid according to the schema.")
    except jsonschema.exceptions.ValidationError as err:
        print(f"Validation error: {err.message}")

    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile, indent=4)
    print(f'Merged JSON written to {output_file}')


output_file = 'rdr3natives.json'
schema_file = 'schema.json'

merge_json_namespaces(output_file, schema_file)
