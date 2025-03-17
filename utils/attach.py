import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    try:
        png = browser.driver.get_screenshot_as_png()
        allure.attach(body=png, name="screenshot", attachment_type=AttachmentType.PNG, extension=".png")
    except Exception as e:
        allure.attach(f"Failed to capture screenshot: {str(e)}", "screenshot_error", AttachmentType.TEXT)


def add_logs(browser):
    try:
        log = "".join(f"{text}\n" for text in browser.driver.get_log(log_type="browser"))
        allure.attach(log, "browser_logs", AttachmentType.TEXT, ".log")
    except Exception as e:
        allure.attach(f"Failed to capture logs: {str(e)}", "logs_error", AttachmentType.TEXT)


def add_html(browser):
    try:
        html = browser.driver.page_source
        allure.attach(html, "page_source", AttachmentType.HTML, ".html")
    except Exception as e:
        allure.attach(f"Failed to capture HTML: {str(e)}", "html_error", AttachmentType.TEXT)


def add_video(browser):
    try:
        video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
        html = (
            "<html><body><video width='100%' height='100%' controls autoplay>"
            f"<source src='{video_url}' type='video/mp4'></video></body></html>"
        )
        allure.attach(html, f"video_{browser.driver.session_id}", AttachmentType.HTML, ".html")
    except Exception as e:
        allure.attach(f"Failed to attach video: {str(e)}", "video_error", AttachmentType.TEXT)