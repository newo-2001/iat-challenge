class Event:
    def __init__(self, name):
        self.callbacks = []
        self.name = name

    def __str__(self):
        return "[EVENT] " + self.name + ", " + str(len(self.callbacks)) + " listener" + ("s", "")[len(self.callbacks) == 1]

    def listen(self, callback):
        self.callbacks.append(callback)

    def fire(self, data):
        for callback in self.callbacks:
            callback(data)


# Called when either of the bumper buttons has been pressed
# Fields:
#   io.Direction side - the side of the button that was pressed from the car's prespective
BumperEvent = Event("BumperEvent")

# Called when the balloon button has been pressed, indicating that it has been popped
BalloonEvent = Event("BalloonEvent")
