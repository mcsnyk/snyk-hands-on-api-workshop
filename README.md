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

## 1. Creating a new organisation using [apiary.io](https://snyk.docs.apiary.io/#reference/organizations/create-organization/create-a-new-organization) 
- [ ] Go to [apiary.io](https://snyk.docs.apiary.io/#reference/organizations/create-organization/create-a-new-organization) and click on "Switch to console" 
<img src="resources_img/switch-to-console.png" width="600"><br/>

- [ ] Now we need to configure the Header-first. For now, we only change the "Authorization" field by adding a valid token to it (replace the text **API_KEY** to a valid **Group-level-token**<br/>   
<img src="resources_img/authentication-apiary-auth.png" width="600">

- [ ] Change the parameters in the Body-section: the name of your new organisation in the Snyk WebUI, your GroupID in the Snyk WebUI, and optionally a organisationID from the Snyk WebUI where we can copy the various integrations-settings.

- [ ] Click on the green button "Call Resources" <br/>
<img src="resources_img/authentication-apiary-auth-body.png" width="600">

## 2. Creating a new organisation using the Snyk API
Let's create a new organisation in your Snyk Group using the Snyk API.
