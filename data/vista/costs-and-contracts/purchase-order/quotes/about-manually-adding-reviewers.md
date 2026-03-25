---
title: "About Manually Adding Reviewers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/quotes/about-manually-adding-reviewers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/quotes/about-manually-adding-reviewers"
---

# About Manually Adding Reviewers

You can manually assign "Active" reviewers (setup in the HQ Reviewers form) to any quote line (in the PO Quote Edit form), regardless of whether you have set the company flag to require approval before adding quote lines to a purchase order.
If you have assigned a default reviewer in PO Company Parameters (Requisition Info tab), that reviewer will be assigned automatically to each line added to a quote, in addition to any default reviewer you may have assigned during quote initialization.
You can add, change, or delete reviewers as desired. Keep in mind that if you have set the company flags to require approval of quotes, there must always be at least one reviewer assigned. Otherwise, the quote line will not go through the approval process and therefore, cannot be added to a purchase order. If the company flags are set to not require approval, deleting all assigned reviewers from a quote line will not prevent the line from being added to a purchase order.
Note: Reviewers cannot be added, changed, or deleted from quote lines that have already been initialized to a purchase order.
When you add reviewers to a quote line, the Status is set to 'Open' and the Assigned Date defaults to the current date. Once the line is approved or rejected (in PO Requisition Reviewer), the Status and Review Date are updated accordingly. If the line was rejected, the rejection reason entered by the reviewer will display in the Description column.
