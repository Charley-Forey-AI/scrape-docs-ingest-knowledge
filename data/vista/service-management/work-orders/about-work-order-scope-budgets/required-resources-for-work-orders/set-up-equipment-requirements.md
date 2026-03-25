---
title: "Set Up Equipment Requirements | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/required-resources-for-work-orders/set-up-equipment-requirements"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/required-resources-for-work-orders/set-up-equipment-requirements"
---

# Set Up Equipment Requirements

You can set up equipment requirements for the various pieces of equipment that are needed to perform a service or complete a scope of work.

Equipment requirements can be set up for serviceable item class maintenance, agreement services, work order quotes, and/or work orders. Depending on where you are setting them up, you must have done the following:

- SM Class Maintenance - [Set up maintenance tasks](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes) for the serviceable item class/type in SM Serviceable Item Class.

- SM Agreement Services - [Set up the agreement service](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup).

- SM Work Order Quotes - [Set up the work order quote/sequence](/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote).

- SM Work Orders - [Set up the work order/scope](/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders).

Note: If you set up tasks (on the Tasks tab) and assigned a standard task to one
 or more of the task sequences, the system automatically adds the equipment
 requirements defined for each of the referenced standard tasks (in SM Standard Task) to
 the serviceable item class/type, quote sequence, agreement service, or work order scope.
 You can modify entries as necessary.

To set up equipment requirements:

1. Access the form for which to set up equipment requirements:OptionDescription
SM Class Maintenance

1. Open the SM Serviceable Item Class form.

1. In the Class field, enter the serviceable item class.

1. Select the Maintenance tab and then double-click in the grid to open the SM Class Maintenance form.

SM Service

1. Open the SM Agreements form.

1. In the Agreement field, enter the agreement.

1. Select the Work Schedule tab and then double-click on the applicable service sequence to open the SM Service form.

SM Work Order Quotes

1. In the Quote ID field, enter the work order quote (must have a status of new).

1. In the Seq field, enter the scope sequence.

SM Work Orders

1. In the Work Order field, enter the work order.

1. In the Seq field, enter the scope sequence.

1. Select the Equipment tab.

1. In the Seq field, enter N or + to add a new sequence. The system automatically assigns the next available sequence number.

1. In the Task field, enter the task associated with this equipment requirement or press F4 to select from a list of valid tasks for the maintenance task.Leave this field blank if the equipment requirement is not associated with a specific task.

1. For Agreement Services, Quotes, and Work Orders only:

1. In the Serviceable Item field, enter the serviceable item associated with this equipment requirement. Leave blank if not associated with a serviceable item.

1. In the EMCo field, enter the EM company for equipment or press F4 to select from a list of valid equipment companies.Note: This field defaults the equipment company from SM Company Parameters.

1. In the Category field, enter the equipment category or press F4 to select from a list of valid equipment categories.

1. In the Equip Qty field, enter the quantity of equipment that will be used.

1. In the Rev Code field, enter the revenue code or press F4 to select from a list of valid revenue codes for the equipment category.

1. In the Rev Code Qty field, enter the number of units for the revenue code (e.g. if the revenue code is Hours, enter the number of hours).

1. For Agreement Services, Quotes, and Work Orders only:

1. In the Cost Rate field, accept the default cost rate or enter a new cost rate. Once you enter the cost rate, the system automatically calculates the Billing Rate and Total Billable; these amounts cannot be changed. For information about how the system determines the cost and billing rates, see [Equipment: Cost Rate](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-smrequiredequipment-form#ID-00041765--en) and [Equipment: Billing Rate.](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-smrequiredequipment-form#ID-0004176e--en)

1. If the equipment for this sequence is taxable, use the Tax Type, Tax Code, and Tax Basis fields to enter tax information as applicable.

1. Save the record.

1. Enter additional equipment requirements as needed.

Related information

- [SM Class Maintenance Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-class-maintenance-form)

- [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form)

- [SM Work Order Quotes Form](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
