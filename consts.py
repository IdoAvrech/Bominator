PART_NAME = "PART NUMBER"
COUNT = "QTY."
DESCRIPTION = "DESCRIPTION"

part_regex = ".+-(\w+)"

# vendors
VEXPRO_REGEX = ".*(217-\d\d\d\d).*"
VEXPRO_LINK = "https://www.vexrobotics.com/{SKU}.html"

ANDYMARK_REGEX = ".*(am-\d\d\d\d).*"
ANDYMARK_LINK = "https://www.andymark.com/search?q={SKU}"

THRIFTY_REGEX = ".*(TTB-\d\d\d\d).*"
THRIFTY_LINK = "https://www.thethriftybot.com/bearings/search?keywords={SKU}"

MCMASTER_REGEX = "(\d{4,5}[A-Z]\d{2,3})"
MCMASTER_LINK = "https://www.mcmaster.com/{SKU}/"

REVROBOTICS_REGEX = ".*(REV-\d\d-\d\d\d\d).*"
REVROBOTICS_LINK = "https://www.revrobotics.com/{SKU}/"

# machines
P_MACHINE = "3D printer"
C_MACHINE = "CNC Router"
L_MACHINE = "Lathe"
M_MACHINE = "Mill"
G_MACHINE = "Miter saw"
O_MACHINE = "Outsourcing"
T_MACHINE = "Tapping"