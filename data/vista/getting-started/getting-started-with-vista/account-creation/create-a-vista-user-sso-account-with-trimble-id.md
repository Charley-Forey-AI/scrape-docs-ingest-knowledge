---
title: "Create a Vista User SSO Account with Trimble ID | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-user-sso-account-with-trimble-id"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/account-creation/create-a-vista-user-sso-account-with-trimble-id"
---

# Create a Vista User SSO Account with Trimble ID

Create a user with a Trimble ID single sign-on (SSO) account
 in Vista.
In order to complete this process, you must have access to
 the VA Password form. For instructions, see [Apply Form Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-form-security-settings).Note: Once implemented in early 2025, Trimble ID will be available to Trimble Construction One cloud-hosted Vista customers only.If you are a legacy cloud or on-premises customer, contact your account representative to learn about how you can transition to the modern cloud and gain access to all the latest features.

1. From the Vista main menu, go to Viewpoint
 Administration > Programs > VA User Profile.

1. At the top of the form,
 select the New Record
 icon () in the toolbar.

1. In the User Name field, enter the
 user's email address. The user name *must* be an email address in order to set up the Vista
 account for Trimble ID.

1. In the User Type dropdown field,
 select Vista.

1. Enter the user's Full Name
 and ensure the Email Address matches the User Name.

1. Select the Is SSO Account
 checkbox when creating the new user. With this checkbox selected, Vista bypasses the creation of a SQL account for
 this user, and instead creates an SSO record based on the user's email
 address.

Note: If you do not
 select the Is SSO
 Account when creating a new Vista account, the user will
 still be able to go through the Trimble ID account migration process and
 log into Vista. When this happens, the system will deactivate the
 original non-SSO account you set up and create a new SSO account for the
 user. To avoid these duplicate deactivated accounts, always select the
 Is SSO
 Account checkbox when creating new Vista users.

1. Configure additional settings and permissions for the user.

1. Use the Form & Report Options section to set general settings for
 the user.Note: This form
 and the User Options form (Options > User
 Options from the main menu) update one another. However, not
 all of the fields in this section update the User Options form.
 Refer to the [User Options](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form) F1 help for each field
 to determine how updates between the forms occur.

1. Use the Defaults section to set default values for the specific
 user.

1. Use the Permissions section to set the user's ability to modify main
 menu or form settings, and to determine if the user can view earnings
 rates in the PR Timecard Entry form.

1. Use the Override Max # of Rows Returned section to limit data records
 in lookups, the attachment lister, and forms.

1. Use the Menu Options section to set the user's menu options.Note: The fields
 in this section update options in the View and Options menus on the
 main menu (and vice versa). Refer to the F1 help for each field to
 determine whether it updates the View or Options menu
 selections.

1. To automatically log this user out of the application after a specific
 number of minutes of idle time, select the Auto-Log Off
 checkbox.

1. To prevent lookup columns from auto-sizing to their contents for this
 user, clear the Auto Size
 Lookup Columns checkbox.

1. [Enable Leave Requests](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/enable-leave-requests) for this employee.

1. [Set Timesheet Permissions](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-timesheet-permissions) for the user.

1. If the user will be using the Project Management module, complete the
 PM Error Corrections and Create and Send sections.

1. In the Security Groups tab, [Add the User to a Security Group](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-users-to-security-groups).

1. In the Notification Prefs tab, [Set User Notification Preferences](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-user-notification-preferences) for the user, as necessary.

1. Save the new user record.

Note: If there is an email
 mismatch, the system will automatically change the User Name to match the Email Address.

After applying security and other settings, ask your
 user to [Log in to Vista Using Trimble ID](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/log-in-to-vista/single-sign-on-with-trimble-id/log-in-to-vista-using-trimble-id). When the user signs in using Trimble ID, their new Vista
 SSO account links to their Trimble ID.For more information, watch this video about
 creating Vista accounts: [Trimble ID Account Creation for Vista - Video](/en/vista/vista/videos/administration/trimble-id-account-creation-for-vista---video).
