# Google Form Data
Using the google drive api to get google form data

# 1. Creating the Form (and the spreadsheet)
**Step 1:** Create a [google form](https://docs.google.com/forms/u/0/) and create the questions you want

**Step 2:** After creating the questions, click on the responses tab

**Step 3:** Then click on the green google sheets button on the top right of the page. This will create a google sheet that contains the responses from your google form. You can rename it if you want, but make sure to remember that name as it will be important later on

# 2. Enabling the API and Generating Keys
**Step 1:** Venture to the [Google Developer Console](https://console.developers.google.com/) and create a project

  You can name it whatever you want it doesn't matter, but it is useful to make it something that relates to your project

**Step 2:** On the left hand side click on "Library"

**Step 3:** Click on the searchbar, and search "Google Drive"

**Step 4:** Click Enable

**Step 5:** You will be redirected to another page. Click "Create Credentials"

**Step 6:** Where it says "Which API are you using", select the google drive API

**Step 7:** You will be calling the API from a web server, so select the second web server option (node.js or tomcat. You are using application data, and you will not be using the API with app engine.

**Step 8:** Click "What credentials do I need"

**Step 9:** You will be prompted to create a service account name. You can name it whatever you want, but give it Editor permissions, but clicking on role, hovering over project, and clicking editor. Use that name to create your service account id, and select JSON as the file that contains the private key that will generate

**Step 10:** A JSON File will be downloaded. Click on it and copy the client email.

**Step 11:** Navigate to the spreadsheet you created in the first part and click on share. You will share the sheet to your service account.

# Next Steps...
Remember the JSON File you downloaded? Copy all of the information from that and paste it into the ex.json file.

**Before you run the python script, you must install the gspread oauth2 package by running `pip install gspread oath2` in your command line.**

In the python script, change the value of the variable googleSheetName to the name of the gooogle sheet you created in the first part.


If you are stuck at any part, you can read [this amazing article](https://towardsdatascience.com/accessing-google-spreadsheet-data-using-python-90a5bc214fd2).
