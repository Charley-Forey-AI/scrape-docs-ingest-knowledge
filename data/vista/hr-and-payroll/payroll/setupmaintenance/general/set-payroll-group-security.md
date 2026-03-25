---
title: "Set Payroll Group Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-payroll-group-security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-payroll-group-security"
---

# Set Payroll Group Security

Payroll information is typically sensitive, so you may choose
 to set up security so that payroll information is available only to those selected employees
 who should have access to it.
Set up security by payroll group using the Group
 Security tab on the PR Groups. Assign users to the group that should have access to
 information associated with that group.
To set up payroll group security:

1. In VA Security Groups,
 set up a security group that does not have users assigned. Set Group
 Type to Data.

1. In VA Data Security Setup:

1. In the
 Datatype field, press
 F4 and select
 bEmployee.

1. Select the
 Secure Datatype check
 box.

1. In the
 Default Security
 Group field, enter the security group that you set up in
 Step 1.

1. On the Secure
 Tables tab, select the Apply Security
 checkbox for each Table Name you want secured.

1. Click Regenerate Views. The VA View Generator form appears.


1. In VA View Generator:

1. From the
 Available Views list,
 select all of the tables that are to be generated and add them to the
 Views to Regenerate
 list. This list should match the tables you chose to secure in Step 2d.


1. Click Regenerate Views.

1. In PR Groups, Group
 Security tab, enter all of the users that should have access to information
 associated with each payroll group that needs to be secured. The system also grants access to
 members assigned to the default security group in VA Data Security Setup.


Related information

- [PR Garnishment Groups Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-garnishment-groups-form)

- [VA Security Groups Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)

- [About the VA View Generator Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-view-generator-form)
