# Abstract Factory

```Python
class DecimalFactory(object):
    @staticmethod
    def build(string):
        return Decimal(string.lstrip('$'))
```