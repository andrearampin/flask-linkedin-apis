''' Get access to OS libraries: '''
import os

''' Import Flask support: '''
from flask import Flask, request, session, redirect, render_template

''' Import OAuth2 libraries: '''
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix

''' Import configuration loader: '''
from loader import ConfigLoader

''' Allow OAuth 2 to work without SSL (only for dev): '''
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

''' Load configuration file: '''
loader = ConfigLoader(os.path.dirname(os.path.realpath(__file__)) + "/config.ini")

''' Print database configuration: '''
oauth = loader.get('oauth')

''' Track LinkedIn connection: '''
linkedin = None
state = None

''' Create Flask application: '''
app = Flask(__name__)


''' Landing page: '''
@app.route("/")
def details():
    data = None
    if linkedin is not None:
        data = linkedin.get(oauth["profile_info_url"]).json()
    return render_template("details.html", title="LinkedIn Platform", data=data)


''' Login page which will automatically redirect to the LinkedIn access request page: '''
@app.route("/login")
def login():
    global linkedin, state
    linkedin = linkedin_compliance_fix(OAuth2Session(oauth["client_id"], redirect_uri=oauth["redirect_uri"]))
    authorization_url, state = linkedin.authorization_url(oauth["authorization_base_url"])
    return redirect(authorization_url)


''' Callback page for LinkeDIn authorisation: '''
@app.route("/auth")
def auth():
    try:
        linkedin.fetch_token(oauth["token_url"], client_secret=oauth["client_secret"], authorization_response=request.url)
    except:
        print("Error : Not ready to authenticate")
    return redirect("/")


''' Run application '''
if __name__ == "__main__":
    app.run()