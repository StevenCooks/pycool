class Car(object):

    def __init__(self, brand, model, template):
        self.brand = brand
        self.model = model
        self.template = template

    def get_brand(self):
        return self.brand
