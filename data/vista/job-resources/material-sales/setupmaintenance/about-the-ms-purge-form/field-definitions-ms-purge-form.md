---
title: "Field Definitions: MS Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-purge-form/field-definitions-ms-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-purge-form/field-definitions-ms-purge-form"
---

# Field Definitions: MS Purge Form

The following is a list of field descriptions for the MS
 Purge form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Tickets

 Check this box to remove ticket detail from the Ticket Detail table (MSTD). The system skips transactions linked to a hauler time sheet and/or included on an invoice and deletes them when purging hauler time sheets or invoices.
 Do not check this box if you do not want to purge ticket detail.

##  Hauler Time Sheets

 Check this box to remove hauler time sheets. The purge process deletes time sheet headers from the Haul Header table (MSHH) and their associated line detail from the Ticket Detail table (MSTD). The system removes the header only after purging all line detail. The system deletes time sheet detail included on an invoice only when purging the invoice.
 Do not check this box if you do not want to purge hauler time sheets.

##  Monthly Sales Totals

 Check this box to remove sales totals from the Sales Activity table (MSSA). You may retain this information on your system for running monthly sales reports.
 Do not check this box if you do not want to purge month sales totals.

##  Deleted Tickets

 Check this box to remove deleted tickets from the Deleted Ticket table (MSTX).
 Do not check this box if you do not want to purge deleted tickets.

##  Invoices

 Check this box to remove MS invoices from the system. The system purges header detail from the Invoice Header table (MSIH) and invoice lines from the Invoice Lines table (MSIL). The system also purges all associated detail from the Ticket Detail table (MSTD).
 Do not check this box if you do not want to purge MS invoices.

##  Restriction Options

 Select the following options to restrict purging.

- Location Group — Check this box to restrict detail for purging to a single location group (indicated to the right of this field). If you do not check this box, the system purges all indicated detail, regardless of location group.

- Location — Check this box to restrict detail for purging to a single location (indicated to the right of this field). If you do not check this box, the system purges all indicated detail, regardless of location.

##  Location

 Specify the location (from IN Locations) for restricting. The system only
 purges detail posted to this location.
 If this field is blank, the system purges all detail, regardless of location.

##  Purge Entries Posted Through

 Enter the month through which to purge detail. The entered month must be closed in the subledger of the current MS company’s GL company. The system purges detail posted in or prior to this month.

##  Location Group

 Specify the location group (from IN Location Groups) for restricting. The system only purges detail posted to locations within this location group.
 If this field is blank, the system purges all detail regardless of location group/location.

## Notes

Use this tab to enter any miscellaneous notes about this item. The space allowance is virtually unlimited.
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
