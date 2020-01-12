class Bus:
    def __init__(self, driver):
        self.driver = driver

    @property
    def driver(self):
        print("Get driver")
        return self._driver

    @driver.setter
    def driver(self, new_driver):
        if new_driver == "Dog":
            print("Set driver as {} failed! A driver must be human!".format(new_driver))
        else:
            print("Set driver {}".format(new_driver))
            self._driver = new_driver


if __name__ == "__main__":
    bus = Bus('Bob')
    print(bus.driver)
    bus.driver = 'Helen'
    print(bus.driver)
    bus.driver = 'Dog'
    print(bus.driver)