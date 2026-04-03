---
title: "Scale Ticket Journal | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-journal"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-journal"
---

# Scale Ticket Journal

This screen presents a summary listing of the tickets being updated. The software identifies tickets imported with customer codes as sales invoices and tickets imported with job numbers as job requisitions. Job requisitions are sorted by job number; sales invoices display with the corresponding customer codes. This update will only post one jobrequisition per scale ticket, regardless of whether it has the same item, job, phase and cost type or not. Transfers display with both the original (from) and destination (to) warehouses. The update will use the sales tax amount stored in the unposted ticket.
This update provides for tickets posting to job requisitions using the multi-company feature. An error listing displays, detailing tickets for which the G/L account information was not set up properly. These tickets will not be updated until the G/L account codes are corrected. Additionally, any job tickets with an invalid phase or cost type will appear on the exception report.
The Materials Management Journal Update to Order Processing automatically creates a separate line for "freight" when the Separate freight billing item on invoices checkbox is selected in the Materials Management Installation screen. If the checkbox is not selected, a separate "freight" line is only created if there is estimated cost set up in Hauler File Maintenance or Customer Material Contract Maintenance. In this case, the sales extension of this line is $0.00. If freight and miscellaneous charges are not separated, and the ticket contains multiple items, the additional charges are bundled with the first item that has a non-zero quantity and a matching tax setting. In the unusual event that every item has a zero quantity, then the software will create separate freight and miscellaneous lines.
Additional protection is incorporated into the Scale Ticket Update to ensure that invoices will be created in Order Processing with invoice numbers that have not already used in either A/R or O/P. This ensures that every invoice created throughout Spectrum is assigned a unique number.
For multi-company job requisitions that include a separate freight or miscellaneous line, the Scale Ticket Update sets the cost type for the line based on the cost type, if any, specified in the General Ledger Chart of Accounts of the destination company.
For mix transactions, the quantity of the mix item (finished product) will be added to the warehouse at the warehouse-specific 'Standard cost' of that item (not the sum of the components). The update will calculate the difference between the raw material cost and the finished product, and the difference will be posted to the Adjustment G/L account code stored in the G/L department assigned to the warehouse of the finished product.

Related information

- [Scale Ticket Journal Update - by Customer](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-transactions/scale-ticket-journal-update---by-customer)

- [Scale Ticket Journal Update - by Job](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-journal-update---by-job)
