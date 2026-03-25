---
title: "About the MS Mass Ticket Edit Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-mass-ticket-edit-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-mass-ticket-edit-form"
---

# About the MS Mass Ticket Edit Form

Use this form to make the same change to several tickets in the batch - for example if you need to change the sale date on each ticket that is associated with a specific location.
Select File > Mass
 Edit from MS Ticket Entry to open this form.
The system limits the information that can be changed on cash and credit card sales,
 entries that have already been invoiced to AR, those with verified haul information,
 or those that have had their Hauler Payment information updated to AP. When
 processed by the Mass Edit program, the status of each transaction will be checked
 to determine whether purchaser (i.e. Customer, Job, or Inventory), pricing, haul
 charge, tax, discount, and/or hauler payment information is eligible to be changed.
 Purchaser and dollar amounts (material, haul, tax, and discount) will not be changed
 on cash or credit card transactions, or any transaction that has already been
 invoiced. Haul information will not be changed on any transaction that has been
 verified, and hauler payment values will not be changed on any entry that has been
 updated to AP.

## Adding Tickets to a Batch

Tickets can only be edited while in a batch; therefore, tickets that have already
 been posted to the Ticket Detail table (MSTD) must be pulled into a current batch
 before they can be edited using this form. Select File > Add
 Tickets in MS Ticket Entry to add tickets you want to edit into the current
 ticket batch.

## Filtering Criteria

 First, using the Filter Criteria
 selection box, select the type of criteria to restrict by (sale date, from location,
 sale type, material, hauler type, or tax).
 Once you select a filter criteria
 option, the system displays one or more series of fields related to that option.
 Each series of fields will include a checkbox option and related filter value
 fields. The checkbox is used to indicate whether you want that data used as
 restriction criteria. If you check the box, the system enables the related filter
 value fields, allowing you to enter specific data.
For example, if you select the Sale Date
 option, the screen displays a Sale Date checkbox and From/Through date fields. If you check
 the Sale
 Date box, the system enables the From
 and Through fields, allowing you to specify the range of sale dates
 that will be eligible. Tickets must have a sales date within this range to be
 included for editing.

## Editing Criteria

Use the Edit Criteria section to indicate how the filtered batch entries are to be
 changed. First, select the type of criteria to restrict by using the Edit Criteria
 selection box; related fields display to the right. For each item, indicate whether
 change will be made to the specified data. There are three options available, though
 not all options are available for all items:

- 0-N/C – Select this option
 if there will be no change to the related data.

- 1-Default – This option is
 only available for some items. Select this option when the specified
 data will be changed to the standard default for that item. For example,
 if you are restricting by “Material”, and you select option 1for UM, the
 edit process will change the unit of measure on all eligible tickets to
 be either the sales unit of measure defined on a quote, if one exists,
 or the sales unit of measure defined for the material in HQ Materials.


- 2-Value – Select this option
 when the related data will be changed to a specific value. When this
 option is selected, the related value field is enabled, allowing you to
 enter the specific value to use. For example, if restricting by
 Material, and you select option 2 for Material Phase, then you must
 enter a valid phase.

## Refresh

After you have entered the applicable Search and Edit Criteria options and clicked
 Process to make the necessary changes to eligible tickets, clicking the Refresh
 button will update the entries in the Batch Detail grid. If you use the Undo button
 (discussed below), clicking Refresh will update the grid with the old values.Note: This step is not required; the system will
 automatically update the specified data once you exit the form and return to MS
 Ticket Entry. However, it does allow you see all of the tickets that are in the
 batch, as well as limited data changes (e.g. From Loc, Material,
 etc.)

## Process

Once you have defined all of the Filter and Edit criteria, click Process
 to implement the edit process. All tickets meeting the filter criteria will be
 updated to reflect the edit criteria. When the mass edit process is complete, a
 message displays informing you of the number of entries that met the filtering
 criteria, the number of entries that were changed, and the number of entries that
 were skipped due to invalid values.

## Clear and Undo

Use the Clear buttons in both the Filter Criteria and Edit Criteria sections of this
 form to clear out existing criteria, allowing you to redefine criteria as necessary.
 Be aware that when you click these buttons, the system clears all fields on the
 form. Use the Undo button to undo any of the processed edits. The Ticket Batch table
 (MSTB) tracks both old and new values for each entry. If tickets have been pulled
 into a batch, the old values will match the values in the Ticket Detail table
 (MSTD). If new tickets have been entered, whether added manually or via upload, the
 old values will become the original values. The new values will be the changed or
 current values, and are the values that will be updated to MSTD when the batch is
 posted. If no change is made to a ticket, the old and new values will be equal.
 Tracking both old and new values in this manner allows you to discard any unwanted
 changes that may result when running this program. By pressing the Undo button, you
 can restore the original values for all new entries, and existing values for all
 ‘changed’ entries in the batch.Note: The Undo
 function restores the entire batch, not just entries affected by a mass edit. In
 general, you should isolate and perform mass edit entries within their own batch
 (i.e. not mixed with new tickets).

## MS Ticket Mass Edit Preview Report

Use this report to preview processed edits before you post the batch. To access this
 report, select Options > Reports > MS
 Ticket Mass Edit Preview. Specify the company, batch month, and batch ID, run the report, and
 all sequences in the batch display, showing both the old and new data for each. This
 will allow you to verify your changes before you post the ticket batch. Use MS
 Ticket Entry or click the Undo button to undo any changes.

Related information

- [About the MS Ticket Entry Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form)
