---
title: "Create a Vista SQL User in VA User Profile | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-sql-user-in-va-user-profile"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-sql-user-in-va-user-profile"
---

# Create a Vista SQL User
 in VA User Profile

Legacy cloud or on-premises customers can set up Vista users
 in VA User Profile with SQL classic credentials, requiring a SQL username and
 password to access the Vista application.
In order to complete this process, you must have access
 to the VA Password form. For instructions, see [Apply Form Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-form-security-settings).Important: If you are a Trimble
 Construction One cloud-hosted Vista customer, this option to
 create new users with classic credentials (SQL or Windows
 logins) will no longer be supported in the fall of 2025. At
 that point, you should [Create a Vista User SSO Account with Trimble ID](/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-user-sso-account-with-trimble-id) when setting up new Vista users. Legacy cloud and
 on-premises customers will still be able to set up
 new users with classic credentials.

1. From the Vista main menu, go to Viewpoint Administration > Programs > VA User Profile.For more information about this form, see [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form).

1. At the
 top of the form, select the New
 Record icon () in
 the toolbar.

1. In the User Name field, enter the user's login name.See [User Name](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049ae1--en) for
 instructions on how to select and format a user name.Tip: Press F1
 to see additional Help on any field in the
 form.

1. Enter the user's User Name.

1. In the User
 Type dropdown field, select Vista.

1. On the Info tab, enter additional
 user information in the upper portion of the form.If you are a cloud-hosted organization with a Named User
 License (NUL) license model, choose a
 License Type from the
 dropdown.

1. Use the Form & Report Options section to set the user's general settings.Note: This form and the User Options form (Options > User
 Options from the main menu) update one
 another. However, not all of the fields in this
 section update the User Options form. Refer to the
 [User Options](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form) F1 help
 for each field to determine how updates between the
 forms occur.

1. Use the Defaults section to set default values for the specific user.

1. Use the Permissions section to set
 the user's ability to modify main menu or form settings, and
 to determine if the user can view earnings rates in the PR
 Timecard Entry form.

1. Use the Override Max # of Rows Returned section to limit data records in lookups, the attachment lister, and forms.

1. Use the Menu Options section to set the user's menu options.Note: The fields in this section update options in the View and
 Options menus on the main menu (and vice versa).
 Refer to the F1 help for each field to determine
 whether it updates the View or Options menu
 selections.

1. To automatically log this user out of the application after a specific number of minutes of idle time, select the Auto-Log Off checkbox.

1. To prevent lookup columns from auto-sizing to their contents for this user, clear the Auto Size Lookup Columns checkbox.

1. [Enable Leave Requests](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/enable-leave-requests) for this employee.

1. [Set Timesheet Permissions](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-timesheet-permissions) for the user.

1. If the user will be using the Project Management module, complete the PM Error Corrections and Create and Send sections.

1. In the Security Groups tab, [Add the User to a Security
 Group](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-users-to-security-groups).

1. In the Notification Prefs tab, [Set User Notification Preferences](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-user-notification-preferences) for the user, as necessary.

1. If the user will be using Viewpoint For Projects™, complete the fields in the Project Collaboration tab.

1. Save the record. If any of the changes impact this form, you may need to close and reopen Vista to see the effect of those changes.If this user has not been
 set up in Microsoft SQL Server, and is not a domain user,
 the system displays a message that the system will attempt
 to create a SQL Server login.

1. Select Close.Note: If the user name contains a domain name, it is assumed that
 you have created a SQL login and the system doesn't
 attempt to create one.
The VA Password form opens.

1. Enter and confirm the password in the appropriate fields and select OK.The system creates the required SQL server login (if the user
 does not already have one), so that the user can access
 information from the Vista database.

1. Save the record.Note:Due to
 updates in the license provisioning process, when you save a new record in VA User
 Profile, the Deactivated
 checkbox will be selected and temporarily unavailable. After approximately one
 minute, the record can be refreshed, which automatically clears the checkbox. If a
 license is available, the user will be successfully activated.

Share the login credentials with the new user so they
 can log in to Vista.

Related information

- [User Type](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-0004bd04--en)

- [Create a Vista Domain User](/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-domain-user)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [About the Vista Configuration Form](/db/organizations/viewpoint/repositories/vista-production/content/documents/Vista/Viewpoint/VPMenu/Forms/Vista_by_Viewpoint_Configuration/c_vpmenuvista_configuration.dita)
