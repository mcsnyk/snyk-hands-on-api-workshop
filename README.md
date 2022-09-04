# Hands-on workshop: Interacting with the Snyk API by using Python-scripts and apiary.io 
   
There are many ways to interact with the Snyk API. 
We will be using [apiary.io](https://snyk.docs.apiary.io/#reference/organizations/create-organization/create-a-new-organization) and Python-scripts now.
   
- Seb Roth held a [workshop](https://github.com/mcsnyk/Seb-snyk-api-workshop) on how to interact with the pysnyk API Client (Small Hands, Windsor 2022).   
There are many language-specific Snyk API Clients Libraries available:   
 		- Python [client library](https://github.com/snyk-labs/pysnyk) for Snyk  
 		- JavaScript [client library](https://github.com/JupiterOne/snyk-client) for Snyk  
 		- Go [client library](https://github.com/picatz/snyk) for Snyk  
 		- PHP [client library](https://github.com/navikt/snyk-api-php-client) for Snyk   
 		- Ruby [client library](https://github.com/edgar/rsnyk) for Snyk   
  
- Rotem Miara also held a workshop on how to onboard projects in the Snyk Web-UI.
     
## 0. Authentication  
Before we can do things with the API, we need to **authenticate** first, because the API needs to know who it is interacting with, and what permissions are assigned to us (what we are allowed to do).   

The authentication happens in form of a **handshake** which means we have to send the following information to the Snyk API first:

<img src="resources_img/authentication-apiary.png" width="600">

or in form of a Python3 code:<br/>
<img src="resources_img/authentication-pycharm.png" width="600">

## 1.a. Creating a new organisation using [apiary.io](https://snyk.docs.apiary.io/#reference/organizations/create-organization/create-a-new-organization) 
- [ ] Go to [apiary.io](https://snyk.docs.apiary.io/#reference/organizations/create-organization/create-a-new-organization) and click on "Switch to console"<br/>
<img src="resources_img/switch-to-console.png" width="600">

- [ ] Now we need to configure the Header-first. For now, we only change the "Authorization" field by adding a valid token to it (replace the text **API_KEY** to a valid **Group-level-token**)<br/>   
<img src="resources_img/authentication-apiary-auth.png" width="600">

- [ ] Change the parameters in the Body-section: the name of your new organisation in the Snyk WebUI, your GroupID in the Snyk WebUI, and **optionally** an organisationID from the Snyk WebUI where we can copy the various integrations-settings from.

- [ ] Click on the green button "Call Resources" <br/>
<img src="resources_img/authentication-apiary-auth-body.png" width="600">

- [ ] Take a look at the Response box below and try to understand what has happened.
- [ ] Go to your Snyk WebUI and check if the new organisation is there.   

## 1.b. Creating a new organisation using httpx and Python
Let's create a new organisation in your Snyk Group using the Snyk API.
In this case we are going to use a fully featured HTTP client for Python3, called [httpx](https://www.python-httpx.org/). <br/>

As mentioned above, the authentication starts with a TCP-handshake. If we didn't use a client (which keeps a connection active and alive), we would have to do this handshake every single time we leverage the various API functions and call the API. A client also allows us to have multiple connections at the same time by reducing overhead operations at a networking level.

- [ ] Please check if Python3 is installed on your machine by running the command (any version above 3.5 should be fine): <br/>
```python3 --version```
- [ ] First of all, we need to install the Python libraries needed (requirements.txt) <br/>
```pip3 install -r requirements.txt``` <br/>

Normally, we should create a virtual environment at the beginning, set environment variables as secrets (Snyk Tokens, Group IDs, Org. IDs...). 
Now we we'll use these secrets in a hard-coded way as regular Python variables.

- [ ] After giving values to the **SNYK_TOKEN**, **GROUP_ID** and **NEW_PROJECT_NAME** variables, run the script:
```python3 create-new-orgs.py```

- [ ] Take a look at the response of the API and try to understand what has happened.
- [ ] Go to your Snyk WebUI and check if the new organisation is there. 
