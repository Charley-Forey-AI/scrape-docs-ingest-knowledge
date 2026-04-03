---
title: "Work Order Materials - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-materials/work-order-materials---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-materials/work-order-materials---cost-center-information"
---

# Work Order Materials - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen for this company, Spectrum will validate the G/L department for the job/phase or site cost center for both job and site work orders. It will look at the material sales G/L account to check that the cost center is permitted for that record; if it is not permitted, an error message will display and the cursor will return to the G/L department field.
For site work orders, a cost center must be assigned to the site (Spectrum will not validate that the operator has security for the cost center at this time). If the site isn't validated, Spectrum will display an error message when the material entry window is opened, and immediately exit the window.
For a job work order, a cost center must be assigned to either the phase or to the job. The validation will take place after the phase and cost type are entered. If the phase isn't validated, Spectrum will return to the phase field and display an error message.
For both job and site work orders, Spectrum will ensure that the G/L department is valid for the job/phase or work site cost center by checking that the cost center is permitted for that record in the material sales G/L account; if not, an error message will display and the cursor will return to the G/L department field.
After the G/L department code is entered, Spectrum will verify that the cost
 center is valid for the debit and credit G/L accounts. Spectrum will read the work order
 G/L department settings for the inventory cost of sales debit and credit accounts (or
 non-inventory accounts if a non-stock item is entered) and will validate that the debit
 and credit accounts are both permitted to use the job/phase/site cost center. If the
 accounts are not validated, an error message will display and the cursor will return to
 the G/L department field.
Note: Validation will occur even if the Does work order reference job
 cost checkbox on the Work Order Installation – Defaults tab is not selected.
For material entries entered via a task, Spectrum will perform the G/L department validation when the Completed checkbox is selected. If the G/L department is invalid, Spectrum will display an error and clear the checkbox.
