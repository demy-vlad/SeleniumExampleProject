import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links_test_ru(self):
        homepage_nav = HomepageNav(self.driver)
        assert homepage_nav.NAV_LINK_TEXT_RU == homepage_nav.get_nav_links_text_ru()

    def test_nav_links_test_ua(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.get_header_lang_ua().click()
        assert homepage_nav.NAV_LINK_TEXT_UA == homepage_nav.get_nav_links_text_ua()