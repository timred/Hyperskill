import json
import re

bus_schema = {
    "fields": [
        {
            "name": "bus_id",
            "type": int,
            "required": True
        },
        {
            "name": "stop_id",
            "type": int,
            "required": True
        },
        {
            "name": "stop_name",
            "type": str,
            "required": True,
            "min_length": 1,
            "regex": "^[A-Z][A-Za-z\\s]+ (Road|Avenue|Boulevard|Street)$"
        },
        {
            "name": "next_stop",
            "type": int,
            "required": True
        },
        {
            "name": "stop_type",
            "type": str,
            "required": False,
            "length": 1,
            "values": ["S", "O", "F"]
        },
        {
            "name": "a_time",
            "type": str,
            "required": False,
            "regex": "^([01][0-9]|2[0-3]):?([0-5][0-9])$"
        }
    ]
}


def invalid_buses(buses):
    errors = {field["name"]: 0 for field in bus_schema["fields"]}

    for bus in buses:
        for field in bus_schema["fields"]:
            bus_field_value = bus[field["name"]]
            if not isinstance(bus_field_value, field["type"]):
                errors[field["name"]] += 1
                continue
            if "length" in field.keys() and len(bus_field_value) != field["length"]:
                if field["required"] or len(bus_field_value) > 0:
                    errors[field["name"]] += 1
                    continue
            if "min_length" in field.keys() and len(bus_field_value) < field["min_length"]:
                if field["required"] or len(bus_field_value) > 0:
                    errors[field["name"]] += 1
                    continue
            if "values" in field.keys() and bus_field_value not in field["values"]:
                if field["required"] or len(bus_field_value) > 0:
                    errors[field["name"]] += 1
                    continue
            if "regex" in field.keys() and re.match(field["regex"], bus_field_value) is None:
                errors[field["name"]] += 1
                continue

    errors["total"] = 0
    for e, v in errors.items():
        if e != "total":
            errors["total"] += v

    return errors


def print_type_required_validation(invalid_data):
    print(f"Type and required field validation: {invalid_data['total']} errors")
    for error, value in invalid_data.items():
        if error != "total":
            print(f"{error}: {value}")


def print_format_validation(invalid_data):
    format_fields = ["stop_name", "stop_type", "a_time"]
    print(f"Format validation: {invalid_data['total']} errors")
    for error, value in invalid_data.items():
        if error != "total" and error in format_fields:
            print(f"{error}: {value}")


if __name__ == "__main__":
    easy_rider = json.loads(input())
    invalid = invalid_buses(easy_rider)
    print_format_validation(invalid)
