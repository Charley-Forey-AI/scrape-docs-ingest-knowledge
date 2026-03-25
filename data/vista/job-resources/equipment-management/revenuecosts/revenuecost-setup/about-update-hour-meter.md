---
title: "About Update Hour Meter | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-update-hour-meter"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-update-hour-meter"
---

# About Update Hour Meter

This option can only be used with hour-based revenue codes,
 and indicates whether the system will automatically update equipment hour meters whenever
 usage is posted.
If checked, the system will calculate the
 number of hours based on the number of units entered during usage posting. For example,
 if you post 2 units to a weekly revenue code that has 40 hours specified as its
 Hours/Time Unit, the system will calculate this as 80 hours. The 80 hours are then
 updated to the equipment’s Hour Meter in EM Equipment.
This option applies to all equipment within
 the specified category. If you wish to override this flag for a specific piece of
 equipment, you can do so using the EM Revenue Rates by Equipment form.
Note: When posting usage, the system will check only the
 category and equipment overrides to determine whether to update the equipment’s hour
 meter. The ‘update hour meter’ flag set at the revenue code level (in EM Revenue Codes)
 is never considered, as it is used as a default only.
Updates to hour meters are also controlled
 by the Meter Update options for Equipment Usage in EM Company Parameters. For more
 information, see [Meter Updates: Equipment Usage](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8af--en), [Meter Updates: Costs Adj and Parts Posting](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8c0--en), and [Meter Updates: Fuel Posting](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8ce--en).
