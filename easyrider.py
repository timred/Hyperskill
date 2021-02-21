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
            "regex": "^([A-Za-z][A-Za-z\s]+ ([Rr]oad|[Aa]venue|[Bb]oul{1,2}evard|[Ss]treet|St\.|Str\.|Av\.)|Elm)$"
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
            if "regex" in field.keys() and not re.match(field["regex"], bus_field_value):
                errors[field["name"]] += 1
                continue

    errors["total"] = 0
    for e, v in errors.items():
        if e != "total":
            errors["total"] += v

    return errors


if __name__ == "__main__":
    easy_rider = json.loads(input())
    invalid = invalid_buses(easy_rider)
    print(f"Type and required field validation: {invalid['total']} errors")
    for error, value in invalid.items():
        if error != "total":
            print(f"{error}: {value}")
