---
title: "Accounts Receivable Installation - Draw Request | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/installation-overview/accounts-receivable-installation---draw-request"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/installation-overview/accounts-receivable-installation---draw-request"
---

# Accounts Receivable Installation - Draw Request

Use this tab to select default draw request settings for the Accounts Receivable module. These settings can be changed as needed at any time.
Note: If you have unposted transactions in [Pre-Billing Quantity Entry](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/pre-billing-quantity-entry) and you open this installation screen, you will receive a warning letting you know that some pre-billing options cannot be changed until the unposted entries are addressed. In this case, go back and finish entering and updating the pre-billing quantities and then return to this screen.
Field
Descriptions

Create invoice from draw request?
Spectrum supports two options for posting draw requests to Invoice Entry, stand-alone draw requests or front-end to invoice processing. Select this checkbox if you will utilize the automatic invoice-creation method in this company while integrating draw requests with Invoice Entry. Leave this checkbox clear to indicate draw request activity will be independent of Customer Invoice Entry.
This checkbox is typically selected in most companies.

Use invoice numbering sequence?
This checkbox is valid only if the Create invoice from draw request checkbox is selected.
Select this checkbox to use the next available invoice number when creating invoices from draw requests. Leave this checkbox clear to use job-based invoice numbers.
If this checkbox is selected the next available A/R invoice number will be used when creating invoices from draw requests. If this checkbox is left clear, the draw invoice number will be assigned as job number + "*" + application number. For example, a draw invoice created for job 100, application 4 would be assigned the invoice number 100*04. If the job number is 8-10 digits long, the software used the invoice sequence regardless of whether or not this checkbox is selected.

Update billing items to invoice?
This checkbox is valid only if the Create invoice from draw request checkbox is selected.
This checkbox determines how A/R invoice lines are created when draw requests are updated to Invoice Entry. If this checkbox is selected, the software will post the description, unit of measure, quantity, unit price and extension for all the current billing items from the draw request. Additionally, the billing item is posted as part of the invoice; then the billing item will post into the description space; and the description of the billing item will post into the remaining part of the description.
If this checkbox is left clear, the software will post a summary billing line to Invoice Entry.
Most users leave this checkbox clear since they attach the A/A draw request to the summary A/R invoice as documentation.
Note: For unit price jobs, the description field is 20 length and the billing item is 8 digits. This fits into the current 30-character description. For fixed price jobs, the 30-character description will be truncated to 19 characters if this option is used (billing item of 10 plus 1 space).

Update billing item as part of description?
This checkbox is valid only if the Update billing items to invoice checkbox is selected.
If this checkbox is selected, the software will post the description, unit of measure, quantity, unit price and extension for all current billing items from the draw request into the Invoice Entry. Also, if the billing item is posted as part of the invoice, then the billing item will post into the description and add a space. The billing item description will post into the remaining part of the description.
If this checkbox is left clear, only the billing item description will post to the invoice detail description and the software will post a summary billing line to the Invoice Entry
Note: For unit price jobs, the description is 20 length and the billing item is eight. For fixed-price jobs, the 30-character description will be truncated to 19 characters if this option is used (billing item of 10 plus 1 space).

Transfer 'materials stored' to 'previously-applied' during update?
Select this checkbox to select how the materials stored column will be handled when fixed price draw requests are updated and new draw requests are created.
If this checkbox is selected, then the software will add the materials stored column to the previous applied amount and clear the materials stored. If this checkbox is left clear, then the materials stored column will remain the same on the new draw request.
This option does not affect unit price draw requests.

Default draw request format
Spectrum supports two AIA draw request formats, general contractor and subcontractor design. Select the default draw request format you want when generating and printing draw requests:

- General contractor – select if you typically issue AIA general contractor format draw requests

- Subcontractor – select if you typically prepare subcontract billings

Entry in this field is strictly for default purposes when using Print Draw Request Billing. At any time the draw requests are printed, either format may be specified by simply overriding this default.

Default unit price entry
Select one of the following options, depending on the default entry you want to use in the Draw Request Billing Entry screen:

- This period

- Job-to-date

If This period is selected, then the software will stop at the Current period quantity field for entry; if Job-to-date is entered, the software will stop at the Job-to-date field for entry.

Pre-billing options

Update quantity entries to draw
Select one of the following option buttons, depending on default quantity entry type you want updated to Draw Request Billing Entry screen:

- Actual

- Engineering

The quantity entry type that is not used to update to draw request will be stored for comparison on the Billing Quantity History Report.
Pre-billing entry is not required in order to produce draw requests in Spectrum. If you want to record daily or weekly quantity information, and want to compare engineering with actual quantity billing, use Pre-Billing Quantity Entry.

Default quantity entry
Select one of the following option buttons, depending on default quantity entry type you want to use in the Pre-Billing Quantity Entry screen:

- Actual

- Engineering

This default type may be overridden during entry. Only one quantity type will be updated to draw requests; the software allows both types to be stored for comparison purposes.

Engineering quantity type
Select one of the following option buttons, depending on the quantity entry method for engineering quantity entries you want to use in the Pre-Billing Quantity Entry screen:

- This period - choose this option if the engineering quantity will be entered for this period

- Job-to-date - choose this option if the engineering quantity entered for the job-to-date

If This period is selected, then the software will stop at the Current period quantity field for entry; if Job-to-date is entered, the software will stop at the Job-to-date field for entry.

Actual quantity type
Select one of the following option buttons, depending on the default entry method you want to use in the Draw Request Billing Entry screen:

- This period – choose this option if the engineering quantity will be entered for this period

- Job-to-date – choose this option if the engineering quantity entered for the job-to-date

If This period is selected, then the software will stop at the Current period quantity field for entry; if Job-to-date is entered, the software will stop at the Job-to-date field for entry.
