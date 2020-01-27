import events

def callbackFunc(event):
    print("[CALLBACK] " + event["text"])

def main():
    print("Hello world!")

    events.BumperEvent.listen(callbackFunc)

    events.BumperEvent.fire({
        "text": "Some event data"
    })

    print(events.BumperEvent)

if __name__ == "__main__":
    main()
else:
    print("This file cannot be loaded as a module")
