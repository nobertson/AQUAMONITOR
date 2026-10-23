import argparse
import time

from anomaly import RollingAnomalyDetector
from config import SENSOR_KEYS
from simulator import read_sensors
from storage import Storage
from validation import check_thresholds, validate


def run(cycles: int, interval: float):
    db = Storage()
    detector = RollingAnomalyDetector()
    for step in range(1, cycles + 1):
        raw = read_sensors(step)
        clean, issues = validate(raw)

        alerts = [f"DATA {issue}" for issue in issues]
        alerts += check_thresholds(clean)
        for key in SENSOR_KEYS:
            z = detector.check(key, clean.get(key))
            if z is not None:
                alerts.append(f"ANOMALY {key}: z-score {z:+.1f}")

        db.save_reading(clean)
        for alert in alerts:
            db.save_alert(clean["timestamp"], alert)
            print(f"[{clean['timestamp']}] ALERT {alert}")
        time.sleep(interval)
    db.close()
    print("Run complete. Data saved to aqua.db")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aquaculture water monitoring prototype")
    parser.add_argument("--cycles", type=int, default=100)
    parser.add_argument("--interval", type=float, default=0.1, help="seconds between readings")
    args = parser.parse_args()
    run(args.cycles, args.interval)
    