import thing

from builder import ThingBuilder

class ThingFactory(object):
    @staticmethod
    def create(name: str):
        builder = ThingBuilder()

        builder.build()
        builder.build_name(name)

        return builder.get_instance()

if __name__ == "__main__":
    result = ThingFactory.create("thing1")

    print(repr(result))
