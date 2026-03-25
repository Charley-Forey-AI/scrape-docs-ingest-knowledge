---
title: "Create an Adjustment Billing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/create-an-adjustment-billing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/create-an-adjustment-billing"
---

# Create an Adjustment Billing

You can create adjustment billings for agreements that are active or have been terminated using the SM Agreement Adjustment form.
Upon opening the SM Agreement Adjustment form, the system automatically displays the agreement number, customer, and effective/expiration dates; this information cannot be edited. If the agreement is expired or terminated, the Notifications area will alert you to that information; however, you will be allowed to continue with the adjustment billing.
To create an adjustment billing:

1. In SM Agreements, select the active or terminated agreement for which to create the adjustment billing.

1. Click Create Adjustment Billing.The SM Agreement Adjustment form displays, defaulting the agreement, customer, effective date, and expiration date. This information cannot be changed.

1. In the Department field, enter the department to which the adjustment billing applies or press F4 to select from a list of valid departments associated with the agreement.If you are distributing revenue across multiple departments (that is, you selected the Post Revenue to Service Center Department checkbox for one or more periodic services in SM Service), the F4 list includes the department associated with the agreement, as well as each department defined for the periodic services. This allows you to apply the adjustment billing to the appropriate department.

1. In the Description field, enter the description you want displayed as the invoice description for this adjustment billing in SM Agreement Invoice Review.

1. In the Amount field, enter the billing adjustment amount. This can be a negative or positive value.

1. From the Tax Type drop-down, select 1-Sales, 2-Use, or 3-VAT to indicate the type of tax to apply to the adjustment billing.

1. In the Tax Code field, enter the tax code to use or press F4 to select from a list of valid tax codes.

1. In the Basis field, enter the amount on which to calculate the tax for this adjustment billing. This amount cannot exceed the adjustment amount. For example, if the adjustment amount is -5,000.00, the tax basis must be between 0 and -5,000.00.

1. Click Create Adjustment.

The system creates an invoice for the adjustment billing and opens the SM Agreement Invoice Review form. As with standard agreement invoices, you can preview the invoice, process, and deliver the invoice as normal. For more information, see [SM Agreement Invoice Review Form](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-agreement-invoice-review-form).
Once you process the adjustment billing invoice, the system updates the Revenue account for the specified department accordingly.

Related information

- [SM Agreement Adjustment Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-adjustment-form)

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)
