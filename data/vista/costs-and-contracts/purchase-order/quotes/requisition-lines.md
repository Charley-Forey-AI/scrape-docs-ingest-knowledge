---
title: "Requisition Lines | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/quotes/requisition-lines"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/quotes/requisition-lines"
---

# Requisition Lines

The Req Lines on Selected Quote tab on the PO Quote Edit form shows all requisition lines
 associated with the selected quote line.
This tab is display only; however, although you cannot edit existing
 requisition lines, options are provided that allow you to add new or existing
 requisition lines or remove requisition lines.
The Add New Req button allows you to create
 a new requisition 'on the fly' and have that requisition line added to the selected
 quote. When selected, the PO Requisition Entry form is displayed, allowing you to enter a
 new requisition. You will note when entering the requisition lines, the material,
 material description, UM, and ECM inputs are disabled, as the information defaults from
 the quote line and cannot be changed. The route is set to 'Quote' and the Status to
 '2-On Quote'. Once you save the requisition line and exit PO Requisition Entry, you are
 brought back to this form. The requisition line is added to the quote line, the quote
 line's status is set to 'Open', and its units updated to reflect the addition of the new
 requisition line.
The Add Existing Req button allows you to
 add existing requisition lines to the quote line. When selected, the PO Add Existing
 Requisition window displays, allowing you to specify the requisition and line number you
 wish to add. Once you select OK, the requisition line is added to the quote line.
 However, requisition lines added to a quote line using this method must reference the
 same material as the quote line. If they do not, a message displays indicating the
 requisition line was not added to the quote line.
Note: Requisition lines (new or existing) do not require
 approval before they are added to a quote line via this form, regardless of how you have
 set the company flags. It is assumed that a purchasing manager will typically use this
 form and that purchasing managers do not generally require prior approval to purchase
 additional materials. In other words, adding requisition lines using the Add Existing
 Req button disregards the Approval Required on RQ for Quote checkbox in PO Company
 Parameters (Requisition Info tab).
The Remove Req button allows you to delete a
 requisition line from a quote line (applies only to quote lines not flagged as
 Complete). Just highlight the line you wish to delete and select the Remove Req button.
 If the requisition line has not already been initialized to a purchase order, it will be
 removed from the quote line.
Note: Removing a requisition line from a quote line does
 not delete the requisition line from PO Requisition Entry. It will still be available
 for initialization to another quote.
Tip: If only one requisition line exists for a quote line
 and you delete it, the Add New Req, Add Existing Req, and Remove Req buttons are
 disabled. The addition of requisition lines to the quote line must then be handled via
 the PO Quote Initialization form (via the Add to Existing) quote option.
The View Req button allows you to review the
 selected requisition line in PO Requisition Entry. However, requisition lines will be
 disabled and cannot be edited or deleted.
