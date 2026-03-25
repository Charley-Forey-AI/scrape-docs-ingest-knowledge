---
title: "Field Definitions: EM Auto Usage Posting Template Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-auto-usage-posting-template-form/field-definitions-em-auto-usage-posting-template-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-auto-usage-posting-template-form/field-definitions-em-auto-usage-posting-template-form"
---

# Field Definitions: EM Auto Usage Posting Template Form

The following is a list of field descriptions for the EM Auto
 Usage Posting Template form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Usage Template

 Enter a code, up to 10 characters, that uniquely identifies this auto usage template.

##  Description

 Enter a description of this auto usage template, up to 30 characters.

##  Category

 Enter the category (from EM Categories) for which you are setting up automatic billing information. All information set up for this category will apply to all equipment within this category.
 If you want to set up automatic billing information for individual pieces of equipment, use the Equipment tab on this form.

##  Category: JC Phase

 Specify the
 phase to use for automatic usage posting to equipment in this category. Must be a valid
 phase based on the ‘Number of Valid Characters in Phase Code’ specified in JC Company
 Parameters. When processing in EM Automatic Usage, the system will validate this phase
 against JC Job Phases or JC Phases.

##  Category: Rules Table

 Specify the rules table (from EM Usage Rules Table) to use for automatic usage posting to equipment in this category. When processing in EM Automatic Usage, the system will use this rules table to determine the revenue codes to use based on the length of time equipment in the specified category is on the job.

##  Category: Min Amt by Bill Period

 Enter the minimum dollar amount per billing period to charge to the job for equipment within this category when posting usage in EM Automatic Usage. Leave blank if there is no minimum required.

## Category: Max Amt by Bill Period

Enter the maximum dollar amount per billing period that can be charged to the job for equipment within this category when posting usage in EM Automatic Usage. Leave blank if there is no maximum required.
If this limit is exceeded during usage posting, the usage amount will reflect the change, but the revenue rate will not be adjusted.

## Category: Billing Starts on Trnsfr Date

This checkbox determines how the system will
 track the monthly billing limit (Max Bill by Month field) for equipment in
 this category.
Check this box to start the billing cycle and monthly billing limit for equipment in this category on the day the equipment is transferred to a job (i.e. "transfer in" date).
For example, if you transfer a piece of equipment to a job on 06/15/09, the bill cycle for the equipment will begin on 06/15/09; the monthly billing limit will be in effect from 06/15/09 through 07/14/09. If the equipment remains on the job site for an extended period of time, the monthly billing limit will continue to apply from the 15th of the month through the 14th of the following month.
Note: In order for this feature to function properly, you
 must specify an amount in the Max Bill by Month field.
Leave this box unchecked to use the standard billing cycle for equipment in this category; monthly billing limit will be based on the calendar month.

## Category: Use Est Out Date

Check this box to use the transfer Est Out Date when determining revenue rates for equipment in this category. During automatic usage posting, the system totals the estimated billable hours for the equipment based on the equipment's 'transfer in' and 'estimated out' dates. It then determines the best revenue rate to use based on where the 'billable hours' fall in the "more than, less than" hours ranges of the rules table.
Note: If the billable hours do not fall in any of the hours ranges, the system uses the last sequence/revenue code.
For example, if you transfer a piece of equipment to the job on 06/01/09 and specify an estimated out date of 12/31/09, the total estimated billable hours will exceed one month; therefore, the system will use the monthly rate from the rules table. If the equipment remains on the job for the entire period, the system will continue billing at the monthly rate. However, if you transfer the equipment to other job sites within the original timeframe, the system will use the actual hours to determine the rate to use for the time on each job.
Leave this box unchecked if not using the transfer Est Out Date to determine revenue rates for equipment in this category. Instead, the equipment's "transfer out" date will be used to determine the revenue rate. If the "transfer out" date is null, revenue rate will be pulled from last sequence/revenue code in the usage rules table.

## Category: Max Bill Amt by Month

Required if Billing Starts on Trnsfr
 Date box is checked.
Enter the maximum dollar amount per calendar month that can be charged to the job for equipment within this category when posting usage in EM Automatic Usage. Leave blank if there is no maximum required.
If you checked the Billing Starts on Trnsfr
 Date box for this category, it is suggested that this amount be equal to the
 monthly rate for equipment in this category. The system will apply this limit based on the
 equipment's "transfer in" date rather than the calendar month. For example, if the
 equipment's "transfer in" date is 06/15/09, the amount specified here will be in effect
 from 06/15/09 through 07/14/09.
If this limit is exceeded during usage posting, the usage amount will reflect the change, but the revenue rate will not be adjusted (causing the amount to no longer accurately reflect the time units x revenue rate).
 For example, you have a monthly limit of $8000 and have already reached $6000 of this limit. You now post usage for 80 time units at a rate of 35.00. The calculated amount of $2800 (80.000 x 35.00) puts you over the $8000 limit, so the amount is adjusted to $2000 (8000 - 6000 = 2000); the revenue rate remains at 35.00, so the amount ($2000) no longer equals the time units x revenue rate.

## Category: Max Bill Amt by Job

Enter the maximum dollar amount that can be charged to the job (over the length of the job) for equipment within this category when posting usage in EM Automatic Usage. Leave blank if no maximum required.
If this limit is exceeded during usage posting, the usage amount will reflect the change, but the revenue rate will not be adjusted.

## Category: Hrs/Day

Enter the standard number of hours in the workday for jobs being charged in EM Automatic Usage using this template.
Note: When defining the ‘hours per day’, make sure to exclude break times. For example, if your workday begins at 08:00 and ends at 17:00 (9 hours), and you normally break for lunch from 12:00 – 1:00 (1 hour), the standard number of hours per day would be 8 (9–1=8).

## Category: Day Start

Enter the normal workday start time for this template/category, in 24-hour format.
Note: Workday hours cannot span multiple days; therefore, the start time must be less than the stop time. If your workday spans a 24-hour period, both start and stop times must be entered as 00:00 (i.e. midnight to midnight).

## Category: Day Stop

Enter the normal workday stop time for this template/category, in 24-hour format.
Note: Workday hours cannot span multiple days; therefore, the stop time must be greater than the start time. If your workday spans a 24-hour period, both start and stop times must be entered as 00:00 (i.e. midnight to midnight).

##  Category: Br1/2/3 Start

 Enter the start time for up to three breaks, in 24-hour format, for this template/category.

##  Category: Br1/2/3 Stop

 Enter the stop time for up to three breaks, in 24-hour format, for this template/category.

##  Equipment

 Enter the equipment (from EM Equipment) for which you are setting up automatic billing information.
 If you want to set up automatic billing information for a category of equipment, use the Category tab on this form.

##  Equipment: JC Phase

 Specify the phase to use for automatic usage
 posting to this equipment. Must be a valid phase based on the ‘Number of Valid Characters
 in Phase Code’ specified in JC Company Parameters. When processing in EM Automatic Usage,
 the system will validate this phase against JC Job Phases or JC Phases.

##  Equipment: Rules Table

 Specify the rules table (from EM Usage Rules Table) to use for automatic usage posting to this equipment. When processing in EM Automatic Usage, the system will use this rules table to determine the revenue codes to use based on the length of time this equipment is on the job.

##  Equipment: Min Amt by Bill Period

 Enter the minimum dollar amount per billing period to charge to the job for this piece of equipment when posting usage in EM Automatic Usage. Leave blank if there is no minimum required.

## Equipment: Max Amt by Bill Period

Enter the maximum dollar amount per billing period that can be charged to the job for this piece of equipment when posting usage in EM Automatic Usage. Leave blank if there is no maximum required.
Ifthis limit is exceeded during usage posting, the usage amount will reflect the change, but the revenue rate will not be adjusted.

## Equipment: Billing Starts on Trnsfr Date

This checkbox determines how the system will
 track the monthly billing limit (Max Bill by Month field) for this piece
 of equipment.
Check this box to start the billing cycle and monthly billing limit for this equipment on the day the equipment is transferred to a job (i.e. "transfer in" date).
For example, if you transfer this equipment to a job on 06/15/09, the bill cycle for the equipment will begin on 06/15/09; the monthly billing limit will be in effect from 06/15/09 through 07/14/09. If the equipment remains on the job site for an extended period of time, the monthly billing limit will continue to apply from the 15th of the month through the 14th of the following month.
Note: In order for this feature to function properly, you
 must specify an amount in the Max Bill by Month field.
Leave this box unchecked to use the standard billing cycle for this equipment; monthly billing limit will be based on the calendar month.

## Equipment: Use Est Out Date

Check this box to use the transfer Est Out Date when determining revenue rates for this equipment. During automatic usage posting, the system totals the estimated billable hours for the equipment based on the equipment's 'transfer in' and 'estimated out' dates. It then determines the best revenue rate to use based on where the 'billable hours' fall in the "more than, less than" hours ranges of the rules table.
Note: If the billable hours do not fall in any of the hours ranges, the system uses the last sequence/revenue code.
For example, if you transfer this equipment to a job on 06/01/09 and specify an estimated out date of 12/31/09, the total estimated billable hours will exceed one month; therefore, the system will use the monthly rate from the rules table. If the equipment remains on the job for the entire period, the system will continue billing at the monthly rate. However, if you transfer the equipment to other job sites within the original timeframe, the system will use the actual hours to determine the rate to use for the time on each job.
Leave this box unchecked if not using the transfer Est Out Date to determine revenue rates for this equipment. Instead, the equipment's "transfer out" date will be used to determine the revenue rate. If the "transfer out" date is null, revenue rate will be pulled from last sequence/revenue code in the usage rules table.

## Equipment: Max Bill Amt by Month

Required if Billing Starts on Trnsfr
 Date box is checked.
Enter the maximum dollar amount per calendar month that can be charged to the job for this piece of equipment when posting usage in EM Automatic Usage. Leave blank if there is no maximum required.
If you checked the Billing Starts on Trnsfr
 Date box for this equipment, it is suggested that this amount be equal to
 the monthly rate for the equipment. The system will apply this limit based on the
 equipment's "transfer in" date rather than the calendar month. For example, if the
 equipment's "transfer in" date is 06/15/09, the amount specified here will be in effect
 from 06/15/09 through 07/14/09.
Warning: If this limit is exceeded during usage posting, the usage amount will reflect the change, but the revenue rate will not be adjusted (causing the amount to no longer accurately reflect the time units x revenue rate).
 For example, you have a monthly limit of $8000 and have already reached $6000 of this limit. You now post usage for 80 time units at a rate of 35.00. The calculated amount of $2800 (80.000 x 35.00) puts you over the $8000 limit, so the amount is adjusted to $2000 (8000 - 6000 = 2000); the revenue rate remains at 35.00, so the amount ($2000) no longer equals the time units x revenue rate.

## Equipment: Max Bill Amt by Job

Enter the maximum dollar amount that can be charged to the job (over the length of the job) for this piece of equipment when posting usage in EM Automatic Usage. Leave blank if no maximum required.
Ifthis limit is exceeded during usage posting, the usage amount will reflect the change, but the revenue rate will not be adjusted.

## Equipment: Hrs/Day

Enter the standard number of hours in the workday for jobs being charged in EM Automatic Usage using this template.
Note: When defining the ‘hours per day’, make sure to exclude break times. For example, if your workday begins at 08:00 and ends at 17:00 (9 hours), and you normally break for lunch from 12:00 – 1:00 (1 hour), the standard number of hours per day would be 8 (9–1=8).

## Equipment: Day Start

Enter the normal workday start time for this template/equipment, in 24-hour format.
Note: Workday hours cannot span multiple days; therefore, the start time must be less than the stop time. If your workday spans a 24-hour period, both start and stop times must be entered as 00:00 (i.e. midnight to midnight).

## Equipment: Day Stop

Enter the normal workday stop time for this template/equipment, in 24-hour format.
Note: Workday hours cannot span multiple days; therefore, the stop time must be greater than the start time. If your workday spans a 24-hour period, both start and stop times must be entered as 00:00 (i.e. midnight to midnight).

##  Equipment: Br 1/2/3 Start

 Enter the start time for up to three breaks, in 24-hour format, for this template/category.

##  Equipment: Br1/2/3 Stop

 Enter the stop time for up to three breaks, in 24-hour format, for this template/category.
