---
title: "Create a Trimble Construction One Analytics Account for Non-Vista Users | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-trimble-construction-one-analytics-account-for-non-vista-users"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-trimble-construction-one-analytics-account-for-non-vista-users"
---

# Create a Trimble Construction One Analytics Account for Non-Vista Users

For Trimble Construction One Analytics users who do *not* require logging in to the Vista application but who *do* require linking Vista security to a Trimble ID, you can create a non-Vista user account and have the account owner migrate their account to a Trimble ID login. This type of account is useful if you access products such as Trimble Construction One Analytics or specific workflows in Vista Web. This account will not have access to the Vista application.
If you are attempting to set up a Vista service / database account
 that does not require a Trimble ID *or* access to the Vista application, see this
 article instead: [Create a Database Account for Non-Vista Users](/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-database-account-for-non-vista-users).
To create a non-Vista user with a
 User Application account
 that is later linked to Trimble ID, complete the following steps:

1. From the Vista main menu, go to Viewpoint
 Administration > Programs > VA User Profile.

1. At the top of the form,
 select the New Record
 icon () in the toolbar.

1. In the [User Type](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-0004bd04--en)
 dropdown, select User Application.

1. Enter required fields, the PR
 Co and Employee # in the HR Employee
 Details section, and any other necessary information. Save the record. If this account has not been set up in
 Microsoft SQL Server, a message displays that the system will attempt to create
 a SQL Server login.

1. Select Close.The VA Password form opens.

1. Enter and confirm the password in the appropriate
 fields and select OK.The system creates the required SQL
 server login (if the user does not already have one), so that the user can
 access information from the Vista
 database.

1. Save the record.

1. Share the SQL login credentials with the user.

1. After creating the User Application account in
 Vista, your user will need to migrate this account to Trimble ID to create a
 fully linked account.

1. To migrate your login to Trimble ID, go to *https://vista-app.viewpoint.cloud/code* where *code* is the unique 3 or 4 character value for your customer
 environment.

1. If you are unsure what your code is, attempt to log into the Vista
 application with your credentials. Your code is the value at the end of
 the URL in the browser address bar.

1. Once you are on the webpage for your environment, *https://vista-app.viewpoint.cloud/code*, follow the prompts to
 finish linking your account. For more information, see [Create a Trimble
 ID](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:accountservices_001:accountservices:accountservices?_gl=1*px8pnc*_ga*MTEwNzUzMDU0MC4xNzI4MDQ0OTc2*_ga_CE8YXBH39Q*czE3NTAxODA5OTMkbzI2OCRnMSR0MTc1MDE4MjQxMyRqNDMkbDAkaDA.).

For more information, watch this video about creating Vista
 accounts: [Trimble ID Account Creation for Vista - Video](/en/vista/vista/videos/administration/trimble-id-account-creation-for-vista---video).
