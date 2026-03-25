---
title: "About Apply to All Quote Lines | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/quotes/about-apply-to-all-quote-lines"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/quotes/about-apply-to-all-quote-lines"
---

# About Apply to All Quote Lines

The Apply to All Quotes section on the PO Quote Edit form allows you to update the vendor, ship location,
 and/or status to all eligible lines on a quote at one time.
Once you enter the value (or values) you wish to
 update, select the Apply button. Each line on the quote is automatically updated
 with the specified vendor, ship location, and/or status. For vendor and ship location,
 entering a dash (-) will set the vendor or ship location to null.
When updating the status, there are three
 options available:

- Open – This option is automatically
 assigned to each quote line when it is created. Indicates the q. (Note: Quote
 lines will also be assigned this status if previously assigned PO's are cleared
 for any requisition line.)

- Ready for Vendor – Indicates the
 quote lines are ready to be sent to vendors. Quote lines with this status will
 print on the PO Requisition Quote Form report, which can then be sent to
 selected vendors for quotes.

- Quoted – Indicates the quote lines
 have been quoted by a vendor (or vendors).

Note: There are three additional status options that can
 be applied to a quote line: Ready for Purchase, Completed, and Denied. These options are
 shown in the drop-down menu of the Status column in the grid. However, they cannot be
 applied manually to any quote line. They are applied automatically by the system based
 on where you are in the quote process. These statuses are applied as follows:

- Ready for Purchase – Indicates
 the quote line is ready for purchase. This status will only be assigned to
 quote lines with a status of 'Quoted' if one of the following conditions is
 met:

- Approval is required and
 all assigned reviewers have approved the line or,

- Approval is not required
 and no reviewers have been assigned to the line or,

- Approval is not
 required, but reviewers have been assigned and all reviewers have
 approved the line.

Note: Quote lines with this status can be initialized to a
 purchase order. (Note: Quote lines will retain this status until all of the requisition
 lines have been initialized to a purchase order.)

- Completed – Indicates this quote
 line is complete (i.e. all requisition lines have been initialized to a
 purchase order).

- Denied – Indicates this quote
 line has been denied. Quote lines can only receive this status if they
 require approval (flag in PO Company Parameters) and one or more reviewers
 flagged the quote line as 'Rejected' in PO Requisition Reviewer.
