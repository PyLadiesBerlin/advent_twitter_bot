from loguru import logger
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


logger = logger.bind(name="PyLadiesAdvent")


def send_email(e, tweet_text, SENDGRID_API_KEY, NOTIFY_EMAIL, subject="unknown"):
    """
    Create the body of the message (a plain-text and an HTML version).
    text is your plain-text email
    html is your html version of the email
    if the reciever is able to view html emails then only the html
    email will be displayed
    """

    text = """
        Hi!\nHow are you?\nPlease check on the Advent project,
        something has gone wrong!
    """

    html = """\n
    <html>
    <head></head>
    <body>
        Hi!<br>
        How are you?
        <p>Something went wrong in the PyLadies Advent project:</p>
        <p><b>%s</b></p>
        <p> Do not freak out, everything is gona be ok. :)</p>
        <p> Please sen the tweet for today manually </p>
        <p>%s</p>
        <br>
        Hugs!<br>
        you
    </body>
    </html>
    """ % (
        e,
        tweet_text
    )

    sg = SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email(NOTIFY_EMAIL)
    to_email = To(NOTIFY_EMAIL)
    subject = "Issue in PyLadies Advent project: " + subject
    content = Mail(
        from_email,
        to_email,
        subject,
        plain_text_content=PlainTextContent(text),
        html_content=HtmlContent(html),
    )
    try:
        response = sg.send(message=content)
        if response.status_code == 202:
            logger.info("Error email sent")
        else:
            logger.info(
                f"Not sure if email was sent, but no exception raised: {response.status_code}"
            )
    except Exception as e:
        raise Exception("Error sending email:", e)
