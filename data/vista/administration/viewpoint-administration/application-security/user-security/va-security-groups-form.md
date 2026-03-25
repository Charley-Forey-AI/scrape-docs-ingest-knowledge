---
title: "VA Security Groups Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form"
---

# VA Security Groups Form

Use this form to set up security groups and add users to them.
Security groups provide a way of administering
 permissions over a group of users rather than setting requirements by individual user.
 Each group is assigned a specific group type (Data, Form, Reports, or Attachment Type).
 Group types determine what areas of the system that users can access. Once you create a
 group, specific permissions can be set in VA Data Security Setup, VA Form Security, VA
 Report Security, or VA Attachment Type Security, depending on the assigned group type.
 For more information on setting up permissions, see [Assign User Security](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-user-security).
This form also pushes security to the SSRS Report Servers set up on the [RP RS Server](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-rs-server-form) form. For more information, see [SSRS Security Overview](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations).
Using group security allows for security maintenance efficiency. It is strongly
 recommended that you assign users to security groups, and then customize individual user
 permissions to override group security. However, you can set permission by user and not
 use group security.
[Create Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/create-security-groups)
[Add Users to Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/add-users-to-security-groups)
Note: Whenever you add, change, or delete a record in this form, the system creates an audit record in the HQMA (HQ Master Audit) table. You can view a list of audit records using the HQ Audit Detail report.

Related information

- [Assign User Security](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-user-security)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)

- [VA Attachment Type Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form)
