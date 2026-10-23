import unittest

from validation import check_thresholds, validate

BASE = {"timestamp": "t", "temperature_c": 28, "ph": 7.5,
        "dissolved_oxygen_mg_l": 7, "turbidity_ntu": 15}


class TestValidation(unittest.TestCase):
    def test_missing_reading_is_flagged(self):
        _, issues = validate(dict(BASE, temperature_c=None))
        self.assertEqual(len(issues), 1)

    def test_impossible_ph_is_rejected(self):
        clean, _ = validate(dict(BASE, ph=15))
        self.assertIsNone(clean["ph"])

    def test_low_oxygen_raises_alert(self):
        alerts = check_thresholds(dict(BASE, dissolved_oxygen_mg_l=3.0))
        self.assertTrue(any("LOW dissolved_oxygen" in a for a in alerts))

    def test_normal_values_raise_no_alerts(self):
        self.assertEqual(check_thresholds(BASE), [])


if __name__ == "__main__":
    unittest.main()
    