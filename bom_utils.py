import re
import consts


def check_vendors(part_name):
    for attribute, value in consts.__dict__.items():
        if re.search("SDS", part_name):
            return part_name, "https://www.swervedrivespecialties.com/", "Swerve Drive Specialties"
        if attribute.endswith("REGEX"):
            pattern = re.compile(value)
            match = re.search(pattern, part_name)
            if match:
                sku_part = match[1]
                link_pattern = getattr(consts, attribute.replace("REGEX", "LINK"))
                link = link_pattern.format(SKU=sku_part)
                return sku_part, link, attribute.replace("_REGEX", "")

    return False


def analyze_part(part_name):
    try:
        part_sku, machine_letters = part_name.split('-')
    except Exception:
        print(f"Bad part name! {part_name}")
        return part_name, []
    machines = []
    for letter_machine in machine_letters:
        try:
            machines += [getattr(consts, letter_machine.upper() + "_MACHINE")]
        except AttributeError:
            print(f"Bad Machine {letter_machine}!")
            exit(1)
    return part_sku, machines


