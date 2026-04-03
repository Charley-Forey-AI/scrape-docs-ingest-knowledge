---
title: "Service Tech Mobile Setup | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-tech/mobile-overview/service-tech-mobile-setup"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/service-tech/mobile-overview/service-tech-mobile-setup"
---

# Service Tech Mobile Setup

Use these steps to set up the Service Tech Mobile app for technicians.
Note: These steps should be performed by the System Administrator at your company.

## 1. Set up Spectrum as a Trimble Construction One Enterprise Product

This step can be accomplished in two ways:

- If you already own the Team product, select the Sign in with Trimble Construction One button to access the Trimble Construction One User Administration screen.

- If you don't own the Team product, contact your Spectrum sales representative to request access to Trimble Construction One User Administration.

## 2. Set up employee records in Spectrum

If you have technicians at your company, they may already be set up as employees in the Spectrum application.
If you need to add a new employee record, do so using the Payroll >  Employee Maintenance screen. If needed, see [Create a New Operator Record](/en/spectrum/spectrum/system-administration/operator-maintenance/create-a-new-operator-record).

## 3. Designate employees as technicians

If not already done, you must take specific action to make a Spectrum employee a technician. Watch this video to learn more about setting up a technician, including assigning Case Types and Work Order types. Written instructions follow.

- To set up a new technician, go to Work Order >  Maintenance >  Technician.The Technician Maintenance screen opens.

- On the Properties tab, enter general info about the technician.

- Specify the Case Types and WO Types the technician can access.

- On the Warehouses tab, specify which warehouses the technician has access to.A Truck warehouse code is typically the inventory of items available in their service vehicle.

- To give the technician access to all truck warehouses, select the Technician has access to all warehouses? checkbox.

## 4. Create technician login credentials

Use the Create Technician Logons screen to create a logon for each technician you set up.
Use this screen to facilitate creating and managing logons for field technicians and other employees that do not already have a Spectrum logon. It provides a list of active technicians who do not have an assigned Spectrum logon, so it is also helpful to set up any new hires in the future. You can review and edit the information as desired and then perform the update to create the new Spectrum operators.
Watch the video below to learn how to create a logon based on an existing logon ID.

- Go to System Administration >  Security >  Create Technician Logons.

- Specify an existing technician to set up, or you can select an entire department of technicians to set up at once.

- Specify the logon ID of the technician you wish to copy from and select Continue.

- Change the logon ID and password for the selected technician(s) as needed, and select Update to create the logon.

## 5. Confirm each technician has a unique email address

A unique email address is required for licensing purposes. This should be a company-provided address using the business domain.
Go to System Administration >  Security >  Operator Maintenance and verify the technician has a unique email address.

## 6. Assign Service Tech licenses

The final step on the Spectrum side is to assign a Service Tech license to the technician. Use the Service Tech License Manager screen to manage your list of available technicians prior to importing them into Trimble Construction One. Watch the video below to learn more about the different options on this screen.

- Go to System Administration >  Security >  Service Tech Licenses and select the new licensed technician.

- The Mobile Ready column indicates technician record status.

Mobile Ready StatusDescriptionRequired Action
No, email address missingThere technician's Spectrum records does not have an email address entered.Select Operator Maintenance to add an email address.
No, duplicate emails foundThe email address specified for the selected technician is in use by another technician. Select Operator Maintenance to make sure the technician has a unique email address.
No, not yet imported into Trimble Construction OneThe record is ready to be imported into Trimble Construction One.Proceed to Step 7.
Yes, imported into Trimble Construction OneThe record has already been imported to Trimble Construction One.The technician may log in and use the Service Tech Mobile app.

## 7. Send Service Tech Mobile email invitations

Once you have set up technicians in the Spectrum application and assigned a Service Tech license to them, you can then proceed to the Trimble Construction One User Management screen where you can add users from Spectrum, confirm user roles, and send them an email invitation to start using the mobile app.

- Go to Trimble Construction One >  User Management and select Add Users from Spectrum.

- Locate and select your technician(s) and select Next.

- Make sure the technician(s) Enterprise Role is 'User'.

- Make sure the technician(s) Project Comm. Role is 'None'.

- Select Send Invitations.

## 8. Technicians must accept the invitation

Each technician receives an email inviting them to join Service Tech and must accept it before they can use the application. Watch the video below to see how the technician can accept this invitation and set their account password.

To accept the invitation:

- In the body of the email, select Confirm Email and Configure Account.A secure web page opens, displaying user-specific information.

- Verify the displayed info is correct, make any needed corrections, and add any missing info.

- Create a unique password and select Create Account.Note: Only the technician knows and can change the password.

## 9. Log in to the Spectrum Service Tech Mobile app

Once the technician has created their password, they are ready to log in using their newly created credentials.
If not already downloaded and installed, use the link pertinent to your mobile device OS:

- [Apple](https://apps.apple.com/us/app/spectrum-service-tech/id1451768891)

- [Android](https://play.google.com/store/apps/details?id=com.viewpoint.servicetech)
