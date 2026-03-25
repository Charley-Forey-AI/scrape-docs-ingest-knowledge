---
title: "About Tracking Hours | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/equipment-meters/about-tracking-hours"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/equipment-meters/about-tracking-hours"
---

# About Tracking Hours

In addition to tracking mileage, you have the option to track usage hours for each piece of equipment.
This information can be used in conjunction with the scheduled maintenance feature of EM to determine when a piece of equipment is due for maintenance. It can also be used to provide statistical information about your equipment, such as the year-to-date usage hours that can be included on reports.
Hours can be tracked automatically (during posting) or using the EM Meter Readings program, both of which will update the equipment’s hour meter in EM Equipment. When tracking hours automatically, updates will depend on the update option you specify for each posting type (e.g. equipment usage posting, cost adjustments and parts posting, and fuel usage posting) in EM Company Parameters. You can specify to only update meters (which includes the hour meter) when the transaction date is greater than last reading date, or to always update meters regardless of the transaction date.
For equipment usage posting, regardless of which update option you select, hour meters will only be updated if the Update Hours option is set to Y (checked) for the posted revenue code. This is done by revenue code (in EM Revenue Codes), with overrides by category (EM Revenue Rates by Category) or by equipment (EM Revenue Rates by Equipment).  Then, during posting, you can enter the new hour meter value, or enter the time units and have the system automatically calculate the hours by multiplying the number of time units by the Hours/Time Unit (as defined in EM Revenue Codes).
