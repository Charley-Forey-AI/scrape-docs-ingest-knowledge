---
title: "Field Definitions: SM Service Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-sm-service-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-sm-service-form"
---

# Field Definitions: SM Service Form

The following is a list of field descriptions for the SM
 Service form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Service Seq

Enter N, New, or + to have the system automatically assign
 the next available service sequential number.

## Description

Enter a description of the service for this agreement, up to 60 characters.

## Service Site

Enter the service site for which this service will be performed. Must be a valid, active service site for the specified customer.
If multiple service sites will receive this same service, you must set them up as a separate service sequence.
Note: Once you activate an agreement, this field is disabled and cannot be edited.

## Assigned Tech

Enter the technician for this agreement service (generally the technician most qualified to handle the work associated with this agreement service). If this technician is Active in SM Technicians and PR Employees, the system will automatically create a single trip on work orders generated from this agreement service, with this technician designated. In addition, this technician will be assigned as the Lead Tech on the work order.
If you leave this field blank, the system will not automatically create trips for work orders generated from this agreement service. Additionally, it will assign the primary technician designated for the service site as the Lead Tech on the work order.

## Call Type

Required.
Enter the call type (from SM Call Types) for this service. Must be an active call type. When generating preventative maintenance work orders for this service, the work order scope will automatically default this call type. May not be overridden.
 This field defaults as follows:

- If you did not set up call type coverage for the agreement type associated with the agreement (in SM Agreement Types), this field defaults as blank.

- If you set up call type coverage and selected the
 Planned checkbox for a single call type only, this field defaults the
 planned call type.

- If you set up call type coverage and selected the
 Planned checkbox for multiple call types or did not select the
 Planned checkbox for any call types, this field defaults as blank.

You are not initially required to enter a call type for services; the system will allow you to save service records without one. However, you must assign a call type to all services defined on the work schedule in order to activate the agreement.
Note: Once you activate an agreement, this field is disabled and cannot be edited.

## Service Center

Enter the service center to use when performing this service or leave blank to use the service center assigned to the service site designated for this agreement service. Must be an active service center.
If no service center is assigned to the service site, the service center specified for the customer will be used.

### For Periodic Services Only

If you selected the Post Revenue to Service
 Center Department checkbox for this agreement service, entry in this
 field is required. When this service is billed, the system will post the revenue to the
 department assigned to this service center.
Note: If you also enter a Division for this service, the
 system will post revenue to the division's "alternate department", if one is
 specified.
If you did not select the Post Revenue to Service
 Center Department checkbox, entry in this field is optional, and is used
 only to designate the service center performing the service. Billing revenue for the
 service will be posted to the department designated for the agreement type specified for
 the agreement.

## Division

This field is enabled only if you entered a
 service center in the Service Center field.
Enter the default service center division for
 this agreement service. Typically, this will be the division that will handle the work
 associated with this service. Press F4 for a list of valid divisions for the
 specified service center.
When you generate a work order (via SM Generate PM Work Orders), the related work order scope will automatically default this division. May be overridden.
Note: If you selected the Post Revenue to Service
 Center Department checkbox for this agreement service and you enter a
 division here, the system will post revenue to this division's "alternate department", if
 one is specified.

## Tax Source

From the drop-down menu, select whether to default the tax code for work completed equipment, labor, miscellaneous, inventory, or purchase lines associated with this service from the C - Service Center or the S - Service Site.
The tax source specified here will default as the Tax Source for the work order scope when generating work orders for this agreement/service (in SM Generate PM Work Orders).
Note: If no tax code is found for the specified location, the tax code will default as null for the work completed line.

## Pricing

The Pricing drop-down on the SM Service form, Info tab.
Specify the pricing method for this agreement service.
Required.

- I - Included in Agreement — The pricing for this service is included in the agreement price. No separate billing will occur. Work order scopes generated from services with this pricing method are assigned a price method of N - Non-Billable (in SM Work Orders).

- P - Periodic — The pricing for this service will be a flat amount that covers the term of the agreement. For example, if the agreement covers a 1-year period and the Price is $3,000, the customer will be charged a total of $3,000 for the year for this service. Work order scopes generated from services with this pricing method are assigned a price method of N - Non-Billable (in SM Work Orders).

- T - Time of Service — This pricing for this service will be either a Flat Rate or Rate Template method. Services of this type are billed separately through the work order.

- Flat Rate - Pricing for this type is a flat amount specified in the Price field. Work order scopes generated from services with this pricing method are assigned a price method of F - Flat Price in SM Work Orders.Note: The Flat Rate method requires that you break down revenue by cost type category. This is done in SM Flat Price Revenue, which is accessed by selecting the Split button. For more information, see [Enter Flat Price Revenue](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue).

- Rate Template - Pricing for this type is derived using a rate template. Work orders scopes generated from services with this pricing method are assigned a price method of T - Time and Materials in SM Work Orders.

Note: Once you activate an agreement, this field is disabled and cannot be edited.

## Time of Service Method

This field is only enabled when the service
 has Pricing method of T-Time of Service.

- Flat Rate - Select this option if you will always charge the same price (indicated to the right) for this service.

- Rate Template - Select this option to use a rate template (indicated to the right) to determine pricing for this service.
Note: Once you activate an agreement, this field is disabled and cannot be edited.

## Price

This field displays only when using the Periodic or Time of Service pricing method.
Enter the amount to charge the customer for this service. The pricing method determines how the service price is represented.

- P-Periodic- The price covers the term of the agreement (i.e. the period indicated by the Effective and Expiration dates). For example, if the price is $10,000 and the agreement is for 2 years, the customer will be charged a total of $10,000 for the 2-year period.

- T-Time of Service, F-Flat Rate - Using the example price above, the customer will be charged $10,000 each time the service is performed. Charges will be billed at time of service via the work order rather than with the agreement billing.Note: For Flat Rate services, if you leave the Price blank, the Split button is disabled.

- T-Time of Service, Rate Template - The amount specified for this pricing method is an estimate only. It does not affect the agreement price; however, it is included in the Est. Service Revenue amount. The amount specified here will be based on the agreement term and the number of scheduled visits. For example, if you specify an amount of $100 and the schedule is monthly for a term of one year, the calculated amount added to the Est. Service Revenue will be $1200.

This amount is currently used for reporting purposes only.
Note: Once you activate an agreement, this field is disabled and cannot be edited.

## Billing Reduction

This field only displays for agreement services with a pricing method of Periodic.
Enter the amount by which to reduce the remaining amount to bill. Do not enter as a negative number, as this number is already assumed negative.
The amount entered here updates the Total Remaining and Billing Reduction amounts as follows:

- Periodic Services Billed with the Agreement - For these services, this amount updates the Total Remaining and Billing Reduction amounts for the agreement (shown when the Billing Schedule tab is selected for the agreement). If the Total Remaining was previously 0.00, entry in this field will produce a negative Total Remaining value. For example, if you 200.00 here, the agreement's Total Remaining will be -200.00. You will need to adjust the agreement's Billing Schedule until the Total Remaining is 0.00.

- Periodic Services Billed Separately - For these services, this amount updates the Total Remaining and Billing Reduction amounts for the agreement service (shown when the Billing Schedule tab is selected for the agreement service); it does not update the agreement's Total Remaining and Billing Reduction amounts. If entry in this field will produce a negative Total Remaining value, you will need to adjust the Billing Schedule for the agreement service until the Total Remaining is 0.00.

## Post Revenue to Service Center Department

This field only displays for services with a pricing method of Periodic.
Select this checkbox to post revenue (from billings) for this agreement service to the service center department. When selected, entry in the Service Center field is required.
Do not select this checkbox if revenue should be posted to the department assigned to the agreement's designated agreement type.

## Billed Separately

Enabled only for services with periodic
 pricing (i.e. the Pricing option is set to P-Periodic).
Check this box to bill this service separately from the periodic billing for the associated agreement.
Leave this box unchecked to include this service in the periodic billing for the associated agreement.

## Rate Template

This field is only enabled when the service
 has a Pricing method of T-Time of Service.
Required.
Enter the rate template for this service. Must be an active template. This template will be used to determine equipment, labor, and material rates when creating work orders for this service.
Note: The rate template specified here cannot be overridden on work orders.

## Auto Schedule Trip

Auto Schedule Trip checkbox on the Schedule tab of the SM Service form.

Select this checkbox to automatically schedule a trip (on the SM Dispatch Board) when a PM Work Order is created for this agreement service.
Leave this checkbox unselected if you do not want trips auto-scheduled for this agreement service.
This checkbox automatically defaults the setting applied to the Auto Schedule Trip checkbox on the SM Agreements form. If you select or deselect this checkbox at the agreement level after this agreement service was created, you will be prompted to update existing services. If you select Yes, this checkbox is automatically updated based on the setting of the agreement checkbox. If you select No, the setting here remains intact, but can be overridden as needed.
Note: Auto-scheduled trips will default to the date and technician specified on the SM Service form.

## Separate Work Order

The Separate Work Order checkbox on the SM Service form, Info tab.
Select this checkbox to always create a separate work order for this agreement service when running SM Generate PM Work Orders.
Note: If you select this checkbox and have also selected the Separate Scope Per Service Item checkbox for the agreement (in SM Agreements, Info tab), the system will still generate a separate work order for this service. Only services not flagged for separate work orders will be set up as separate scopes on a single work order.

Do not select this checkbox if you want to combine this service on a single work order/scope with other services not flagged for separate work orders that have the same service site, service center, pricing method (and rate template, if applicable), call type, and schedule date. If other services with matching criteria are not available at the time of work order generation, a separate work order will be created for this service.
Note: The system may add services to an existing work order scope if the work order has a status of New and meets the criteria specified above.

## Matl Tax Override

The Matl Tax Override drop-down on the SM Service form.

This field defaults the Matl Tax Override option specified for the agreement in SM Agreements. If the Matl Tax Override field is blank for the agreement, this field defaults the Matl Tax Override option specified for the Call Type assigned to this agreement service. If the call type option is blank, this field defaults as blank.
Select the default tax type to use for material-related work completed
 lines associated with this agreement service.

- Blank – Use the standard tax type defaulting behavior. For taxable material-related work completed lines, the tax type defaults as Sales. For non-taxable material-related work completed lines, the tax type defaults as blank.

- N - No Tax – Default the tax type as "blank" for material-related work completed lines.

- S - Sales Tax Only – Default the tax type for taxable material-related work completed lines as Sales (US) or VAT (AU/CA).

- U - Use Tax Only (US companies only) – Default the tax type as Use for taxable material-related work completed lines.

The option you select here will be used as the default Matl Tax Override for work order scopes associated with this agreement service.
Note: If you amend or renew this agreement/agreement service, the value in this field remains the same; however, you can override the value as needed.

## Tax Option Override

The Tax Option Override drop-down on the SM Service form, Info
 tab.

This field defaults as the [Tax Option Override](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form/field-definitions-sm-agreements-form#concept-g0232ikc--en) specified for
 the agreement (in SM Agreements) or as blank if no override was defined for the
 agreement.
You can either accept the defaulted value or choose one of the overrides listed below.
 Options selected here will default on the work order scopes generated from this
 agreement service.
If you leave this field blank, the Tax Option Override on work order scopes generated
 from this service will default as blank. You can override the default at the work order
 scope level or leave it blank to use the Tax Option defined for the Call Type specified
 on the work order scope.
Note: Entering or changing the Call Type for this agreement
 service will not affect the value in this Tax Option Override
 field.

Note: Services with a pricing method of I-Included in Agreement or
 P - Periodic will
 generate Non-Billable work order scopes. Services with a pricing method of
 Time of Service,
 Flat Rate will
 generate Flat Price work order scopes. Work completed lines posted to Non-billable
 and Flat Price scopes are flagged as Non-Billable and therefore will only allow
 applying cost tax (that is, taxes applied at the time of purchase). If you select a
 Tax Option Override option other than N-Not Taxable or P-Taxable at Purchase Only for these services, the system ignores
 the "tax at billing" portion on the related work order.

- N - Not Taxable - Do not apply taxes at the time of purchase or billing. The cost and billing tax types and tax codes default as blank, regardless of whether the SM cost type specified for the work completed line is taxable. You may override the defaults as needed.

- P - Taxable at Purchase Only - Apply taxes at the time of purchase only. If the cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope and the Cost Tax Code defaults from the service site or service center depending on the Tax Source defined for the work order scope. The billing tax type and billing tax code default as blank. If the cost type is not taxable or no cost type is specified, all tax fields default as blank. You may override as needed.

- B - Taxable at Billing Only - Apply taxes at the time of billing only. If the line's cost type is taxable, the billing tax type and billing tax code default to the Tax Type and Tax Code specified for the work order scope. The Cost Tax Type and Cost Tax Code default as blank. If the cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.

- M - Taxable at Purchase/Markup at Billing - Apply taxes at the time of purchase and also apply taxes to the markup amount at the time of billing. If the line's cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope and the Cost Tax Code defaults from the service site or service center depending on the Tax Source defined for the work order scope. The billing tax type and tax code default to the Tax Type and Tax Code specified for the work order scope; however, the tax basis defaults the markup amount only. If the line's cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.Note: For taxable purchases, the bill tax basis is reduced by the amount that was previously taxed at the time costs were recorded. If you did not capture taxes when recording costs, there is no credit to apply to the transaction at billing; therefore, the bill tax basis is calculated using the full billing subtotal, not just the markup.

- F - Full Tax at Purchase and Billing - Apply tax fully at time of purchase and at time of billing. If the line's cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope, and the Cost Tax Code defaults from the service site or service center, depending on the Tax Source defined for the work order scope. The billing tax type and billing tax code default to the Tax Type and Tax Code specified for the work order scope, and the tax basis defaults the full billable amount. If the line's cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.

Note: If you amend or renew this agreement/agreement service, the value in this field remains the same; however, you can override the value as needed.

## Cost Revenue Margin

The Cost Revenue Margin field on the SM Service form, Info tab.

This field displays only for Flat Price agreement services.
Enter the expected margin percentage to apply when recognizing revenue for work orders generated from this flat price agreement service. If no margin applies, enter 0.00.

## Derive

Select this checkbox to calculate the budget values (labor hours, cost total, pricing total, and profit) for the agreement service based on the detailed cost estimates from the Material, Equipment, Labor, and Misc tabs.
Note: If you have entered summarized cost estimates in SM Service Detail (accessed via the Detail button), selecting this checkbox will not affect those entries.
Do not select this checkbox if you want to calculate budget values using the summarized cost estimates entered in SM Service Detail (accessed by clicking the Detail button).
 For detailed information about how the system updates the budget values, see [About Service Budgets](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/about-agreement-service-budgets).

## Contact Before Scheduling

Check this box if the customer requires that you contact them before scheduling this service.
Leave this box unchecked if the customer does not require that you contact them before scheduling this service.

## Due

From the drop-down menu, select the 'due' type:

- 1-Due On — Select this option if this service will be due on a
 specific date.

- 2-Due By — Select this option if this service will be due by a
 specific date.

- 3-Due Within — Select this option if this service will be due
 within a specified date range (based on the number of days indicated in the Days field
 (to the right).

When generating preventative maintenance work orders, the system defaults the selected option on the work order scope and uses it in conjunction with the schedule pattern to determine a due date for the specified service.

## Days

This field is enabled only if you selected 3-Due Within as the Due option.
Enter a number to represent the number of days in the 'due within' range (e.g. due within 30 days).
The system will use this number when generating preventative maintenance work orders for this service, in conjunction with the recurrence pattern specified below, to determine the beginning/ending days in a 'due within' range on the work order scope.

## Recurring Pattern

Specify when the service will occur by selecting the appropriate radio button.

- Task Scheduled - Select this option to define a task scheduling frequency. The screen displays an additional field for specifying a frequency code.

Note: You will use this option when you want to [set up a task schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling/set-up-an-agreement-task-schedule) for the agreement that will include the selected agreement service. For more information about task schedules, see [SM Agreement Task Schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-task-schedule-form).

- Daily - Select this option to define a daily frequency. The screen displays additional options to allow defining the daily recurrence pattern.

- Weekly - Select this option
 to define a weekly frequency. The screen displays additional options to allow
 defining the daily recurrence pattern.

- Monthly (default) - Select this option to define a daily frequency. The screen displays additional options to allow defining the daily recurrence pattern.

- Yearly - Select this option to define a daily frequency. The screen displays additional options to allow defining the daily recurrence pattern.

 Once you select the frequency option, the screen displays additional options related to that frequency to allow defining the recurrence pattern.

## Frequency

Enter a frequency code to indicate how often
 this service will be performed (e.g. weekly, monthly, etc.). Press F4 for a list
 of valid frequency codes.
Note:The frequency code specified here is informational
 only. You will [set up the actual task schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling/set-up-an-agreement-task-schedule) in SM Agreement Task
 Schedule.

## Recurrence: Daily

Specify the daily recurrence pattern.

- Every _____ day(s)

If you select this option, use the Days field (to
 the right) to specify the number of days (e.g. Every 30 days).

- Every weekday

## Recurrence: Weekly

Using the Recurs every _____ week(s) on field,
 enter how many weeks between services. Then check the box for each day of the week on which
 the service will be performed.
Example:

## Recurrence: Monthly

Specify the monthly recurrence pattern.
Option 1

1. In the first text box, enter the day of the month.

1. In the second text box, enter the number of months.

1. Example:
Option 2

1. From the first drop-down, select one of the following options to represent the day number:

- 1-First

- 2-Second

- 3-Third

- 4-Fourth

- 5-Last

1. From the second drop-down, select one of the following options to represent the day:

- 1-Day

- 2-Weekday

- 3-Weekend Day

- 4-Sunday

- 5-Monday

- 6-Tuesday

- 7-Wednesday

- 8-Thursday

- 9-Friday

- 10-Saturday

1. In the text box, enter the number of months.

1. Example:

Option 3

1. From the first drop-down, select one of the following options to represent the day number:

- 1-First

- 2-Second

- 3-Third

- 4-Fourth

- 5-Last

1. From the second drop-down, select one of the following options to represent the day:

- 1-Day

- 2-Weekday

- 3-Weekend Day

- 4-Sunday

- 5-Monday

- 6-Tuesday

- 7-Wednesday

- 8-Thursday

- 9-Friday

- 10-Saturday

1. Check the box next to each month in which the service will occur.
Example:

## Recurrence: Yearly

Specify the yearly recurrence pattern.
Option 1
Recurs every _____ year(s):

1. Using the Recurs every _____
 year(s) field, enter how many years between services.

1. From the drop-down, select one of the following options to represent the month:

- 1-January

- 2-February

- 3-March

- 4-April

- 5-May

- 6-June

- 7-July

- 8-August

- 9-September

- 10-October

- 11-November

- 12-December

1. In the text box, enter the day of the specified month.

1. Example:

Option 2
Recurs every _____ year(s):

1. Using the Recurs every _____
 year(s) field, enter how many years between services.

1. From the first drop-down, select one of the following options to represent the day number:

- 1-First

- 2-Second

- 3-Third

- 4-Fourth

- 5-Last

1. From the second drop-down, select one of the following options to represent the day:

- 1-Day

- 2-Weekday

- 3-Weekend Day

- 4-Sunday

- 5-Monday

- 6-Tuesday

- 7-Wednesday

- 8-Thursday

- 9-Friday

- 10-Saturday

1. From the third drop-down, select one of the following options to represent the month:

- 1-January

- 2-February

- 3-March

- 4-April

- 5-May

- 6-June

- 7-July

- 8-August

- 9-September

- 10-October

- 11-November

- 12-December

Example:

## Total Remaining

The system displays an amount in this field based on the total price of the agreement service. If a billing schedule has already been entered, this amount should be 0.00.
The Billing Reduction field (below) allows you to reduce the amount remaining to bill for the agreement service; however, you can also reduce the amount to bill by entering the total amount to bill in this field.
 For example, if the defaulted Total Remaining
 is 2500.00 and you want to reduce that amount by $500, enter 2,000.00 in
 this field and the system will automatically update the Billing
 Reduction field by the reduction amount (in this case, $500).
 If the defaulted Total Remaining is 0.00
 (e.g. this is an amendment that did not add additional pricing to the agreement service),
 but you want to reduce the remaining amount to bill by 500.00, enter -500.00 in this
 field. The system will update the Billing Reduction field to $500.
Note: The Total Remaining amount should always equal 0.00 when a billing schedule exists. If a billing reduction results in a Total Remaining amount that is less than or greater that 0.00, you will need to adjust the billing schedule until the Total Remaining equals 0.00.

## Task

The Task field on the SM Work Orders form, scope Tasks tab.
Enter N or + to add a new task. The system
 automatically assigns the next available sequence number.
Note: For work orders generated from an agreement (via SM Generate PM Work Orders) or work order quote (in SM Work Order Quotes), this field defaults from the agreement service or work order quote task and is disabled.

## Standard Task

The Standard Task field on the SM Work Orders form, scope Tasks tab.
Enter the standard task associated with this
 task sequence. Press F4 for a list of valid standard
 tasks.
Leave this field blank if this task is not associated with a standard task.
Note: For work orders generated from an agreement (via SM Generate PM Work Orders) or work order quote (in SM Work Order Quotes), this field defaults from the agreement service or work order quote task and is disabled.

## Task Name

The Task Name field on the SM Work Orders form, scope Tasks tab.
Required.
Enter a name for the task, up to 60 characters. If you specified a standard task for this task, the field defaults the task name from SM Standard Tasks. Overriding the task name here will not affect the standard task name.
Note: For work orders generated from an agreement (via SM Generate PM Work Orders) or quote (in SM Work Order Quotes), this field defaults from the service or quote task and is disabled.

## Task Description

The Task Description field on the SM Work Orders form, scope Tasks tab.
Enter a description of this task (character allowance is virtually unlimited). If you specified a standard task for this task, the field defaults the description from SM Standard Tasks.
Note: For work orders generated from an agreement (via SM Generate PM Work Orders) or quote (in SM Work Order Quotes), this field defaults from the service or quote task and is disabled.

## Serviceable Item

The Serviceable Item field on the SM Work Orders form, scope Tasks tab.
Enter the serviceable item to which this task
 applies. Press F4 for a list of serviceable items for the service site associated with the
 work order quote or work order.
Tip: You can set up a serviceable item on the fly by
 pressing F5 from this field. Once set up, you can reference the serviceable item
 here.
Leave this field blank if this task is not associated with a serviceable item.
Note: For work orders generated from an agreement (via SM Generate PM Work Orders) or quote (in SM Work Order Quotes), this field defaults from the service or quote task and is disabled.

## Class

The Class field on the SM Work Orders form, scope Tasks tab.
Required if you will be specifying an
 equipment type in the Type field.
Enter the class of equipment to which this
 task applies. Press F4 for a list of valid classes.
Leave this field blank if this task does not apply to a piece of equipment.
Note: This field is disabled if:

- you entered a serviceable item for this task. Defaults from SM Serviceable Items.

- this task is for a work order scope generated from an agreement (via SM Generate PM Work Orders) or a quote (in SM Work Order Quotes). Defaults from the agreement service or quote sequence.

## Type

The Type field on the SM Work Orders form, scope Tasks tab.
Entry in this field requires that you first
 enter the equipment class in the Class field.
Enter the equipment type. Press F4 for a list
 of valid equipment types for the specified equipment class.
Leave blank if this task does not apply to a piece of equipment.
Note: This field is disabled if:

- you entered a serviceable item for this task. Defaults from SM Serviceable Items.

- this task is for a work order scope generated from an agreement (via SM Generate PM Work Orders) or a quote (in SM Work Order Quotes). Defaults from the agreement service or quote sequence.

## Manufacturer

The Manufacturer field on the SM Work Orders form, scope Tasks tab.
Enter the manufacturer for the specified equipment class/type, up to 20 characters. Leave blank if you do not know this information or if this task does not apply to a piece of equipment.
Note: This field is disabled if:

- you entered a serviceable item for this task. Defaults from SM Serviceable Items.

- this task is for a work order scope generated from an agreement (via SM Generate PM Work Orders) or a quote (in SM Work Order Quotes). Defaults from the agreement service or quote sequence.

## Model

The Model field on the SM Work Orders form, scope Tasks tab.
Enter the model number for the specified equipment class/type, up to 60 characters. Leave blank if you do not know this information or if this task does not apply to a piece of equipment.
Note: This field is disabled if:

- you entered a serviceable item for this task. Defaults from SM Serviceable Items.

- this task is for a work order scope generated from an agreement (via SM Generate PM Work Orders) or a quote (in SM Work Order Quotes). Defaults from the agreement service or quote sequence.

## Serial Number

The Serial Number field on the SM Work Orders form, scope Tasks tab.
Enter the serial number for the specified equipment class/type, up to 60 characters. Leave blank if you do not know this information or if this task does not apply to a piece of equipment.
Note: This field is disabled if:

- you entered a serviceable item for this task. Defaults from SM Serviceable Items.

- this task is for a work order scope generated from an agreement (via SM Generate PM Work Orders) or a quote (in SM Work Order Quotes). Defaults from the agreement service or quote sequence.
