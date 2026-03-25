---
title: "Setting Security on Work Centers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/work-centers/setting-security-on-work-centers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/work-centers/setting-security-on-work-centers"
---

# Setting Security on Work Centers

Set security for work center templates.
Use the VA Work Center Security form to set security on work centers. This determines which users and/or security groups can create Dashboard, PM, SM, and Accounting Work Centers
Assign security for all users before allowing them access to the system. It is recommended that you assign security to groups of users. Then, if desired, you can customize individual user settings. There are three access levels available for inquiry security access:

- Allowed – Use this option to allow the specified security group or user access to the selected template(s).

- None – This option does not set any specific access to the selected template(s). It is most commonly used at the user level to defer security to the group level.

- Denied – Use this option to deny access to the selected template(s) for specific users.

See [VA Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form) and [About the Interaction Between Group and User Level Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings) to learn more.
When using VA Work Center Security to set security, set filtering criteria first and then set security access by security groups or individual users.
To set security for Work Center templates:

1. Open VA Work Center Security.

1. In the Company section, select to filter by either a Select Company or Across All Companies.

- If you selected Select Company, enter the company number in the text box, or press F4 to select from a list of companies. If you do not see a company in this list, you may not have been granted form security permissions to administer work center security for that company.

- If you do not have security permissions for all companies, the all-companies option displays as Across Companies I have permissions for. For more information, see [Company](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-security-form/field-definitions-va-work-center-security-form#ID-0004a3a3--en).

1. In the Group/User section, select to filter by either Security Group or User.

- If you selected Security Group, enter a specific group in the text box, or leave it blank to filter by all groups.

- Note: Only Security Groups that have a Group Type of 2-Reports (set in [VA Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form)) can be assigned Work Center Security.

- If you selected User, enter a specific user in the text box, or leave it blank to filter by all users.

1. Click the Refresh button once the Company and Group/User sections are complete. The system will display all records that match the filter criteria in the grid.

1. Set access levels:

- To set access levels for individual records: In the grid , use the drop-down in the Access column to set the access level for each query.

- To set the same access level for all records: Click Initialize Access Level. In the Initialize Security Access form, select an option in the Access Level section and click Apply. The Initialize Security Access form closes, and all records in the VA Inquiry Security grid display the same access level.

- Note: The PM template determines access to PM work centers and the
 SM template determines access to SM work centers. All other templates
 determine access to dashboard work centers.

1. In the VA Work Center
 Security form, click the Apply button. A message
 displays stating that the system updated work center security successfully.


1. Repeat these steps to set security for additional users or security groups. Note: If you set template security for security groups, and then need to customize an individual user, repeat the above steps with filtering by that user in Step 2, and then changing the access level appropriately for individual templates.

Related information

- [About Work Center Setup](/en/vista/vista/system-tools/work-centers/about-work-center-setup)

- [About the Dashboard Work Center](/en/vista/vista/system-tools/work-centers/about-the-dashboard-work-center)

- [About the Service Management Work Center](/en/vista/vista/system-tools/work-centers/about-the-service-management-work-center)

- [About the Project Management Work Center](/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center)

- [VA Security Groups Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form)

- [About the User Options Form](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form)
