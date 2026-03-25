---
title: "Quote Lines | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/quotes/quote-lines"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/quotes/quote-lines"
---

# Quote Lines

When you add a line to a quote (via PO Quote Edit), the ship location, vendor, vendor material number, unit cost, and total cost default as null, regardless of whether you entered this information on the requisition line.
Because quotes are sent to vendors for pricing, you may not typically know this information until after quotes are returned from the vendors and you select the quote (vendor) you will be using.
When you are ready to send a quote to vendors for pricing, you must set the status to 'Ready for Vendor'. This will allow you to print the quote using the PO Requisition Quote Form report. (Note: You can print the quote form for one or more quotes at one time; however, each vendor must be printed separately. In addition, vendors specified on quote lines are ignored by the Quote Form report. If you want the form printed for the vendor specified on the quote line, you must specify that vendor when printing the form.)
Once the vendor quotes are returned and you have selected the vendor you will be using, you can then assign that vendor to the quote line. At that time, you will need to also enter the unit price and any other needed information (i.e. ship location, vendor material number, expected date, and/or notes). Once you have completed entering the information, you must set the status to 'Quoted'. If you do not require approval for purchase and have not assigned any reviewers to the quote line, the system will automatically set the status to 'Ready for Purchase'. If approval is required, setting the status to 'Quoted' will allow the reviewer(s) to pull the quote line up in PO Requisition Reviewer for review and approval. Once approved, the status will be set to 'Ready for Purchase'. Quotes flagged as 'Ready for Purchase' can then be initialized to a purchase order.
Note: If you have specified a Threshold Amount in PO Company Parameters (Requisition Info tab) and the total cost of the quote line exceeds the specified amount, the quote line is automatically assigned the default Threshold Reviewer, regardless of whether or not approval is required for purchase. The reviewer must approve the line before the status will be set to 'Ready for Purchase'.
Use the Reviewers tab for reviewing, adding, or deleting reviewers for a quote line.
