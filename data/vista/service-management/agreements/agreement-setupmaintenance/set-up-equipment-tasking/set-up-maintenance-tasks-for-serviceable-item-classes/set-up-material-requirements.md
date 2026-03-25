---
title: "Set up Material Requirements | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes/set-up-material-requirements"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes/set-up-material-requirements"
---

# Set up Material Requirements

Material requirements represent all of the materials and/or parts that you need to complete a task or scope of work.
You can set up material requirements for serviceable item class maintenance, agreement services, work order quotes, and/or work orders. Depending on where you are setting them up, you must have done the following:

- SM Class Maintenance - [Set up maintenance tasks](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes) for the serviceable item class/type in SM Serviceable Item Class.

- SM Agreement Services - [Set up the agreement service](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup).

- SM Work Order Quotes - [Set up the work order quote/sequence](/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote).

- SM Work Orders - [Set up the work order/scope](/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders).

Note: If you set up tasks (on the Tasks tab) and assigned a standard task to one or more of the task sequences, the system automatically adds the material requirements defined for each of the referenced standard tasks (in SM Standard Task) to the serviceable item class/type, quote sequence, agreement service, or work order scope. You can modify entries as necessary.

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

1. Select the Material tab.

1. In the Seq field, enter N or + to add a new sequence. The system automatically assigns the next available sequence number.

1. In the Task field, enter the task associated with this material requirement or press F4 to select from a list of valid tasks for the maintenance task.Leave this field blank if the material requirement is not associated with a specific task.

1. For Agreement Services, Quotes, and Work Orders only:

1. In the Serviceable Item field, enter the serviceable item associated with this material requirement or press F4 to select from a list of valid serviceable items.Leave this fieldLeave this field blank if this material requirement is not associated with a serviceable item.

1. To enter a part type:

1. In the Part Type field, enter a part type for the material requirement or press F4 to select from a list of valid SM part types.

1. To enter a material:

1. Leave the Part Type field blank.

1. In the Material field, enter the material for this material requirement or press  F4 to select from a list of valid HQ materials.

1. In the UM field, accept the default unit of measure or enter a new unit of measure for the selected material. Press F4 to select from a list of valid HQ materials.

1. In the Matl Qty field, enter the quantity of the material for this material requirement.

1. Save the record.

1. For Agreement Services, Quotes, and Work Orders only:

1. In the Cost Rate field, accept the default cost rate or enter a new cost rate. For information about how the cost rate defaults, see the [F1](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-smrequiredmaterial-form#ID-000416f0--en) help.

1. In the Cost ECM field, accept the defaulted cost ECM or select a new ECM to represent the cost rate quantity. Changes to the Cost ECM will update the Cost Total.

1. In the Cost Total field, accept the default amount. You can change this amount if applicable and the system will update the Cost Rate.Note: If this material line is for a Time and Material scope or a Time of Service, Rate Template agreement service, the system automatically calculates the Billing Rate and Total Billable; these amounts cannot be changed. For information about the billing rate default, see [Material: Billing Rate](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-smrequiredmaterial-form#ID-00041704--en).

1. If the material for this sequence is taxable, use the Tax Type, Tax Code, and Tax Basis fields to enter tax information as applicable.

1. Save the record.

Related information

- [SM Class Maintenance Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-class-maintenance-form)

- [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form)

- [SM Work Order Quotes Form](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
