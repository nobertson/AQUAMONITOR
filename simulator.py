import random
from datetime import datetime, timezone


def read_sensors(step: int) -> dict:
    """Simulated readings. Replace with real sensor code (serial, MQTT, etc.)."""
    temp = 28 + 2 * random.uniform(-1, 1)
    ph = 7.5 + 0.3 * random.uniform(-1, 1)
    oxygen = 7 + 0.8 * random.uniform(-1, 1)
    turbidity = 15 + 5 * random.uniform(-1, 1)

    # Inject faults so the alerting logic can be demonstrated
    if step % 40 == 0:
        oxygen -= 3.5      # sudden oxygen drop
    if step % 55 == 0:
        temp = None        # sensor dropout

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "temperature_c": temp,
        "ph": ph,
        "dissolved_oxygen_mg_l": oxygen,
        "turbidity_ntu": turbidity,
    }
