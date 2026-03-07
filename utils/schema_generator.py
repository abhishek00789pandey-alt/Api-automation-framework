import json
from genson import SchemaBuilder


def generate_schema(data, output_file):

    builder = SchemaBuilder()
    builder.add_object(data)

    schema = builder.to_schema()

    with open(output_file, "w") as f:
        json.dump(schema, f, indent=4)

    print(f"Schema generated and saved to {output_file}")