---
title: "Prevent Use of Third-Party Applications to Modify Tables | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/user-security/prevent-use-of-third-party-applications-to-modify-tables"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/user-security/prevent-use-of-third-party-applications-to-modify-tables"
---

# Prevent Use of Third-Party Applications to
 Modify Tables

Use the VA Application Role Security form to prevent unauthorized users from modifying Vista™ data tables via third-party applications such as MS Query or MS Access.
Note: To access this form, you must have permissions set up via [VA Form Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form) and have system administrator permissions in SQL Server.
To prevent third-party programs from being used to modify security tables and data tables:

1. In VA Application Roll
 Security, select the Use Application Security
 checkbox. This will automatically select the Lockdown
 Security Tables checkbox.

1. Click Update
 Security. The security settings are saved. To prevent access via
 third-party programs to:

- Security tables but allow
 access to data tables, follow the above procedure, except that the
 Use Application
 Security checkbox is unselected, but the Lockdown Security Tables checkbox is selected.

- Neither security tables nor
 data tables, follow the above procedure, except that both the Use
 Application Security and the Lockdown Security Tables checkboxes are unselected.


- Data tables but allow access
 to security tables, note that this combination is not allowed. If the
 Use Application
 Security checkbox is selected, then the Lockdown Security Tables checkbox must be selected
 also.

Related information

- [VA Application Role Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-application-role-security-form)
