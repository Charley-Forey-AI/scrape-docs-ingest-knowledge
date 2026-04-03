---
title: "Work Order Other Charges - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-other-charges/work-order-other-charges-for-site-work-orders/work-order-other-charges---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-other-charges/work-order-other-charges-for-site-work-orders/work-order-other-charges---cost-center-information"
---

# Work Order Other Charges - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen for this company, Spectrum will perform additional validation during entry.
For a site work order, a cost center must be assigned to the work site; Spectrum will not validate that the operator has security for the cost center at this time. If the cost center cannot be validated, an error message will display when the other cost entry window is opened and the window will immediately close.
For a job work order, a cost center must be assigned to either the phase or to the job; the validation will take place after the phase and cost type are entered. If the cost center cannot be validated, the cursor will return to the Phase field and display an error message.
After the G/L department code is entered, Spectrum will verify that the cost center is valid for the G/L accounts using the work order G/L department settings for the Other item code; if the G/L department code is validated, Spectrum will then verify that the debit and credit accounts are both set up to use the job/phase/site cost center. If this cannot be verified, an error message will display and the cursor will return to the G/L department field.
For both job and site work orders, Spectrum will validate that the G/L department is valid for the job/phase or work site cost center. Spectrum will read the work order G/L department settings for the Other item code and will use the Sales G/L account. It will check that the cost center is permitted for that record, and if it is not, an error message will display and the cursor will return to the G/L department field.
For entries entered via a task, Spectrum will perform the G/L department validation when the Completed checkbox is selected.
