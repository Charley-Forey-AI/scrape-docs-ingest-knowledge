---
title: "Securing Datatypes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes"
---

# Securing Datatypes

Use the VA Data Security Setup form to secure datatypes.
When securing datatypes, you will select the datatype that requires security and then indicate to which tables the security applies.
Note: The Secure Tables tab displays all tables that contain an occurrence of the specified datatype, the field name (Instance Column), and the Qualifier Column (the qualifier is generally the company). Field names may differ between forms. For example, if the datatype is ‘bEmployee’, the instance column might be called 'Employee’ on one form and ‘Contact Name’ on another.
To secure datatypes:

1. In the VA Data Security Setup form, enter a datatype in the Datatype field. Press F4 for a list of valid datatypes.

1. Select the Secure Datatype checkbox.

1. Enter a security group in the Default Security Group field. Note: The system automatically grants this security group access to any new instance of the specified datatype. If you do not assign a default, you must manually assign access in VA Data Security Access.

1. Save the record. The
 system displays a dialog box asking if you want to update all instances of the
 specified datatype with the new default security group.

1. Click Yes to have each instance of the datatype set to the specified default security group. Note: If you click No, the system sets the security group to blank for each applicable instance and you will need to assign security manually. For more information, see [VA Data Security Access](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-data-security-access-form).

1. On the Secure Tables tab, check the Apply Security box for each table that requires security. The system checks the Not Synchronized box for each table that you select. Note: When the Not Synchronized box is checked, it means that you have not yet updated security for the table.

1. Click the Regenerate
 Views button. The VA View Generator form displays.

1. Use the VA View Generator form to regenerate views. For more information, see [VA View Generator](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-view-generator-form).

1. Close VA View Generator.
 Focus returns to VA Data Security Setup. The system checks the Secured box for each table that was previously unsynchronized. Note: When the Secured box is checked for a table, this indicates that
 datatype security is active.

1. Use VA Data Security Access to assign access permission for any other security groups, as necessary. If you change the default security group for a secured datatype, a message displays indicating that the default security group has changed and asks if you wish to update all instances with the new default security group. Click Yes to have the system update all instances currently assigned the previous default security group (or where the security group is blank) with the new security group. The system leaves all other instances intact.
Note: If Application Role Security is on, views grant modification access to users logged in through the system. If Application Role Security is off, views grant access to all permissions, including third-party tools. For more information, see [VA Application Role Security](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-application-role-security-form).

Related information

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)

- [About the VA View Generator Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-view-generator-form)

- [VA Application Role Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-application-role-security-form)
