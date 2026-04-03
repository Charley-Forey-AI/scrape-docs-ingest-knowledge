---
title: "Recurring Equipment Charge Processing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/recurring-equipment-charge-processing"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/recurring-equipment-charge-processing"
---

# Recurring Equipment Charge Processing

The Recurring Equipment Transaction Report / Update screen will allow entry of the last billing date, transaction date and batch code, which will be used for creating the Equipment Control transactions. When recurring billings are created, the billing rate is defined based on the number of days an item has been issued to a job.
If a job's status has been set to Closed and/or if a phase's status is set to Complete, an error message will occur on the recurring report and the information entered will not update to the Equipment Control system.
Once the report is previewed, the update automatically creates E/C transactions for all issued equipment. If there are any active attached equipment codes for the equipment specified for the selected requisitions, the software automatically generates the additional equipment transaction records (based on the stand-by hours for the primary equipment), and the rates are based on the attached equipment.
The Equipment screen stores the date and time of the latest recurring update for the equipment, along with the total billed-to-date. Based on how many days (or hours) since the last billing for the equipment, the system determines which billing rate (hourly, daily, weekly or monthly) using the rate schedule in the Equipment Tracking Installation screen. If, however, the requisition has an expected billing period entered, and this billing period is greater than system determined billing period, then the requisition billing period is used. For example, if there have been five working days since the last recurring update for an equipment, and the rate schedule is set up to bill a weekly rate for this, but the expected billing period was set up as monthly, then the monthly rate is used.
