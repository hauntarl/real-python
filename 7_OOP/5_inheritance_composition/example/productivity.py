# a class that conforms to IWorker interface from the UML diagrom can be used
# in track() of the ProductivitySystem.
# UML: https://files.realpython.com/media/ic-class-explosion.a3d42b8c9b91.jpg
# NOTE: from the UML, as you can see things are starting to get pretty messy,
# if requirements change or we need to add a new features then the number of
# classes we create might start growing exponentially, this is called the
# Class Explosion Problem. One way to counter it is using multiple inheritance
class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking employee productivity')
        print('=' * 20)
        for e in employees:
            e.work(hours)
            print()
