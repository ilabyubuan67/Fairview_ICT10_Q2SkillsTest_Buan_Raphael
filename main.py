from pyscript import document,display

# Variable and values
nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Flourine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon",18, 39.948),

    "Se": ("Selenium", 34,	78.971),
    "Br": ("Bromine",	35,	79.904),
    "Kr": ("Krypton",	36,	83.798),
    "I":	("Iodine",	53,	126.90),
    "Xe":	("Xenon",	54,	131.29),
    "Rn":	("Radon",   86,  222),
}

def add_element(e):
    # Gets the value from what they inputted in the textbox
    element_symbol = document.getElementById("element_symbol").value.strip()
    element_data = nonmetals.get(element_symbol, ("Not Found", "N/A",))

    element_name = element_data[0]
    element_number = element_data[1]
    atomic_mass = element_data[2]
# Result
    document.getElementById("output1").innerHTML = f"""
    <p>Element: {element_symbol}</p>
    <p>Element Name: {element_data[0]}</p>
    <p>Atomic Number: {element_data[1]}</p>
    <p>Atomic Mass: {element_data[2]}</p """