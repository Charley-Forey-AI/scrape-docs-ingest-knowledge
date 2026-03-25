---
title: "Set up an Agreement in SM Agreements | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-an-agreement-in-sm-agreements"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-an-agreement-in-sm-agreements"
---

# Set up an Agreement in SM Agreements

You can use the SM Agreements form to set up agreements for managing and billing services, including setting up budgets, billing and amortization schedules, and labor allocations.
Note: You can also use the Agreements tab in SM Customers to quick-add agreements if needed; however, to enter an agreement in its entirety (including agreement services, task schedules, budgets, etc.), you must use SM Agreements.

When you first add an agreement, it is set up as a quote. Once the quote is approved, it becomes an agreement. The process outlined here guides you through the process of setting up the agreement quote.

1. Open SM Agreements.

1. In the Agreement field, enter N, New, or + to have the system auto-assign an agreement number or enter the agreement number manually.Note: The system automatically sets the Revision and Version values, which cannot be changed. For more information about the Revision, see the [Revision](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form/field-definitions-sm-agreements-form#ID-00041125--en) F1 help. For information about Versions, see [About Agreement Versions / Terms](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-versions--terms).

1. In the Description field, enter a description of this agreement.

1. If applicable, in the Alt Agreement field, enter the alternate agreement identification number used by the customer to track this agreement.

1. In the Agreement Type field, enter the agreement type or press F4 to select from a list of valid agreement types.

1. In the Customer field, enter the SM customer or press F4 to select from a list of valid SM customers.

1. Optionally, in the Customer PO field, enter the customer's PO number to default work orders generated for this agreement.

1. Enter the agreement dates:

- Effective Date - the date this agreement became or will become effective

- Expiration Date - the date this agreement expires

- Renew Through - If the agreement type is flagged for auto renewal, the date through which to renew the agreement.

1. If you entered a Renew Through date, enter the renewal markup percent in the Renewal Markup field.

1. In the Rate Template field, enter the rate template to use for (add-on) work performed on a work order that is not covered by the agreement price.

1. In the Agreement Price field, enter the agreement amount. This amount represents the total charge to the customer (for all services listed on the work schedule) for the life of the agreement.

1. From the Matl Tax Override drop-down, select one of the following (see the [F1 help](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form/field-definitions-sm-agreements-form#ID-000411ca--en) for more information about each option):

- Blank.

- N - No Tax

- S - Sales Tax Only

- U - Use Tax Only

1. From the Tax Option
 Override drop-down, select one of the following (see the [F1 help](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form/field-definitions-sm-agreements-form#concept-g0232ikc--en) for more information):

- N - Not Taxable

- P - Taxable at Purchase Only

- B - Taxable at Billing Only

- M - Taxable at Purchase/Markup at Billing

- F - Full Tax at Purchase and Billing

1. If you are not using "As Costs Incurred" revenue recognition (that is, the Recognize Revenue as Costs Incurred checkbox is not selected in SM Company Parameters), select the revenue recognition method from the Revenue Recognition drop-down.

- B - As Billed - Select to recognize agreement revenue as it is billed

- S - Amortize - Select to amortize agreement revenue based on an amortization schedule. For more information, see [Set up an Agreement Amortization Schedule
 Manually](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/set-up-an-agreement-amortization-schedule-manually).

Note: If the Recognize Revenue as Costs Incurred checkbox is selected in SM Company Parameters, the Revenue Recognition drop-down is disabled and set to C - As Costs Incurred.

1. In the Margin field, enter a mark-up percentage to apply when recognizing revenue for this agreement. During the revenue recognition process (in SM Revenue Recognize), the system determines the revenue to recognize by applying the margin to the sum of all associated costs (that is, work completed lines posted to the agreement work order).
Note: Entry in this field is required for As Costs Incurred revenue recognition.

1. In the Invoice Format field, enter the custom report to use for printing agreement billing invoices for this customer. Leave blank to use the Def. Agreement Inv. Report specified in SM Company Parameters.

1. Select the Auto Schedule Trips checkbox to have a service automatically scheduled on the Dispatch Board. Note: Auto-scheduled trips will default to the date and technician specified on the SM Service form.

1. If you are using the [Tasking](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling) feature and want to create a separate work order scope for each service item when generating PM work orders, select the Separate Scope Per Service Item checkbox.If you leave this checkbox unselected, service items will be grouped together on the same work order scope. For more information, see the [Separate Scope Per Service Item](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form/field-definitions-sm-agreements-form#concept-54e54ad0-7459-40d6-99c9-c77d270e3e69--en) F1 help.

1. If the Agreement Type you specified in Step 5 is flagged for auto-renewal (in SM Agreement Types), enter the date through which to renew the agreement in the Renew Through field. Date must be greater than the expiration date specified for the agreement.

1. [Set up an agreement budget](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-an-agreement-budget).

1. [Set up services for the agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup).

1. [Set up a billing schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup).

1. [Set up an amortization schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup).

1. [Set up labor allocations](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-labor-allocations).

1. [Activate the agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-activation--deactivation-form).

Related information

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

- [SM Agreement Types Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-types-form)

- [Set Up Equipment Tasking](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking)
