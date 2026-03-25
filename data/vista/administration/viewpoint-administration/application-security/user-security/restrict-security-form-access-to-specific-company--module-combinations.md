---
title: "Restrict Security Form Access to Specific Company / Module Combinations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/user-security/restrict-security-form-access-to-specific-company--module-combinations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/user-security/restrict-security-form-access-to-specific-company--module-combinations"
---

# Restrict Security Form Access to Specific
 Company / Module Combinations

Security Administration is used to allow Security Administrators by Company/Module. The user will still require company access via VA Form Security.
A [Master Security Administrator](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/create-a-master-security-administrator) can restrict can restrict a Security Administrator’s access to administering only specific module/company combinations. When a Security Administrator’s security form access has been restricted, the user will see only the specified module/company combinations in the VA Form Security and VA Report Security grids.
For example, a Master Security Administrator could grant a Security Administrator access to only the Payroll module (PR) in Company 1, while granting access to only Accounts Payable (AP) in Company 2, and no access in any other companies. When that Security Administrator is using VA Form Security or VA Report Security, he or she will see only Companies 1 and 2 in the Companies box, and in the grids, will be able to administer only Payroll (PR) in Company 1 and only Accounts Payable (AP) in Company 2
To restrict a user's security form access to specific company/module combinations:

1. If this has not been done yet, use VA Form Security to grant the user access to VA Form Security and VA Report Security, either individually or as part of a security group. Restrict the user's access to specific companies and modules as needed.

1. Open the [VA Security Administration](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-administration-form) form. (If you cannot open this form, you are not a Master Security Administrator or the Security Administration in VA Site Settings has not been enabled; therefore you cannot proceed.)

1. In the Companies box, select the company (or companies) in which you want to restrict security administration permissions to only certain modules. Selecting Global will set permissions in all companies.

1. In the Users box, select the user (or users) for whom you want to restrict security form access.

- To find options in the selection box, type in the Search field to filter options in the selection box. Typing the first letter or number only will automatically check the first option starting with that letter or number. Search is case-sensitive.

- To filter by all, select the All checkbox. If you have first filtered the selection box by using the Search field, using All will select all of the filtered options, but will not select options not found by the search.

1. Click Refresh Grid to display the results in the grid.

1. If desired, change the grid display.

1. Changing the Grid DisplayTo change the display in the grid, check the Grouping checkbox. The grid then displays in a standard table format, which allows for filtering by specific values in each column.
You can then regroup the grid into a custom hierarchy by dragging column headers to the gray area along the top of the grid. Additionally, you can use a wildcard (*, %) to filter information in the grid.

1. In the Access column, select Full for each company/module combination to which you want to grant this user access. If you do not want to grant access to the user for a company/module combination, leave the Access column set to None.

1. Once you set the user's access level for all company/module combinations, click Apply.

Related information

- [Interaction Between Group and User Level Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings)

- [Create a Master Security Administrator](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/create-a-master-security-administrator)

- [VA Security Administration Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-administration-form)

- [User Permission Levels](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/user-permission-levels)

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)
