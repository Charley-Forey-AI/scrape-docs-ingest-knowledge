---
title: "Set Up Equipment Tasking | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking"
---

# Set Up Equipment Tasking

Service Management's equipment tasking feature allows you to set up maintenance tasks for serviceable items and then use them to automatically generate services on an agreement.
You might typically use this feature if you have service maintenance tasks that are common to classes of equipment and that you perform on a regular basis (e.g. yearly, monthly, quarterly, etc.). For example, if you annually perform winter maintenance on all heating systems, you might set up a serviceable item class of HEAT EQUIP (in SM Serviceable Item Class), create a "winter" maintenance task for the HEAT EQUIP class (in SM Class Maintenance), and then assign the HEAT EQUIP class to all applicable serviceable items. Then when creating agreements for a customer/service site, you can use those maintenance tasks to automatically generate agreement services.
The following instructions provide an overview to setting up and using the equipment tasking feature. As you follow each of the steps, select the links to get more information on completing the step.

1. In SM Company Parameters, set the [Agreement Sync Options](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#ID-00042933--en). These options allow for automatic updates to agreement services and/or work order scopes when changes are made to serviceable items parts and/or class maintenance tasks, equipment, labor, and/or materials.

1. [Set up the frequency codes](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-frequency-setup-form) that will be used for task scheduling in SM Frequency Setup. Frequency codes identify how often a task is to be performed.

1. [Set up task groups](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-task-group-form). Task groups identify the crafts/classes needed when performing maintenance tasks. You will assign task groups to maintenance tasks when scheduling them in SM Agreement Task Schedule. The system uses task groups in conjunction with other information (such as call type and price method) to determine whether scheduled services on agreement can be grouped together on a work order/scope. Note: If you select the Separate Scope Per Service Item checkbox for an agreement in SM Agreements (Info tab), the work order generation process (SM Generate PM Work Orders) generates a separate work order scope for each service item rather than grouping them on the same work order scope.

1. [Set up serviceable item classes and types](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-serviceable-item-classifications) in SM Serviceable Item Class. Classes and types are used to identify the various classifications of equipment (serviceable items) that are maintained at each of your service sites. Each serviceable item that you set up requires a class and a type.

1. [Set up maintenance tasks](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes) by serviceable item class/type in SM Class Maintenance. Maintenance tasks will be used to auto-generate agreement services, so you must set up at least one maintenance task per class, with a minimum of one required task. Tasks that you want included automatically on an agreement should be flagged as Recommended.Note: You can also set up required resources (labor, materials, and equipment) as needed for each class maintenance task.

1. [Set up serviceable items for service sites](/en/vista/vista/service-management/service-management-setup/set-up-serviceable-items) in SM Serviceable Items, making sure to assign a class/type to each serviceable item that you want to include in equipment tasking.Note: Class maintenance tasks (Step 4) must be defined for the serviceable item's class or class/type in order to use the equipment tasking feature.

1. [Set up an agreement in SM Agreements](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-an-agreement-in-sm-agreements). Assign an Agreement Type that has Call Types set up under the Agreement Type Coverage tab. Do not activate the agreement.

1. [Auto-generate agreement services](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/auto-generate-agreement-services). With this step, you will auto-generate agreement services by selecting the appropriate serviceable items (in SM Maintenance Item Selection) and then indicating which tasks associated with each serviceable item are to be included on the agreement (in SM Agreement Maintenance).

1. [Schedule maintenance tasks](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling/set-up-an-agreement-task-schedule). Each agreement service that you generate will be flagged with a recurring pattern of Task Scheduled (on the Schedule tab of SM Service). In order to activate the agreement and to generate service dates, you must have at least one month scheduled (in SM Agreement Task Schedule) for each applicable service.

1. [Activate the agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-activation--deactivation-form). Once you activate the agreement, the system automatically generates a list of service dates based on the task schedules and displays them on the Work Orders tab of SM Agreements. The service dates can then be used to generate work orders.

Related information

- [SM Frequency Setup Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-frequency-setup-form)

- [SM Task Group Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-task-group-form)

- [SM Agreement Task Schedule Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-task-schedule-form)

- [SM Serviceable Item Class Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-serviceable-item-class-form)

- [SM Class Maintenance Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-class-maintenance-form)

- [SM Serviceable Items Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-serviceable-items-form)

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

- [Generate Preventative Maintenance Work Orders](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-the-work-order-generation-process/generate-preventative-maintenance-work-orders)
