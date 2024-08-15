from src.events.event_manger import EventManager


class EventManagerFactory:
    def __call__(self) -> EventManager:
        return EventManager()
