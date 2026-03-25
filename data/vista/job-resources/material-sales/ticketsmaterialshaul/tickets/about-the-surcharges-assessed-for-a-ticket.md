---
title: "About the Surcharges Assessed for a Ticket | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-surcharges-assessed-for-a-ticket"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-surcharges-assessed-for-a-ticket"
---

# About the Surcharges Assessed for a Ticket

If you are using the Surcharges feature, you can review the
 surcharges assessed for a ticket on the Surcharge tab in MS Ticket Entry.
The system calculates surcharges based on the
 surcharge codes defined for the surcharge group (assigned at the quote level or in MS
 Company Parameters), the data entered for the ticket, and the rates defined on the quote
 (Surcharge Overrides tab) or in MS Surcharge Codes. The assessed surcharges are then
 displayed on this tab and can be edited or deleted as necessary. You can also add new
 surcharges manually if desired.
Surcharges will not be assessed if:

- the Apply Surcharges checkbox is not selected on the quote associated
 with the ticket or,

- the Apply Surcharges checkbox is selected for the quote, but no
 surcharge group is assigned to the quote or in MS Company Parameters or,

- no quote exists for the ticket's purchaser and no default surcharge group is
 specified in MS Company Parameters.

- the ticket is for a C-Cash or X-Credit Card sale and the Calculate
 Surcharges on Cash Sales checkbox is not selected for applicable
 surcharge codes in MS Surcharge Codes.

What happens to surcharges when you change a ticket?
If you change any values on the ticket, the system automatically re-assesses the surcharges for that ticket. The system handles this as follows:

- If you make changes to a new ticket (add mode), the system removes the
 existing surcharges, then reassesses them and adds the new entries to the surcharges
 grid. Manually added surcharges are not reassessed and will need to be added back
 manually.

- If you make changes to a ticket that was pulled back into a batch (change
 mode), the system sets all surcharges to 'Delete' and highlights them in red. It
 will then reassess the surcharges and add them below the original surcharges. Any
 manually added surcharges will need to be re-entered. Once you post the batch, the
 system deletes the surcharges flagged as 'Delete'. This allows for the surcharges to
 be backed out of GL and then re-added with the new values.

Note: There is a 'parent/child' relationship between MS tickets
 and their associated surcharges. If you post a ticket (aka parent ticket) and need to
 make changes to the surcharges (aka child tickets), you will need to reference the
 parent ticket; you cannot pull a child ticket into the batch without its parent
 ticket.
