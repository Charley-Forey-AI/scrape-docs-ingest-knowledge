---
title: "Copy Security Using the VA User Profile Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/user-security/copy-security-using-the-va-user-profile-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/user-security/copy-security-using-the-va-user-profile-form"
---

# Copy Security Using the VA User Profile Form

When creating users in VA User Profile, the system allows you to copy security from one user account to another.
Before you copy security to a new user, you must have saved the user login in the system.

The copy includes module, form, tab, report, attachment, and data security settings. Additionally, the system assigns the security groups from the source account to the destination account.
When you copy security permissions, the system copies only those permissions from companies to which your user account also has access. Your access is determined by the security permissions given to your user account in VA Form Security. If desired, you can run the VA Copy Security Report to preview which permissions will be added.
If [VA Security Administration](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-administration-form) is turned on, you are able to copy security for only the company/module combinations for which you were given permissions in the VA Security Administration form.
To copy security to a user account:

1. In VA User Profile, select the login that requires security.

1. Select Copy Security. The VA Copy Security form displays.

1. On the VA Copy Security form, specify the source user account you are copying from in the Copy from Login Name field.

1. If you want to see which permissions will be added to the destination user account, select Preview. The VA Copy Security Audit Report opens.

1. To copy permissions, select OK on the VA Copy Security form. The system copies the security setup from the source user account to the selected destination user account. If you are copying security to a user account that already has security settings, the system displays the following warning:

- Select Yes to replace the user's existing security setup with the new security setup. Once the copy process is complete, the destination user may no longer have access to the same modules, forms, tabs, reports, and datatypes they previously had access to. In addition, the system removes the destination user from any previously assigned security groups, unless the source user also belongs to those security groups. You may want to review the new security setup and make any necessary modifications.

- Select No to add new security, but leave the existing security intact. For example, User A has access to all modules except AP, AR, JB, and PR. User B has access to the same modules as User A, plus access to AP and AR. To copy the security for AP and AR from User B to User A, select No and the copy process skips the existing module security and adds the security for AP and AR. Additionally, when you select No, the copy process skips any security that is more restrictive than the existing security. For example, User A has security for AP set up at the Tab level. User B has security for AP set up at the Form level. If you copy from User A to User B, and do not select Yes to replace security, the copy process does not copy User A's AP security to User B.

- Select Cancel to return to return to VA User Profile and leave security settings unchanged.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [VA Copy User/Group Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-copy-usergroup-security-form)

- [Copy User or Group Security](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/copy-security-using-the-va-user-profile-form/copy-user-or-group-security)

- [About the VA Copy Security Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/about-the-va-copy-security-form)

- [Assign User Security](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-user-security)
