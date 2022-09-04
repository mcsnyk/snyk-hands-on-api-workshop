# Hands-on workshop: Interacting with the Snyk API by using Python-scripts and apiary.io 
   
There are many ways to interact with the Snyk API. 
We will be using [apiary.io](https://snyk.docs.apiary.io/#reference/organizations/create-organization/create-a-new-organization) and Python-scripts now.   
- Seb Roth held another [workshop](https://github.com/mcsnyk/Seb-snyk-api-workshop) on how to interact with the pysnyk API (Small Hands, Windsor 2022).   
- Rotem Miara held a workshop on how to onboard projects in the Snyk Web-UI.
     
## 0. Authentication  
Before we can do things with the API, we need to authenticate first, because the API needs to know who it is interacting with an what permissions are assigned to us (what we are allowed to do).   
The authentication happens in form of a handshake which means we have to send the following information to the Snyk API first:

<img src="resources_img/authentication-apiary.png" width="600">

or in form of a Python3 code:
<img src="resources_img/authentication-pycharm.png" width="600">

## 1. Creating a new organisation using [apiary.io](https://snyk.docs.apiary.io/#reference/organizations/create-organization/create-a-new-organization) 


## 2. Creating a new organisation using the Snyk API
Let's create a new organisation in your Snyk Group using the Snyk API.
