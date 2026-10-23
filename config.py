SENSOR_KEYS = ["temperature_c", "ph", "dissolved_oxygen_mg_l", "turbidity_ntu"]

# Acceptable operating ranges (adjust for your species)
THRESHOLDS = {
    "temperature_c": (24.0, 32.0),
    "ph": (6.5, 9.0),
    "dissolved_oxygen_mg_l": (5.0, 12.0),
    "turbidity_ntu": (0.0, 50.0),
}

# Physically possible ranges, used to reject faulty sensor values
VALID_RANGES = {
    "temperature_c": (0, 50),
    "ph": (0, 14),
    "dissolved_oxygen_mg_l": (0, 20),
    "turbidity_ntu": (0, 1000),
}
