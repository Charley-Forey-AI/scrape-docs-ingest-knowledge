---
title: "Field Definitions: SMRequiredEquipment Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-smrequiredequipment-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-smrequiredequipment-form"
---

# Field Definitions: SMRequiredEquipment Form

The following is a list of field descriptions for the
 SMRequiredEquipment form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Equipment: Seq

Enter N, New, or +. The system will auto-generate a
 sequence number for the requirements entry.
Note: For class maintenance tasks, agreement services, work order quotes, or work orders defaulting requirement records from a standard task (assigned on the Tasks tab), this field cannot be edited. However, you can add new requirement records.

## Equipment: Task

Enter the task associated with this
 requirements entry or leave blank if this requirements entry is not related to a task.
 Press F4 for a list of valid tasks (those set up on the Tasks tab).
Note: For class maintenance tasks, agreement services, work order quotes, or work orders defaulting requirement records from a standard task (assigned on the Tasks tab), this field cannot be edited. However, you can add new requirement records.

## Equipment: Serviceable Item

Enter the serviceable item for this equipment
 requirement or press F4 to select from a list of serviceable
 items for the service site associated with the agreement service, work order quote, or work
 order.
 Leave this field blank if this equipment requirement is not associated with a serviceable item.
This field defaults as blank except when one of the following conditions applies:

- If you manually entered this equipment requirement
 and you specified a task (in the Task field), this field defaults
 the serviceable item from the task (if applicable). You may override the default as
 applicable.

- If this equipment requirement was auto-added to a work order from an agreement or quote, this field defaults the serviceable item from the agreement service or quote equipment requirement. Default may be overridden if needed.

Tip: You can set up a serviceable item on the fly by
 pressing F5 from this field. Once set up, you can reference the serviceable item
 here.

## Equipment: EMCo

Enter the EM company for this requirements entry. This will be the company in which the equipment category associated with this line resides. Initially defaults the EM Co specified in SM Company Parameters for the active SM company.
Note: Class Maintenance, Agreement Services, Work Order Quotes, and Work Orders only:
Note: For requirement entries auto-populated from a standard task (assigned on the Tasks tab), this field will automatically default as defined for the requirements record in SM Standard Tasks (if applicable). Default may be overridden.

## Equipment: Category

Enter the category of equipment for this
 requirements entry. Press F4 for a list of valid equipment
 categories for the specified equipment company.
Note: Class Maintenance, Agreement Services, Work Order Quotes, and Work Orders only:
Note: For requirement entries auto-populated from a standard task (assigned on the Tasks tab), this field will automatically default as defined for the requirements record in SM Standard Tasks (if applicable). Default may be overridden.

## Equipment: Equip Qty

Enter the quantity of equipment (within the specified category) that will be needed to complete the work.
Note: Class Maintenance, Agreement Services, Work Order Quotes, and Work Orders only:
Note: For requirement entries auto-populated from a standard task (assigned on the Tasks tab), this field will automatically default as defined for the requirements record in SM Standard Tasks (if applicable). Default may be overridden.

## Equipment: Rev Code

Enter the revenue code for this requirements
 entry. Press F4 for a list of valid revenue codes for the equipment category.
Note: Class Maintenance, Agreement Services, Work Order Quotes, and Work Orders only:
Note: For requirement entries auto-populated from a standard task (assigned on the Tasks tab), this field will automatically default as defined for the requirements record in SM Standard Tasks (if applicable). Default may be overridden.

## Equipment: Rev Code Qty

Enter the number of units for the specified revenue code (e.g. if the revenue code is Hours, enter the number of hours).
Note: Class Maintenance, Agreement Services, Work Order Quotes, and Work Orders only:
Note: For requirement entries auto-populated from a standard task (assigned on the Tasks tab), this field will automatically default as defined for the requirements record in SM Standard Tasks (if applicable). Default may be overridden.

## Equipment: Cost Rate

This field defaults the rate for the specified category/revenue code from EM Revenue Rates by Category. You may override the default for work orders only; for work order quotes, this field is disabled.

## Equipment: Cost Total

This field defaults the total cost for this requirements line and cannot be edited.

## Equipment: Billing Rate

This field only displays for work order and work order quote scopes with a Time and Materials pricing method, and agreement services with a Time of Service, Rate Template pricing method.
Display only, the billing rate for the selected required equipment sequence. Rate defaults as a calculation of the cost rate x the equipment markup defined on the template associated with the agreement service, work order quote scope, or work order scope.
Note: The system uses a specific hierarchy to determine the equipment rates to use for calculating billable rates. For more information, see [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy).

## Equipment: Total Billable

This field only displays for work order and work order quote scopes with a Time and Materials pricing method and agreement services with a Time of Service, Rate Template pricing method.
Display only, the total billable for this required equipment sequence.

## Equipment: Tax Type

Tax Type field on the Equipment tab of the following forms: SM Service, SM Work Order Quotes, and SM Work Orders.
This field only displays for work order quotes and customer work orders with a pricing method of T-Time and Material, and for agreement services with a pricing method of T-Time of Service, Rate Template.
If the equipment required for the quote, work order, or agreement service is taxable, specify the tax type:

- 1 - Sales

- 3 - VAT

## Equipment: Tax Code

Tax Code field on the Equipment tab of the following forms: SM Service, SM Work Order Quotes, and SM Work Orders.
This field only displays for work order quotes and customer work orders with a pricing method of T-Time and Material, and for agreement services with a pricing method of T-Time of Service, Rate Template.
Enter the tax code to use for calculating the tax amount for this equipment sequence. This field initially defaults the tax code for the Service Site or Service Center, depending on the Tax Source specified for the quote, work order, or agreement service. If no tax code is specified for the service site or service center, defaults as blank.

## Equipment: Tax Basis

Tax Basis field on the Equipment tab of the following forms: SM Service, SM Work Order Quotes, and SM Work Orders.
This field only displays for work order quotes and customer work orders with a pricing method of T-Time and Material, and for agreement services with a pricing method of T-Time of Service, Rate Template.
Enter the taxable portion of the total amount for this equipment sequence or accept the default amount (defaults from Total Billable).
