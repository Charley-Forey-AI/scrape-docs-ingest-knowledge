---
title: "Update Draws to Invoice Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/update-draws-to-invoice-entry"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/update-draws-to-invoice-entry"
---

# Update Draws to Invoice Entry

This update transfers billing draw requests to the Invoice Entry screen. The invoice number in Invoice Entry will be the job number and the application number, separated by an asterisk (for example, application 7 for job 9312 would display in Invoice Entry as invoice number 9312*07). This feature will also create the next draw request for each job, if desired. During the update, Spectrum will search the Change Request and Change Order header files for any records that may have been previously transferred to the current application number and will create additional line items for those records.
The next invoice number that will be used in Invoice Entry is determined
 in the Accounts Receivable Installation > Properties tab at the Next invoice number field. If the job number is 8-10 digits long,
 the software will use the invoice sequence regardless of Accounts Receivable installation
 settings stating otherwise.
Click the Select button to open the Select Applications to Update window and select which draw requests to update. Applications appear here when they have a period to (G/L date) entered on them. Unposted applications include those with non-zero amounts in the 'This period billing' column.
After draw request applications are transferred to Invoice Entry, the Sales Journal should be printed and updated. The Sales Journal Update will only update Job Costs if the options were set appropriately on the Accounts Receivable Installation screen. Accounts Receivable Installation prompts are available to designate whether to post all of the draw request billing items with current work performed to Invoice Entry detail as separate lines. Alternatively, draw requests may be transferred in summary. If billing items are to be transferred in detail, the Accounts Receivable Installation screen then provides the option whether to include the billing item code as part of the description. Up to 9,999 draw requests be updated at a time.
If the 'Use online tax calculation service' checkbox is selected on the Installation screen and the sales tax code for the draw request is an online tax code, the draw request will pass along this status to the invoice.
Once you preview the report associated with this screen, the software will take you to the [Sales Journal / Update](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/sales-journal--update) screen.
Note: When an override terms code is assigned to the
 contract, this code is assigned during the update.
