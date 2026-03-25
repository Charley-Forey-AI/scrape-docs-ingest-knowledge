---
title: "Base Revenue on Haul Charges | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets/base-revenue-on-haul-charges"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets/base-revenue-on-haul-charges"
---

# Base Revenue on Haul Charges

Base revenue on haul charges.
If you want revenue charges based on values
 entered with the haul code, set up the revenue code as follows (in EM Revenue Codes):

- Set the revenue code basis to be equal to the haul code basis. For
 example, if the haul code’s Haul Rate is Based On field is
 set to 2-Per Hour, then set the revenue code’s Revenue Basis option to
 Hour.

- Check the Based on MS Haul Charge/Surcharge
 box. This will flag the revenue code so that when entering tickets or hauler time
 sheets, the revenue basis, rate, and total will default from the values entered for
 the haul code.

When tickets and hauler time sheets are entered,
 the program will check to make sure that the basis of the revenue code is consistent
 with the posted haul code. If the haul code is unit based, the revenue code must also be
 unit based, and its unit of measure must match the material unit of measure entered for
 the ticket. Likewise, if the haul code is hourly based, the revenue code or pay code
 must also be hourly based.
If the validation is successful, the revenue
 code’s standard rates will be ignored, and the values entered for the haul code will
 then default into the related revenue fields. For example:

Haul CodeBasisRateCharge_Rev CodeBasisRateTotal
2 (Per Hour) 16 15.00 $240.00 1 (Per Hour) 16 15.00 240.00

Related information

- [About Entering Haul Charges with Tickets](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-entering-haul-charges-with-tickets)
