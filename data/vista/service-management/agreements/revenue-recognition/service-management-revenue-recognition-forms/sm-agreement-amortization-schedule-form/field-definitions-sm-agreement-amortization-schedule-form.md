---
title: "Field Definitions: SM Agreement Amortization Schedule Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-agreement-amortization-schedule-form/field-definitions-sm-agreement-amortization-schedule-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-agreement-amortization-schedule-form/field-definitions-sm-agreement-amortization-schedule-form"
---

# Field Definitions: SM Agreement Amortization Schedule Form

The following is a list of field descriptions for the SM
 Agreement Amortization form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Deferral

Enter N, New, or + to create a new deferral. The system
 will automatically assign the next sequential number available for this agreement.

## Amount

Enter the deferral amount. The amount specified here must be less than or equal to the Total Remaining amount for the agreement (indicated above the tab pages).
When running the amortization process (using SM Agreement Amortize Revenue), the system will move this amount from the Deferred Rev account to the Revenue account (both defined for agreements in SM Departments) for specified date.
Note: The system will determine the actual amount to recognize based on the amount that is available to recognize (i.e. billed amount) and the date/month in which you run the amortization process. For example, if you have a monthly amortization schedule and you skip the amortization process for one or more months, the system will amortize unrecognized amounts for all months prior to and including the specified date/month. The total amount will be posted to the post month specified during amortization. See [SM Agreement Amortize Revenue](/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-revenue-recognition-form) for more information.

## Deferral

Enter the deferral date. When running the amortization process, the system will use this date in conjunction with the "through date" specified in SM Agreement Amortize Revenue to determine if the specified amount should be recognized.
 For example, if you enter 12/15/13 here and run SM Agreement Amortize Revenue on 12/31/13, the system will include this amount in the amortization process. However, if you run SM Agreement Amortize Revenue on 11/31/13, the system will not include this amount in the amortization process.
