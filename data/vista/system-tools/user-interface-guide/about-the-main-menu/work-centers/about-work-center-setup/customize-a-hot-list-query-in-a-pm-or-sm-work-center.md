---
title: "Customize a Hot List Query in a PM or SM Work Center | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-work-center-setup/customize-a-hot-list-query-in-a-pm-or-sm-work-center"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-work-center-setup/customize-a-hot-list-query-in-a-pm-or-sm-work-center"
---

# Customize a Hot List Query in a PM or SM Work Center

You can customize Hot List queries for PM and SM Work Centers so
 they display the information you want.
Follow the steps below to customize a Hot List query for a PM or SM Work Center. Changes made to a Hot List query using this option only affect how the query
 displays on the selected Work Center for your user account. If you have multiple Work
 Centers, only the selected Work Center is affected by the changes.

1. Select the Work Center (PM or SM) containing the Hot List item to change.

1. From the Hot List menu folder
 (Items  >  Hot
 Lists), select the query you want to change (e.g. Overdue Work Orders) so that it
 displays in the grid section (center pane).

1. Click the Inquiry Settings icon
 () above the grid.The Inquiry Settings form displays.

1. Use the Inquiry tab to modify the maximum number of items that will display on the query grid.

1. Use the Parameters tab to
 customize which items will display in the list. A description of each parameter displays in the
 Description
  column, including the expected format of the parameter value. Examples:

- In the SM Work Center, if the Overdue Work Orders query should only include work
 orders due within 14 days from today's date, enter 14 in the
 Parameter Value field of
 the @DaysFromToday parameter.

- In the PM Work Center, if the Hot List should only include PCOs with a create date
 within the last two days, enter %D-2 in the @PCOCreationDateFilter field.

Note: When entering parameter values, make sure that you
 do not include the spaces, apostrophes, or <>'s that display in the format
 description. For more information, see [About Parameter Values](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-the-dashboard-work-center/about-parameter-values).

1. Click OK to save the
 changes.

 The Hot List is updated with your changes.For
 additional information about customizing queries, see [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form).

Related information

- [About Work Center Setup](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-work-center-setup)

- [About the Work Centers form](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-work-centers-form)

- [About Creating Queries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries)
