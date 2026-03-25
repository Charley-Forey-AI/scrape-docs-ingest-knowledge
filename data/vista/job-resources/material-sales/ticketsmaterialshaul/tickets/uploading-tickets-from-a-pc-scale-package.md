---
title: "Uploading Tickets from a PC Scale Package | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/uploading-tickets-from-a-pc-scale-package"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/uploading-tickets-from-a-pc-scale-package"
---

# Uploading Tickets from a PC Scale Package

If your company currently uses a PC Scale package, use the Imports (IM) module to import, edit, and upload data into MS.
Typically, companies who haul their own materials or provide haul services to their customers, use ‘scale houses’ or ‘weigh stations’ to weigh the loads being hauled to and from their location. The truck is weighed before and after loading, and the information is entered directly into the computer or recorded on a ticket for later entry. Depending on the scale package, the type of information entered may differ. Generally, ticket information includes the truck type, tare, gross, and net weights, driver, material, and pricing information.
The IM module provides a means of importing this information into MS. There are several standard templates provided for uploading tickets (e.g. Alkon, AMI, Libra, Seltec, etc.); however, you can create your own templates. The import loads the text file from your scale package into a work file, which you can use to edit records as necessary. You can then upload the work file into MS Ticket Entry. If tickets do not require any further editing, process the batch as normal. If additional editing is required, use MS Ticket Entry. For more information about importing third-party data, see Imports in Related Topics below.
When importing material sales tickets, you should consider the following unique conditions before performing the import.

- Weight UM – If the weight UM for an imported ticket is not a valid HQ unit of measure, you will receive an error when trying to validate and post the ticket batch. Because the weight UM (shown to the right of the Net Weight in MS Ticket Entry) is display only, there is no way to correct the invalid unit of measure on the ticket. Therefore, you will need to delete the ticket batch, fix your import template or text file, and then re-import the data.

- Metric UM – If you are using quotes that specify to Use Metric UM and your import template specifies to Use Viewpoint Default Value for the UM, the system converts the imported UM, Unit Price, and Units values to metric. If you do not want this conversion to occur, uncheck the Use Metric UM option for all applicable quotes or uncheck the Use Viewpoint Default Value in the import template (IM Template Detail).

- Cash Sales – If you are importing cash sale tickets, and the import template specifies to Use Viewpoint Default Value for Unit Price or Material Total, the system ignores the setting. The system assumes that since the material has been paid for, you will want the actual unit price and material total to be included on the ticket and invoice.

In order to provide a record of changes made to tickets uploaded from a scale package, the MS Ticket Entry database table has an internal flag (i.e. not visible on form) that is set to indicate whether or not changes have been made to uploaded tickets. Initially, this flag is set to No. If you make changes, this flag is set to Yes. When you post the ticket batch, the system updates the corresponding flag in the Ticket Detail (MSTD) and Deleted Tickets (MSTX) tables with this status.
If you want to record specific values changed on a ticket, as well as when the change was made, and/or who made the changes, select the Tickets audit checkbox in MS Company Parameters. Auditing does not record changes to entries in a ticket batch until the batch is posted to the Ticket Detail table. Once posted, you can review the changes using the HQ Audit Detail report. You can also create your own reports to track and view this information.

Related information

- [About the MS Ticket Entry Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form)
