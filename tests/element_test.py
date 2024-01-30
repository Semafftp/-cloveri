import time

from pages.elements_main_page import MainPage, LogoOhCannonPage, CompetitionNumber2Page, LandingPageForTheCoursePage, \
    LogoForTheProjectPage, LogoContestPage, LogoForTheStepPage


# https://step.skroy.ru/

class TestElements:
    class TestMainPage:

        def test_main_page(self, driver):
            main_page = MainPage(driver, 'https://step.skroy.ru/')
            main_page.open()
            main_page.all_tasks()

    class TestLogoOhCannon:
        def test_logo_oh_cannon(self, driver):
            logo_oh_cannon = LogoOhCannonPage(driver, 'https://step.skroy.ru/tasks/')
            logo_oh_cannon.open()
            logo_oh_cannon.logo_oh_cannon()
            time.sleep(5)

    class TestCompetitionNumber2:  # COMPETITION_NUMBER_2
        def test_competition_number2(self, driver):
            competition_number2 = CompetitionNumber2Page(driver, 'https://step.skroy.ru/tasks/')
            competition_number2.open()
            competition_number2.competition_number2()

    class TestLandingPageForTheCourse:  # LANDING_PAGE_FOR_THE_COURSE
        def test_landing_page_for_the_course(self, driver):
            landing_page_for_the_course = LandingPageForTheCoursePage(driver, 'https://step.skroy.ru/tasks/')
            landing_page_for_the_course.open()
            landing_page_for_the_course.landing_page_for_the_course()

    class TestLogoForTheProject:  # LOGO_FOR_THE_PROJECT
        def test_logo_for_the_project(self, driver):
            logo_for_the_project = LogoForTheProjectPage(driver, 'https://step.skroy.ru/tasks/')
            logo_for_the_project.open()
            logo_for_the_project.logo_for_the_project()

    class TestLogoContest:  # LOGO_CONTEST
        def test_logo_contest(self, driver):
            logo_contest = LogoContestPage(driver, 'https://step.skroy.ru/tasks/')
            logo_contest.open()
            logo_contest.logo_contest()

    class TestLogoForTheStep:  # LOGO_F0R_THE_STEP
        def test_logo_for_the_step(self, driver):
            logo_for_the_step = LogoForTheStepPage(driver, 'https://step.skroy.ru/tasks/')
            logo_for_the_step.open()
            logo_for_the_step.logo_for_the_step()
            time.sleep(5)
