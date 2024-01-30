from selenium.webdriver.common.by import By


class StepTasksPageLocators:
    # Locators main page
    ALL_TASKS = (By.CSS_SELECTOR, "#__next > div > div > div > a")
    LOGO_OH_CANNON = (By.CSS_SELECTOR, "#__next > div > div > div > div > div:nth-child(1) > a")
    COMPETITION_NUMBER_2 = (By.CSS_SELECTOR, "#__next > div > div > div > div > div:nth-child(2) > a")
    LANDING_PAGE_FOR_THE_COURSE = (By.CSS_SELECTOR, "#__next > div > div > div > div > div:nth-child(3) > a")
    LOGO_FOR_THE_PROJECT = (By.CSS_SELECTOR, "#__next > div > div > div > div > div:nth-child(4) > a")
    LOGO_CONTEST = (By.CSS_SELECTOR, "#__next > div > div > div > div > div:nth-child(5) > a")
    LOGO_F0R_THE_STEP = (By.CSS_SELECTOR, "#__next > div > div > div > div > div:nth-child(6) > a")

    # Locators StepDownloadingTheSolution

    YOUR_MAIL = (By.CSS_SELECTOR, "#modal > div > div > div > div > form > label:nth-child(2) > input")
    LINK_TO_THE_JOB = (By.CSS_SELECTOR, "#modal > div > div > div > div > form > label:nth-child(3) > input")
    DOWNLOAD_FILE = (By.CSS_SELECTOR, '#fileInput')
    COMMENT = (By.CSS_SELECTOR, "#modal > div > div > div > div > form > label.style_margin_mb32__Ckz26 > textarea")
    I_WILL_PARTICIPATE = (By.CSS_SELECTOR, "#completed_work > div.style_button__NDhWB.style_button_purple__VPfEU")
