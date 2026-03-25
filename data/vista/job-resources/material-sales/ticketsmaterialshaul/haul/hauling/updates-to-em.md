---
title: "Updates to EM | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/updates-to-em"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/haul/hauling/updates-to-em"
---

# Updates to EM

If you are posting the equipment usage/revenue associated with tickets or time sheets, updates to EM will depend on the Equipment Revenue interface level you have specified in MS Company Parameters (Ticket Updates tab).
If you do not want any update to occur, set the level to 0 (No Update). Otherwise, set the level to Summary or Detail based on your company’s needs.

- Summary – Transactions are summarized by EM Co#, Equipment, Revenue Code, and Sale Type.   Total revenue units, and an average revenue rate will be calculated from the sum of Total Revenue and Usage Units.

- Detail – One EM entry is made for each ticket or time sheet posted. Posted usage units and revenue rates will be available along with the MS Trans# and Ticket.

When processing a batch of tickets or time sheets, the equipment revenue distributions are tracked in the MS Equipment Revenue Audit (MSEM) and MS Revenue Breakdown (MSRB) tables. These tables are loaded during batch validation and are used to print the MS Equipment Revenue Audit List. Once the batch is validated and posted, equipment revenue/usage is then updated to EM, creating entries in the EMRD (EM Revenue Detail) and EMRB (EM Revenue Breakdown Detail) tables based on the interface level.
