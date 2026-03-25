---
title: "Set the Maximum Number of Records for Lookups | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-the-maximum-number-of-records-for-lookups"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/set-the-maximum-number-of-records-for-lookups"
---

# Set the Maximum Number of Records for Lookups

You can set the maximum number of records that return to a lookup when users press F4.
Entering a value here is useful when lookups are associated with tables containing hundreds or thousands of records, which can affect the load/refresh speed.
The specified maximum is a system-wide setting that affects all lookups. Typically, you do not want to be too restrictive with lookups that normally return a smaller record set. Consider setting a threshold that restricts larger lookups, but does not affect smaller ones. If the number of records exceeds the designated maximum, a message displays indicating that there are additional records.
To set the maximum number of records:

1. Open VA Site Settings.

1. in the Max Number of
 Rows section, enter a number in the Lookups field. If the number of records exceeds
 the designated maximum, a message displays indicating that there are
 additional records. If the record you are looking for is not in the current
 record set, enter selection criteria and click Refresh to re-query the
 database. You can include wildcards (*, %) or comparison operators (<,
 >, <>, =, >=, <=) to refine the search as necessary (for
 example, >6000, *6000, etc.). Clicking Refresh returns a record set based
 on the entered criteria. For more information on wildcards and comparison
 operators, refer to F4 (The Lookup Window) in Related Topics below.
Note: You can override the system-wide setting
 for individual users using the User Options form or the VA User Profile
 form.

Related information

- [About the User Options Form](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [Increase Form Record Load Speed](/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records/increase-form-record-load-speed)

- [Lookups](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049cde--en)
