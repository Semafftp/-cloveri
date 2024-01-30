import time
from generator.generator import generated_file

from locators.elements_main_page_locators import StepTasksPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = StepTasksPageLocators()

    def all_tasks(self):
        self.element_is_visible(self.locators.ALL_TASKS).click()


class LogoOhCannonPage(BasePage):
    locators = StepTasksPageLocators()

    def logo_oh_cannon(self):
        path = generated_file()
        self.element_is_visible(self.locators.LOGO_OH_CANNON).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.YOUR_MAIL).send_keys("stage@stage.com")
        self.element_is_visible(self.locators.LINK_TO_THE_JOB).send_keys("https://www.resizepixel.com/ru/download")
        self.element_is_present(self.locators.DOWNLOAD_FILE).send_keys("G:\pythonProject\step.skroy.ru\img\sampleFile.pdf")
        self.element_is_visible(self.locators.COMMENT).send_keys("keyword")
        time.sleep(5)


class CompetitionNumber2Page(BasePage):
    locators = StepTasksPageLocators()

    def competition_number2(self):
        self.element_is_visible(self.locators.COMPETITION_NUMBER_2).click()
        self.element_is_visible(self.locators.LOGO_OH_CANNON).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.YOUR_MAIL).send_keys("stage@stage.com")
        self.element_is_visible(self.locators.LINK_TO_THE_JOB).send_keys("https://www.resizepixel.com/ru/download")
        self.element_is_present(self.locators.DOWNLOAD_FILE).send_keys(
            "G:\pythonProject\step.skroy.ru\img\sampleFile.pdf")
        self.element_is_visible(self.locators.COMMENT).send_keys("keyword")
        time.sleep(5)


class LandingPageForTheCoursePage(BasePage):
    locators = StepTasksPageLocators()

    def landing_page_for_the_course(self):
        self.element_is_visible(self.locators.LANDING_PAGE_FOR_THE_COURSE).click()
        self.element_is_visible(self.locators.LOGO_OH_CANNON).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.YOUR_MAIL).send_keys("stage@stage.com")
        self.element_is_visible(self.locators.LINK_TO_THE_JOB).send_keys("https://www.resizepixel.com/ru/download")
        self.element_is_present(self.locators.DOWNLOAD_FILE).send_keys(
            "G:\pythonProject\step.skroy.ru\img\sampleFile.pdf")
        self.element_is_visible(self.locators.COMMENT).send_keys("keyword")
        time.sleep(5)


class LogoForTheProjectPage(BasePage):
    locators = StepTasksPageLocators()

    def logo_for_the_project(self):
        self.element_is_visible(self.locators.LOGO_FOR_THE_PROJECT).click()
        self.element_is_visible(self.locators.LOGO_OH_CANNON).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.YOUR_MAIL).send_keys("stage@stage.com")
        self.element_is_visible(self.locators.LINK_TO_THE_JOB).send_keys("https://www.resizepixel.com/ru/download")
        self.element_is_present(self.locators.DOWNLOAD_FILE).send_keys(
            "G:\pythonProject\step.skroy.ru\img\sampleFile.pdf")
        self.element_is_visible(self.locators.COMMENT).send_keys("keyword")
        time.sleep(5)


class LogoContestPage(BasePage):
    locators = StepTasksPageLocators()

    def logo_contest(self):
        self.element_is_visible(self.locators.LOGO_CONTEST).click()
        self.element_is_visible(self.locators.LOGO_OH_CANNON).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.YOUR_MAIL).send_keys("stage@stage.com")
        self.element_is_visible(self.locators.LINK_TO_THE_JOB).send_keys("https://www.resizepixel.com/ru/download")
        self.element_is_present(self.locators.DOWNLOAD_FILE).send_keys(
            "G:\pythonProject\step.skroy.ru\img\sampleFile.pdf")
        self.element_is_visible(self.locators.COMMENT).send_keys("keyword")
        time.sleep(5)


class LogoForTheStepPage(BasePage):
    locators = StepTasksPageLocators()

    def logo_for_the_step(self):
        self.element_is_visible(self.locators.LOGO_F0R_THE_STEP).click()
        self.element_is_visible(self.locators.LOGO_OH_CANNON).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.I_WILL_PARTICIPATE).click()
        self.element_is_visible(self.locators.YOUR_MAIL).send_keys("stage@stage.com")
        self.element_is_visible(self.locators.LINK_TO_THE_JOB).send_keys("https://www.resizepixel.com/ru/download")
        self.element_is_present(self.locators.DOWNLOAD_FILE).send_keys(
            "G:\pythonProject\step.skroy.ru\img\sampleFile.pdf")
        self.element_is_visible(self.locators.COMMENT).send_keys("keyword")
        time.sleep(5)
