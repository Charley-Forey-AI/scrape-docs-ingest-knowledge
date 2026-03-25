---
title: "Create User Profiles in Vista and Link Them to Cloud User Records | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-vrl-cloud/create-user-profiles-in-vista-and-link-them-to-cloud-user-records"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-vrl-cloud/create-user-profiles-in-vista-and-link-them-to-cloud-user-records"
---

# Create User Profiles in Vista and Link Them to Cloud User Records

You must provide each user access to
 Vista by setting
 up a user profile in Vista VA User Profile,
 which contains username and password credentials so that the user can log in.
Important: Use these instructions only if you are a
 cloud system administrator of a cloud-deployed organization using a deployment
 method *other than* VRL cloud to access Vista.To create Vista profiles for a VRL (cloud or
 on-premises) or LAN environment, see [Create a Vista SQL User
 in VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-vista-sql-user-in-va-user-profile).

To set up a Vista user:

1. From the Vista main menu, select Viewpoint Administration > Programs > VA User Profile.

1. In the User Name field, press
 F4.The System Users Lookup form
 appears with the Viewpoint
 Users radio button selected by default.

1. Change the selection to Systems Users.The list refreshes to display system users. These are the user records you created in the Cloud Admin Portal.For an active directory (AD) user to show up as a systems user in the F4 lookup on the VA User Profile form, the service account running the Vista Application Services must have permission to enumerate AD groups. Typically, application services run as the Network Service account, which has sufficient permissions on most systems.

1. Locate and select the username.

1.  Select OK to accept your selection and close the list.

1. In the User Type drop-down list, select Vista.

1. Save the record.

1. Complete other fields as desired. Press F1 for information on any field.

The user can now log in using credentials you just created.
Provide the username and password to the user.
