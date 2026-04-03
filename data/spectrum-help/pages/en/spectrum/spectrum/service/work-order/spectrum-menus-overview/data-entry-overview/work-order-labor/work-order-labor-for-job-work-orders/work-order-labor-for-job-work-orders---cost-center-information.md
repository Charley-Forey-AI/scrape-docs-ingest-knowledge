---
title: "Work Order Labor for Job work orders - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-labor/work-order-labor-for-job-work-orders/work-order-labor-for-job-work-orders---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-labor/work-order-labor-for-job-work-orders/work-order-labor-for-job-work-orders---cost-center-information"
---

# Work Order Labor for Job work orders - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, Spectrum will validate the G/L department entry. Spectrum will first determine the cost center based on the Work Order Header Table. Next, it will check that the Payroll department specified for that G/L department is valid for the cost center entered (setup in the cost center overrides for that Payroll department). In addition, it will validate that the labor sales G/L account permits the cost center to be used with that account. For EU, ER, EO, and ED pay types, it will also validate that the equipment sales G/L account permits the cost center to be used with that account. It will also validate that the cost of sales debit and credit G/L accounts permit the cost center to be used with that account. If any of these validations fail, Spectrum will issue an error message and return the cursor to the G/L department field. Validation will only be done if the Payroll module is enabled in the current company in the Company Installation screen.
For labor entries entered via a task, Spectrum will perform the G/L Department validation when the labor line Completed checkbox is checked. If the G/L department isn't validated, Spectrum will display an error and clear this checkbox.
Labor validation will be done in both the main screen and the Labor Hours Entry by Work Order window. In this window, tasks can be entered in Proposed Work Order Entry, Work Order Entry, and in the service contract schedule. The Work Order Installation – Defaults tab includes the Automatically transfer task detail setting to determine if a task will create labor, material, and other cost lines when the task is added to a work order.
