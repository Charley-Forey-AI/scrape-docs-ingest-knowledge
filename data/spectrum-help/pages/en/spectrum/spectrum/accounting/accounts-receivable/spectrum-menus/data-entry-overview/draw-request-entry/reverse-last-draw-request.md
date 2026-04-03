---
title: "Reverse Last Draw Request | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/reverse-last-draw-request"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/reverse-last-draw-request"
---

# Reverse Last Draw Request

You can reverse the last posted draw request for a customer and issue a credit memo for the application.
The next application (if one has been created) will be deleted. The application which is reversed will then be considered as the "current period" by the software. Change order and change request information from the reversed draw request will not be retained.
Example: Invoice 9317*07-I created through a draw request could be reversed to 9317*07-C using this screen. The invoice from the new draw would be numbered 9317A07 I; if reversed, the credit memo would be numbered 9317A07 C. It would be possible to create and reverse the same draw request 26 times, up through 9317Z07.
This screen should be used any time a draw request is reversed. If it becomes necessary to reverse a billing created through a draw request, do not reverse the invoice; reverse the draw request. The [Sales Journal / Update](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/sales-journal--update) should then be run after draw requests have been reversed.
If the contract G/L distribution feature is enabled on the Contracts > Edit Contract > Distribution tab for the draw request that is to be reversed, then the reverse draw
 request will be calculated with the same distribution being applied to the credit memo that
 is created.
Important: It is not necessary to transfer to Invoice Entry,
 as this feature automatically creates the credit memo in Invoice Entry; DO NOT use Update
 Draws to A/R Invoice when reversing draw requests.

Related information

- [Sales Journal / Update](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/sales-journal--update)

- [Reversing a Draw Request](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/reversing-a-draw-request)
