---
title: "Equipment Management | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management"
---

# Equipment Management

Equipment Management provides full equipment management capabilities to help you manage both cost and revenue on your equipment.
For general contractors, it provides automatic billing and location tracking capabilities, as well as detailed cost and revenue reporting. For heavy/highway contractors, it provides the ability to set up detailed preventative maintenance schedules that work in conjunction with a powerful work order system.
Using Equipment Management, you can enter and process equipment work orders, timecards, equipment and fuel usage, cost adjustments, and cost allocations, as well as transfer components from one piece of equipment to another and/or equipment from one location to another, and track meter readings and equipment depreciation.
Equipment Management is fully integrated with other Vista™ modules (Payroll, Purchase Order, Inventory, Job Cost, Material Sales, and General Ledger) for single step data entry and updates.

- Equipment Revenue - Revenue is the usage of equipment as it is charged to jobs, other pieces of equipment, or overhead accounts. This involves assigning usage rates (such as hourly, daily, weekly, or standby usage rates) to pieces of equipment, and then posting usage time either in Payroll with the timecard of the person operating the equipment, or through EM’s Usage Posting or Automatic Usage programs. The extended dollars are then credited to the equipment as income while the job receives a direct cost of the same amount for the expense. Revenue is charged at revenue rates that are set up by category, but can be overridden by equipment. If you have special rates that are used for certain jobs, you can set up the special rates using job templates. For more information, see:

- [Basic Setup Steps](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/set-up-and-process-equipment-revenue)

- [Using Revenue Breakdown Codes](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-revenue-breakdown-codes)

- Component Tracking - Components are elements that are essential to the operation of a primary piece of equipment such as engines, transmissions, drive lines, and so forth. EM provides you with the ability to track the location and costs all of the components used on your equipment. See [Component Tracking](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/component-tracking) for more information.

- Attachments - Attachments are pieces of equipment that are “attached” to other pieces of equipment (e.g. a bucket attached to a backhoe or a trailer attached to a dump truck). See [Equipment Attachments](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-componentsattachments/about-equipment-attachments) for more information.

- Equipment Management Levels - Equipment Management is sold in two levels:

- Equipment Management - This level provides basic location tracking and transfer abilities. By setting up a database of all your equipment, you can track the location and movement of equipment and tools between jobs, shops, or other locations. Equipment can be designated as an attachment (buckets, plows, etc) to a primary piece of equipment so that when one is moved, the other is automatically moved with it. A component tracking feature also allows you to track the movement of components for a piece of equipment (engines, transmissions, drive lines, etc.). Costs incurred on the equipment can also be tracked, as well as the revenue earned by the equipment when charged to jobs, equipment, or overhead.

- Equipment Maintenance - This level provides an optional maintenance and work order system. You can set up detailed preventative maintenance schedules that include maintenance activities (oil & lube, tune-ups, etc.), parts required, and the estimated hours to perform each service. Work orders can be set up automatically by initializing based on items due for maintenance. Non-scheduled items can be entered on work orders manually.

- Depreciation - The Depreciation feature in EM provides you with the ability to set up equipment asset records so that the system will create and post depreciation entries to GL when you run the EM Depreciation Processing program. See [Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation) for more information.

- Overhead Allocation - EM’s Cost Allocations feature allows you to automatically allocate overhead and/or indirect costs to equipment, charging equipment cost accounts and crediting other specified accounts. Allocations can be run on a monthly basis, or for any other applicable time frame. See [Overhead Allocation](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-overhead-allocation) for more information.

- Meter Readings - You can use the [EM Meter Readings](/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-readings-form) form to record odometer and hour meter readings on equipment - for example if you want to include odometer/hour readings on reports, or accumulated hours and mileage on reports to determine statistics such as cost per hour and miles per gallon. Entering meter readings is generally used in conjunction with the scheduled maintenance. Because scheduled maintenance relies on the mileage and/or hours (of usage) posted to the equipment, the odometer and hour meter must be updated regularly in order for the system to know when scheduled maintenance is due on a piece of equipment. By comparing the ‘Last Done’ meter readings (in EM Standard Maintenance Groups) to the equipment’s current meter reading (EM Equipment), the system can determine if the equipment is due for service.

- Updates to the Equipment Master - The Reading Date and the New Readings entered in the Meter Readings program for both the Hour Meter and the Odometer will update corresponding fields in EM Equipment (Meters tab). When you are entering readings, if the equipment’s mileage or hours have changed since the last reading, enter the new readings to update EM Equipment. If the mileage or hours have not changed, but you want EM Equipment to be updated with the reading date, enter the old reading as the new reading and specify the reading date.

- Updates to the Meter Readings File - Each time you post a reading, the system will post the difference between the old reading and the new reading to the Meter Readings (EMMR) file. Even if the equipment has been idle, and therefore the mileage and/or hours have not changed since the last reading, by entering the “old” reading as the “new” reading, the Equipment Master will be updated with the reading date and create a zero-unit entry in the Meter Readings file. This way you will always have a record of all readings, no matter what the mileage or hours are. Additionally, by saving this mileage/hour data, you will have historical details that can be used to show:

- the total miles driven in a year

- the miles per gallon of fuel used (only if you are also recording the equipment’s fuel costs)

- the calculated revenue per mile

- Updating Meters During Transaction Posting - In addition to updating meters using EM Meter Readings, odometers and hour meters are also updated when posting equipment usage (in EM, MS, and PR), cost adjustments and parts (in EM), and fuel usage (EM). Updates are controlled by update options in EM Company Parameters. See [Meter Updates: Equipment Usage](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8af--en) for more information.

- Tracking Usage - In addition to tracking mileage, you have the option to track usage hours for each piece of equipment. See [Tracking Hours](/en/vista/vista/job-resources/equipment-management/equipment-meters/about-tracking-hours) for more information.

- Meter Replacement - At the time of meter replacement, [EM Equipment](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form) will contain the current readings of both the hour and mileage meters for the equipment. The initial reading on the new meter, along with the replacement date, should be entered in EM Equipment rather than in EM Meter Readings. By doing this, you are updating the meter reading without updating the actual miles or hours. Any subsequent readings on the new meter should be entered in [EM Meter Readings](/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-readings-form).Note: Odometers and hour meters are also updated when posting equipment usage, cost adjustments and parts , and fuel usage in EM. The system will include replaced meter reading values when updating the current total odometer and current total hours for the equipment; however, if the transaction's posted date occurs prior to the odometer and/or hour meter replacement date, the current total hours/odometer will exclude the replaced meter reading.

- Equipment Location Tracking and Transfers - You can transfer equipment from one location to another, and track equipment by location. Once equipment has been set up using the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form) form, you can track the movement of equipment and tools as it moves to jobs or separate locations on a job, or the shop, and yard. Equipment may be designated as being attached to another piece of equipment, so that when one is moved, the other is automatically moved with it. For more information, see [EM Location Transfer](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-location-transfer-form) .

- Checklists and Processing Logs - Workflow module - The Implementation Checklists and Processing Logs for this module are available in the Workflow module. To view the checklists and logs, use the WF Checklist Template form. For information on processing the checklists and logs, see the Workflow [Overview](/en/vista/vista/system-tools/work-flow). If you do not have the Workflow module, you can use the WF Templates report (VA Reports menu) to view or print the checklists and logs.
