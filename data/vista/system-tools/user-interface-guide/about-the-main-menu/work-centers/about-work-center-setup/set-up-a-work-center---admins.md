---
title: "Set Up a Work Center - Admins | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-work-center-setup/set-up-a-work-center---admins"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-work-center-setup/set-up-a-work-center---admins"
---

# Set Up a Work Center - Admins

Administrators must set up Work Centers before users can access and use them.
Administrators must have permissions to access the VA Viewpoint Administration module.
To set up a Work Center:

1. In the VA Site Settings form

1. select the Activate Work Centers checkbox. This gives all users access to the Work Centers form (Options > Work Centers), which allows users to maintain their own Work Centers.

1. in the Number of Tabs field, enter the maximum number of Work Centers that each user can have on their main application window, up to 6.

1. In the VA Work Center Security form, define which templates users can access. For example, if a user needs a PM Work Center, you must give them access to the "PM" template.

1. In the VA Inquiry Security form, set up query security. Users should have access only to queries necessary for their daily activities. For more information, see [Set Security for Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/set-security-for-inquiries).Queries determine what data will display in the grid section of a Work Center. For example a user can add the Hot List query to a Dashboard Work Center grid section if they want to see a list of PM module documents that might require action.
The standard PM, SM, and Accounting Work Centers include several queries that you can launch from the menu. For example the standard PM Work Center includes the Hot List, Projects, Contracts, and several other queries.

- If a user has Allowed or None access to a query, it is displayed in the menu and can be used.

- If a user has Denied access to a query, it is not displayed in the menu.

- Users can only add a query to a Work Center if they have Allowed access to it.

1. Optional: Create Query/Work Center AssociationsBefore you can add a query or inquiry to a Work Center, the query/inquiry has to be associated with that Work Center using the Associations tab on the [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form) form. The standard PM, SM, and Accounting Work Center have several queries that are launched from the menu and these queries are already associated to the applicable Work Center. However, you must perform this step if you plan to add queries/inquiries to a Dashboard Work Center or if you are adding custom queries/inquiries to any work center.

- Accounting Work Center - Add the Accounting template to the Associations tab of each query that users should be able to access from an Accounting Work Center. For example, if you want to add an AR Invoices inquiry to the Accounts Receivable work center menu, open that query in VA Inquiries, add the Accounting template to the Associations tab, and select the Active checkbox.

- Dashboard Work Center - Verify that the queries that users will access from the Dashboard Work Center are associated with the correct templates using the Associations tab and that the Active box is checked. For example, if users should be able to add the inquiry to a Dashboard Work Center using the grid template, add the Grid template to the Associations tab and select the Active checkbox.

- Project Management Work Center - Add the PM template to the Associations tab of each query that users should be able to access from a PM Work Center. For example if you created a modified version of the PM Hot List query, open that query in VA Inquiries, add the PM template to the Associations tab, and verify that the Active checkbox is selected.

- Service Management Work Center - Add the SM template to the Associations tab of each query that users should be able to access from an SM Work Center. For example, if you created a modified version of the SM Hot List query (Overdue Work Orders), open that query in VA Inquiries, add the SM template to the Associations tab, and verify that the Active checkbox is selected.

1. Dashboard Work Centers Only: Set up report security using [VA Report Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form). Only reports that users can access will be available in the Report Configuration form associated with the report sections on Dashboard Work Centers. Note: My Viewpoint reports are associated with the Report module and with the “My VP” report type. When filtering for My Viewpoint reports in VA Report Security, filter by the RP module. After refreshing the grid, filter by the “My VP” report type. For more information on VA Report Security, see [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form).

1. Optional: Create a Work Center profile, or use the save and load feature. For more information, see [About Work Center Profiles](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-work-center-setup/about-work-center-profiles).
