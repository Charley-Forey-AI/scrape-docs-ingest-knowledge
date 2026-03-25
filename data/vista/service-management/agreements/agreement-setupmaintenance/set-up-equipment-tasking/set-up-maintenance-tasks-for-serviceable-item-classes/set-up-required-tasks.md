---
title: "Set up Required Tasks | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes/set-up-required-tasks"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes/set-up-required-tasks"
---

# Set up Required Tasks

Required tasks represent items of work that you need to complete for a scope of work. For example, when you change the oil in a car, tasks might typically include draining the old oil, putting in a new filter, and adding the new oil.
You can set up required tasks for serviceable item class maintenance, work order quotes, agreement services, and/or work orders. In addition, you can associate tasks with material, labor, equipment, and miscellaneous requirements by referencing the task on the related requirements tabs.
If you set up a task that references a standard task, any equipment, labor, and material requirements that have been defined for the standard task (in SM Standard Tasks) will be set up automatically for the class maintenance task, agreement service, work order quote, or work order. If miscellaneous requirements also exist for the standard task, they will be handled as follows:

- Work Order Quotes & Agreement Services - The system will set up corresponding miscellaneous requirements for the quote or agreement services.

- Work Orders - The system creates a miscellaneous work completed line for each miscellaneous requirement and assigns it a status of Provisional.

- Class Maintenance - Miscellaneous requirements are currently not used.

Click on the following links for information about setting up required tasks.
Setting up Required Tasks for Serviceable Item Class Maintenance
The following instructions assume that you have already [set up maintenance tasks for the serviceable item class/type](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes) in SM Serviceable Item Class. If you have not, you will need to do so before you can set up required tasks.

1. Open the SM Serviceable Item Class form.

1. In the Class field, enter the serviceable item class or press F4 to select from a list of valid classes.

1. Click the Maintenance tab and then double-click in the grid to open the SM Class Maintenance form.

1. Click the Tasks tab.

1. In the Task field, enter N or + to add a new task. The system automatically assigns the next available sequence number.

1. In the Standard Task field, enter the standard task associated with this task or press F4 to select from a list of valid standard tasks.Leave this field blank if this task is not associated with a standard task.

1. In the Task Name field, enter the name of the task or accept the defaulted task name (only applies if you specified a Standard Task).

1. In the Task Description field, enter a description of the task or accept the defaulted task description (if you specified a Standard Task).

1. The Recommended checkbox automatically defaults as selected. Accept the default or clear the checkbox if this is not a recommended task.Note: Selecting this checkbox indicates that the task should be automatically included on the agreement when the class maintenance task is added. Tasks that are not marked as Recommended will be available to be included during the tasking process.

1. Save the record.

1. Repeat Steps 5-10 to enter additional tasks.

Setting up Required Tasks for Agreement Services
The following instructions assume that you have already [set up agreement services](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup) in SM Service. If you have not, you will need to do so before you can set up required tasks.

1. Open the SM Agreements form.

1. In the Agreement field, enter the agreement to work with (cannot be an active agreement) or press F4 to select from a list of agreements.

1. Click the Work Schedule tab.

1. In the Work Schedule grid, double-click on the service sequence to work with to open the SM Service form.

1. Click on the Tasks tab.

1. In the Task field, enter N or + to add a new task. The system automatically assigns the next available sequence number.

1. In the Standard Task field, enter the standard task associated with this task or press F4 to select from a list of valid standard tasks.Leave this field blank if this task is not associated with a standard task.

1. In the Task Name field, enter the name of the task or accept the defaulted task name (only applies if you specified a Standard Task).

1. In the Task Description field, enter a description of the task or accept the defaulted task description (if you specified a Standard Task).

If this task is associated with a serviceable item:

1. In the Serviceable Item field, enter the serviceable item to which this task applies or press F4 to select from a list of serviceable items for the service site.
 The system automatically defaults the serviceable item class and type, as well as the manufacturer, model number, and serial number, and disables these fields.

1. Save the record.

If this task is not associated with a serviceable item:

1. Leave the Serviceable Item field blank.

1. In the Class field, enter the equipment class or press F4 for a list of valid classes.
Leave the Class field blank if this task is not equipment-specific.

1. In the Type field, enter the equipment type or press F4 for a list of valid types for the specified class.
 Leave the Type field blank if you did not enter a class in the Class field or if you entered a class, but this task is not specific to a classification type.

1. In the Manufacturer field, enter the manufacturer of the equipment.
Leave the Manufacturer field blank if you do not know this information or if this task is not equipment-specific.

1. In the Model field, enter the model number.
 Leave the Model field blank if you do not know this information or if this task is not equipment-specific.

1. In the Serial Number field, enter the equipment serial number.
Leave the Serial Number field blank if you do not know this information or if this task is not equipment-specific.

1. Save the record.

1. Repeat Steps 6-10 to enter additional tasks.

Note: You can edit the required tasks for an agreement service as often as needed prior to activating the agreement. Once you activate the agreement, changes to the required tasks will require creating an amendment.
Setting up Required Tasks for a Work Order Quote
The following instructions assume that you have already [set up the work order quote/sequence](/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote) in SM Work Order Quotes. If you have not, you will need to do so before you can set up tasks.

1. Open the SM Work Order Quotes form.

1. In the Quote ID field,enter the work order quote to work with or press F4 to select from a list of valid work order quotes.

1. In the Seq field (lower section of form), enter the sequence to work with or press F4 to select from a list of quote sequences.

1. Click on the Tasks tab.

1. In the Task field, enter N or + to add a new task. The system automatically assigns the next available sequence number.

1. In the Standard Task field, enter the standard task associated with this task or press F4 to select from a list of valid standard tasks.Leave this field blank if this task is not associated with a standard task.

1. In the Task Name field, enter the name of the task or accept the defaulted task name (only applies if you specified a Standard Task).

1. In the Task Description field, enter a description of the task or accept the defaulted task description (if you specified a Standard Task).

If the task is associated with a serviceable item:

1. In the Serviceable Item field, enter the serviceable item to which this task applies or press F4 to select from a list of serviceable items for the service site.
 The system automatically defaults the serviceable item class and type, as well as the manufacturer, model number, and serial number, and disables these fields.

1. Save the record.

If the task is not associated with a serviceable item:

1. Leave the Serviceable Item field blank.

1. In the Class field, enter the equipment class or press F4 for a list of valid classes.
Leave the Class field blank if this task is not equipment-specific.

1. In the Type field, enter the equipment type or press F4 for a list of valid types for the specified class.
 Leave the Type field blank if you did not enter a class in the Class field or if you entered a class, but this task is not specific to a classification type.

1. In the Manufacturer field, enter the manufacturer of the equipment.
Leave the Manufacturer field blank if you do not know this information or if this task is not equipment-specific.

1. In the Model field, enter the model number.
 Leave the Model field blank if you do not know this information or if this task is not equipment-specific.

1. In the Serial Number field, enter the equipment serial number.
Leave the Serial Number field blank if you do not know this information or if this task is not equipment-specific.

1. Save the record.

1. Repeat Steps 5-9 to enter additional tasks.

Setting up Required Tasks for a Work Order
The following instructions assume that you have already [set up the work order/scope](/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders). If you have not, you will need to do so before you can set up tasks.

1. Open the SM Work Orders form.

1. In the Work Order field, enter the work order to work with or press  F4  to select from a list of work orders.

1. In the Seq field (lower section of form), enter the sequence to work with or press F4 to select from a list of work order sequences.

1. Click on the Tasks tab.

1. In the Task field, enter N or + to add a new task. The system automatically assigns the next available sequence number.

1. In the Standard Task field, enter the standard task associated with this task or press F4 to select from a list of valid standard tasks.Leave this field blank if this task is not associated with a standard task.

1. In the Task Name field, enter the name of the task or accept the defaulted task name (only applies if you specified a Standard Task).

1. In the Task Description field, enter a description of the task or accept the defaulted task description (if you specified a Standard Task).

If the task is associated with a serviceable item:

1. In the Serviceable Item field, enter the serviceable item to which this task applies or press F4 to select from a list of serviceable items for the service site.
 The system automatically defaults the serviceable item class and type, as well as the manufacturer, model number, and serial number, and disables these fields.

1. Save the record.

If the task is not associated with a serviceable item:

1. Leave the Serviceable Item field blank.

1. In the Class field, enter the equipment class or press F4 for a list of valid classes.
Leave the Class field blank if this task is not equipment-specific.

1. In the Type field, enter the equipment type or press F4 for a list of valid types for the specified class.
 Leave the Type field blank if you did not enter a class in the Class field or if you entered a class, but this task is not specific to a classification type.

1. In the Manufacturer field, enter the manufacturer of the equipment.
Leave the Manufacturer field blank if you do not know this information or if this task is not equipment-specific.

1. In the Model field, enter the model number.
 Leave the Model field blank if you do not know this information or if this task is not equipment-specific.

1. In the Serial Number field, enter the equipment serial number.
Leave the Serial Number field blank if you do not know this information or if this task is not equipment-specific.

1. Save the record.

1. Repeat to enter additional tasks.

Related information

- [SM Class Maintenance Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-class-maintenance-form)

- [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form)

- [SM Work Order Quotes Form](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [Set Up Equipment Requirements](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes/set-up-equipment-requirements)

- [Set up Labor Requirements](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes/set-up-labor-requirements)

- [Set up Material Requirements](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes/set-up-material-requirements)

- [Set Up Miscellaneous Requirements](/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/required-resources-for-work-orders/set-up-miscellaneous-requirements)
