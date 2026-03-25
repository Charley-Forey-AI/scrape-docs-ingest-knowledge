---
title: "Field Definitions: EM Miles by State Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-miles-by-state-em-kilometers-by-stateem-kilometers-by-province-form/field-definitions-em-miles-by-state-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-miles-by-state-em-kilometers-by-stateem-kilometers-by-province-form/field-definitions-em-miles-by-state-form"
---

# Field Definitions: EM Miles by State Form

The following is a list of field descriptions for the EM
 Miles by State form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 Enter the sequence number of an existing entry or enter N, New, or + to add a new sequence. The system will automatically assign the next available sequential number.

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

##  Equipment

 Enter the equipment (from EM Equipment) for which to enter mileage by state information.
Note: Once you add lines to this transaction, this field is disabled.

##  Reading Date

 Enter the reading date for this transaction, typically the day the trip occurred. Initially defaults as null for first entry in the batch, then defaults the date from the previous transaction.

##  Begin Odo

 Specify the beginning odometer
 reading for this trip. Initially defaults the ‘End Odo’ from the last 'miles by state'
 posting.
 This reading applies to all lines entered for this transaction, and will be used in conjunction with the ending odometer reading to provide the Total Miles.
Note: This is a stand-alone form; therefore, readings
 entered in this form will not update EMEM (Equipment).

##  End Odo

 Specify the ending odometer reading
 for this trip.
 This reading applies to all lines entered for this transaction, and will be used in conjunction with the ending odometer reading to provide the Total Miles.
Note: This is a stand-alone form; therefore, readings
 entered in this form will not update EMEM (Equipment).

##  Line

 Enter a sequence number for this line or enter N, New, or + to have the system auto-assign the next available sequential number.

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

##  Usage Date

 Enter the usage date for this mileage reading. Initially defaults the header usage date.

##  State

 Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, and the record will not be saved.
Note: The name of this field differs depending on the
 Default
 Country specified in HQ Company Setup. For the United States (US) and
 Australia (AU), the label displays as "State". For Canada (CA), the label displays as
 "Province".

##  Loaded

 Enter the on-road miles traveled in this state with a full load. If a breakdown of loaded vs. unloaded miles is not required by this state, this amount should include both loaded and unloaded on-road miles.
Note: This reading, in conjunction with the 'unloaded' and
 'off road' mileage, will be used to calculate the Undistributed mileage. If the
 ‘Undistributed’ amount (shown to the right of the line number) does not equal 0.00, when
 you move off the line, a message displays indicating the sequence contains undistributed or
 over-distributed miles; however, entry is allowed.
 When you are ready to post the batch, if you have not fully distributed the Total Miles for the batch, a message displays indicating that there are undistributed or over-distributed miles left in the batch. You have the option to ‘cancel’ the operation or to continue posting the batch. If you click ‘Cancel’, the EM Batch Warnings window displays, providing a list of the sequences in the batch that are out of balance. Information shown includes the equipment, total miles, and undistributed amount.

##  Unloaded

 Enter the on-road miles traveled in this state with an empty load. If a breakdown of loaded vs. unloaded miles is not required by this state, leave this field blank and include the unloaded on-road miles in the value for loaded on-road miles.
Note: This reading, in conjunction with the 'unloaded' and
 'off road' mileage, will be used to calculate the Undistributed mileage. If the
 ‘Undistributed’ amount (shown to the right of the line number) does not equal 0.00, when
 you move off the line, a message displays indicating the sequence contains undistributed or
 over-distributed miles; however, entry is allowed.
 When you are ready to post the batch, if you have not fully distributed the Total Miles for the batch, a message displays indicating that there are undistributed or over-distributed miles left in the batch. You have the option to ‘cancel’ the operation or to continue posting the batch. If you click ‘Cancel’, the EM Batch Warnings window displays, providing a list of the sequences in the batch that are out of balance. Information shown includes the equipment, total miles, and undistributed amount.

##  Off-Road

 Enter the total off-road miles traveled in this state. Off-road miles include any miles traveled on roads that are not considered a main highway or thoroughfare, such as logging roads or other unfinished roads. This also includes when vehicle is unloading materials at a site.
Note: This reading, in conjunction with the 'unloaded' and
 'off road' mileage, will be used to calculate the Undistributed mileage. If the
 ‘Undistributed’ amount (shown to the right of the line number) does not equal 0.00, when
 you move off the line, a message displays indicating the sequence contains undistributed or
 over-distributed miles; however, entry is allowed.
 When you are ready to post the batch, if you have not fully distributed the Total Miles for the batch, a message displays indicating that there are undistributed or over-distributed miles left in the batch. You have the option to ‘cancel’ the operation or to continue posting the batch. If you click ‘Cancel’, the EM Batch Warnings window displays, providing a list of the sequences in the batch that are out of balance. Information shown includes the equipment, total miles, and undistributed amount.
