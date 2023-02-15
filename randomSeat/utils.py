from .dataStruct import *

class SeatArragement:
    def __init__(self,  seat_format: str) -> None:
        seat_chart = []
        for i in seat_format.split('\n'):
            seat_chart.append([Aisle() if j==' ' else Seat() for j in i])
        self.seat_chart: list[list[Seat|Aisle]] = seat_chart

    def __repr__(self) -> str:
        return f''
            

class Seat:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f'<Seat()>'


class Aisle:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f'<Aisle()>'




