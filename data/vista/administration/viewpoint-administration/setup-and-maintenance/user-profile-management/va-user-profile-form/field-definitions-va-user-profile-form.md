---
title: "Field Definitions: VA User Profile Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form"
---

# Field Definitions: VA User Profile Form

The following is a list of field descriptions for the VA User
 Profile form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## User Name

Enter the user's login name, up to 128 characters.
If... Then... For example
...this user is being set up for SSO with Trimble ID... Note: Once implemented in early 2025, Trimble ID will be available to Trimble Construction One cloud-hosted Vista customers only.If you are a legacy cloud or on-premises customer, contact your account representative to learn about how you can transition to the modern cloud and gain access to all the latest features.

If you have a legacy cloud or on-premises deployment method, this option to have an email address as a user name is not available to you.
...enter their email address in the User Name field and select the Is SSO Account checkbox. If a company email is required, enter that email in the User Name field.If the email address they are going to user for their Trimble ID is *john_doe@mycompany.com*, the user name entered here must be that same email address.
...this user is already or will be defined separately in SQL Server... Note: Classic login credentials will no longer be supported for Trimble Construction One cloud-hosted Vista users in the fall of 2025.
...enter the user name that is or will be defined in SQL Server. The user name in this field must exactly match the user name defined in SQL Server, including matching the case. If the user name in SQL Server is *JohnD*, the user name set up here must be entered exactly the same, as *JohnD*.
...this user is being set up as a domain user... Note: Classic login credentials will no longer be supported for Trimble Construction One cloud-hosted Vista users in the fall of 2025.
...enter the Windows user name. The user name in this field must exactly match the Windows user name, including matching the case. If the Windows user name is *DOMAINNAME\JohnD*, the domain user name must be entered as *DOMAINNAME\JohnD*.

You can also press F4 to open the lookup and select from a list:

- Viewpoint Users: displays the list of users who are already set up as SQL Server users and which already exist in Vista. Select this option if you want to find and edit a user who has already been set up.

- System Users: displays the list of users who already have access to the database at the SQL level, either by having been set up as SQL Server users or as members of a Windows domain group. These users do not exist in Vista. Select this option if you want to quickly create a new Vista record for a user who already has access to the database.

Related information

- [Create a Vista Domain User](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-vista-domain-user)

- [User Type](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-0004bd04--en)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## User Type

The User Type dropdown on the VA User Profile form.
Note: To set up users, you must have access to the VA Password form.
There are two types of users that you can create in Vista:VistaThis user type is for standard users who can access the Vista application. See [Create a Vista SQL User
 in VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/account-creation/create-a-vista-sql-user-in-va-user-profile).Set up all users needing access to the frontend of the Vista application with the Vista user type.
User ApplicationThis user type is for integrations, service accounts, and third-party applications that need access to the Vista database. This user type does not occupy a Vista license and cannot be used to log in to the Vista application. The system assigns this user type the VCSUsers SQL role, which provides access to views only (not tables) and does not circumvent datatype security. If you're using datatype security, assign this user to the security groups that will give the third-party application the appropriate access to secured data.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Full Name

 Enter the user’s actual name. This field is for informational purposes only.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Email Address

Email Address field in the VA User Profile form
Displays the user's email address.
Since this email address is used as a login credential, it must not be used on any other Vista profile.
It's also used by the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature in the Project Management module.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Phone #

 Enter the user’s phone number. This field is for informational purposes only.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Deactivated

Due to
 updates in the license provisioning process, when you save a new record in VA User
 Profile, the Deactivated
 checkbox will be selected and temporarily unavailable. After approximately one
 minute, the record can be refreshed, which automatically clears the checkbox. If a
 license is available, the user will be successfully activated.
If you want to deactivate a user account, select
 this checkbox.
When you deactivate a user account, you should also disable the user's access to the Microsoft SQL Server database. For more information, see [Deactivate a User Account](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/remove-users/deactivate-a-user-account).

## Expires

The Expires date field in the VA User Profile form, Info tab.
Enter a date this user profile should expire. The system treats expired profiles the same as deactivated.
When you deactivate a user account, you should also disable the user's access to the Microsoft SQL Server database. For more information, see [Deactivate a User Account](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/remove-users/deactivate-a-user-account).

## Is SSO Account

The Is SSO Account checkbox on the VA User Profile form, Info tab.
Important: This field applies to *cloud-hosted customers only*.

When selected, this checkbox indicates that the user profile is set up as an SSO account with Trimble ID.
Admins can edit this field to complete the following actions:
Set up a new Vista user with SSOWhen creating a new Vista user, if Trimble ID has been enabled for your company, select this checkbox to set up the new user to log into Vista with Trimble ID.
Vista bypasses the creation of a SQL account for this user, and instead creates a Trimble ID record, based on the user's email address.
Note: In the rare instance that you are setting up a User Type of User Application, *do not* select this checkbox. For more details about this setup, see [User Type](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-0004bd04--en).

Unlink SSO from an existing Vista user profileAdmins can update existing Vista user profiles to unlink users from their SSO Trimble ID accounts. For an existing SSO user, deselect the Is SSO Account checkbox. For more details, see [Unlink Trimble ID from a Vista User's Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/single-sign-on-with-trimble-id-admin-information/unlink-trimble-id-from-a-vista-users-profile).

## Domain
 Login

Entry in this field is necessary only for users of BI dashboard reports.
Enter the user’s Windows domain login to enforce the user’s Vista™ software security settings on the SSRS server used to process information for the Business Intelligence (BI) dashboard reports.

Related information

- [VA Business Intelligence Mgmt Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-business-intelligence-mgmt-form)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## License Type

The License Type drop-down on the VA User Profile form, Info tab.
*This
 field is enabled only for organizations with Vista deployed in the cloud and with the Named User License (NUL) model.*
Use this drop-down to designate this user's type of Vista license.

- 0-Office - for those needing full use of Vista accounting and operational capabilities.

- 1-PM - for those accessing Vista forms and reports aligned only with project management functions.

For organizations using the CUL license model, this field is disabled and the default license type is 0-Office for all users.
Designating a license type does not restrict a user's access to programs and reports that they have been given permission to access. Instead it serves to limit—by license type—which users can run certain reports. Note: If users with a PM license are granted access to programs or reports that require an Office license, they will be allowed to use these programs and reports, but they will be counted as using an Office license.

You can learn more by visiting these Help pages:

- [Office License Required](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form/field-definitions-rp-report-titles-form#ID-0003dd510001--en)

- [Vista Licensing ](/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing)

- [Assess License Usage](/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing/assess-license-usage)

Organization License ModelDeploymentLicense Type(s) available
Concurrent User License (CUL)Cloud *or* On-premises0-Office
*Drop-down is disabled.*

Named User License (NUL)Cloud *only*0-Office (default)
1-PM (optional)

## Use 'Enter' as 'Tab'

Check this box to have the Enter key work like the Tab key. When the user presses Enter, the system moves to the next field in the tab sequence. If pressed to trigger an action (for example, the Save and Go button ), the system moves to the next field or action (once the action has been performed).
Uncheck this box if using only the Enter key to trigger an action (e.g. validating/posting batches). When pressing Enter at a field, the cursor remains at the field and the user must press the Tab button to move to the next field.
Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Confirm Updates

Check this box to have the system flash a ‘confirm update’ message when moving off a changed record. The displayed message allows the user to save the record or cancel the change.
Uncheck this box to have the system automatically save the record and move to the next record.
Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Extend Controls When Editing

Check this box to extend fields where the number of characters entered exceeds the display allowance. For example, if you enter an address of 35 characters in a field that allows 60 characters, but normally only displays 30 characters, the field extends to accommodate the 35 characters when you focus on the field.
Uncheck this box if you do not want fields extended when the number of characters entered exceed the number of characters displayed. User must scroll through the field to see the entire value.
Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Display Tool Tips

Check this box to display tool tips. When the mouse hovers over a form icon/name, brief information about the selected form displays (for example, the form name and 'last accessed' info). This box also enables tool tips at the field level in forms, although it only applies to fields that have a description. For example, if you hover over a phase field, the tool tip is the phase description.
Uncheck this box if you do not want tool tips displayed when hovering the mouse over a form icon/name.
Note: You can override this setting by selecting the Display Tool Tips option on the Main Menu’s View menu.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Smart Cursor - Highlight Active Control

Check this box to activate smart cursor. When the smart cursor is in use, the system highlights active fields for easier identification. Use the Color Selections form (Main Menu > Options > Colors) to determine the highlight color. For best results the highlight color should stand out from the current color scheme.
Uncheck this box if you do not want to use the smart cursor feature. The system will not highlight active fields, but you will be able to identify them by the blinking cursor.
Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Save Printer Settings with Each Report

Check this box to save report printer settings to the database. The system uses the specified printer settings each time the report runs.
Uncheck this box to always use the default settings for a report. Any settings made when running the report will not be saved once the report is closed.
Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Merge Grid Key Columns

Check this box to merge the key columns of grids when multiple records exist where one or more key values are the same. This prevents the values from repeating for each record in the grid. For example, in PR Craft Classes, you might have multiple classes assigned to a single craft. When you merge the grid key columns, grid records look like this:
Craft
Craft Desc
Class
Class Desc

100

Carpenter

100
Apprentice

101
Journeyman

103
Foreman

Uncheck this box if you do not want to merge grid key columns. Key values will repeat for every record. When you do not merge grid key columns, grid records look like this:
Craft
Craft Desc
Class
Class Desc

100
Carpenter
100
Apprentice

100
Carpenter
101
Journeyman

100
Carpenter
103
Foreman

Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Alternate Grid Row Colors

Check this box to display grid rows in alternating colors of light blue and white. This applies to the Grid tab and any related grids on a form.
Uncheck this box to display all grid rows as white.
Note: The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Save Last Used SSRS Parameters

Checked by default.
When this checkbox is selected, the next time that you run an SSRS report that you previously ran, the parameters will be automatically set to be the same as the last time you ran that SSRS report. These saved parameters will override any report parameter defaults.
Uncheck this box if you do not want to save the SSRS parameters you last used.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Show Unsaved Changes

Show Unsaved Changes checkbox in the VA User Profile form
Select this checkbox to have the system provide this user an opportunity to save any data that was not saved before an interrupted connection.
When the user re-establishes a connection, they will see a notification with an option to view and save any unsaved changes.
Note: Notifications do not appear for forms used only for setup. They appear only for forms that store your operational data.
Help Keyword 350037897

## SSRS Report Viewer Options

Select how you would like to view SSRS reports
 launched from the application.

- Launch in Browser - Select this
 option if you want the report to open immediately in a browser. Once the report
 displays, you can select the report parameters using a toolbar at the top of the
 browser.

- Launch Parameters Form - Select
 this option if you want a report parameters form to open before launching the report.
 This is similar to how Crystal Reports are launched.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Restricted Batches

Indicate the default batch-restriction status.
Check this box to default the Restricted
 Access box in the Batch Selection form (for applicable modules) as checked
 each time this user creates a batch. Restricted batches allow only the user who creates the
 batch to access it.
Uncheck this box to default the Restricted
 Access box in the Batch Selection form (for applicable modules) as unchecked
 each time this user creates a batch. Unrestricted batches allow all users to access the
 batch, regardless of who created the batch.

- You can override the default batch-restriction status at the time you create a batch.

- Batches that are created 'behind the scenes' (e.g. AR 'Credit Taxes' and 'Apply Retainage' hot key functions, IM Import, IN Physical Count, IN Monthly Reconciliation, IN Rollup, PR to AP Update, etc.) also default as specified by this checkbox.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Send Email Via SMTP

Use this checkbox for the selected user in VA User Profile to override the [site-wide setting in VA Site Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000499e6--en).
Tip: It is necessary to actively check or uncheck this checkbox only if the user has MS Outlook installed.

- Check this box to force email from this user's
 Vista™ account to be sent via SMTP, even when the user has
 Outlook installed and the Send Email Via SMTP checkbox is
 not checked in VA Site Settings.

- Uncheck this box if the Send Email Via
 SMTP checkbox is checked in VA Site Settings, but you want this
 user's email to default to sending from MS Outlook rather than SMTP.

-  Leave this checkbox in the null state (with a blue square in the box) if you do not want to override the site-wide setting for this user.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Company

Enter the default company for this user. Press F4 for a list of valid companies.
Users can change their default company by selecting a company in the Company drop-down on the Main Menu, which resets this field’s default.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## AP Pay Category

If you are using pay categories (AP Company Parameters), you can specify a default pay category for the user. This pay category overrides the default pay category specified in AP Company Parameters and is the default pay category for this user when entering transactions in AP Transaction Entry, AP Recurring Invoices, AP Unapproved Invoices and PO Purchase Order Entry, as well as when updating subcontracts to AP (in SL Update to AP).
Note: If you have set up a pay category default in F3 Properties (not recommended), it overrides the default specified here. As logins are not company specific, the system does not validate this field. If this user posts in multiple companies, it is suggested that this pay category be set up for each AP company in which this user will be posting.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Notify By

Use this field to select by default how the user will receive notifications generated by Notifier. For example if you use the [Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) feature and the user is an approver, this is how the user will receive a notification that they have a document to review.

- 0-Email – Select this option if the user should receive an email message..

- 1-VP Message – Select this option if the user should receive a VP message
 that can be viewed using the [VA
 Messages ](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-messages-form) form.

The selection in this field only determines the default behavior. You can override the default behavior using the Notification Preferences tab. For example if the user should receive emails when they have a document to review but should receive all other notifications using VP Messages, you can set that up using the Notification Preferences tab.
Users can change the option in this field by
 selecting Options > User
 Options from the toolbar on the main application window. This will launch the [User Options ](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form) form.
Click [here](/en/vista/vista/system-tools/work-flow/about-automated-notifications) for more information on using notifications.
Note: The selection in this field also affects how the Create and Send feature
 in the Project Management module will function. For more information, see [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature).

## Menu Administrator

Select this checkbox to allow the user to add, edit, or delete Main Menu subfolders.

Related information

- [Main Menu Options](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options)

## Form Administrator

Check this box if the user should be able use
 the [Form Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-form-properties-form) and [Field Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form) forms to change the settings of a form -
 for example add a tab to a form that displays a query, or add a report to a form that can
 be launched using the Options > Reports menu on a form.
Note: This does not apply to the Fields and Security tab in Form Properties and the Property Values tab in Field Properties—these are display only tabs.
Clear this checkbox to allow user to only change
 settings on the User tab in Form Properties and the User Overrides tab in Field Properties.
 All other tabs in both forms will be read only.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Display Earnings Rates in PR Timecard Entry

Select this box to permit user access to rates in PR Timecard Entry. When you select this box, the system enables the Hourly Rate and Amount fields in PR User Grid options. Users can set these fields to display the Rate and Amount fields in the Job and/or Mechanics timecard grids in PR Timecard Entry. For more information, refer to Related Topics below.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [About the PR User Grid Options Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-user-grid-options-form)

## Disallow Self Security Assignment

Disallow Self Security Assignment checkbox in the VA User Profile form
Select this checkbox to prevent this Vista user from changing their own security access settings.
Note: Selecting the Disallow Self Security Modifications (All Users) checkbox in the VA Site Settings form overrides this field so that it makes no difference what you select here. If that box is selected, all users in the organization are treated as if this box were selected for them.

Related information

- [Disallow Self Security Modification (All Users)](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-00049943--en)

## Enable Shared Search

Enable Shared Search checkbox in the VA User Profile form
Select this checkbox to allow this user to share their searches with all other users. The shared search is specific to the Search panel in the form that the user created it in.

## View Application Logs

The View Application Logs checkbox in the VA User Profile form.
Select this checkbox if you want this user to be able to access and view the application logs accessible from the Main Menu: Help > System > View Logs.

## Lookups

Enter the maximum number of rows returned when using a lookup. This is useful when you have lookups associated with tables containing hundreds or thousands of records, which can affect the refresh speed.
Keep in mind that this option affects all lookups for this user, so set a limit that is not too restrictive. Typically, you do not want to restrict lookups that normally return a much smaller record set. For example, if you have 200,000+ material and/or phase records, you might set this option to 10,000. This would increase the refresh speed for the material and phase lookups without limiting the records returned for lookups having less than 10,000 records.
If the number of records in a table exceeds
 the designated limit, a message displays indicating that there are more records than the
 system can display. If the record you are looking for is not in the current record set,
 enter selection criteria and click Refresh to re-query the database. You can
 include wildcards (*, %) or comparison operators (<, , <, =, =, <=) to refine your
 search as necessary (e.g. 6000, *6000, etc.). Once you click Refresh, the
 lookup returns a record set based on the entered criteria.
Note: This option overrides the Lookups setting in VA Site Settings for this user only. Users can also override the setting for their login by updating the Lookups field in User Options (Main Menu, Options menu).

Related information

- [Auto Size Lookup Columns](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049d9f--en)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [System Forms](/en/vista/vista/system-tools/user-interface-guide/system-forms)

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [Set the Maximum Number of Records for Lookups](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-the-maximum-number-of-records-for-lookups)

## Page Size

Page Size field in the VA User Profile form
Using this field can help make some Vista forms load faster.
Enter the maximum number of records per page that you want the system to return when this user opens any form. Forms will initially retrieve only the number of records that you choose here; for forms associated with tables containing an extensive number of records, the form can load faster.
The number that you specify affects forms for this user only, and only if the following apply:

- the user has enabled the feature on the form

- the number you've chosen is smaller than what is entered in the Page Size field in the VA Site Settings form.

Note: Users can also set this field value on their own by going to Main Menu > Options > Forms.

 When this user has enabled this on the form, opening a form with more records than the number entered here will cause the system to group all records over that number into subsequent pages, each containing up to that same number of records. The status bar in each form indicates the page number, as well as the total number of pages (for example, Page 1 of 500).
When you are on the Grid tab of a form, you can use the Previous Page and Next Page navigation buttons to view any additional pages of records. However, if you know the ID of a record, you can enter that ID in the appropriate key field and the system display that record. For example, you can enter a vendor number in the Vendor field of AP Vendors, and the system display that vendor record.

Related information

- [Page Size](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-00049885--en)

- [Search Form Records](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records)

- [Increase Form Record Load Speed](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records/increase-form-record-load-speed)

- [About the Search Panel](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records/about-the-search-panel)

## Attachment Lister

Enter the number of attachments that you want to display in the attachment lister for all forms for this user. When the user opens the attachment lister (by clicking the drop-down arrow next to the Attachments button and selecting Attachment Lister), the system displays the most recently added attachments for all forms, up to the specified number for this user.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Suppress Max Warning Rows

Suppress Max Warning Rows checkbox in the VA User Profile form
Check this box to turn off prompts for this user to use filters.
If this box is selected, when you are about to open a form that calls records numbering more than what is entered in the Max Warning Rows field in the VA Site Settings form, you won't receive a prompt to use a filter.
The system prompts you because filtering records on large data sets can speed up the form load.For example, if the Max Warning Rows field in the VA Site Settings form is 5,000, and a user opens a form that maintains 6,000 records, the system will ask the user if they want to filter the records before querying the database. However, if you select this checkbox, this user will not receive these prompts.

Related information

- [Max Warning Rows](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000498ab--en)

- [Page Size](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049cf3--en)

- [Increase Form Record Load Speed](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records/increase-form-record-load-speed)

## Display Accessible Only

Select this checkbox to display only those forms and reports that this user has permission to access.
Clear this checkbox to display all forms and reports display, regardless of security setup. The system disables forms and reports that the user does not have permission to access.
Note: You can override this setting by selecting the Display Accessible Items Only option on the Main Menu’s View menu.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Minimize Menu on Use

Select this box to have the system auto minimize the Main Menu when the user opens a form or report. This can be useful in keeping the screen less cluttered when working in forms or viewing reports.
Users can override this setting by selecting
 View  > Minimize Menu on
 Use from the Main Menu.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

##  Hide Standard Module Folders

 Select this box to have the hide module folders on the Main Menu. This is useful if you have set up your Company and/or My Viewpoint folders to contain all necessary forms for the user.
 Users can override this setting by using the Hide Standard Module Folders option on the Main Menu’s View menu.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Allow Multiple Instances of a Form

Select this box to allow multiple instances of a form to be open at once. This is useful for opening another batch without interrupting the batch you are currently working in.
If you do not select this box, the user can only open one instance of a form at a time.

- This option only affects the current user; it does not affect the ability of multiple users to have the same form open at the same time.

- The User Options form and the VA User Profile form update each other, so you only need to set this field once to affect both forms.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Display Active Info

This
 field determines what information displays in the upper left corner of the Main Menu.
 Select one of the following options:

- 0-None – Select this option if you do not want to display any information.

- 1-PM Project - Select this option to display the currently active PM project. This information refreshes each time a new project is accessed in forms where the key field is Project (e.g. PM Projects, PM Change Orders, PM Material Detail, PM Meeting Minutes, etc.).

- 2-PR Pay Period - Select this option to display the currently active pay period. This information refreshes each time you specify a new pay period in PR Pay Period Control.

- 3-JC Job - Select this option to display the
 currently active JC Job. This information refreshes each time you enter a new job in
 non-batch forms where the key field is Job (e.g. JC Jobs, JC Job Phases, JC Change
 Orders, etc.).

This field updates the Display Active Info option in the Main Menu’s View menu and vice versa.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Allow Auto Log Off

Unchecked by default. Enabled only if the [Use Auto-Log Off](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000498e1--en) checkbox is checked in [VA Site Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form).
Check this box to automatically log this user off of Vista after a specific number of minutes of idle time (set in VA Site Settings). Logging a user off will release that Vista license for use by another user.
Tip: Typically, you will want to use this feature with intermittent users of Vista. You may not want to apply it to users, such as Accounting personnel, who may be frequently processing data or running long data processes.
For more information, see [Logging Users Off Automatically After Idle Time](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/log-users-off-automatically-after-idle-time).

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [Use Auto-Log Out](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000498e1--en)

- [Minutes to Log Out](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000498fa--en)

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

## HR Co

Use this field only if you are using the leave request functionality in the HR module. For more information, refer to Leave Requests in Related Topics below.
Enter the HR company that this user belongs
 to. Press F4 for a list of valid companies.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [About Leave Requests](/en/vista/vista/hr-and-payroll/human-resources/leave/about-leave-requests)

## HR Resource

Use this field only if you are using the leave request functionality in the HR module. For more information, refer to Leave Requests in Related Topics below.
Enter the resource number that should be
 associated with this user. Press F4 for a list of resources.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [About Leave Requests](/en/vista/vista/hr-and-payroll/human-resources/leave/about-leave-requests)

## PR Co

Use this field only if you are using the [timesheet entry functionality](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets) in the PR module.
Enter the PR company that this user belongs to. Press F4 for a list of valid companies.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Employee

Use this field only if you are using the [timesheet entry functionality](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets) in the PR module.
Enter the employee number to associate with this user. Press F4 for a list of employees.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## My Timesheet Permissions

Use this field only if you are using the timesheet entry functionality in the PR module.
Select a timesheet entry permission level for this user:

- Enter for Self - the user can only enter timesheet for themselves (using PR My Timesheet).

- Enter for Self and Others - the user can enter timesheets for all employees within the same payroll group (using PR My Timesheet). This permission setting is meant for managers and foremen.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## PM Error Corrections

Use this section to choose which PM module forms this user can make changes to interfaced data by selecting Task > Correct Item in. For more information, see [Enable/Disable the Error Correction Feature in PM](/en/vista/vista/project-management/setupmaintenance/enabledisable-the-error-correction-feature-in-pm).

Related information

- [Enable/Disable the Error Correction Feature in PM](/en/vista/vista/project-management/setupmaintenance/enabledisable-the-error-correction-feature-in-pm)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Allow Document Edit

Use this checkbox to enable the selected user
 in VA User Profile to edit Word documents prior to sending them via Create & Send. If
 you clear the checkbox for a user, the Create Document from Template and
 Edit
 Document(s) buttons do not appear for them on the Create & Send
 Documents tab.

Related information

- [PM Create & Send Settings Form](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Select All Attachments

Use this checkbox to set a select-all-attachments default for the selected user in VA User Profile to automatically attach all documents when using Create & Send.

- If selected, all attachments will appear as selected for attachment on the Create & Send Attachments tab.

- If not selected, all attachments will appear as unselected on the Create & Send Attachments tab, and the user can select which attachments to include.

Related information

- [PM Create & Send Settings Form](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Auto Size Lookup Columns

Selected by default. This allows lookup columns to autosize to their contents for this user.
Clear this checkbox to prevent lookup columns from autosizing to their contents for this user. Clearing the checkbox may improve performance.
For a change to this checkbox to take effect, you must save the change, close Vista, and then reopen Vista.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [Use Auto-Log Out](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000498e1--en)

- [Minutes to Log Out](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000498fa--en)

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

## Aatrix Exe Path

The Exe Path field on the VA User Profile form, Info tab.
The location this user must use to access the Aatrix executable.
For use by administrators to override the setting in the same-named field in the VA Site Settings form. If you leave this field blank, the system uses the site-wide entry.
Important: This user must have sufficient permissions to the location in order to run Aatrix.

## Aatrix History Path

The History Path field on the VA User Profile form, Info tab.
For use by hosted environment administrators.
Enter the path that Aatrix will use to maintain data history for this user. The path specified here overrides the Aatrix history path defined in VA Site Settings.
If you leave this field blank, the system uses the site-wide entry.
Important: This user must have sufficient permissions to the location in order to run Aatrix.

## Security Group

 Enter a Security Group for the user. After saving the record, VA Security Groups is updated.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Source

Specify the notification source. Press F4 for a list of valid notification processes. These processes include Notifier jobs, leave requests, Workflow checklists, and unapproved invoices. For more information, refer to Related Topics below.

Related information

- [About Automated Notifications](/en/vista/vista/system-tools/work-flow/about-automated-notifications)

- [About Leave Requests](/en/vista/vista/hr-and-payroll/human-resources/leave/about-leave-requests)

- [Checklists](/en/vista/vista/system-tools/work-flow/checklists)

- [About Unapproved AP Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-unapproved-ap-invoices)

## Destination

Select a destination for notifications sent from the source specified in the Source field. You can have notifications sent to this user’s email address or via Vista™’s internal messaging system. For more information on the internal messaging system, refer to VA Messages in Related Topics below.

Related information

- [About the VA Messages Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-messages-form)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

## Role

The Role field on the VA User Profile form, Roles tab.
Enter the role to assign to this user or press F4 to select from a list of valid roles.
Roles are created and maintained using the
 [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) form. You can access the HQ Roles form by pressing
 F5
 in this field.

## Active

The Active checkbox on the VA User Profile form, Roles tab.
Select this checkbox if this role is active for this user.
Leave checkbox unselected if this role is not active for this user.

## Notes

The Notes field on the VA User Profile form, Roles tab.
Use this field to enter miscellaneous notes about the selected role. The space allowance is virtually unlimited.
You can double-click in this field to bring up the Grid Notes form for easier entry. The Grid Notes form also allows adding standard notes.

### Add a Standard Note

Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note, double-click in this field to access the Grid Notes form, and then click the Standard Notes icon in the toolbar to open the Standard Note Copy form. Enter the standard note to copy (or select from F4 lookup) and click OK. The system inserts the selected note into the field.

### Spelling Check

You can run a spell check on any text in a form. To run a spelling check on the text in this field, click the Spelling icon on the toolbar or select Tools > Spelling .

## Username

This field only applies if you have Viewpoint For Projects™.
Enter the Viewpoint For Projects™ username associated with this Vista user account.
Only Vista users who are associated with a Viewpoint For Projects™ account can send Viewpoint For Projects™ invitations to PM module project contacts.
Click [here](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview) for an overview on Viewpoint For Projects™ integration.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [Viewpoint For Projects (VFP) Integration Overview](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview)

## Password

This field only applies if you have Viewpoint For Projects™.
Enter the Viewpoint For Projects™ user account password.
Click [here](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview) for an overview on Viewpoint For Projects™ integration.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [Administering VFP Settings](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/administering-vfp-settings)
