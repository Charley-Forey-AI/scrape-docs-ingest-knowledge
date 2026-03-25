---
title: "Field Definitions: SM Amortization Schedule Mod Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-amortization-schedule-mod-form/field-definitions-sm-amortization-schedule-mod-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-amortization-schedule-mod-form/field-definitions-sm-amortization-schedule-mod-form"
---

# Field Definitions: SM Amortization Schedule Mod Form

The following is a list of field descriptions for the SM
 Amortization Schedule Mod form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Amount

Amount field on the field on the SM Amortization Schedule Mod form.
Enter the deferral amount. The amount specified here must be less than or equal to the Total Remaining amount for the agreement (indicated above the tab pages).
When running the amortization process (using SM Agreement Amortize Revenue), the system will move this amount from the Deferred Rev account to the Revenue account (both defined for agreements in SM Departments) for specified date.

## Date

Date field on the field on the SM Amortization Schedule Mod form.
Enter the deferral date. When running the amortization process, the system will use this date in conjunction with the "through date" specified in SM Agreement Amortize Revenue to determine if the specified amount should be recognized.
For example, if you enter 12/15/19 here and run SM Agreement Amortize Revenue on 12/31/19, the system will include this amount in the amortization process. However, if you run SM Agreement Amortize Revenue on 11/31/19, the system will not include this amount in the amortization process.

## Notes

Notes field on the field on the SM Amortization Schedule Mod form.
Enter any miscellaneous notes about this item.
