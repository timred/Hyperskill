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


def invalid_route(buses):
    bus_stops = dict()
    for bus in buses:
        try:
            bus_stops[bus["bus_id"]].append(bus["stop_type"])
        except KeyError:
            bus_stops[bus["bus_id"]] = [bus["stop_type"]]

    for bus, stops_list in bus_stops.items():
        if stops_list.count("S") == 1 and stops_list.count("F") == 1:
            continue
        else:
            return bus
    return False


def parse_stop_types(buses, bus_stops):
    stop_types = dict()
    for bus in buses:
        try:
            stop_types[bus["stop_type"]].add(bus["stop_id"])
        except KeyError:
            stop_types[bus["stop_type"]] = {bus["stop_id"]}

    bus_lines = parse_lines(buses)
    for stop in bus_stops.keys():
        counter = 0
        for line in bus_lines.values():
            if stop in line:
                counter += 1
        if counter >= 2:
            try:
                stop_types["T"].add(stop)
            except KeyError:
                stop_types["T"] = {stop}
    return stop_types


def stops(buses):
    bus_stops = dict()
    for bus in buses:
        bus_stops[bus["stop_id"]] = bus["stop_name"]
    return bus_stops


def parse_lines(buses):
    bus_lines = dict()
    for bus in buses:
        try:
            bus_lines[bus["bus_id"]].add(bus["stop_id"])
        except KeyError:
            bus_lines[bus["bus_id"]] = {bus["stop_id"]}
    return bus_lines


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


def print_bus_stops(bus_stops):
    print("Line names and number of stops:")
    for bus, stops_list in bus_stops.items():
        print(f"bus_id: {bus}, stops: {len(stops_list)}")


def print_stop_types(stop_types, bus_stops):
    print(f"Start stops: {len(stop_types['S'])} {sorted([bus_stops[stop] for stop in stop_types['S']])}")
    print(f"Transfer stops: {len(stop_types['T'])} {sorted([bus_stops[stop] for stop in stop_types['T']])}")
    print(f"Finish stops: {len(stop_types['F'])} {sorted([bus_stops[stop] for stop in stop_types['F']])}")


def invalid_times(buses):
    return_value = False

    bus_times = dict()
    for bus in buses:
        try:
            bus_times[bus["bus_id"]].append(bus)
        except KeyError:
            bus_times[bus["bus_id"]] = [bus]

    print("Arrival time test:")
    for bus, detail in bus_times.items():
        current_time = detail[0]["a_time"]
        for stop in detail[1:]:
            next_time = stop["a_time"]
            if current_time >= next_time:
                print(f"bus_id line {bus}: wrong time on station {stop['stop_name']}")
                return_value = True
                break
            current_time = next_time

    if not return_value:
        print("OK")

    return return_value


if __name__ == "__main__":
    easy_rider = json.loads(input())
    easy_rider_stops = stops(easy_rider)
    easy_rider_stop_types = parse_stop_types(easy_rider, easy_rider_stops)
    print("On demand stops test:")
    wrong_stops = set()
    try:
        on_demand = easy_rider_stop_types["O"]

        for stop_type, stops in easy_rider_stop_types.items():
            if stop_type != "O":
                wrong_stops |= on_demand.intersection(stops)
    except KeyError:
        pass
    if wrong_stops:
        print(f"Wrong stop type: {sorted([easy_rider_stops[wrong_stop] for wrong_stop in wrong_stops])}")
    else:
        print("OK")
