---
title: "Field Definitions: EM Usage Posting Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-usage-posting-form/field-definitions-em-usage-posting-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-usage-posting-form/field-definitions-em-usage-posting-form"
---

# Field Definitions: EM Usage Posting Form

The following is a list of field descriptions for the EM
 Usage Posting form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 Enter the sequence number of an existing entry or enter N, New, or + to add a new sequence. The system will automatically assign the next available sequential number.

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

## Type

 Enter the transaction type for this equipment usage entry. Inputs required on the rest of the form for this transaction may vary depending on the transaction type selected here.   

- Job — Select this option to post usage to a specific job.

- Equipment — Select this option to post usage to another piece of equipment. For example if one piece of equipment was used to repair another piece of equipment.

- Work Order — Select this option to post usage to equipment on work orders.

- Expense — Select this option to post usage directly to a GL account.

##  Equipment

 Enter the equipment that was used or press
 F4
 to select one from a list.

## Revenue Code

Enter a revenue code or press F4 to select
 one from a list. The revenue code determines the usage rate for the entry.
Revenue codes are created and maintained using the [EM Revenue Codes ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-codes-form) form.

##  PR Co

 Specify the Payroll company (set up in PR Company Parameters) of the employee that operated this equipment.

##  Employee

 Enter the employee (from PR Employees) that operated this equipment. If entered, this will update EMRD (Revenue Detail), JCCD (JC Cost Detail) for jobs, and EMCD (EM Cost Detail) for equipment types.

##  JCCo

 This field is accessible only when Type is
 J-Job.
 Enter the JC company (set up in JC Company Parameters) to which you are posting usage.

## Job

 This
 field is accessible only when Type is J-Job.
Enter the job (set up in JC Jobs) to which you
 are posting usage. If you are restricting usage to the current job (option in EM
 Categories), the job specified here must be the job assigned to the equipment in EM
 Equipment.
Note: If you enter a soft- or hard-closed job, you can save the record only if you allow posting to hard and/or soft-closed jobs (flags in JC Company Parameters). Status for hard/soft closed jobs displays in red beside the sequence.

## Phase

 This field is accessible only when Type is
 J-Job.
Specify the phase (set up in JC Phases or JC
 Job Phases) to which you are posting this usage entry.

##  Cost Type

 This field is accessible only when Type is
 J-Job.
 Specify the cost type (set up for the job in JC Job Phases) to which you are posting this usage entry.

##  EMCo

 This field is accessible only when Type is
 E-Equipment.
 Specify the EM company (set up in EM Company Parameters) to which you are posting this usage entry.

## Equipment - Charged (Cost Equipment)

 Enter the equipment that is being charged for
 the usage or press F4 to select it from a list. This is the equipment that was used to repair
 another piece of equipment.
This field is enabled only when Equipment is
 selected in the Type field.

##  Comp Type

 This field is accessible only when Type is
 E-Equipment and if you allow posting costs to components for the equipment
 (flag in EM Equipment).
 Enter the component type (from EM Component Types) for this usage entry, if applicable.
Note: If components exist for the equipment being costed, entry here will provide a default of the first component defined for the equipment. However, you may skip this field and enter the component code directly; the component type will then automatically default here.

##  Component

 This field is accessible only when Type is
 E-Equipment and if you allow posting costs to components for the equipment
 (flag in EM Equipment).
 Enter the component (set up in EM Equipment)
 for this usage entry. Must be a valid component for the equipment specified above. If you
 entered a component type in the Comp Type field, defaults the first
 component (of the specified component type) on record for the equipment (in EM Equipment).
 You may override the default as necessary; the system will automatically update the
 component type (as defined for the new component) if necessary.

##  Work Order

 This field is accessible only when Type is
 W-Work
 Order.
 Specify the work order (set up in EM) to charge with equipment usage. Charging usage to a work order means that one piece of equipment was used to repair another piece of equipment. The work order is for the piece of equipment that is being repaired.

##  WO Item

 This field is accessible only when Type is
 W-Work
 Order.
 Specify the work order item to charge with equipment usage. This item must exist on the work order and will determine the cost code and cost type in the next fields.

## Field Ticket

The Field Ticket field on the EM Usage Posting form.
Enter the field ticket number for this equipment usage entry or press F4 to select from a list of valid field tickets for the specified job/contract.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to equipment usage for a job is only useful if the job's contract/contract item has a bill type of T&M or Both.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Description

Enter a description of the usage transaction. The value in this field can be up to 30 characters long.
The description will update the Memo column in the EM Revenue Detail (EMRD) table, and it displays on some reports (EM Monthly Cost and Revenue Drilldown, etc.).

## EM Cost Code

This field is accessible only when Type is
 E-Equipment or W-Work Order.
Enter the cost code to which this usage entry applies. Initially defaults as follows:

- If a work order entry, defaults the cost code specified for the work order item. May be overridden if allowing changes to the cost code for work orders (flag in EM Company Parameters, Work Orders tab).

- If an equipment entry and a component type/component specified, defaults the cost code assigned to the component type (in EM Component Types). If no component type/component specified, defaults as ‘null’.

## EM Cost Type

This field is accessible only when Type is
 E-Equipment or W-Work Order.
Enter the cost type to which this usage transaction applies.

##  Date

 Specify the actual date of the equipment usage. Most tables updated will have both an actual date and a posting date (the date entered in the Batch Processing form). If you want to report the actual date of the usage, it should be entered here.
 This date may update the equipment's odometer and/or hour meter reading dates (in EM Equipment) depending on the update option selected for equipment usage in EM Company Parameters.

## Offset Account

This field is enabled for:

- J-Job transaction types — Enabled when the
 Allow GL
 account override when posting costs checkbox is selected (in JC
 Company Parameters, GL Cost tab).

- E-Equipment or W-Work Order transaction types —
 Enabled when the Allow GL Account Override checkbox
 is selected (in EM Company Parameters).

- X-Expense transaction types — Always enabled.

Enter the offset account to charge for this usage entry. This account offsets the equipment revenue accounts. Initially defaults as follows:

- J-Job — Defaults the GL account designated (in JC
 Departments) for the specified cost type.

- E-Equipment or W-Work Order — Defaults the GL account designated (in EM Departments) for the specified cost code or cost type (if no override for cost code).

- X-Expense — Defaults as null. The account entered here must have sub ledger code of 'null'.

##  Odometer

 Enter the current odometer reading
 on the equipment.
Once the equipment usage is processed, this odometer will create a meter history record in [EM Meter Readings ](/en/vista/vista/job-resources/equipment-management/equipment-meters/about-the-em-meter-readings-form)and it will update the odometer reading in the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form) form based on the selection in the Meter section on the Updates tab of the EM Company Parameters form. See [Meter Updates: Equipment Usage](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8af--en) for more information.
Note: If you enter 0.00 as the new reading, EMMR (Meter
 Readings) will be updated with the current odometer reading from EMEM (Equipment).
This field will default with the last odometer reading on the equipment from the EM Equipment form.
If there are multiple entries for a single piece of equipment in the same batch, this field will default to the odometer reading entered on the previous transaction.

## Hour Meter

Enter the current hour meter on the
 equipment. The difference between this value and the current hours will default into the
 Time
 Units field.
This field is enabled only when the revenue
 code selected in the Revenue Code field is set up update hour meters (Update Hour
 Meters checkbox in the ER Revenue Codes form, Info tab).
Changing the hour meter
Change the value in this field will update the hour meter in EM Equipment (based on the update option for equipment usage in EM Company Parameters).
In addition, a meter history record is created
 in EMMR (Meter Readings). If you enter 0.00 as the new reading, EMMR (Meter Readings) will
 be updated with the current odometer reading from EMEM (Equipment).
Multiple transactions in the batch for the same piece of equipment
If there are multiple entries in the batch for the same piece of equipment, this field will default based on the transaction with the lower sequence number in the batch.

## Time Units

 Specify the number of time units (of the Time
 U/M displayed at the bottom of the form) for this usage entry. The system will convert
 these units to hours using the Hour/Time Unit defined for the specified
 revenue code (in EM Revenue Codes) and store them in the Revenue Detail table (EMRD).
 If you have checked the Update Hour
 Meter flag for the revenue code (in EM Revenue Rates by Equipment or EM
 Revenue Rates by Category), hours are updated to the equipment’s hour meter.
 For entries withType set to
 J-Job, if you have checked Track Hours for the JC cost type (in JC
 Cost Types), the system will post the hours to Job Cost.
Note: If this batch was created using EM Automatic Usage and
 the specified revenue code is designated as a monthly revenue code (the Monthly Revenue
 Code box is checked in EM Revenue Codes), this field will default total
 units as a percentage of 1.000. For usage reflecting an entire month, the field will
 display '1.000'. For usage of less than an entire month, the field will display the usage
 percentage as a decimal. It is suggested that to ensure proper posting, you do not change
 this value.

##  Work Units

 This field is accessible only if you have
 checked the Work
 Units with Usage option for the revenue code (in EM Revenue Rates by
 Equipment or EM Revenue Rates by Category).
 Enter the number of work units (of the Work U/M displayed at the bottom of the form) completed for this usage entry. Work units allow you to track the production of the equipment (e.g. tons hauled).

##  Rate

 This field is accessible only if you have
 checked the Allow
 Rate Change option in EM Company Parameters (Usage tab) and you have checked
 the Allow Posting
 Override flag in EM Revenue Rates by Category or EM Revenue Rates by
 Equipment.
 Specify the rate at which to calculate usage time for this piece of equipment. Initially defaults the rate specified for the revenue code in EM Revenue Rates by Category or EM Revenue Rates by Equipment.

##  Amount

 The total amount defaults based on the calculation of Time Units x Rate for this transaction. You should not need to change this amount; however, if you do change the calculated amount, neither the rate nor the time units will be updated.
