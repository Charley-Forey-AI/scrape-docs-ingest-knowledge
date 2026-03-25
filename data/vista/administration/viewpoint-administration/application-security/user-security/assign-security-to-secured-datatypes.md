---
title: "Assign Security to Secured Datatypes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-security-to-secured-datatypes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-security-to-secured-datatypes"
---

# Assign Security to Secured
 Datatypes

Use this form to assign security groups access to secured datatypes. When assigning security, you must filter for all instances of a datatype and assign security to security groups. You cannot assign datatype security to individual users.
Prior to assigning access here, you must secure the datatype in [VA Data Security Setup](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form).
Note: Restricting access to a specific module or form does not prevent unauthorized users from accessing restricted data from another module or form, or even in a related inquiry or report. You must secure the datatype and associated tables to ensure restricted access.
There are two access levels available for data security access:

- Allowed – Use this option to allow access to the datatype for the selected security group.

- Not Allowed – Use this option to not allow access to the datatype for the selected security group.

The rest of this topic discusses setting security for secured datatypes. For more information on security, refer to [Assigning User Security](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-user-security).
To assign security to secured datatypes:

1. Open VA Data Security Access.

1. Enter the secured datatype in the
 Datatype
 field.

1. Enter the security group in the
 Group
 field or leave blank to filter by all groups.

1. Enter the company in the
 Company
 field or leave blank to filter by all companies. Press
 F4
 for a list of companies. If you do not see some company options in this list, you may not have been granted form security permissions to administer security for that company.

1. Click the
 Refresh
 button. All records matching the filter criteria display in the grid.

1. Select the
 Allow Access
 checkbox for each record that requires access to the datatype. Note: To select or deselect the
 Allow Access
 checkbox for all records in the grid, select the appropriate option in the Initialize Access section of the form and click the
 Initialize
 button. All records in the grid display the same setting.

1. Click the Apply button.
 The system applies access to all selected security group records in the grid.

1. Close the form or perform another search to assign security to additional records.

Maintaining Security for Orphaned Records
You can maintain data level security for orphaned records so that users have the ability to access any associated detail that may still exist in the system. For example, if data level security is set up for a contract, and then you purge the contract/job, you can maintain the security for that job in the VA Data Security Access form, so that associated details (e.g., invoices, payments, reports, etc.) are still accessible. To delete orphaned records, use VA Data Security Purge. For more information, refer to [VA Data Security Purge](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-purge-form).

Related information

- [Assign User Security](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/assign-user-security)

- [Set Data Level Security for Custom Fields](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/set-data-level-security-for-custom-fields)

- [View the Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log)

- [VA Data Security Access Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-data-security-access-form)

- [VA Data Security Setup Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form)

- [VA Security Groups Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form)

- [VA Data Security Purge Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-purge-form)
