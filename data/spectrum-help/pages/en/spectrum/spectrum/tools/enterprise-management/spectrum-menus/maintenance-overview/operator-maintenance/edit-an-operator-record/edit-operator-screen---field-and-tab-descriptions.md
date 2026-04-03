---
title: "Edit Operator Screen - Field and Tab Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/operator-maintenance/edit-an-operator-record/edit-operator-screen---field-and-tab-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/operator-maintenance/edit-an-operator-record/edit-operator-screen---field-and-tab-descriptions"
---

# Edit Operator Screen - Field and Tab Descriptions

Use these descriptions as a reference when completing the fields in the Edit Operator screen. Access this screen from the Operator Maintenance screen.
Information contained in this window is available for review using the Operator Listing screen. See [View a List of Operators](/en/spectrum/spectrum/system-administration/installation/view-a-list-of-operators).

## Properties tab

Fields/ButtonsDescriptions
User TypeSelect a valid User type for the Operator (Office, Project Manager, Field, Employee Kiosk, Subcontract Kiosk, Service Tech). This is a required field , but can be changed later.
Logon IDDefaults from the Operator Maintenance screen. Press Enter to keep this ID, or type a new ID. The user can change this in Operator Preferences.
NameDefaults from the Operator Maintenance screen. Press Enter to keep this name or type a new name.
E-mailEnter the email address for this operator. The operator can change this in Operator Preferences.Note: A message displays below this field to let you know if the email address has been authenticated (has a username) or if it requires authentication in the E-mail Servers screen.

Credentials (button)Opens the E-mail Credentials window.
Email address and Email server are required.The Username field is required only if the selected Email server requires authentication.
Not all authentication mechanisms require a password, but you may enter one, up to 80 characters.

 Contact
ProfileEach operator is assigned to a Profile that controls the default Dashboard and Navigation Bar layout. The software ships with two standard profiles: DEFAULT and FULL. All users are initially set to DEFAULT for security reasons; this is the lowest level and contains only those apps that are safe for all users (for example Favorites, My Jobs, and To Do List).
Time-out minutesSet the default time limit that the system will remain open without the user's activity. The default limit is 120 minutes. This time limit can also be found in the Operator Preferences window.
Default scheme The security scheme that has been assigned to this operator defaults from the Operator Maintenance screen. Choose one:

- Press Enter to use the default scheme.

- Enter a different scheme.

- Press F4 to select from a list of available schemes. For more information about schemes, see [Security Schemes Overview](/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/security-schemes-overview).

Authorized to maintain 'saved selections' for all users? Select if this user should have the authority to maintain the saved selections for other operators.
Authorized to add Crystal Reports?Select if this user should have the ability to add custom Crystal Reports to the system.
TID usernameIf the user logs in using Trimble ID, their username is listed.Note: Every user's Trimble ID is unique.

StatusSelect the status you want to assign this operator.
If set to Inactive, the operator cannot log in.Tip: The Inactive status is useful if you want to retain all user information but prevent logging in, such as during a leave of absence.

Company preference
Always start in last company accessed?Select to which company the application should direct the operator upon logging in.
Always start in same company?

## Companies tab

Use this tab to add, edit, and delete selected companies, or add all companies found in the Enterprise Installation company list to this operator's profile.
You can also use this screen to edit company information for the companies an operator has access to, that is, those appearing to this operator when they select the Companies button on the Site Map.
FieldsDescriptions
CompanyA list of the company codes which this operator can access.
TitleA list of the company names which this operator can access.
Default?Displays either Yes or nothing, depending on the selection(s) in the Company preference section of the Properties tab.
OverridesA list of the current company-specific or scheme settings defined for this operator.
Buttons
NewSelect to add a new or existing companies to this operator's list.
SwitchSelect a company appearing in the operator's list and select this button to make changes to that company.
DeleteSelect a company appearing in the operator's list and select this button to remove that company from the list.
Add All CompaniesSelect to add all the companies listed in the Enterprise Installation screen to this operator's company list.

## Scheme tab

Use this tab to apply a security scheme to an operator.
Fields/ButtonsDescriptions
Scheme setting for this companyDecide whether you want this operator to use the default security scheme, override the security scheme, or override the scheme and use the company-specific settings.

- Use operator default scheme

- Use override scheme

- Specify company overridesSelecting this option enables the Restriction times code drop-down.

Authorization in this company
Allow access to command prompt?Enabled only if the Scheme setting option is set to Specify company overrides. Most operators don't need access to the command prompt.

## Categories tab

This tab displays only if the current operator is not assigned for security schemes in this company. Use this screen to assign security levels (1-9) to the available SPECTRUM categories.
Fields/ButtonsDescriptions
CategoryThe available modules are listed. Select New to include a category not listed for this operator.
LevelFor each module, enter a number (1 to 9) indicating this operator's level of security clearance for access to the module. If you enter (1), it's likely this this user will not have access - because the module will probably be assigned a number higher than (1). If you enter (9), this user will necessarily have access to the module - because the module cannot have a higher number assigned to it.
While using the application, the clearance level you enter here is compared by the system to the required security level entered for the module on the Function Security Maintenance screen. If the level here is the same or higher than the level assigned to the function, the system will permit the access.

DescriptionView only. Displays the description of the category.

## Jobs tab

This tab is available only if the Utilize job-based security checkbox is selected on the Job Cost Installation - Security tab and this operator possesses security access to the JC or PJ category from the scheme or operator override category list.
This tab works in conjunction with the Job Cost and Project Management modules and is used to restrict access to job information in certain inquiries, reports, and file processing.

## Cash Management tab

This tab is available only if the Cash Management Installation checkbox for account-based security is selected and the operator possesses security access to the CM category from the scheme or operator override category list.
This tab works in conjunction with the Cash Management module and is used to restrict access to certain inquiries, reports, data entry, and maintenance screens.

## Images tab

This tab is available only if the Document Imaging module is present on your system.

## Invoices tab

This tab is available only if the Use Invoice Approval processing checkbox is selected in the Accounts Payable Installation - Invoice Approval tab and if the operator has security access to the AP category from the scheme or operator override category list.Note: The Invoice Approval Routing enables the option to track invoices by routing them through reviewers for approval.
