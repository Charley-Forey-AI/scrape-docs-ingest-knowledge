---
title: "Ticket Verification | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/ticket-verification"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/ticket-verification"
---

# Ticket Verification

Ticket verification is an optional feature that allows you to reconcile tickets with time sheet entries.
It is expected that tickets uploaded from a scale package, or manually entered in the system, will generally be posted before the hauler’s time sheet. When you enter time sheets, the system will automatically display any tickets that match the hauler type (Equipment or Haul Vendor), the posting date, and equipment or truck information. Ticket detail can then be reviewed by clicking the Tickets button in the time sheet header. If a ticket is found that matches the time sheet information, you can check the Verify button, thereby indicating that the ticket is accounted for. If all tickets in the grid can be accounted for, you can use the Verify All button to verify all of the tickets at one time. Once ‘verified’, the Ticket Detail table (MSTD) is automatically updated, and you will not be able to edit or delete the time sheet. If it is necessary to change detail on a time sheet (date, hauler type, haul vendor, driver, EM company, equipment, or employee), you must first clear the verified ticket.

## Time Sheet Updates

Once a time sheet is entered, its
 information is available for updates to:

- Job Cost – Haul charges posted
 to jobs

- Equipment Management – Equipment
 revenue from usage

- Accounts Receivable – Haul
 charges invoiced to customers or sister-companies

- Accounts Payable – Payments to
 haul vendors

- Inventory – Haul charges posted
 to IN locations

Entries are stored in the MSHB (Haul
 Header) and MSLB (Haul Line Batch) tables until the time sheet batch is validated
 and posted. Once posted, header detail is stored in the MS Haul Header table (MSHH)
 and line detail is stored in the MSTD table (MS Ticket Detail). Updates to JC, EM,
 and IN occur as soon as the batch is processed. However, updates to AR (customer and
 intercompany transactions) will only occur once you have generated and posted
 invoices in MS Invoice Edit, and updates to AP (haul vendor payments) will only
 occur once you have generated and posted AP invoices in MS Haul Payment Worksheets.
