import uuid

class Event:
    def __init__(self, name):
        self.callbacks = {}
        self.name = name

    def __str__(self):
        return "[EVENT] " + self.name + ", " + str(len(self.callbacks)) + " listener" + ("s", "")[len(self.callbacks) == 1]

    def listen(self, callback):
        id = uuid.uuid1().hex
        self.callbacks[id] = callback
        return id

    def fire(self, data):
        for callback in self.callbacks.values():
            callback(data)

    def removeListener(id):
        if (callbacks[id]):
            del callbacks[id]


# Called when either of the bumper buttons has been pressed / released
# Fields:
#   io.Direction side - the side of the button that was pressed / released from the car's prespective
BumperPressEvent = Event("BumperPressEvent")
BumperReleaseEvent = Event("BumperReleaseEvent")

# Called when the balloon button has been pressed, indicating that it has been popped
BalloonEvent = Event("BalloonEvent")
