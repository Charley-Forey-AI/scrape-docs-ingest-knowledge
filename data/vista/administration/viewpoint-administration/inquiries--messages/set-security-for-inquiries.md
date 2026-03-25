---
title: "Set Security for Inquiries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/inquiries--messages/set-security-for-inquiries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/inquiries--messages/set-security-for-inquiries"
---

# Set Security for Inquiries

Use the VA Inquiry Security form to set up security on queries and inquiries used by the Dashboard, PM, SM, and Accounting Work Centers.
Queries determine the type of information that displays on the Grid sections of a Work Center.
Assign security for all users before allowing them access to the system. It is recommended that you assign security to groups of users. Then, if desired, you can customize individual user settings. There are three access levels available for inquiry security access:

- Allowed – Use this option to grant access for the specified query.

- None – This option does not set any specific access to the query. It is most commonly used at the user level to defer security to the group level.

- Denied – Use this option to deny access to the query (available only when setting security for an individual user).

See [VA Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form) and [About the Interaction Between Group and User Level Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings) to learn more.
When setting inquiry security, you will set filtering criteria and then set security access by security groups or individual users.
To set security for queries:

1. Open the VA Inquiry Security form.

1. In the Company section, select to filter by either a Select Company or Across All Companies.

- If you selected Select Company, enter the company number in the text box, or press F4 to select from a list of companies. If you do not see a company in the list, you may not have been granted form security permissions to administer inquiry security for that company.

- If you do not have security permissions for all companies, the all-companies option displays as Across Companies I have permissions for. For more information, see [Company](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form/field-definitions-va-inquiry-security-form#ID-00049029--en).

1. In the Group/User section, select to filter by either Security Group or User.

- If you selected Security Group, enter a specific group in the text box, or leave it blank to filter by all groups.

- If you selected User, enter a specific user in the text box, or leave it blank to filter by all users.

1. Click the Refresh button. The system displays all records matching the filter criteria in the grid.

1. Set access levels:

- To set access levels for individual records: In the grid , use the drop-down in the Access column to set the access level for each query.

- To set the same access level for all records: Click Initialize Access Level. In the [Initialize Security Access](/en/vista/vista/administration/viewpoint-administration/work-centers/initialize-security-access-form) form, select an option in the [Access Level](/en/vista/vista/administration/viewpoint-administration/work-centers/initialize-security-access-form/field-definitions-initialize-security-access-form#ID-000490e9--en) section and click Apply. The Initialize Security Access form closes, and all records in the VA Inquiry Security grid display the same access level.

1. In the VA Inquiry Security form, click the Apply button. A message displays stating that the system updated query security successfully. Note: If you set query security for security groups, and then need to customize an individual user, repeat the above steps with filtering by that user and then changing the access level appropriately for individual queries.

Related information

- [About the VA Inquiry Security Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form)

- [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)

- [VA Security Groups Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form)

- [About the Dashboard Work Center](/en/vista/vista/system-tools/work-centers/about-the-dashboard-work-center)

- [About the Service Management Work Center](/en/vista/vista/system-tools/work-centers/about-the-service-management-work-center)

- [About the Project Management Work Center](/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center)
