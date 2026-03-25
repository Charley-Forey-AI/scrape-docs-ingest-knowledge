---
title: "Change the Application Role Security Password | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/user-security/change-the-application-role-security-password"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/user-security/change-the-application-role-security-password"
---

# Change the Application Role Security Password

Vista uses the application role password to access MS SQL Server. This password was set by default when the Vista application was first installed.

- You must have security access to the [VA Application Role Security](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-application-role-security-form) form, granted using the [VA Form Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form) form.

- You must have system administrator permissions in MS SQL Server.

Changing the application role password requires a few supporting steps:

- Prior to changing the password, you must ensure no other users are logged in and that no one can log in to Vista so you can safely turn off Application Security.

- After changing the password, you must turn
 Application Security back on, stop and restart the Viewpoint Remote Service,
 and then ensure users are once again allowed to log in.

 All these requirements are covered in these steps:

1. Prevent new login instances.

1. Navigate to the Configure Viewpoint Remote Service application on the server.

1. Clear the Allow Logons checkbox.

1. Remove existing login instances.

1. In the VA Application Role Security form, click View Logged on Users.The Logged On Users window appears, displaying a list of users already logged in.

1. Send an email to alert users to log out.For instructions, see [Email Logged On Users](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-logged-on-users-form/email-logged-on-users).Important: Proceed only after all users are logged out.

1. Turn off Application Security.

1. If the Use Application Security checkbox is selected, clear it.Application security is now disabled.

1. Click Update Security.

The system logs you out.

1. Create the new password.

1. Enter the password in the New Password field.

1. Re-enter it in the Re-enter Password field.

1. Click Update Password.

1. Turn Application Security back on.

1. If you cleared the Use Application Security checkbox in step 3, select it now.

1. Click Update Security.

1. Stop and start the Viewpoint Remote Service. Use the Start-Stop Viewpoint Remote Service application on the server.

1. Reinstate users' ability to log in.

1. Navigate to the Configure Viewpoint Remote Service application on the server.

1. Select the Allow Logons checkbox.

The Application Role Security password is now changed.

Related information

- [VA Application Role Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-application-role-security-form)

- [New Password](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-application-role-security-form/field-definitions-va-application-role-security-form#ID-00047f5c--en)

- [Re-enter Password](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-application-role-security-form/field-definitions-va-application-role-security-form#ID-00047f63--en)
