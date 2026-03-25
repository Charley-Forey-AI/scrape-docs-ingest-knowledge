---
title: "Field Definitions: EM Automatic Usage Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-automatic-usage-form/field-definitions-em-automatic-usage-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-automatic-usage-form/field-definitions-em-automatic-usage-form"
---

# Field Definitions: EM Automatic Usage Form

The following is a list of field descriptions for the EM
 Automatic Usage form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Actual Date

 Required.
 Specify the date that will be the actual date in EM Revenue Detail (EMRD) for this batch of usage transactions. Typically, this will be the last day in the billing period. Initially defaults the current date.

##  Beginning/Ending Date

 Required.
 Enter the beginning and ending date for this billing period.

##  Beginning Template / Ending Template

 User these fields to create a range of
 templates to include in the usage posting. Press F4 to select a template from a list.
Leave these fields blank to include all usage templates.
Usage templates are created and maintained using the [EM Auto Usage Posting Template ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-auto-usage-posting-template-form) form.

##  Beginning/Ending Category

 Enter the beginning and ending category in a range of categories to include for usage posting or leave blank to include all categories. Press F4 for a list of valid equipment categories.

## Delete and Replace Duplicate Entries

Check this box to delete and replace duplicate entries when processing automatic usage. When running auto usage, the system:

- looks for an existing entry for the same batch month, batch, equipment, day, job, and revenue code, and if found, deletes the existing entry and inserts the new entry;

- looks to see if an auto usage batch has already been posted for the same day, and if so, looks for an existing entry for the same equipment, day, job, and revenue code. If a matching entry is found, it adds the entry to the batch and marks it for deletion. The new entry is inserted and processed as normal.

Leave this box unchecked if you do not want the system to delete and replace duplicate entries when running auto usage. If you run auto usage multiple times in a month, it may cause doubling of one or more entries. You will need to mark duplicate entries for deletion before posting the batch.

##  Beginning/Ending Location

 Enter the beginning and ending in a range of locations to exclude from processing in this batch. All pieces of equipment transferred to any location within this range (via EM Location Transfers or EM Mass Location Transfer v11) will be excluded from the billing process. Press F4 for a list of valid equipment locations.
Note: Use of this feature allows you to exclude non-billable
 time on a job for equipment while maintaining the ability to track the location of the
 equipment to the job.

## Dates to Exclude from Billing: Date 1-6

Enter up to six non-working days (such as holidays) to exclude from the billing process. Dates specified here must fall within the date range specified in Beginning/Ending Date fields.

##  Bill Saturdays

 Check this box to include Saturdays when billing equipment usage.
 Leave this box unchecked to exclude Saturdays when billing equipment usage.

##  Bill Sundays

 Check this box to include Sundays when billing equipment usage.
 Leave this box unchecked to exclude Sundays when billing equipment usage.
