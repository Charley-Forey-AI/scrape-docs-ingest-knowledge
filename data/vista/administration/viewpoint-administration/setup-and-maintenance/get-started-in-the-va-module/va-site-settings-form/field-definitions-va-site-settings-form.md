---
title: "Field Definitions: VA Site Settings Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form"
---

# Field Definitions: VA Site Settings Form

The following is a list of field descriptions for the VA Site
 Settings form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Lookups

The Lookups field on the VA Site Settings form, Settings tab.
Enter the maximum number of records that return to a lookup when users press F4. Entering a value here is useful when lookups are associated with tables containing hundreds or thousands of records, which can affect the load/refresh speed.
The specified maximum affects all lookups, so consider how restrictive you want to be. Typically, you do not want to be too restrictive with lookups that normally return a smaller record set. Consider setting a limit that restricts larger lookups, but does not affect smaller ones.
If the number of records exceeds the designated maximum, a message displays indicating that there are additional records. If the record you are looking for is not in the current record set, enter selection criteria and click Refresh to re-query the database. You can include wildcards (*, %) or comparison operators (<, >, <>, =, >=, <=) to refine the search as necessary (for example, >6000, *6000, etc.). Clicking Refresh returns a record set based on the entered criteria.
Note: You can override settings for individual users using the User Options form or the VA User Profile form.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [Auto Size Lookup Columns](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049d9f--en)

- [About the User Options Form](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [Set the Maximum Number of Records for Lookups](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-the-maximum-number-of-records-for-lookups)

## Forms

The Forms field on the VA Site Settings form, Settings tab.
Enter the maximum number of records the system returns when you open a form. Entering a value here is useful when forms are associated with tables containing thousands of records that can affect the load/refresh speed
The specified maximum affects all forms, so consider how restrictive you want to be. Typically, you do not want to be too restrictive with forms that normally return a smaller record set. Consider setting a threshold that affects only those forms returning a larger number of records. For example, if you maintain a material file with 100,000 records or more, but the vendor file contains maybe 8,000 records, set a threshold of 10,000, which would affect the material records, but not the vendor records.
Note: Clicking Form Search in the Records menu opens the Form Search form, where you can change the records returned to the form by entering a set of filter criteria. For more information, see [Form Search](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records/about-the-search-panel).
Note: You can override these site-wide settings for an individual user with the [User Options](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form) form or the [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) form.

Related information

- [Search Form Records](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records)

- [About the Search Panel](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records/about-the-search-panel)

## Page Size

The Page Size field in the VA Site Settings form, Settings
 tab.
You can use this field to help make

 Vista forms load faster.
Enter the maximum number of records per page that you want the system to return when any user opens any form. Forms associated with tables containing an extensive number of records will initially retrieve only the number of records that you choose here so the form can load faster. The value in this field only affects users who have opted to use the paging functionality on a form-by-form basis using the paging drop down in the form header's task bar.
During the install process, the system applies the value found in the
 Forms field of the Max Number of Rows section as the default value for this
 field. If you enter a lower value in this field, the speed that forms load may increase
 because the system must retrieve fewer records before displaying the form.
If you choose to enable faster form loads by entering a lower number, consider the following:

- This setting only affects forms where the user has enabled paging using the Pagination On/Off field in the drop-down in the form header's task bar.

- For users that want to override this setting with a lower number on all their forms, change the value in the Page Size field of the VA User Profile form

- Users that have enabled the paging feature cannot opt to set their paging value higher than this setting.

- When any user opens a form with more records than the number in this field, the system groups all records over that number into subsequent pages, each with that same number of records.

Important: This 'paging' result is often confused with missing records. To see more records, navigate to subsequent pages. Use the filter bar as needed.

- Use the green-colored Previous Page and Next Page navigation buttons to view any additional pages of records.

- The status bar in each form will indicate the page number you are on, as well as the total number of pages (for example, Page 1 of 50).

- If you know the ID of a record, you can
 enter that ID in the appropriate key field to display that record. For example, if
 you enter a vendor number in the Vendor field of AP Vendors, the system displays that vendor
 record

Related information

- [Page Size](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049cf3--en)

- [Increase Form Record Load Speed](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records/increase-form-record-load-speed)

- [About the Search Panel](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records/about-the-search-panel)

## Max Warning Rows

The Max Warning Rows field on the VA Site Settings form, Settings tab.
Max Warning Rows field in the VA Site Settings form
Set a row-count threshold to limit the number of rows loaded during a query to ensure that forms load faster.
If a user opens a form that would query the database for more records than the number you set here, Vista will provide the user a chance to apply a filter, which if applied allows the form to load faster.
For example, if you enter 5,000 in this field, and a user opens a form that maintains 6,000 records, the system will ask the user if they want to filter the records before querying the database.
You can override this warning for individual users by checking the Suppress Max Warnings Rows checkbox in the VA User Profile form.

Related information

- [Suppress Max Warning Rows](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049d37--en)

- [Page Size](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-00049885--en)

## Days to Keep Log History

The Days to Keep Log History field on the VA Site Settings form, Settings tab.
 Enter the number of days to keep application log entries. The system deletes older entries on startup.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

## Activate Work Centers

The Activate Work Centers checkbox on the VA Site Settings form, Settings tab.
Select this checkbox to activate the Work Centers
 feature and allow all users access to the [Work Centers](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-work-centers-form) form (which is opened from the main
 application window by selecting Options > Work
 Centers).
Note: Although checking this box gives all users access to the Work Centers form, they will only be able to add the Work Centers to which they have been granted access using the [VA Inquiry Template Security ](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-security-form) form.
Leave this box unselected if you will not be using the Work Centers feature.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [About Work Center Setup](/en/vista/vista/system-tools/work-centers/about-work-center-setup)

## Number of Tabs

Number of Tabs field on the VA Site Settings form, Settings tab.
Enter the maximum number of Work Center tabs that each user should be allowed to add to their main application window. For example if you enter a "2" in this field, a user could add a Dashboard Work Center and PM Work Center in addition to the Menu tab on their main application window.
If you leave this field blank, users will be limited to a total of six Work Center tabs on the main application window.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [About Work Center Setup](/en/vista/vista/system-tools/work-centers/about-work-center-setup)

## Use Auto-Log Out

The Use Auto-Log Out checkbox on the VA Site Settings form, Settings tab.
Select this checkbox to enable the system to automatically log users off of Vista after a specific number of minutes of idle time. Logging a user off will release that Vista license for use by another user.
Once you select this checkbox, go to VA User Profile and select the Allow Auto Log Off checkbox for each user to whom you want to apply this feature. The setting will take effect after the affected user logs out and then logs back in.
Leave this checkbox unselected (default) if you do not want to use the 'auto log off' feature.
For more information, see [Logging Users Off Automatically After Idle Time](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/log-users-off-automatically-after-idle-time).

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [Minutes to Log Out](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000498fa--en)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [Allow Auto Log Off](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049d88--en)

- [Log Users Off Automatically After Idle Time](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/log-users-off-automatically-after-idle-time)

## Minutes to Log Out

The Minutes to Log Out field on the VA Site Settings form, Settings tab.
Enabled and required if the [Use Auto-Log Off](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000498e1--en) checkbox is selected.
Defaults to 120 minutes. You can change the default to a number from 15 to 120.
Enter the number of minutes of idle time, after which selected users (in VA User Profile) will be automatically logged off. Idle time for a user starts at the last press of a keyboard key or movement of a mouse. For example, if you enter a "60" in this field, when a selected user has not pressed a keyboard key or moved the mouse for 60 minutes, that user will be automatically logged off.
For more information, see [Logging Users Off Automatically After Idle Time](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/log-users-off-automatically-after-idle-time).

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [Allow Auto Log Off](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049d88--en)

- [Use Auto-Log Out](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-000498e1--en)

- [Log Users Off Automatically After Idle Time](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/log-users-off-automatically-after-idle-time)

## Login Message

The Login Message field on the VA Site Settings form, Settings tab.
Enter the login message to display when users log on to the system, up to 1,024 characters.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [Create a Login Message](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/create-a-login-message)

## Login Message Will Be Displayed

The Login Message Will Be Displayed checkbox on the VA Site Settings form, Settings tab.
Select this checkbox to display the Log On Message when users log on to the system.
Leave this checkbox unselected if you don't want a log on message displayed each time a user logs onto the system.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [Create a Login Message](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/create-a-login-message)

## Poll Interval (sec), LAN Client

The Poll Interval (sec), LAN Client field on the VA Site Settings form, Settings tab.
Enter the polling interval, in seconds, for the LAN (internal) client. Interval must be equal to or greater than 5 seconds, but cannot exceed 3600 seconds.
The interval specified here determines the wait time between checks to the database for message retrieval. When you send a message, the system puts it in the database, where it sits until it is retrieved. Each running client will check the database periodically and retrieve any applicable messages.
Note: When you change the polling interval, the client making the change and all clients started after the change will use the new interval. Clients that are already running will not use the new interval until the next time they log in.
You can set separate intervals for LAN and Internet clients. This way, you can specify shorter intervals for the faster LAN clients and longer intervals for the slower Internet clients.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [Send an Immediate Message](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/send-an-immediate-message)

- [Poll Interval (sec), Internet Client](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-00049976--en)

## Poll Interval (sec), Internet Client

The Internet Client field on the VA Site Settings form, Settings tab.
Enter the polling interval (in seconds) to use for immediate messages sent via the Internet (external) client. Interval must be equal to or greater than 5 seconds, and not exceed 3600 seconds.
The interval specified here determines the wait time between checks to the database for message retrieval. When you send a message, the system puts it in the database, where it sits until it is retrieved. Each running client will check the database periodically and retrieve any applicable messages.
Note: When you change the polling interval, the client making the change and all clients started after the change will use the new interval. Clients that are already running will not use the new interval until the next time they log in.
You can set separate intervals for LAN and Internet clients. This way, you can specify shorter intervals for the faster LAN clients and longer intervals for the slower Internet clients.

Related information

- [Poll Interval (sec), LAN Client](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-00049966--en)

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [Send an Immediate Message](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/send-an-immediate-message)

## Logged On Users uses Form Security

The Logged On Users uses Form Security field on the VA Site
 Settings form, Settings tab.
Select this checkbox to secure the [Logged On Users](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-logged-on-users-form) form using VA Form Security.
With this checkbox selected, the Logged On Users form:

- After login - available only to users given permissions to view the form

- Before login - not available to any user

Leave this checkbox unselected if not using Form security for the Logged On Users form.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

- [About the Logged On Users form](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-logged-on-users-form)

## Enable Security Administration

The Enable Security Administration checkbox on the VA Site Settings form, Settings
 tab.
Select this checkbox to turn on VA Security Administration. The first user to select this checkbox becomes the first Master Security Administrator.
Once this checkbox is selected by the first
 Master Security Administrator, it can only be cleared by a Master Security Administrator.
 It is grayed out for users who are not Master Security Administrators.
Leave this checkbox unselected (default) if not using VA Security Administration.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [VA Security Administration Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-administration-form)

- [Create a Master Security Administrator](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/create-a-master-security-administrator)

- [Turn on the VA Security Administration Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/turn-on-the-va-security-administration-form)

## Disable Saving Password on Login

The Disable Saving Password on Login checkbox on the VA Site Settings form, Settings
 tab.
Select this checkbox to remove the Save Password
 checkbox from the Vista Log On screen. This will require all users to enter their
 password each time they log in to Vista.
Leave this checkbox unselected (default) to allow users to save their login passwords.
 When not selected, the Save Password checkbox displays on the
 Vista Log On
 screen.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

- [Log in to Vista Using Classic Credentials](/en/vista/vista/system-tools/user-interface-guide/log-in-to-vista/log-in-to-vista-using-classic-credentials)

## Disallow Self Security Modification (All Users)

The Disallow Self Security Modification (All Users) checkbox on the VA Site Settings
 form, Settings tab.
Select
 this checkbox to prevent all Vista users from changing their own security access settings. This
 affect all users. It also overrides any user-by-user selection(s) of the Disallow Self Security
 Assignment checkbox in the VA User Profile form.
Leave this checkbox unselected to allow users to change their own security access
 settings.

Related information

- [Disallow Self Security Assignment](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049cca--en)

## Organization ID

The Organization ID field on the VA Site Settings form,
 Settings tab.
The system automatically populates this field with the organization ID specified during installation of Vista. You should not need to change this value; however, you can update it if needed.
Vista uses this unique identifier to track the speed and stability of your Vista environment to ensure that your solution is consistently performing at peak efficiency.

## Username

The Username field on the VA Site Settings form, Add'l Settings tab.
This field applies only if you have Viewpoint For Projects™. See [ Integration Overview](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview) for an overview on Viewpoint For Projects™ integration.
Enter the Username for accessing Viewpoint For Projects™.
Note: Once you enter the username and password, you must associate Vista with a specific Viewpoint For Projects™ enterprise. For more information, see [Enterprise](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-00049986--en).

Related information

- [Viewpoint For Projects (VFP) Integration Overview](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview)

- [Administering VFP Settings](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/administering-vfp-settings)

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

## Password

The Password field on the VA Site Settings form, Add'l Settings tab.
This field only applies if you have Viewpoint For Projects™. See [ Integration Overview](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview) for an overview on Viewpoint For Projects™ integration.
Enter the Password for accessing Viewpoint For Projects™.
Note: Once you enter the username and password, you must associate Vista with a specific Viewpoint For Projects™ enterprise. For more information, see [Enterprise](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-00049986--en).

Related information

- [Viewpoint For Projects (VFP) Integration Overview](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview)

- [Administering VFP Settings](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/administering-vfp-settings)

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

## URL

The URL field on the VA Site Settings form, Add'l Settings tab.
This field applies only if you have Viewpoint For Projects™. See [ Integration Overview](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview) for an overview on Viewpoint For Projects™ integration.
Enter the URL to use for Viewpoint For Projects™.
Note: Once you enter the username and password, you must associate Vista with a specific Viewpoint For Projects™ enterprise. For more information, see [Enterprise](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-00049986--en).

## Enterprise

The Enterprise field on the VA Site Settings form, Add'l Settings tab.
Once you have entered a Username and Password for accessing, Viewpoint For Projects™ , click the Select button to associate Vista with a specific
 Viewpoint For Projects™
 enterprise.
You can associate projects in the selected enterprise with the projects in Vista.
 See [ Integration Overview](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview) for an overview on Viewpoint For Projects™ integration.

Related information

- [Viewpoint For Projects (VFP) Integration Overview](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview)

- [Administering VFP Settings](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/administering-vfp-settings)

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

## Comdata FTP Settings

The Comdata FTP Settings section on the VA Site Settings form, Add'l Settings tab.
These fields apply only if you are using Comdata as your credit service provider. See [Setting Up Credit Card Payments](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments) and [Setting Credit Services Information](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/set-up-credit-services-with-comdata) for information on the process.
Enter the URL, Port, User ID, and Password for the SFTP server. These values were provided to you by Comdata.
You can override these fields per FTP session in the AP FTP form, or per company in AP Company Parameters.

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

## Customer API URL

The Customer API URL field on the VA Site Settings form, Add'l Settings tab..
Enter the URL (provided by Corpay) to use for invoice attachment file uploads, payment batch uploads, and return file processing.

## Identity URL

The Identity URL field on the VA Site Settings form, Add'l Settings tab.

Enter the URL (provided by Corpay) for the ePayments identity API.

## Exe Path

The Exe Path field on the VA Site Settings form, Add'l Settings tab.
For use by hosted environment administrators.
Enter the path your hosted or on-premise environment will use to access the Aatrix executable.
Important: All users must have sufficient permissions to this location in order to run Aatrix.

Note: You can override this path by user in VA User Profile. The system will only use this location if no location is specified for the selected user in VA User Profile. If no location is specified for the user and you do not specify a location here, the system will install Aatrix on the user's local computer.

## History Path

The History Path field on the VA Site Settings form, Add'l Settings tab.
For use by hosted environment administrators.
Enter the path that Aatrix will use to maintain data history.
Note: You can override this path by user in VA User Profile. The system will only use this path if no history path is specified for the selected user in VA User Profile. If no history path is specified at the user level or here, the system will store Aatrix history on the user's local computer.

## Vista Web URL

The Vista Web URL field on the VA Site Settings form, Add'l Settings tab.
This field is automatically populated when you install Vista Web and displays the base URL used for Vista Web forms.
If you are using a Direct Company Login (PRCo Specific URLs), this field may not auto-populate with the company-specific URL. You will need to enter the base portal URL (for example: https://vistawebportal.com).

Related information

- [Vista Web Forms](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/vista-web-forms)

## MFA Required

The MFA Required field on the VA Site Settings form, Add'l Settings tab. Use this field to configure single sign-on (SSO) settings.
You must be a system administrator in order to view and edit this field.
Note:Trimble ID must be enabled for your company in order for SSO settings to work.

Depending on how your company wants to implement authentication during sign-in, select one of the following options from the MFA Required dropdown field:

- None: Select this option if you do not want to require any sort of multifactor authentication at log in. Users can still choose to enable MFA on an individual basis while setting up their Trimble ID profile.

- MFA: Select this option to require multifactor authentication through Trimble ID. Other MFA methods are not permitted with this option.

- Federated: Select this option to require multifactor authentication, either through external providers (such as Microsoft, Okta) *or* through Trimble ID. Federated authentication is based on a user's email domain.

For more information about setting up MFA, see [Configure Multifactor Authentication and Additional Login Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/configure-multifactor-authentication-and-additional-login-settings).

## Allow Social Logins

Note: To simplify login settings and eliminate potential configuration conflicts, this option has been removed.

## User Email Enforcement

The User Email Enforcement checkbox on the VA Site Settings form, Add'l Settings tab. Use this field to configure single sign-on (SSO) settings.
You must be a system administrator in order to view and edit this field.
Note:Trimble ID must be enabled for your company in order for SSO settings to work.

Select the User Email Enforcement checkbox to require users to log into Vista using their company email. This setting mandates that a user's email in their VA User Profile matches the email used with their Trimble ID profile.
If the emails do not match, the user needs to edit their Trimble ID profile to have the same email address as in the VA User Profile. For more information about setting up your Trimble ID, see [Upgrade Your Vista Login to Trimble ID](/en/vista/vista/system-tools/user-interface-guide/log-in-to-vista/single-sign-on-with-trimble-id/upgrade-your-vista-login-to-trimble-id).
For more information about setting up login settings, see [Configure Multifactor Authentication and Additional Login Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/configure-multifactor-authentication-and-additional-login-settings).

## Send email via SMTP

The Mail setting Send email via SMTP checkbox on the VA Site Settings form,
 Email Settings tab.
Select this checkbox to force all email from this company's
 Vista accounts to be sent via SMTP,
 even when users have MS Outlook installed.

You can override this setting [on a per-user basis in VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049c6a--en).

Related information

- [VA Site Settings Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form)

## Use SSL/TLS

The Mail setting Use SSL/TLS checkbox on the VA Site Settings form, Email
 Settings tab.
SMTP is used to send emails generated by clients within the Vista system.
When the Use SSL/TLS
 checkbox is selected, the email connection runs under either SSL or TLS protocols, which
 are secure protocols. Some email services accept only connections from SSL or TLS. If
 you check this box, make sure your [Host](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-76v1pwu6--en) and [Port](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form/field-definitions-va-site-settings-form#ID-pu8c0vib--en) settings support SSL or TLS.

## Email Client

The Mail settings Email Client dropdown field
 on the VA Site Settings form, Email Settings tab. SMTP is used to send emails generated by clients within the Vista system.
Select the endpoint for your email provider:

- Basic SMTP

- Microsoft 365

- Gmail (experimental)

See the following articles for configuration information, depending on if you
 are using SMTP Basic Auth or SMTP OAuth (Microsoft or Gmail):

- [Configure SMTP Basic Auth Email
 Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-basic-auth-email-settings)

- [Configure SMTP OAuth Email Settings in
 Vista](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-up-vista-to-send-emails/configure-smtp-email-settings/configure-smtp-oauth-email-settings-in-vista)

## Frequency (sec)

The Send Email Frequency field on the
 VA Site Settings form, Email Settings tab.
In the Frequency
 (sec) field, enter how often queued emails will be sent, in seconds.
Note: Changes that you make to this value will go into effect the
 next time the Vista application services are started.

## Retry Attempts

The Send Email Retry Attempts field on
 the VA Site Settings form, Add'l Settings tab.
In the Retry Attempts field, enter how many times the system should attempt to send queued emails before giving up.

## Host

The SMTP Basic System Settings Host field on the VA Site
 Settings form, Email Settings tab. SMTP is used to send emails generated by clients within the Vista system.
If you are setting up SMTP Basic Auth, enter the Host name, which is a
 server name in your organization or a third-party ISP's DNS name or IP
 address. Examples: *smtp.office365.com*, *smtp.gmail.com*
Note: If you are setting up SMTP OAuth, this field
 automatically populates with the correct value.

## Port

The SMTP Basic System Settings Port field on the VA Site
 Settings form, Email Settings tab. SMTP is used to send emails generated by clients within the Vista system.
If you are setting up SMTP Basic Auth, in the Port field, enter the
 port number used on the server for SMTP.
Note: If you are setting up SMTP OAuth, this field
 automatically populates with the correct value.

## Email Address

The SMTP Basic System Settings Email
 Address field on the VA Site Settings form, Email Settings tab. SMTP is used to send emails generated by clients within the Vista system.
In the Email Address
 field, enter the email used as the outgoing address (the *from* address) in emails sent via SMTP. This is the address of the main
 administrator account you set up for your email provider.
Note: There are several other areas of Vista that send emails: AP
 Email Pay Info, PR Pay Stub Notify, and WF Notifier Job Manager. If the From (also called Return Email Address) field is
 left blank in these other areas, the address you enter here in VA Site Settings will
 be the default outgoing address for emails sent from those other areas. For more
 information, see the following:

- [AP Email Pay Info Fields](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-email-pay-info-form/field-definitions-ap-email-pay-info-form#ID-00005f24--en)

- [PR Pay Stub Notify Fields](/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-pay-stub-notify-form/field-definitions-pr-pay-stub-notify-form#ID-00039cea--en)

- [WF Notifier Job Manager Fields](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager/field-definitions-wf-notifier-job-manager-form#ID-0004de88--en)

## Domain

The SMTP Basic System Settings Domain
 field on the VA Site Settings form, Email Settings tab. Some SMTP services require a valid username and password to be sent as part of the email sending request.
If your SMTP service requires authentication and the service is within an NT domain, enter this name in the Domain field.
This field is not required if you are setting up SMTP OAuth.

## Username

The SMTP Basic System Settings Username
 field on the VA Site Settings form, Email Settings tab. Some SMTP services require a valid username and password to be sent as part of the email sending request.
If your SMTP service requires a username of a
 registered user, enter it in the Username field.
 Example: *mysmtpaccount@company.com*
This field is not required if you are setting up SMTP OAuth.

## Password

The SMTP Basic System Settings Password
 field on the VA Site Settings form, Email Settings tab. Some SMTP services require a valid username and password to be sent as part of the email sending request.
If your SMTP service requires authentication, enter the password of a registered user in the Password field.
This field is not required if you are setting up SMTP OAuth.

## Client ID

The SMTP OAuth Client ID field on the
 VA Site Settings form, Email Settings tab.
Enter your email provider's Client ID.
This field is required, unless your Email
 Client is SMTP Basic Auth. If
 Email Client is blank, this field is disabled.

## Tenant ID

The SMTP OAuth Tenant ID field on the
 VA Site Settings form, Email Settings tab.
Enter your email provider's Tenant ID.
This field is required only if your Email Client is
 Microsoft 365. If your client is
 SMTP Basic Auth or
 Gmail, this field is not required. If
 Email Client is blank, this field is
 disabled.

## Client Secret

The SMTP OAuth Client Secret field on
 the VA Site Settings form, Email Settings tab.
Enter the secret from your email provider settings.
This field is required, unless your Email
 Client is SMTP Basic Auth. If
 Email Client is blank, this field is disabled.
