from .tfl import tflAPI
from typing import Literal


class journey(tflAPI):
    def getJourneyModes(self):
        return super(journey, self).sendRequestUnified(
            "/Journey/Meta/Modes")
    def getJourneyResults(self, origin: str, destination: str, via: str, nationalSearch: bool, date: str, time: str, timeIs):
        pass