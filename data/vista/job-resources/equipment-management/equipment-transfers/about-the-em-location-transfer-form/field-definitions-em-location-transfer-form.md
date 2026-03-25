---
title: "Field Definitions: EM Location Transfer Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form/field-definitions-em-location-transfer-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form/field-definitions-em-location-transfer-form"
---

# Field Definitions: EM Location Transfer Form

The following is a list of field descriptions for the EM
 Location Transfer form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Equipment

Equipment field on the EM Location Transfer form, Info tab
 Required.
By default, the field displays the last piece of equipment transferred.
Enter the piece of equipment to transfer or
 press F4 to select from a list of equipment.
Note: If you specify an attachment as the equipment to transfer, the system will detach the attachment from its primary equipment with the transfer. If you do not want to detach the attachment, cancel the transaction. To keep the equipment/attachment relationship intact, you must transfer the primary equipment. The system will automatically transfer the attachment with the primary equipment.

Related information

- [About the EM Location Transfer Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)

## Sequence

Sequence field on the EM Location Transfer form, Info tab
Required.
By default, this field displays the sequence number for the last equipment transfer.
Enter the sequence number of an existing entry
 or enter N, New, or + to add a new sequence. The system
 automatically assigns the next available sequence number.

Related information

- [About the EM Location Transfer Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)

##  JC Co

JC Company field on the EM Location Transfer form, Info tab
 Required if transferring equipment to a job.
 Enter the JC company you are transferring the
 specified equipment to or press F4 to select from a list of JC companies.

Related information

- [About the EM Location Transfer Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)

- [JC Company Parameters Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)

## Job

Job field on the EM Location Transfer form
Enter the job the equipment will be
 transferred or press F4 to select from a list of JC jobs. If
 you enter a soft- or hard-closed job, the status displays (in red) adjacent to the job
 value.
Note: Entry in this field requires entry of a JC company.

Related information

- [About the EM Location Transfer Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)

- [JC Jobs Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)

##  Location

Location field on the EM Location Transfer form
 Enter the location you are transferring the
 specified equipment to or press F4 to select from a list of EM locations.
 The location must be an active location (i.e. the Active checkbox is selected for the
 location in [EM
 Locations ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-locations-form)).

Related information

- [About the EM Location Transfer Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)

- [About the EM Locations Form](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-locations-form)

- [Active](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-locations-form/field-definitions-em-locations-form#ID-0000c62b--en)

## Date

Date field on the EM Location Transfer form, Info tab
Required.
Enter the date that you transferred this equipment to the new job/location or select the transfer date from the calendar.
Note: When you save a transfer record, the system verifies
 that there is no more than one transfer for the specified equipment on that date that does
 not have a transfer time. This means that if you want to transfer a piece of equipment more
 than once in the same day, only one of the transfers can be missing a Time.

## Time

Time field on the EM Location Transfer form, Info tab
Enter the time when the equipment was transferred to the new location, using 24-hour format (00:00 - 23:59).
When you save a transfer record, the system
 verifies that there is no more than one transfer for the specified equipment on that date
 that does not have a transfer time. This means that if you want to transfer a piece of
 equipment more than once in the same day, only one of the transfers can be missing a
 Time.
Important: If you use the [EM
 Automatic Usage ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-automatic-usage-form) form, you should specify the time for each equipment transfer.
 The automatic usage process uses the date and time of each transfer when billing for usage.
 For example, if a piece of equipment is transferred to Job A on 4/12/2019 at 10:00 and to
 Job B on 4/22/2019 at 9:00, the system will calculate usage on Job A based on the number of
 working days between 4/12/2019 and 4/22/2019 and the number of working hours within each
 day.
Important: If you do not specify the time, the system assumes the full number of working hours within the day. This means that if you transfer a piece of equipment directly from one job to another, the system will bill a full day of usage to both jobs based on the Hrs/Day specified for each job's template in [EM Auto Usage Posting Template ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-auto-usage-posting-template-form).
Important: If the time of transfer is prior to the workday start time (specified in EM Auto Usage Posting Template), usage charged to the job begins at the workday start time. If the time of the next transfer is after the workday stop time, usage charged to the previous job ends at the workday stop time.

Related information

- [About the EM Location Transfer Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)

## Estimate Out Date

Estimate Out Date field on the EM Location Transfer form, Info tab
Enter the date you estimate this equipment will be transferred from the new location or select the date from the calendar. You may use this date to determine future scheduling for this equipment.
Note: If you selected the Use Est Out
 Date checkbox for a category or piece of equipment on the auto usage
 posting template, and you transfer the equipment to a job that uses that template, entry is
 required in the Estimate Out Date field to calculate revenue properly.

##  Memo

Memo field on the EM Location Transfer form, Info tab
 Enter a memo, up to 60 characters, related to this equipment transfer.

Related information

- [About the EM Location Transfer Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)

- [About the EM Automatic Usage Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-automatic-usage-form)

## Search Criteria: JCCo

JCCo field under the Search Criteria section of the EM Location Transfer form.
Enter a JC company to filter on or press F4 to select from a list of JC companies.
Use the additional search-criteria fields (Job, Location, Date) to refine your search.

## Search Criteria: Job

Job field under the Search Criteria section of the EM Location Transfer form.
Enter a job to filter on or press F4 to select from a list of JC jobs.
Use the additional search-criteria fields (JCCo, Location, Date) to refine your search.

## Search Criteria: Location

Location field under the Search Criteria section of the EM Location Transfer form.
Enter a location to filter on or press F4 to select from a list of EM locations.
 Use the additional search-criteria fields (JCCo, Job, Date) to refine your search.

## Search Criteria: To Date

To: Date field in the Search Criteria section of the EM Location Transfer form.
Enter ending date in a range of dates by which to filter equipment transfers.
Use the additional search-criteria fields (JCCo, Job, Location) to refine your search.

## Search Criteria: From Date

From: Date field in the Search Criteria section of the EM Location Transfer form.
Enter beginning date in a range of date by which to filter equipment transfers.
Use the additional search-criteria fields (JCCo, Job, Location) to refine your search.

## Notes

EM Location Transfer form, Notes tab
Enter any notes on the location transfer.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

Related information

- [About the EM Location Transfer Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)

- [About the EM Automatic Usage Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-automatic-usage-form)

## Equipment

Equipment field on the EM Location Transfer form, Attachments tab
 Required.
Enter the equipment to attach or press
 F4
 to select from a list of active equipment. The Equipment Desc field is automatically
 filled in with the description for the piece of equipment.

Related information

- [About Transferring Attachments/Components](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-transferring-attachmentscomponents)

- [About the EM Location Transfer Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)

## Memo

Memo field on the EM Location Transfer form, Attachments tab
Enter a memo, up to 60 characters, related to the attachment transfer.

Related information

- [About Transferring Attachments/Components](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-transferring-attachmentscomponents)

- [About the EM Location Transfer Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form)

## Override Date Time

Override Date Time checkbox on the EM Location Transfer form, Attachments tab
Select the checkbox if you want to specify
 the date and time of the attachment transfer. Once the checkbox is selected, the
 Date
 and Time fields are enabled.
If the checkbox is not selected, the system uses the date and time of the primary equipment transfer as the date and time of the attachment transfer.

### Example

Suppose that you have used the EM Location Transfer
 form to transfer a dump truck with a trailer attachment to a job site on 4/1/19. A few
 weeks later, on 4/26/19, the trailer needs to be moved to a shop for maintenance. To
 move the trailer, you again use the EM Location Transfer form, specifying the trailer as
 the equipment to transfer and the shop as the location. When the record is saved, the
 system detaches the trailer from the dump truck and transfers the trailer to the new
 location.
On 4/29/19, the maintenance on the trailer is
 finished, so you want to move the trailer back to the job site and attach it to the dump
 truck. To do this, you use the EM Location Transfer form to find the original transfer
 record for the dump truck to the job site (i.e. the transfer record from 4/1/19). In the
 Attachments tab, you add a new record for the trailer attachment. In this record, you
 select the Override Date Time checkbox and specify 4/29/19 as the date and 09:00
 as the time. When the record is saved, the system transfers the trailer from the shop to
 the job site on the specified date and attaches the trailer to the dump truck.
Note: In this scenario, there will be two attachment records for
 the trailer--one for the original transfer on 4/1/19 and one for the transfer on
 4/29/19.

## Date

Date on the EM Location Transfer form, Attachments tab
Enabled if the Override Date
 Time checkbox is selected.
By default, this field displays the current date.
Enter the date the attachment was transferred to the primary equipment.
Note: The date and time specified must be after the primary equipment transfer date.

## Time

Time field on the EM Location Transfer form, Attachments tab
Enabled if you select the Override Date
 Time checkbox.
Enter the time the attachment was transferred to the primary equipment.
Note: The date and time specified must be after the primary equipment transfer date.
