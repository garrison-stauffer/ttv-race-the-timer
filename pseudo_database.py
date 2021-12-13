

class PseudoDatabase:

    def __init__(self):
        print("instantiated database")

    def register_timer(self, timer_name):
        print("registering " + timer_name)

    def get_timer(self, timer_name):
        print("fetching " + timer_name)


db = PseudoDatabase()
