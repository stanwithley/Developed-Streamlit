class Trip:
    # all_cities از قبل مقداردهی شده (مثلاً در فایل اولیه)،
    # اگر نه باید اینجا مقدار دهی شود.
    all_cities = ("Tehran", "Mashhad", "Isfahan", "Shiraz", "Tabriz")  # مثال

    def __init__(self, train, origin_city, destination_city, passengers=None):
        self.train = train
        self.origin_city = origin_city
        self.destination_city = destination_city
        self.passengers = passengers if passengers is not None else []

    def origin_city_validation(self, origin_city):
        if origin_city not in Trip.all_cities:
            raise Exception("This input is not a verified city!")
        if origin_city == self.destination_city:
            raise Exception("Origin and destination cities can't be the same!")
        if origin_city != self.train.last_visited_city:
            raise Exception("The train of the trip is not available in the origin city!")
        return origin_city

    def train_validation(self, train):
        from types import MethodType
        # بررسی نوع (یا isinstance)
        if not isinstance(train, Train):
            raise Exception("This input is not a train!")
        if train.is_on_trip:
            raise Exception("This train is not available!")
        return train

    def __call__(self):
        # ظرفیت باقی‌مانده = ظرفیت کل - مجموع وزن بار مسافران
        total_load = sum(p.load_weight for p in self.passengers)
        remaining_capacity = self.train.weight_capacity - total_load
        return remaining_capacity


class Passenger:
    def __init__(self, fullname, load_weight):
        self.fullname = fullname
        self.load_weight = load_weight

    def attend_trip(self, trip):
        # ظرفیت باقی‌مانده قطار در این سفر
        remaining_capacity = trip()
        if self.load_weight <= remaining_capacity:
            trip.passengers.append(self)
        else:
            raise Exception("Heavy load!")

    def cancel_trip(self, trip):
        if self in trip.passengers:
            trip.passengers.remove(self)
        else:
            raise Exception("This passenger is not attended to this trip!")

    def __str__(self):
        return self.fullname
