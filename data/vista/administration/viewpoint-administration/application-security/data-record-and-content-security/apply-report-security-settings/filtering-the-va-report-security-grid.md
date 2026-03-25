---
title: "Filtering the VA Report Security Grid | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-report-security-settings/filtering-the-va-report-security-grid"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-report-security-settings/filtering-the-va-report-security-grid"
---

# Filtering the VA Report Security Grid

When assigning report security in VA Report Security, you first filter for specific
 groups/users or reports, and then set access levels.
The following
 instructions detail how to filter the report security grid in VA Report Security. For more
 information , see the F1 Help in each field.

1. Select the company (or
 companies) to filter by from the
 Companies
 list. To set security for all companies, select
 Global
 .

-  If you do not see a company in
 this list, you have not been granted form security permissions to administer
 report security for that company.

- If the
 Global
 option is not available, then you have not been granted form
 security permissions to administer report security for all companies.
Note:

- When setting up security
 on SSRS reports, always use the
 Global
 option.

- Users who need to run
 cross-company reports should be given access to the report(s) in all
 applicable companies.

1. Select the module (or
 modules) to filter by from the Modules list. To filter by all
 modules, select All.

1. In the Select By
 field, select whether to filter by Group #Group
 Name, User, or Report.
 The selection box to the right displays all available groups, users, or reports
 (depending on the filter selection).

1. Select the Group(s),
 User(s), or Reports(s) to filter by in the selection box.

- To find options in the selection
 box, type in the
 Search
 field to filter options in the selection box.

-  To find options by first letter
 or number, type that character to automatically check the first option starting
 with that letter or number in the selection box. If you type the character
 again, the system will check the next option with the same first character.

- To filter by all, select the

 All
 checkbox. If you have first filtered the selection box by using
 the
 Search
 field, using
 All
 will select all of the filtered options, but will not select
 options not found by the search.

1. Click the
 Refresh
 Grid
 button to display the results in the grid.The system groups the filter results
 in the grid differently depending on the filter selection in the
 Select
 By
 field.

- If you filter by Report, the
 system groups the results hierarchically by Company, Module, Report, and
 Groups/Users.

- If you filter by Group # or Group
 Name, the system groups the results by Company Module, Group, and Report.

-  If you filter by User, the system
 groups the results by Company, Module, User, and Report.

- If [VA Security Administration](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-administration-form) is turned on, you
 may see only some company/module combinations in the grid, regardless of the
 modules selected in Step 2.

1. If desired, check the

 Grouping
 checkbox to enable you to change the grid display. For more
 information, see [Changing the Grid Display](#ID-0004952c--en__ID-0004956c).

1. If desired, click the

 Refresh
 Grid
 button again to clear the grid. 

Now you can apply report security for the records
 in the grid. For more information, see [Applying
 Report Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-report-security-settings).[About Changing the Grid Display](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-report-security-settings/about-changing-the-grid-display#concept-4198--en__concept-4198)

Related information

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)

- [Apply Report Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-report-security-settings)

- [User Permission Levels](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/user-permission-levels)

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

- [Interaction Between Group and User Level Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings)
