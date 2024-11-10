class McLarenF1:
    def show_speed(self):
        print("McLaren F1: максимальная скорость 386 км/ч.")

class McLarenP1:
    def show_acceleration(self):
        print("McLaren P1: разгон 0–100 км/ч за 2,8 секунды.")

class McLaren650S:
    def show_comfort(self):
        print("McLaren 650S: уровень комфорта 85/100")

class McLarenMP4_12C:
    def show_technology(self):
        print("McLaren MP4-12C: улучшенная аэродинамика и легкий дизайн")

class McLarenArtura(McLarenF1, McLarenP1, McLaren650S, McLarenMP4_12C):
    def show_features(self):
        print("McLaren Artura: сочетание лучшего из всех предыдущих моделей")
        self.show_speed()
        self.show_acceleration()
        self.show_comfort()
        self.show_technology()
new_mclaren = McLarenArtura()
new_mclaren.show_features()