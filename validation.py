from config import VALID_RANGES, THRESHOLDS


def validate(reading: dict):
    """Return (clean_reading, issues). Missing or impossible values become None."""
    clean, issues = dict(reading), []
    for key, (low, high) in VALID_RANGES.items():
        value = reading.get(key)
        if value is None:
            issues.append(f"{key}: missing reading")
        elif not low <= value <= high:
            issues.append(f"{key}: impossible value {value}")
            clean[key] = None
    return clean, issues


def check_thresholds(clean: dict):
    """Return alert messages for values outside the acceptable range."""
    alerts = []
    for key, (low, high) in THRESHOLDS.items():
        value = clean.get(key)
        if value is None:
            continue
        if value < low:
            alerts.append(f"LOW {key}: {value:.2f} (min {low})")
        elif value > high:
            alerts.append(f"HIGH {key}: {value:.2f} (max {high})")
    return alerts
