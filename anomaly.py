from collections import deque
from statistics import mean, stdev


class RollingAnomalyDetector:
    """Flags values far from the recent average (rolling z-score)."""

    def __init__(self, window=30, z_limit=3.0, min_points=10):
        self.window = window
        self.z_limit = z_limit
        self.min_points = min_points
        self.history = {}

    def check(self, key, value):
        """Return the z-score if the value is anomalous, otherwise None."""
        if value is None:
            return None
        buffer = self.history.setdefault(key, deque(maxlen=self.window))
        result = None
        if len(buffer) >= self.min_points:
            spread = stdev(buffer)
            if spread > 0:
                z = (value - mean(buffer)) / spread
                if abs(z) >= self.z_limit:
                    result = z
        buffer.append(value)
        return result
    