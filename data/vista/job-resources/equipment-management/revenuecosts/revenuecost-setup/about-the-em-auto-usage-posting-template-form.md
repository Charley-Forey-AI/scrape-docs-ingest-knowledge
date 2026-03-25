---
title: "About the EM Auto Usage Posting Template Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-auto-usage-posting-template-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-auto-usage-posting-template-form"
---

# About the EM Auto Usage Posting Template Form

Use this form to set up each of the auto usage templates that will be used to charge jobs automatically when posting usage in EM Automatic Usage.
Each template defines how the EM
 Usage Posting form will calculate and post usage for each category or
 piece of equipment assigned to the template. Jobs that will be
 automatically charged for usage based on time recorded in the EM Location
 Transfers or EM Mass Location Transfer v11 forms must be assigned the
 appropriate auto usage template in EM Job Templates.

- Usage Rules - The usage rules table determines what revenue
 rates will be used when posting equipment usage for any
 job referencing the template. During usage posting, the
 system totals the equipment's usage hours and then
 determines the revenue code to use based on which "more
 than hours, less than hours" range the usage hours fall
 in. If the rules table is using the Job to Date hour
 basis, the system will use the total hours on the job
 'to-date' (including the hours posted in the current
 billing period) to determine the revenue rate. If the
 hours basis is Billing Period, only the hours posted in
 the current billing period will be used.

- Billing Starts on Transfer Date - The
 Billing Starts on Trnsfr
 Date checkbox determines how the system will track the
 monthly billing limit (Max Bill Amt by Month) for a category or piece of
 equipment. When checked, the system starts the category or equipment
 billing cycle on the day the equipment is transferred to a job and bases
 the monthly billing limit on the transfer date (e.g. if you transfer a
 piece of equipment to a job on 06/15/09, the monthly limit for that
 equipment will apply from 06/15 to 07/14). If the Billing
 Starts on Trnsfr Date box is unchecked, the monthly
 billing limit will be based on the calendar month.Note: In order to use this feature, you must specify a
 value in the Max Bill by Month
 field. Additionally, this feature is intended for use with equipment
 that will remain on a job site for an extended period of time without
 multiple transfers on and off the job. When multiple transfers occur,
 the system has no way to determine what the actual 'beginning date'
 is.

- Use Est Out Date - If you have equipment that will be on a
 job for more than one billing cycle or an extended
 period of time, checking this box allows the system to
 use the equipment's 'transfer in' date and 'estimated
 out' date to determine the best revenue rate to use.
 For more information, see [About Use Est Out Date](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-use-est-out-date#concept-5657--en__concept-5657).

- Standard Hours/Break Times - The system uses the standard
 hours (sum of day start and stop times, less break
 times) to calculate the total number of hours a piece
 of equipment is on the job on a normal day. For more
 information, see [About Standard Hours/Break Times](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-standard-hoursbreak-times#concept-5253--en__concept-5253).

Related information

- [About the EM Auto Use Template Copy Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-auto-use-template-copy-form)
