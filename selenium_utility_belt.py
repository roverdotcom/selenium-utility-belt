from selenium import webdriver

class SeleniumUtilityBelt(object):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        super(SeleniumUtilityBelt, self).setUp()

    def open(self, url):
        self.driver.get("%s%s" % (self.live_server_url, url))

    def find(self, selector):
        return self.driver.find_elements_by_css_selector(selector)

    def get_classes(self, element):
        return element.get_attribute('class').split(' ')

    def get_elements_or_raise(self, selector):
        elements = self.find(selector)

        if not elements:
            raise AssertionError('{} is not on the page'.format(selector))

        return elements

    def assertHasClass(self, selector, cls):
        elements = self.get_elements_or_raise(selector)

        for element in elements:
            classes = self.get_classes()
            if not cls in classes:
                raise AssertionError(
                    "All {}'s do not have the class {}".format(selector, cls))

    def assertOnPage(self, selector, visible=None):
        elements = self.get_elements_or_raise(selector)

        if visible is not None:
            for element in elements:
                displayed = element.is_displayed()
                if visible and not displayed:
                    raise AssertionError(
                        '{} is not visible on the page'.format(selector))
                elif not visible and displayed:
                    raise AssertionError(
                        '{} is visible on the page'.format(selector))
