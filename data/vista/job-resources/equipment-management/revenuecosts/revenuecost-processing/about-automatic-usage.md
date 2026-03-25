---
title: "About Automatic Usage | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-automatic-usage"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-automatic-usage"
---

# About Automatic Usage

Equipment Management's automatic usage feature allows you to automatically process equipment usage.
The system creates automatic usage entries based on the following information:

- The number of hours that the piece of equipment was on the job during the billing period (determined by transfers posted in EM Location Transfers or EM Mass Location Transfer v11.Note: If the Use Est Out Date box is checked for a category or equipment on the usage template, the estimated billable hours for the equipment will be based on the equipment's 'transfer in' and 'estimated out' dates.

- The auto usage template (set up in EM Auto Usage Posting Template) assigned to the job in EM Job Templates. The template determines which job phase to charge, the minimum and maximum charges per billing period, whether billing is based on calendar month or starts on 'transfer in' date, whether you are using the equipment's 'estimated out' date to determine billable hours, the number of hours per day, and which Rules table to use.If the calculated amount exceeds the maximum limit specified on the usage template, the usage amount will reflect the change, but the revenue rate will not be adjusted.
For example, say the Maximum Limit = $1000, the Revenue Rate = $150, and the Time Units = 10
If the calculated amount is $1500, automatic usage will stop at $1000 (limit); however, because the revenue rate is not adjusted, the result will look like this: $150 * 10 = $1000

- The Rules table (defined in EM Usage Rules Table) assigned to the usage template in EM Auto Usage Posting Template, which determines the revenue code to use. The Hour Basis specified for the Rules table determines whether the billing rates will based on the total number of hours the equipment has been on the job (Job To Date option), or on the total number of hours the equipment has been on the job during the billing period (Billing Period option).

- The Hours/Time Unit field in EM Revenue Codes, which is used to convert between hours and the time unit of each revenue code. Note: For revenue codes with the Monthly Revenue Code box checked, the Hours/Time field is ignored and the system will set the total time units to 1.00, regardless of how many hours are in the month. Typically, this will only apply to revenue codes assigned to thresholds (in the Rules table) designated for monthly billing.

- Either the billing rates specified on the template (if job assigned a revenue template in EM Job Templates) or the standard revenue rates set up in EM Revenue Rates by Equipment.

Using this program creates revenue transactions just as if you had entered them in EM Usage Posting. Once you have processed an auto-usage posting batch, you can edit the transactions in EM Usage Posting before you post the batch.
