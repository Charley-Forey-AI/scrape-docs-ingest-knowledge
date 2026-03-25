---
title: "Field Definitions: SM Work Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form"
---

# Field Definitions: SM Work Orders Form

The following is a list of field descriptions for the SM Work Order Quotes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Search By

Select one of the following search options:

- A-All (default) – Select this option to show both customer and job work orders.

- C-Customer – Select this option to show only customer work orders. When selected, the screen displays a Customer field to allow additional filtering by a specific customer..

- S-Service Site – Select this option to show only work orders for a specific service site. When selected, the screen displays a Service Site field for entering the filter-by service site (required)..

- J-Job – Select this option to show only job work orders. When selected, the screen displays JCCo and Job fields to allow additional filtering by a specific JC company and job.

## Status

Select the status by which to search for work orders:

- Not Closed – Select this option to show all work orders that have not been closed. This will include work orders with a status of New, Open, and Complete.

- New – Select this option to show only those work orders with a status of New.

- Open – Select this option to show only those work orders with a status of Open.

- Closed – Select this option to show only those work orders with a status of Closed.

- All – Select this option to show all work orders, regardless of their status.

## Customer

This field only displays when you select C-Customer as the Search By option.
Enter the customer by which to search for work orders or press F4 to select from a list of valid SM customers.
Leave blank to show work orders for all customers.

## Service Site

This field only displays when you select S-Service Site as the Search By option.
Entry in this field is required.
Enter the service site by which to search for
 work orders. Press F4 to select from a list of valid service sites.

## JCCo

This field only displays when you select J-Job as the Search By option.
Enter the Job Cost company by which to search
 for work orders or press F4 to select from a list of valid Job
 Cost companies.
Leave blank to show job work orders for all Job Cost companies.

## Job

This field only displays when you select J-Job as the Search By option.
Enter the job by which to search for work
 orders or press F4 to select from a list of valid jobs for the specified JC company.
Leave this field blank if:

- you did not specify a company in the JCCo field.

-
you specified a company in the JCCo field, but want to show all job work orders for that company.

## Center

Enter the service center by which to search
 for work orders. Press F4 to select from a list of valid service
 centers.
Leave this field blank to show work orders for all service centers.

## Date

Enter the beginning and/or ending date by which to search for work orders.

- If you enter only a beginning date, the list will include all work orders entered on or after the specified date.

- If you enter only an ending date, the list will include all work orders entered on or prior to the specified date.

- If you enter both a beginning and ending date, the list will include all work orders entered within the specified date range (i.e. on or after the beginning date and on or prior to the ending date).

Leave these fields blank to include all work orders, regardless of their entry date.

## Work Order

Required.
Enter a work order number (between 0 and
 2,147,483,647), or enter N, New, or + to have the system automatically assign
 the next sequential work order number that is not already in use.
If a value is specified in the [Next Work Order Number](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#ID-00042877--en) field in SM Company Parameters, the system will assign the first unused sequential number after that value to the next work order. Once the system assigns the next available work order number here, it will update the Next Work Order Number accordingly.

## Quote

This field only displays for work order scopes that were generated from a work order quote.
Display only, the quote associated with this work order scope.

## Ready for Review

The Ready for Review drop-down on the SM Work Order form, Search section.
Use this option to search for work orders that are ready for review (that is, work orders that are ready to bill and require review and approval). Select one of the following:

- Primary - Show only work orders for which you are the [primary reviewer](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-1625--en__PrimaryVSAlternate).

- Alternate - Show only work orders for which you are an [alternate reviewer](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-1625--en__PrimaryVSAlternate).

- All - If the Use Review Process checkbox is selected in SM Company Parameters, select this option to show all work orders assigned to you that are ready for review. If the Use Review Process checkbox is not selected, select this option to show all work orders that are ready for review, regardless of reviewer.

Note: Search results will only include work orders that have one or more Closed or Completed scopes with unbilled amounts, and meet other search criteria. For example, if you also select to filter by a Status of Open, the results will only include open work orders that have one or more Completed or Closed scopes with unbilled amounts

Leave this field blank if not restricting the search to only work orders that are ready to bill.

### Primary Reviewer vs. Alternate Reviewer

The system uses the following hierarchy to determine primary and alternate reviewers.

- Work Order

- Service Site

- Customer

- Division

- Service Center

For example if a reviewer is found at the work order level, that reviewer (along with its authorized users) becomes the primary reviewer. Reviewers found at higher levels (service site, customer, division, and service center) become alternate reviewers. If a reviewer is not found at the work order level, the system continues searching at each level until a reviewer is found. The first reviewer found becomes the primary reviewer and reviewers found at the higher levels become alternate reviewers.

## Reviewer

Reviewer field on the SM Work Order form, Search
 section.
This field is enabled once you select an option in the Ready for Review drop-down.
If you are an authorized user for multiple reviewers and you want to filter work orders
 by a specific reviewer (for which you are an authorized user), enter the reviewer here.
 Press F4 to select from a list of reviewers for which you are an
 authorized user.

## Description

The Description field on the SM Work Orders form, header Info tab.
Enter a description for this work order. This will typically be a description of the problem, maintenance request, or any other service being requested. Space allowance is virtually unlimited.

## Site

The Site field on the SM Work Orders form, header Info tab.
Enter the service site requesting the service
 work. Press F4 for a list of valid service sites.
If the work order is for a new service site,
 press F5 to access SM Service Sites and set up the service site. Once you return
 to this form, enter the new service site here.
Note: For customer work orders:

- If the customer is 'on hold' in
 AR Customers, a message displays indicating that the selected customer is
 currently on credit hold in AR; however, the entry is allowed.

- If the customer is 'inactive' in
 AR Customers, a message displays indicating that the selected customer is
 inactive; you will be unable to save the record.

Note: For job work orders:

- If the job is hard or soft-closed and
 you do not allow posting to closed jobs (i.e. the Allow Posting to
 Hard-Closed Jobs and/or Allow Posting to Soft-Closed
 Jobs boxes are unchecked in JC Company Parameters), a message
 displays indicating that the job is closed; and you will be unable to save the
 record.

### Changing the Service Site

You can change the service site on an existing
 work order if:

- no billings have occurred

- the work order was not generated from a
 quote or an agreement

- all work completed lines (if any) have a status of 'Provisional'

When you successfully change a service site,
 the system:

- updates the customer or job accordingly


- updates contact information and leaves
 requested by information intact

- updates the default service center and
 clears the division on each scope if not valid for the new service center

- updates the pricing method to T&M if
 the new site is a job site or to non-billable if the new site is flagged as
 non-billable; otherwise, leaves the pricing method 'as is'

- updates the bill to information, rate
 template, tax source, tax type, and tax code for each scope accordingly (customer
 work orders only)

- removes all agreement-related
 information if the new site is a job site and agreement-related scopes were added
 manually

- removes existing standard charges (if
 applicable) and adds those defined for the new service site

- removes the scope phases if changing
 from one job site to another and the phases are not valid for the new job

## Type

The Type drop-down on the SM Work Orders form, header Info tab.

This field is only enabled until you select a service site for the work order. Once the service site is selected, this field populates based on whether it is a customer service site or a job service site.
Select the work order type.

- C-Customer

- J-Job

The type you select determines what fields display in the work order header.

## Customer

Applicable to customer work orders only.
Display only, the customer associated with the specified service site.
Tip: You can press F5 to access the SM Customers form for additional information about the customer.

## PR State

For customer work orders only.
Enter the state where the work being done for this work order is located. Initially defaults the state designated in the service site's address (in SM Service Sites).
The system may use this state as the default tax, unemployment, and/or insurance state on timecards referencing this work order in PR Timecard Entry, depending on the "Use Job/SM Work Order" settings in PR Company Parameters (State/Local tab) and the "Always use Employee's Work/Resident" settings in PR Employees. For more information about these settings, see the F1 help.
Note: For information about state defaults for labor hours posted to job-related SM work orders, see the [Ins State ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form/field-definitions-pr-timecard-entry-form#ID-0003b0e7--en), [Tax State ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form/field-definitions-pr-timecard-entry-form#ID-0003b148--en), and [Unemp State ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form/field-definitions-pr-timecard-entry-form#ID-0003b23a--en)F1 help in PR Timecard Entry.

## PR Local Code

Enter the
 local code that identifies the city, county, or other taxing district in which the work being
 performed for this work order is located. Defaults the local code defined for the service site
 specified on this work order. Press F4 for a list of valid local codes (defined in PR Local
 Codes).
The system may use this code as the default local code on timecards referencing this work order in PR Timecard Entry, depending on how you set the
 Use Job, SM Work Order or Office Local for Local Tax
 checkbox in PR Company Parameters (State/Local tab) and the
 Always Use Employee's Work/Resident Local Code
 checkbox in PR Employees.
The following table displays how timecards will default this code based on these two checkboxes.
Use Job, SM WO, or Office Local
Use Employee Local
Local Default

Defaults from the
 Work Office Local Code
 field in PR Employees. If blank, the system defaults from the
 Resident Local Code
 field.

If you specify a job in the Job field
 (PR Timecard Entry) and the PR Local Code field (JC Jobs) is not blank, defaults from the PR Local
 Code field in JC Jobs.
If you specify a job in the Job field, and the
 PR Local
 Code field (JC Jobs) is blank, the default value is
 the Resident Local Code field in the PR Employees form.
If you do not specify a job in the
 Job
 field, defaults from the
 Office Local
 field in the PR Company Parameters form, if it is not blank.
If you do not specify a job in the
 Job
 field, and the
 Office Local
 field in PR Company Parameters is blank, defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
SM Work Orders:
If a job work order, defaults from the PR Local
 Code field in the JC Jobs form, if it is not
 blank. If the job's PR Local Code field is blank, defaults as blank, the default value is the Resident Local Code field in the PR Employees form.
If a customer work order, defaults from the
 PR Local Code
 field in SM Work Orders. If you do not specify a PR Local Code on the work order, defaults as blank.

Defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
 If both the
 Work Office Local Code
 and the
 Resident Local Code
 fields in PR Employees are blank, defaults as blank.

Defaults from the
 Work Office Local Code
 field in PR Employees. If that field is blank, defaults from the
 Resident Local Code
 field in PR Employees.
 If both the
 Work Office Local Code
 and the
 Resident Local Code
 fields in PR Employees are blank, defaults as blank.

For more information on setting tax and insurance information for your company, see [Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). For more information on setting tax and insurance information for individual employees, see [Setting Employee Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information).

## Job

Applicable to job work orders only.
Display only, the job associated with the specified service site.
Tip: You can press F5 to access the JC Jobs form for
 additional information about the job.
Note: If the job is hard or soft-closed and you do not
 allow posting to closed jobs (i.e. the Allow Posting to Hard-Closed Jobs and/or
 Allow Posting to
 Soft-Closed Jobs boxes are unchecked in JC Company Parameters), a message
 displays indicating that the job is closed; and you will be unable to save the
 record.

## Costing Method

The Costing Method drop-down on the SM Work Orders form, header Info tab.
This field is only displayed and enabled for job work orders.
Required.
Specify how costs will be sent to Job Cost for work completed on this job work order. Initially defaults the setting defined for the service site.

- Actual Cost - Select this option to send actual costs to Job Cost. When entering work completed for this work order, the system sets the Total Billable equal to the Total Actual Cost and sends this amount to Job Cost.Note: For work completed Equip, Misc, and Inventory lines, the billable amount is sent to Job Cost once you save the work completed line. For work completed Labor lines, actual costs are updated to Job Cost once you process payroll and run PR Ledger Update. For work completed Purchase lines, actual costs are updated to Job Cost once you pay the invoice in AP Transaction Entry.

- Markup - Select this option to send revenue (cost + markup) as cost to Job Cost. When capturing work completed, the system calculates the billable amount based on the rate template assigned to the work order scope, and sends this amount as cost to JC.Note: For Labor and Purchase lines, actual costs are updated to the corresponding work completed line and the billable amount recalculated. The system then sends the new billable amount to Job Cost.

Once you begin entering work completed, this field is disabled and cannot be changed. The only time this does not apply is when all work completed lines on the work order are miscellaneous work completed lines with a "provisional" status (those auto-added to the work order from standard charges or miscellaneous requirements). In this case, this field is enabled and will remain so until you manually enter one or more work completed lines of any type.

## Lead Tech

Enter the lead technician for this work order
 or press F4 to select from a list of preferred site technicians, preferred customer
 technicians, active technicians, or all technicians.
Leave this field blank to have the system auto-assign a lead technician using the technician from the first trip you create for the work order. If you do not assign a technician when first creating trips, the system will use the first technician assigned to any trip on the work order. You may override the auto-assignment as needed.
Agreement Work Orders
If you generated this work order from an agreement (using SM Generate PM Work Orders), this field defaults the Assigned Tech designated for the agreement service. If you did not assign a technician to the agreement service, this field defaults the primary technician designated for the related service site.

## Reviewer

Reviewer field on the SM Work Order field,
 Work Order header section.
Enter a reviewer’s ID in the Reviewer field,
 so that reviewer can select work orders as ready-to-bill and so that any applicable
 unapproved invoices in accounts payable will get this reviewer assigned by default.
 Press F4 for a list of active reviewers.
If you
 leave this field blank, reviewers set at any of the following fields will be able to review
 this work order:

- SM Service Site

- SM Customer

- SM Service Division

- SM Service Center

## Center

Required.
Enter the service center that will be performing the service work on this work order.

- Although you are not initially required to enter a service center when adding a work order, you will be required to assign a service center before you can capture work completed or create invoices.

- For work orders with an agreement, this field is disabled. If the work order doesn't have an agreement, you may change the service center. If you change the service center for a work order and save it, any costs or billings that have been captured will need adjusting entries to be posted to the GL, if the GL accounts differ based on the service center change.

## Site Contact: Name

Enter the name of the contact for the
 specified service site. Initially defaults the Default Contact from the service site, if
 applicable.

-  The contact specified here can be a site or customer contact, or any contact not already set up for the site or customer. Press F4 for a list of valid site contacts, customer contacts, or HQ contacts.

- You can also set up a contact on-the-fly by pressing F5 to access the HQ Contacts form. Once you have [set up the contact](/en/vista/vista/administration/headquarters/company-setup/set-up-hq-contacts) and returned to this form, you can enter the new contact here. Be aware that setting up a new contact in HQ Contacts and adding them to a work order here does not automatically set them up as a customer contact (in SM Customers) or a site contact (in SM Service Sites).

## Site Contact: Phone

Enter the phone number of the site contact specified above. Initially defaults the phone number defined for the site contact (in HQ Contacts) specified above.

## Requested By: Name

Enter the name of the person who made the service request.
Note: The person specified here can be a site or customer contact, or any contact not already set up for the site or customer. If you specified a Caller Name in SM Call Handler, it will appear here. Press F4 for a list of valid site and customer contacts.

## Requested By: Date

Enter the date this service request was made. Initially defaults the current date.

## Requested By: Phone

Enter the phone number of the person who made the service request.
Note: If you specified a site, customer, or HQ contact, this field will automatically default the phone number specified for the contact in HQ contacts. If you specified a Caller Phone number in SM Call Handler, it will appear here. May be overridden as necessary.

## Requested By: Time

Enter the time this service request was made. Initially defaults the current time.

## Certified Payroll

For customer work orders only.
Check this box if this work order should be included in certified payroll reporting. When running Certified Payroll reports (e.g. PR Certified Payroll Transcript, PR Certified Report with Liabilities, etc.), if you specify to include SM work orders, the report will include this work order.
Leave this box unchecked to exclude this work order from certified payroll reporting.
Note: This field defaults the setting specified for this work order's service site in SM Service Sites.

## Start Date for Certifieds

This field displays only on non-Job work orders.
If you are including this job on certified payroll reports, enter the start date for certified payrolls (should be the date labor actually started on this work order). This date will be used to calculate the week number on the certified payroll reports (e.g. PR Certified Payroll Transcript, PR Certified Report with Liabilities, etc.).

## Craft Template

For Customer work orders only.
Enter the craft template for this work order
 or press F4 to select from a list of valid craft templates (set up in PR Templates)
 for the PR Co associated with this SM Company. Initially defaults the craft template
 specified for the service site (in SM Service Sites). If you did not assign a craft
 template to the service site, this field defaults as blank.
The system will use this template to determine craft/class pay rate defaults in PR Timecard Entry for labor hours posted to this work order. If you leave this field blank, the system will determine the employee's pay rate using the standard hierarchy. See [Crafts, Classes, and Templates](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-crafts-classes-and-templates) in the Payroll online help for more information.

## Ready To Bill

The Ready to Bill checkbox on the SM Work Order form, Header Info tab.
Select this checkbox to if the work completed
 item is ready to bill.
This checkbox allows you to mark all items and scopes for the work order as ready-to-bill.
If your log-in is associated with a reviewer on the work order, then you are able to select this checkbox. However it does not appear if you are not a reviewer for the work order.
Note:If the Ready To Bill checkbox is in an "indeterminate" state (meaning that it is neither selected nor unselected), this means that at least one scope is not ready to bill.

## Seq

Enter N, New, or + to add a new work order sequence; the
 system will automatically assign the next sequential number.
Note: When adding a new work order, the system will automatically add a single work order sequence and skip this field. However, if you have set up F3 overrides at the scope level for default behaviors or added "required value" validation, this may impact the system's ability to auto-add and save the work order scope. If the defaults are invalid (e.g. you default a call type that has since be deactivated) or you require entry in a field and do not auto-default a value, the system will display an error indicating the problem. Although it will 'create' the scope, you will be unable to save the record until the correct information has been entered.

## Scope

Enter the work scope (set up in SM Work Scopes) that represents the work to be done on this work order sequence.
If this work order was generated from a work order quote, this field defaults the work scope from the quote sequence. May be overridden.

## Priority

Enter the priority of the work order scope. If you entered a work scope, this field will default the priority specified for the work scope (in SM Work Scopes). May be overridden as necessary.

## Scope Detail

Enter a description of the problem or service request that will be handled by this work order scope. Space allowance is virtually unlimited.
If this work order was generated from a work order quote, this field defaults the scope detail specified for the quote sequence. May be overridden.

## Due

Specify the due date type for this work order scope.

- 0-By — Select this option if this work order scope is due by a
 specific date. When selected, the second date field (right) is enabled; use this field
 to enter the "due by" date.

- 1-Within — Select this option if this work order due within a
 specified time-frame. When selected, both date fields (right) are enabled. Use these
 fields to enter the beginning and ending date in the "due within" date range.

Note: These fields are informational only; however, if you
 are using SM Work Centers, the specified dates can be used to identify overdue work orders
 (Items > Hot
 Lists > Overdue Work
 Orders).

- If you generated this work order using SM Generate PM Work
 Orders, this field defaults based on the scheduling options defined for the agreement
 service (in SM Work Schedule, Schedule tab) and cannot be changed.

- If you generated this work order from a work order quote, this
 field defaults from the quote sequence. May be overridden as needed.

## Start Date

This field is only enabled when due date type is 1-Within.
Enter the beginning date in a range of dates within which the work order scope is due.
Note: This field is informational only; however, if you are
 using SM Work Centers, this date can be used to identify overdue work orders (Items > Hot
 Lists > Overdue Work
 Orders).

- If you generated this work order using SM Generate PM Work
 Orders, this field defaults based on the scheduling options defined for the agreement
 service (in SM Work Schedule, Schedule tab) and cannot be changed.

- If you generated this work order from a work order quote, this
 field defaults from the quote sequence. May be overridden as needed.

## End Date

This field is enabled when due date type is 0-By or 1-Within.
If you selected 0-By as the due date type, specify the date by which this work order scope is due.
If you selected 1-Withinas the due date type, specify the ending date in a range of dates within which the work order scope is due.
Note: This field is informational only; however, if you are
 using SM Work Centers, this date can be used to identify overdue work orders (Items > Hot
 Lists > Overdue Work
 Orders).

- If you generated this work order using SM Generate PM Work
 Orders, this field defaults based on the scheduling options defined for the agreement
 service (in SM Work Schedule, Schedule tab) and cannot be changed.

- If you generated this work order from a work order quote, this
 field defaults from the quote sequence. May be overridden as needed.

## Division

The Division field on the SM Work Orders form, scope Info tab.
Enter the service center division for this work order scope or press F4 for a list of valid divisions for the specified service center. This will generally be the division that handles the type of work defined for this scope.

- If you generated this work order using SM Generate PM Work Orders, this field defaults the division specified for the agreement service (if applicable). May be overridden.

- If this work order was generated from a work order quote, this field defaults the division specified for the quote sequence. May be overridden.

## Call Type

The Call Type field on the SM Work Orders form, scope Info tab.

Enter the call type (from SM Call Types) for this work order scope. Press F4 to select from a list of call types by service center or all call types. If you specified a division for the work order scope, you will also have the option to view call types by division.
This field defaults as follows:

- For manually created work orders, this field defaults as blank.

- For work orders generated from service call (via SM Call Handler), this field defaults the call type specified for the service call. May be overridden.

- For work orders generated from a work order quote (via SM Work Order Quotes), this field defaults the call type specified for the quote sequence. May be overridden.

- For work orders generated from an agreement (via SM Generate PM Work Orders), this field defaults the call type specified for the agreement service (in SM Service) and is disabled.

Note: Although you are not required to enter a call type when adding sequences to a work order or entering work completed, you will be required to assign a call type before you can close the work order scope.
Note: It is important to note that assigning a call type after you have entered/invoiced work completed will affect the cost and revenue accounts if tracking WIP for the call type and/or if overrides exist in SM Departments for the call type.Changing the Call Type
You can change the call type for any work order (except for those generated from an agreement), regardless of whether you have entered work completed, billed the work order, or closed the scope. For more information, see [Changing Call Types](/en/vista/vista/service-management/work-orders/about-work-order-sequences).

## Serviceable Item

Enter the item being serviced, if applicable.
 Press F4 for a list of valid serviceable items for the specified service
 site.
Note: This field is disabled if this a preventative maintenance work order (i.e. agreement-related work order generated using SM Generate PM Work Orders).

## Material Tax Override

The Material Tax Override drop-down on the SM Work Orders form, Info tab of scope section.

This option applies to material-related lines only; that is, Inventory, Purchase, and Miscellaneous lines with a material-related cost type (cost type with an SM Cost Type Category of M - Material).
 Select the tax type override option for this work order scope.

- Blank – Use the standard tax type defaulting behavior. For taxable material-related work completed lines, the tax type defaults as Sales. For non-taxable material-related work completed lines, the tax type defaults as blank.

- N - No Tax – Default the tax type as "blank" for material-related work completed lines.

- S - Sales Tax Only – Default the tax type for taxable material-related work completed lines as Sales (US) or VAT (AU/CA).

- U - Use Tax Only (US companies only) – Default the tax type as Use for taxable material-related work completed lines.

 This field defaults as follows:

- If the work order scope is associated with an agreement, this field defaults the material tax override specified on the agreement service (for generated work orders) or agreement (for manually entered work orders).

- If the work order scope was generated from a work order quote, this field defaults the material tax override specified on the quote scope.

- If you manually entered this work order and specified a call type for the work order scope, this field defaults the material tax override specified for the call type. If you did not enter a call type, this field defaults as blank.

## Assignment

Assignment field on the SM Work Orders form, Info tab of scope section.
Enter
 an assignment number, or press F4 for the SM Assignment Lookup from
 which to select an assignment number. Press F5 to connect to the [SM Assignments](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-assignments-form) form.

## Tax Option Override

The Tax Option Override drop-down on the SM Work Orders form,
 Info tab of the scope section.

This field defaults the Tax Option Override defined for the
 agreement, agreement service, or work order quote scope associated with this work order
 scope, *or* it defaults as blank if no overrides were defined at those levels or if the work order scope was manually entered.
If you want to override the default, choose one of the override
 options listed below. The system uses the option selected here to determine the
 taxability of work completed lines associated with this work order scope.
If you leave this field blank, the system uses the Tax Option defined
 for the Call Type associated with the work order scope instead.
Note: Changing the work order scope Call Type will not affect the
 value selected in this field.

Note: Work completed lines associated with Flat Price or Non-Billable work order scopes are non-billable; therefore, taxes may only be applied at the time of purchase (cost tax). If you select an option other than N-Not Taxable or P-Taxable at Purchase Only for these scopes, the system ignores the bill tax portion.Additionally, you can only apply cost tax to Misc, Inventory, and Purchase lines; you cannot apply cost tax to Equip or Labor work completed lines.

- N - Not Taxable - Do not apply taxes at the time of purchase or billing. The cost and billing tax types and tax codes default as blank, regardless of whether the SM cost type specified for the work completed line is taxable. You may override the defaults as needed.

- P - Taxable at Purchase Only - Apply taxes at the time of purchase only. If the cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope and the Cost Tax Code defaults from the service site or service center depending on the Tax Source defined for the work order scope. The billing tax type and billing tax code default as blank. If the cost type is not taxable or no cost type is specified, all tax fields default as blank. You may override as needed.

- B - Taxable at Billing Only - Apply taxes at the time of billing only. If the line's cost type is taxable, the billing tax type and billing tax code default to the Tax Type and Tax Code specified for the work order scope. The Cost Tax Type and Cost Tax Code default as blank. If the cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.

- M - Taxable at Purchase/Markup at Billing - Apply taxes at the time of purchase and also apply taxes to the markup amount at the time of billing. If the line's cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope and the Cost Tax Code defaults from the service site or service center depending on the Tax Source defined for the work order scope. The billing tax type and tax code default to the Tax Type and Tax Code specified for the work order scope; however, the tax basis defaults the markup amount only. If the line's cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.Note: For taxable purchases, the bill tax basis is reduced by the amount that was previously taxed at the time costs were recorded. If you did not capture taxes when recording costs, there is no credit to apply to the transaction at billing; therefore, the bill tax basis is calculated using the full billing subtotal, not just the markup.

- F - Full Tax at Purchase and Billing - Apply tax fully at time of purchase and at time of billing. If the line's cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope, and the Cost Tax Code defaults from the service site or service center, depending on the Tax Source defined for the work order scope. The billing tax type and billing tax code default to the Tax Type and Tax Code specified for the work order scope, and the tax basis defaults the full billable amount. If the line's cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.

## Revenue Recognition

Revenue Recognition drop-down list on scope section of the SM Work Orders form, Info tab.
Select how to recognize revenue:

- B - As Billed - (default) select this option to have revenue recognized as it is billed

- C - As Costs Incurred - select this option to have revenue recognized as costs are incurred

## Rate Template

Enter the rate template (from SM Rate Templates) for this work order scope. Initially defaults the rate template as follows:

- Customer Work Orders - Defaults the rate template from the service site or customer (if no rate template is assigned to the service site). If you did not assign a rate template to the service site or customer, this field defaults as blank.

- Job Work Orders - Defaults the rate template from the service site or as blank if no rate template is assigned to the service site.

- Auto-Generated Agreement Work Orders - For Time and Material price method only, defaults the rate template associated with the agreement service and is disabled. Cannot be changed.

- Manually Added Agreement Work Orders - Defaults the rate template from the agreement or blank if no rate template is assigned to the agreement.
Note: A rate template must be assigned to the agreement if you plan to use agreement rates for work completed (by selecting the
 Agreement Rates
 checkbox for the work order scope or the work completed line). If you did not assign a rate template to the agreement, you must leave the
 Agreement Rates
 box unchecked and enter a rate template here.

 The rate template specified here will be used to determine billable rates for equipment, labor, inventory, and purchase lines associated with this work order scope.
Note: You are not required to enter a rate template in order to save the work order scope; however, you will need to assign a rate template in order to invoice billable work completed lines.
Note: For job work orders using the Markup
 Cost Method
 , the rate template is used to calculate the billable amounts that will be sent as costs to Job Cost. Therefore, you must assign a rate template to the scope before you can:

- enter work completed in SM Work Orders

- run PR Ledger Update for labor lines entered directly in Payroll

- post an invoice batch for SM purchase orders or for miscellaneous lines entered directly in AP Transaction Entry

Conditions that control the display and disabling of this field
The following details the different conditions in which this field is hidden or displayed and disabled.

- This field does not display for:

- customer work orders with a
 Price Method
 of N - Non-Billable or F-Flat Price.

- job work orders with a
 Costing Method
 of Actual Cost.

- for work orders scopes generated from an agreement service where the
 Price Method
 is N - Non-Billable or F-Flat Price.

- manually added work order scopes that reference an agreement and have a
 Price Method
 of N - Non-Billable.

-  manually added work order scopes that reference an agreement, have a
 Price Method
 of T-Time and Material, and have the
 Agreement Rates
 box checked.

- This field displays, but is disabled:

- for work orders scopes generated from a work order quote where the
 Price Method
 is T-Time and Materials. Defaults the rate template assigned to the quote sequence (in SM Work Order Quotes).

- for work orders scopes generated from an agreement service where the
 Price Method
 is T-Time and Materials. Defaults the rate template assigned to the agreement service (in SM Service).

- once you manually enter work completed for a customer work order or a job work order using a
 Cost Method
 of Markup.

## Agreement

 The Agreement field on the SM Work Orders form, Info tab in lower section of
 form.
This field is for customer work orders only.
Enter
 the agreement for this work order scope or press F4 to select from a list of active agreements
 for the customer.
This field defaults as follows:

- If the Default Agreement Number on Work Order
 Scopes checkbox is selected in SM Company Parameters, and the service
 site associated with this work order is included in Spot Coverage on a single active
 agreement, this field defaults the agreement number.
If the service site is included in Spot Coverage for multiple agreements or if the
 service site is not included in Spot coverage on any agreement, this field defaults
 as blank.

- If the
 Default Agreement Number on Work Order Scopes
 checkbox is not selected in SM Company Parameters, this field will always default as blank.

## Rev

This field only displays if an active agreement exists for the specified customer (in SM Agreements).
Display only, the agreement revision to which this work order scope applies.

## Agreement Rates

This field only displays for manually entered work order scopes where you specified an agreement and a Price Method of T-Time and Material.
Select this checkbox to use the rate template specified on the agreement.
Leave this checkbox unselected to use the rate template specified for the work order scope.

- You can change the setting of this option for a work order scope (manually added only), as long as you have not billed any work completed lines that reference the scope. Once you bill one or more work completed lines, this field is disabled.

Note: If you change the setting of this option, the system will automatically update the coverage and pricing for all related work completed lines accordingly.

- Work order scopes generated from an agreement service that have a pricing method of T-Time of Service and type of R-Rate Template will not display this checkbox; however, the system will use the rate template associated with the agreement service to calculate billable rates.

## Price Method

The Price Method drop-down on the SM Work Orders form, scope Info tab.

This field displays for customer work orders only.
Select the price method for this work order scope:

- N - Non-Billable — Select this option if you are not charging for work covered by this work order scope. The system automatically defaults this option for all work orders referencing a service site with the Non-Billable checkbox selected in SM Service Sites.

- T - Time and Material — Select this option to bill work completed using the rate template assigned to the work order scope. The system automatically defaults this option for all work orders referencing a service site with the Non-Billable checkbox unselected in SM Service Sites. If you select this option, a Ready To Bill checkbox appears, allowing you to mark the scope items as ready to bill, if you are an authorized reviewer.

- F - Flat Price — Select this option to charge a flat price (designated to the right) for all work covered by this work order scope. You will be required to break down revenue by cost type category using SM Flat Price Revenue (accessed via the Split button). For more information, see [Enter Flat Price Revenue](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue).If you select this option, a Ready To Bill checkbox appears, allowing you to mark the scope items as ready to bill, if you are an authorized reviewer. In addition, a Partial Bill checkbox displays, allowing you the option to enter a partial-billing amount.

For work order scopes generated from a quote, this field defaults the price method from the quote sequence and is disabled.

### Agreement Work Orders

For preventative maintenance work orders (those generated using SM Generate PM Work Orders), this field is disabled and defaults based on the pricing method defined for the agreement service (in SM Work Schedule).

- N - Non-Billable — Defaults for services with a pricing method of I-Included in Agreement or P-Periodic. All work associated with this scope will be included in the agreement or agreement service pricing.

- T - Time and Material — Defaults for services with a pricing method of T-Time of Service and a method type of R-Rate Template. All work associated with this scope will be billed using the rate template defined for the agreement service.

- F - Flat Price — Defaults for services with a pricing method of T-Time of Service and a method type of F-Flat Rate.

For manually added work order scopes that reference an agreement, select the pricing method to use for determining billable rates for work completed:

- N - Non-Billable — Select this option to include the work covered by this scope in the agreement price; no extra billing will occur.

- T - Time and Material — Select this option to bill work covered by this scope separate from the agreement using a rate template. If you select the Agreement Rates checkbox (to the right), the system uses the rate template assigned to the agreement (in SM Agreements). If you do not select the Agreement Rates checkbox, the system uses the rate template specified for the work order scope.

- F - Flat Price — Select this option to bill work covered by this scope separate from the agreement; all work covered by this scope will be included in the flat price designated to the right.

You can change the price method for a work order scope (manually added scopes only), as long as you have not billed any work completed lines that reference the scope; the system automatically updates the coverage and pricing for all related work completed lines accordingly. Once you bill one or more work completed lines, this field is disabled.

## Price

Price field on the SM Work Orders form, Info tab, work order scope section.
This field only displays for customer work
 order scope with a Price Method of F-Flat Price.
Required.
Enter the price that will be charged for the work covered by this work order scope. All work completed lines associated with this work order scope will be included in this price and will show a billing rate/total billing of blank.
For Flat Price work order scopes generated from an agreement (via SM Generate PM Work Orders), this field is disabled, and defaults the flat price specified for the agreement service.

## Margin

Margin field on scope section of the SM Work Orders form, Info tab.
This field displays for Flat Price work order scopes only.

Enter the expected margin percentage to apply when recognizing revenue for this flat price scope. If you created this work order from a work order quote (via SM Work Order Quotes), this field defaults the margin specified for the quote scope.
During the revenue recognition process (in SM Revenue Recognize), the system determines the revenue to recognize by applying the margin to the sum of all associated costs.

 For example, if the total cost posted to the scope is $2,500 and the margin is 20%, the recognized revenue will be $3000 ($2,500.00 x 1.2 = 3,000.00).Note: When recognizing revenue for flat price scopes, the system will not exceed the Flat Price amount. If the total costs plus the margin will exceed the Flat Price amount, the system will stop recognizing revenue at the Flat Price amount.

## Ready To Bill

The Ready to Bill checkbox on the SM Work Orders form, scope Info tab.
This checkbox only displays for work orders where you specify a Price Method of F-Flat Price or
 T-Time and Material
 .

- Selecting
 Ready To Bill
 for Time and Material marks all line items as Ready to Bill for that scope
Note: If the Ready To Bill checkbox is in an "indeterminate" state for Time and Material (meaning that it is neither selected nor unselected), this means that at least one work item line (but fewer than all) is marked as Ready to Bill

- Selecting
 Ready To Bill
 for Flat Price provides you with a
 Partial Bill
 option, which gives you with an editable
 Amount
 field which allows you to bill less than the full amount (it defaults to the amount remaining to be billed). The related percentage field is also editable, and reflects the percentage of the figure in the
 Amount
 field, and vice versa.
Note: If the Ready To Bill checkbox is in an "indeterminate" state for Flat Price (meaning that it is neither selected nor unselected), this means that the full amount is not billable (meaning the full amount has been adjusted to a partial amount in the Amount field or
 billing amount percentage
 fields.

## Partial Bill

This checkbox only displays for work orders
 where you specify a Price Method of F-Flat Price and is only selectable if you have
 selected the Ready
 To Bill checkbox.
When you select Partial Bill,
 you are able to adjust both the amount in the Amount field (which defaults to the
 amount remaining to be billed) , and the billing amount percentage field (which
 reflects the percentage of the total ready-to-bill amount in the Price field).

## Not to Exceed

This field only displays if the Price Method is T-Time and Material.
Optional.
Enter the billable limit for this work order scope. You will only enter a value here if work completed equipment, labor, parts (stocked and purchased), and miscellaneous charges posted to this work order scope should not exceed a specified amount.

- This field is disabled for work order scopes that were generated from a Time and Material work order quote sequence. Defaults the value from the quote sequence, if applicable.

- Entry in this field is informational only. You will typically enter a value here if work completed lines posted to this work order scope should not exceed a specified amount; however, the amount specified here will not be used to validate total billable amounts on work completed lines.

## Phase

The Phase field on the SM Work Orders form, scope Info tab.

This field displays for job work orders only.
Enter the phase to which costs will be posted when capturing work completed for this work order sequence. Press F4 to select from a list of valid job or phase master phases.
This field initially defaults a value as follows:

- If you did not enter a work scope in the Scope field, defaults as blank.

- If you entered a work scope in the Scope field, defaults the phase assigned to the work scope in SM Work Scopes. May be overridden. If you did not assign a default phase to the work scope, this field defaults as blank.

### Locked Job vs. Non-Locked Job

If the Phases on this job are locked checkbox is selected for the job in JC Jobs, you must enter a phase that is set up for the job in JC Job Phases. If you enter a non-job phase, an error displays and you must either enter an existing job phase or add the phase to the job (by pressing F5 to access JC Job Phases).
Tip: If you enter a phase that is not set up for the job, you can press F5 from this field to access JC Job Phases. Once you add the phase and exit JC Job Phases, you can enter the phase here.

If the Phases on this job are locked checkbox is not selected for the job in JC Jobs, you can enter any phase from JC Job Phases or JC Phases, or any phase that matches the valid part of phase defined in JC Company Parameters.
For example, say the Number of valid characters in Phase code field is set to 8 (in JC Company Parameters). JC Phases contains phases 03110-120 and 03110-140-. If you enter phase 03110-120-100, the system allows it since the first 8 characters match the first 8 characters of phase 03110-120-. However, if you enter phase 03110-130-, it is not allowed, since the first 8 characters do not match any phase in JC Phases.
Note: If the job is not locked and you select a phase that does not exist for the job, the system adds the phase (and the specified JC cost type) to the job once you enter a work completed line referencing this scope.

## Customer PO

For customer work orders only.
Enter the PO number (provided by the customer) for this work order scope. Up to 30 characters allowed. Initially defaults as follows:

- If this work order was generated from a work order quote, this field defaults the customer PO specified for the quote sequence. May be overridden.

- If this work order was generated from an agreement, this field defaults the Customer PO specified for the agreement (in SM Agreements) and is disabled. If no customer PO was specified for the agreement, this field defaults as blank and is enabled.

- If this work order is not associated with an agreement, this field defaults as blank.

Note: If the specified service site or customer requires a
 PO on all service work orders (i.e. Customer PO Override in SM Service Sites
 or Customer PO
 Setting in SM Customers is R-Required), and you do not enter a value here,
 the system will display a warning; however, the record will be saved. The system will
 display a second warning when billing work completed for this work order scope if no PO is
 assigned.

## Insurance Code

For customer work orders only.
Enter the insurance code to use as a default on timecards referencing this work order scope (in PR Timecard Entry). Initially defaults the insurance code specified for the service site (in SM Service Sites). Press F4 for a list of valid insurance codes (from HQ Insurance Codes).
The system may use this code as the default
 insurance code on timecards referencing this work order in PR Timecard Entry, depending on
 how you set the Insurance Based on Phase or SM Work Order Scope checkbox in PR Company
 Parameters (Job Cost/Service Mgmt tab) and the Always Use Employee's Work/Resident Standard
 Insurance Code checkbox in PR Employees. If the work order is not assigned
 an insurance code, the system will use the employee’s insurance code (Ins Code field,
 PR Employees).
Note: For information about insurance code defaults for labor hours posted to job-related SM work orders, see the [Ins Code ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form/field-definitions-pr-timecard-entry-form#ID-0003b29c--en) F1 help in PR Timecard Entry.

## Bill To

The Bill To field on the SM Work Orders form, scope Info tab.
For customer work orders only.
 Required.
Specify the AR customer to bill for work completed on this work order. This may be the site customer (specified above) or a different AR customer.
This field initially defaults the alternate bill to customer specified for the service site in SM Service Sites or for the customer in SM Customers. If no alternate bill to customer is defined at the service site or customer level, this field defaults the service site customer.
Note: This field is disabled for preventative maintenance work orders (generated via SM Generate PM Work Orders). However, it is enabled for scopes manually added to a preventative maintenance work order.

## Tax Source

The Tax Source drop-down on the SM Work Order form, Work Order scope section, Info tab.

This field displays for customer work orders only.
From the drop-down menu, select whether to default the tax code for work completed lines from the 0-Service Center or the 1-Service Site. The field initially defaults as follows:

- For manually entered work order scopes, this field defaults to 1-Service Site.

- For work orders generated from a work order quote, this field defaults the tax source specified for the quote sequence.

- For work orders generated from an agreement, this field defaults the tax source defined for the agreement service in SM Service.

You may override the default as needed.
Note: In instances where a work order does not have a service site, tax source information will default from the service center instead.

## Tax Type

The Tax Type field on the SM Work Orders form, Work Order scope section, Info tab.

This field displays for customer work orders only.
If billable amounts for work covered by this work order scope are taxable, specify the default Bill Tax Type for work completed lines. Leave blank if taxes are not applicable. May be overridden.
Initially defaults as follows (depending on the Tax Source designed for the scope):

- If the service center or service site is assigned a tax code, this field defaults as 1-Sales (US) or 3-VAT (AU/CA)

- If the service center or service site is not assigned a tax code, this field defaults as blank.

Note: This field is disabled for flat price scopes generated from an agreement.

## Tax Code

The Tax Code field on the SM Work Order form, Work Order scope section, Info tab.

This field displays for customer work orders only.
If billable amounts for work covered by this work order scope are taxable, specify the default Bill Tax Code for work completed lines. Must be a valid tax code for the specified tax type.
Note: If you change this tax code after you have entered work completed lines, the system updates the tax code and tax amounts for the work completed lines.

This field defaults as follows:

- If this work order scope was added manually, this field defaults the tax code assigned to the Service Site or Service Center, depending on the Tax Source specified for the work order scope. If no tax code is specified for the service site or service center, this field defaults as blank. May be overridden.

- If this work order was generated from a work order quote, this field defaults the tax code specified for the quote sequence. If no tax code is specified for the quote scope, this field defaults as blank. May be overridden.

- If this work order was generated from an agreement, this field is disabled. Defaults the tax code assigned to the Service Site or Service Center, depending on the Tax Source for the work order scope. If no tax code is specified for the service site or service center, this field defaults as blank.

Note: For Flat Price scopes only: Once you enter a tax code, the system calculates a tax amount (shown in the Est. Billable Tax field) based on the taxable split revenue amounts (defined in SM Flat Price Revenue). See the [Est. Billable Tax](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-00045782--en) F1 help for more information.

## Est. Billable Tax

The Est. Billable Tax field on the SM Work Orders form, Work Order scope Info tab.
This field displays for Flat Price work order scopes only.
Display only, the estimated tax amount for this work order scope sequence (if applicable). The system calculates this amount based on the taxable split revenue sequence amounts and the tax rate for the specified tax code. For example, say the work order scope price is 5,000.00. You have 3 split revenue sequences:
Because only $2,500.00 of the revenue amount is flagged as taxable, the system calculates tax only on the $2,500.00, not the total flat price of $5,000.00.
If you change the Amount or Taxable flag on any of the split revenue sequences, the system automatically updates the estimated billable tax.
Note: When you generate an invoice that includes a taxable flat price scope, the system recalculates the tax amount for the scope based on the tax rate applicable at the time of billing. If it differs from the amount originally calculated for the flat price scope, this field is updated accordingly.

## Derived

Select this checkbox to calculate the budget values (labor hours, cost total, pricing total, and profit) for the work order scope based on the detailed cost estimates from the Material, Equipment, and Labor tabs.
Note: If you have entered summarized cost estimates in SM Work Order Cost Detail (accessed via the Detail button), selecting this checkbox will not affect those entries.
Do not select this checkbox if you want to calculate budget values using the summarized cost estimates entered in SM Work Order Cost Detail (accessed by clicking the Detail button on the work order scope).
 For detailed information about how the system updates the budget values, see [About Work Order Scope Budgets](/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets).

## Billed Information: Amount

The Billed Information: Amount field on the SM Work Orders form, scope Info tab.

This field only displays for Flat Price work order scopes once you select the Ready To Bill and Partial Bill checkboxes.
The amount in this field defaults to the amount remaining to be billed; however, it is adjustable when you select the Partial Bill checkbox. To adjust this amount, enter the amount of the total price to bill. The system automatically adjusts the (unlabeled) billed percent field (to the right) accordingly.

## Billed Information: Percent

The Percent field (unlabeled) in the Billed Information section of the SM Work Orders form, scope Info tab.

This field only displays for Flat Price work order scopes once you select the Ready To Bill and Partial Bill checkboxes.
The percentage in this field defaults to 100% of the ready-to-bill amount; however, it is adjustable when you select the Partial Bill checkbox. To adjust the percentage, enter the percent of the total price to bill. The system automatically adjusts the Billed Information: Amount field accordingly.

## Service

The Service field on the SM Work Orders form, scope Services tab.
This field only displays for work orders generated from an agreement (via SM Generate PM Work Orders).
Display only, the service to which this work order scope applies.

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

## Completed

The Completed checkbox on the SM Work Orders form, scope Tasks tab.
Select this checkbox to mark this work order scope task completed.
Leave this checkbox unselected if you have not completed this work order scope task.
Note: This checkbox is informational only; it does not affect related material, equipment, labor requirements, nor does it affect work completed miscellaneous lines generated from a standard task associated with the task.
Note: Once you close the work order scope, this field is disabled and cannot be changed.

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

## Line Type

The Line Type field on the SM Work Orders form, Work Completed tab.
Select the line type for this work completed entry.
For labor and equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- 1 - Equip — Select this option to capture the equipment used to complete this work order.Note: You must have the Equipment Management module (EM) in order to use this type.

- 2 - Labor — Select this option to capture the technician's labor hours for this work order.

- 3 - Misc — Select this option to capture the miscellaneous expenses required to complete this work order.

- 4 - Inventory — Select this option to capture materials pulled from Inventory that were used to complete this work order.Note: You must have the Inventory module (IN) in order to use this type.

- 5 - Purchase — This option is used for materials purchased from a vendor that were used to complete this work order. However, you cannot manually add lines of this type here; the system generates a work completed purchase line when you post a purchase order (in SM Purchase Order Entry or PO Purchase Order Entry) that is associated with an SM work order. Work completed purchase lines will also be generated when distributing existing purchase order items to SM work orders (in PO Item Distribution).Note: You must have the Purchase Order module (PO) in order to use this type.

## Line #

If you are entering this work completed line using the Work Completed grid, this field is display only. The system auto-assigns a line number once you save the work completed line.
If you are entering this work completed line
 using any of the work completed forms, enter N or + to add a new work completed line; the
 system will automatically assign the next sequential number.

## Status

The Status field on the SM Work Orders form, Work Completed tab.

Display only, the system-assigned status for the work completed line.
The following tables describe the statuses that may be applied to work completed lines throughout the work order process.
Table 1. Statuses applicable for new work completed linesNewAssigned to new work completed lines that do not reference a flat price scope or are not flagged as non-billable.
ProvisionalCosts have not been posted. This status is assigned to:

- Equip, Misc, and Inv lines that were either imported or added to a work order when not using the auto-batching feature (that is, the Auto Post New Work Completed checkbox is unselected in SM Company Parameters).

-  Misc lines auto-generated from miscellaneous requirements or standard charges.

Non-Billable Assigned to all work completed lines referencing a work order scope with a Price Method of Non-Billable. This status is also used for work completed lines that reference a Time and Material work order scope, but for which you manually selected the line's Non-Billable checkbox.
Flat PriceAssigned to work completed lines that reference a flat price scope.
Adj Assigned to work completed lines with the Adj checkbox selected.
Ready to BillAssigned to work completed lines with the Ready to Bill checkbox selected.

Table 2. Statuses applicable once work completed lines are flagged as Ready to BillPending Inv Line is on an unposted invoice. This status is assigned to all work completed lines on a work order when you create an invoice session (by clicking the Bill WO button).
PreBilling This status is assigned to work completed lines that have been selected for billing in SM Work Order Billing, but are not currently in an invoice session (that is, no invoice has been generated).Note: This is a temporary status that will only be assigned as long as the SM Work Order Billing form is open and no invoice has been generated for the work completed line. Once you close the SM Work Order Billing form, if you have not generated an invoice for the work completed line, the status is reset to New.

BilledAssigned to all work completed lines on a work order once the invoice is processed (that is, sent to Accounts Receivable).

Table 3. Status combinations applicable once work completed lines are flagged as Ready to BillProv & PreBilling Line is selected for billing, but no invoice has been created and no costs have been posted.
Prov & Billed Line is on a posted invoice, but no costs have been posted.
Prov & Pending Inv Line is on a unposted invoice and no costs have been posted.

## Has Adj

The Has Adj checkbox on the SM Work Orders form, Work Completed tab.
This field is display only and indicates whether the selected work completed line has been adjusted; that is, a cost adjustment line was applied to the selected work completed line. Cost adjustment lines appear with a Status of Adjustment.

##  Adj

The Adj checkbox on the SM Work Orders form, Work Completed tab, and on the related SM Work Completed forms.
Select this checkbox to create a cost adjustment to this work completed line.
Note: You can only create adjustments to Equip, Labor, Misc, and Inventory lines.

## Orig Line #

The

This field also appears on the SM Work Completed form under the Cost Adjustment Info section.
Enter
 the original work completed line to adjust. Press F4 for a list of completed customer work
 order lines.
This
 field is enabled if you have selected either the Adj checkbox on the Work Completed tab
 or the Create
 Adjustment checkbox under the Cost Adjustment Info section of the SM Work
 Completed form.

## Dest SM Co

Dest SM Co # field on the SM Work Orders Work Completed tab.
This field also appears as the SM Co field under the Destination Adjustment section of the Cost Adjustment Info section of the SM Work Completed form.
Defaults to the SM company associated with
 Orig Line #
 field entry.
Enter the company the cost adjustment will be made to. Press
 F4
 for a list of SM companies from which to choose.
This field is enabled if you have selected either the
 Adj
 checkbox on the Work Completed tab or the
 Create Adjustment
 checkbox on the SM Work Completed form, under the Cost Adjustment Info section.

## Dest Work Order

Dest Work Order field on the SM Work Orders Work Completed tab.
This field also appears as the Work Order field under the Cost Adjustment Info drop-down section of the SM Work Completed form.
Enter a
 destination work order for the cost adjustment. Press F4 for a list of customer work orders
 from which to choose.
This
 field is enabled if you have selected either the Adj checkbox on the Work Completed tab
 or the Create
 Adjustment checkbox on the SM Work Completed form, under the Cost
 Adjustment Info section.

## Dest Scope

Dest Scope field on the SM Work Orders Work
 Completed tab.
This field also appears as the Scope Seq field under the Destination Adjustment of the Cost Adjustment Info drop-down section of the SM Work Completed form.
Defaults to the scope associated with the
 Dest Work
 Order entry.
Enter scope for the cost adjustment will be
 made to. Press F4 for a list of work order scopes from which to choose.
This field is enabled if you have selected
 either the Adj checkbox on the Work Completed tab or the Create
 Adjustment checkbox on the SM Work Completed form, under the Cost
 Adjustment Info section.

## Scope Seq

Required.
Enter the work order scope to which this work
 completed entry applies or press F4 to select from a list of valid scopes
 for the work order.
For work completed purchase lines (type 5-Purchase), this field defaults the scope sequence specified for the purchase order item (in SM Purchase Order Entry, PO Purchase Order Entry, or PO Item Distribution) and cannot be changed.
For labor and equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- If you enter a scope that is closed, a message displays indicating such and you will be unable to save the line. You must either reopen the scope or enter a different (open) scope.

- If you change the scope for a work completed line (labor, equipment, miscellaneous, or inventory lines only) and the new scope has a different rate template, the system will recalculate the Bill Rate and Bill Subtotal values.

- Once you bill this work completed line (i.e., the invoice is sent to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Date

Required.
Enter the date for this work completed entry; typically the date the work was completed. Defaults the current date.
Work Completed Labor
 For work completed labor lines, the date entered here determines the start date for the timesheet (header) based on the pay period defined for the technician's payroll group. For example, if you have a pay period of 04/01/12 through 04/07/12, and you enter labor hours for 04/02/12, the timesheet created in PR My Timesheet will have a Start Date of 04/01/12, with time posted on 04/02/12.
However, because timesheets are in 7-day increments, if your pay periods span multiple weeks, the system will use the pay period start "day" to determine the start date for labor hours posted in each week of the pay period. For example, say your pay period runs 04/01/12 — 04/15/12. The start date, 04/01/12, falls on Sunday, so this is the "day" the system will use when determining the Start Date for timesheets posted in each week of the pay period. Therefore, labor hours posted on 04/01/12 through 04/07/12 will have a start date of 04/01/12; labor hours posted on 04/08/12 through 04/14/12 will have a start date of 04/08/12; and labor hours posted on 04/15/12 will have a start date of 04/15/12.
This date cannot be edited if you initiated the work completed line in PR Timecard Entry or you initiated the work completed line in SM Work Orders, but the corresponding timesheet has been approved and sent to a timecard batch.
For labor and equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- You can make changes to this date as long as the new date falls within the specified Post Month. However, once you bill the work completed line (i.e. the invoice is sent to AR), you can only change this date via the SM Invoice Review form (accessed by double-clicking the invoice line).

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

## Non-Billable

The Non-Billable checkbox on the SM Work Orders form, Work Completed tab.
Select this checkbox if this work completed line is not billable (that is, it will not be used to generate an invoice). The Bill Rate, Bill Subtotal, and and tax-related fields will be disabled and default as blank.
Leave this box unselected if this work completed line is billable and will be used to generate an invoice.
The enabling/disabling and defaulting of this field is as follows:

- If this work completed line is associated with a Flat Price work order scope that was manually added or generated from a work order quote or Time of Service, Flat Price agreement service, this field is disabled and defaults as checked. For these lines, work completed is covered in the flat price amount.

- If this work completed line is associated with a Time and Material work order scope that was manually added or generated from a work order quote or Time of Service, Rate Template agreement service, this field is enabled and defaults as unchecked.

- If this work completed line is associated with a Non-Billable work order scope that was manually added or generated from an Included in Agreement or Periodic agreement service, this field defaults as checked and is disabled. For these lines, work completed is covered by the agreement price (Included in Agreement or Periodic, Not Billed Separately services) or the agreement service price (Periodic, Billed Separately services).

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- If this work completed line is associated with an agreement and you have set up spot work coverage for the agreement/service site, this checkbox defaults based on the line type and the spot coverage defined for the agreement/service site. For more information, see [Agreement Covered Spot Work](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-agreement-covered-spot-work).

## Ready To Bill

The Ready to Bill checkbox on the SM Work Orders form, Work Completed tab, and on the
 related SM Work Completed forms (such as SM Work Completed Equipment).
For Customer Work Orders only.
This field only displays if your login is
 associated with a reviewer on the work order; however, it does not display until after you
 have entered and saved the work completed line (either in the Work Completed grid or the
 related Work Completed form).
Select this checkbox to if the work completed
 item is ready to bill.
Note: This field is disabled if:

- The work completed item is marked as Non-Billable.

- The work completed item has already been billed.

## Agreement

For customer work orders only.
This field is enabled/disabled depending on the following:

- If this work completed line is associated with a preventative maintenance work order (i.e. agreement-related work order auto-generated using SM Generate PM Work Order), this field defaults the agreement from the work order scope and is disabled.

- If this work completed line is associated with a quote-generated work order, this field is disabled and defaults as blank.

- If you manually entered the work order scope and:

-  you specified an agreement at the scope level, this field defaults the specified agreement and is disabled.

- you did not specify an agreement at the scope level, this field defaults as null and is enabled. You may enter a valid agreement or leave blank if the work completed line is not associated with an agreement.
Note: If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

## Revision

For customer work orders only.
Display only, the revision number of the agreement specified for this work completed line (at the scope level or line level).

## Agreement Rates

The Agreement Rates checkbox on the SM Work Orders form, Work Completed tab and related work completed forms.
Select this checkbox to derive the billable rate/amount for this work completed line using the rate template assigned to the specified agreement or agreement service.
Leave this checkbox unselected to derive the billable rate/amount for this work completed line using the rate template assigned to the associated work order scope.
This field is enabled and defaults as unselected if you manually added the work order scope and:

-  it is assigned an agreement, has a Time and Material price method, and the
 Agreement Rates
checkbox is unselected.

- it is not assigned an agreement and has a Time and Material price method, but you specified an agreement for the work completed line.

This field is disabled if:

- you generated the work order from an agreement (via SM Generate PM Work Orders) and the work order scope price method is Time and Material or Flat Price. Defaults as selected.

- you generated the work order from an agreement and the work order scope price method is Non-Billable. Defaults as unselected.

- you manually added a Time and Material work order scope, assigned it to an agreement and selected the scope's
 Agreement Rates
 checkbox. Defaults as selected.

- you manually added a Flat Price or Non-Billable work order scope, assigned it to an agreement. Defaults as unselected.

- the work completed line is associated with a closed scope (that is, the work order scope was closed after the work completed line was entered).

## Post Month

This field displays for Equipment, Miscellaneous, and Inventory lines only.
Required.
Enter the posting month (must be an open month) for this work completed line. For Equipment lines, this will become the batch month for equipment usage. For Misc lines, this will become the batch month for posting costs to GL. For Inventory lines, this will be the batch month for material usage (IN). For or purchase order receipts (PO).
For labor and equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- This field initially defaults the current month; however, if you change the date (in the Date field), this field will default the month from the newly entered date. Default may be overridden.

- Once you save the work completed line, this field is disabled and cannot be changed.

## Reference No

Enter a reference number for this work
 completed line, up to 60 characters, if applicable. Initially defaults the reference number
 from existing work completed entries (for the work order) with the same work order scope
 and date, if applicable; otherwise, defaults as null.
You can use the reference number to represent
 any pertinent value; however, reference numbers are primarily intended as a mechanism for
 auto-selecting customer work orders for billing (in SM Work Order Billing) or reporting
 purposes. They are not used anywhere else in the system.Note: Although you cannot bill job
 work orders here in SM, you can use the reference number on job-related equipment lines
 for reporting purposes.If this work completed line is associated with a closed scope
 (i.e. the work order scope was closed after the work completed line was entered),
 this field is disabled and cannot be changed

## Serviceable Item

Enter the serviceable item for this work completed line (i.e. the equipment or item that was serviced) or press F4 to select from a list of valid serviceable items for the specified service site.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Technician

The Technician field on the SM Work Order form, Work Completed tab, and on the related SM Work Completed forms.
Required for 2-Labor line types only.
Enter the technician who performed the work
 associated with this work completed line or press F4 to select from a list of valid SM
 technicians.
For labor and equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- The technician specified here can be from any Payroll company; however, he/she must be set up in SM Technicians for the active SM company and must be flagged as "Active" in PR Employees. If the technician is flagged as "inactive", a warning displays and you will be unable to save the record.

- If this work completed line is associated with a closed scope (that is, a work order scope that was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (send it to AR), edits to this field are only allowed via the SM Invoice Review form (accessed by double-clicking the invoice line).

Note: In order to enter work completed labor lines, you must be set up in VA User Profile with a PR Co and Employee designation, as well as the appropriate My Timesheet Permissions setting (1-Enter for Self or 2-Enter for Self and Others). If this is not done, you will receive an error message once you enter a value in this field. The message displayed depends on whether you are entering time for yourself or for another user. You will be unable to proceed until you set up the required information in VA User Profile. For more information, see [Set Timesheet Permissions](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-timesheet-permissions).

## Standard Item

The Standard Item field on the SM Work Orders form, Work Completed tab.

This field displays for Miscellaneous lines only.
Enter the standard item for this work completed miscellaneous line or leave blank if no standard item applies to this line. Press F4 for a list of valid standard items.
 You will generally use this field to identify work order charges that are not specific to labor, equipment, or parts on a work order. If you select an existing standard item, it will be used to default the Cost Rate and Bill Rate values for this line.

- If the work order scope specified for this line has a Price Method of Non-Billable or Flat Rate, the Bill Rate will be set to blank (and cannot be changed), regardless of whether the standard item specifies a Bill Rate.

- If the work completed miscellaneous line originated in AP Transaction Entry, the Cost values will default from the AP transaction; the cost rate defined for the standard item will not be used. Changes to the cost rate must be handled directly in AP Transaction Entry.

- For work completed miscellaneous lines that originated in SM Work Orders, if the work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

Note: For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## AP Reference

The AP Reference field on the SM Work Orders form, Work Complete tab.

Display-only field applicable to Miscellaneous work complete lines generated from AP only.
Shows the AP reference specified for the AP invoice line and cannot be changed.

## Labor Code

This field displays for Labor lines only.
Enter the labor code for this work completed
 labor entry or press F4 to select from a list of valid labor
 codes.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Description

The Description field on the SM Work Orders form, Work Completed tab, and the SM Work Completed Labor and SM Work Completed Misc forms.
This field displays for Labor and Miscellaneous lines only.
Enter a description, up to 60 characters.
 For work completed labor lines, this will be
 a description of the labor performed. If you entered a labor code in the Labor Code
 field, this field defaults the labor code description (as defined in SM Labor Codes); may
 be overridden.
For miscellaneous lines, this will be a
 description of the miscellaneous charge. If you entered a standard item in the Item field
 (left), this field defaults the description defined for the standard item in SM Standard
 Items. If you entered a free-form value in the Item field, this field defaults as
 "Standard Item not on file"; may be overridden.

- When processing invoices (via SM Invoice Review), the system will automatically truncate descriptions exceeding 30 characters to accommodate the 30-character allowance for invoice lines in AR.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## SM Cost Type

The SM Cost Type field on the SM Work Orders form, Work Completed tab and related work completed forms.
Enter the cost type (from SM Cost Types) that applies to this work completed line. You must specify a cost type that is assigned an SM Cost Type Category that is valid for the work completed line type. For example, if you are entering a work completed Equipment line, you must assign a cost type with a category of E-Equipment. This does not apply to work completed miscellaneous lines, which will allow any SM cost type, regardless of the cost type category.
This field is disabled as follows:

- For Labor and Equip lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and can only be changed via PR Timecard Entry.

- For work completed Misc lines generated from an AP invoice (via AP Transaction Entry or AP Unapproved Invoice Posting), this field defaults from the invoice line and can only be changed via AP Transaction Entry.

- For work completed Purchase lines, this field defaults from the purchase order item and can only be changed via the SM Purchase Order Entry or PO Purchase Order Entry forms.

- For work completed lines associated with a closed scope (where the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- Once you create and process an invoice (send it to AR), this field is disabled; however, you can change the SM Cost Type via the SM Invoice Review form (by double-clicking the invoice line or selecting the invoice line and selecting Edit Record).

## EM Co

This field displays for Equipment lines only.
Required.
Enter the EM company for the equipment used to
 complete this work order. Defaults the EM Co specified for the active SM company
 in SM Company Parameters.
For equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Equipment

This field displays for Equipment lines only.
Required.
Enter the equipment (from EM Equipment) used
 to perform the work on this work order. Equipment must be flagged as Active or Down in EM
 Equipment. Press F4 for a list of valid equipment.
For equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Rev Code

This field displays for Equipment lines only.
Required.
Enter the revenue code that applies to this equipment work completed line. Defaults the revenue code assigned to the equipment in EM Equipment, if applicable.
For equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.
The revenue code will be used to derive the
 Cost
 Rate for this work completed line. The system defaults the Cost Rate for
 the equipment/revenue code from EM Revenue Rates by Equipment. If no rate is defined for
 the equipment/revenue code, the system uses the rate defined for the equipment
 category/revenue code in EM Revenue Rates by Category.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Time Units

For Equipment lines only. This field is
 enabled only when the specified revenue code is hour-based (i.e. the Revenue Basis
 is Hour in EM Revenue Codes).
Enter the number of time units (of the Time UM
 shown to the left) for this work completed equipment line. When updating the equipment's
 usage to EM (upon saving the record), the system will convert these units to hours using
 the Hour/Time
 Unit defined for the specified revenue code (in EM Revenue Codes) and store
 them in the Revenue Detail table (EMRD).
For equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

-  If you selected the Update Hour
 Meter checkbox for the revenue code in EM Revenue Rates by Equipment
 or EM Revenue Rates by Category, the hours will be updated to the equipment’s hour
 meter.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Work Units

This field displays for Equipment lines only
 and is only enabled when the specified revenue code is unit-based (i.e. the Revenue Basis
 is Unit in EM Revenue Codes).
Enter the number of work units (of the Work UM displayed to the left) for this work completed equipment entry.
For equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Pay Type

This field displays for Labor lines only.
Required.
Enter the pay type (from SM Pay Types) for this work completed labor entry. The pay type specified here will be used to determine the Cost Rate for this work completed line as follows:

-  If the pay type's Cost Method is 'Multiplier', the pay type factor will be used in conjunction with the technician's pay rate (defined in SM Technicians) to determine the Cost Rate.

- If the pay type's Cost Method is 'Dollar Rate', the rate defined for the pay type is used as the Cost Rate.

This pay type will be updated to the technician's timesheet (in PR My Timesheet) and will determine the default earnings code (which may be overridden).
For labor lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Craft

This field displays for Labor lines only.
Required.
Enter the craft under which this technician
 worked for this work completed line or press F4 to select from a list of valid
 crafts.
This field initially defaults the craft assigned to the technician in PR Employees (if applicable). However, if the craft template associated with the work order or job (if a job work order) has a reciprocal agreement with a type of Override, the system will override the employee's standard craft with the Job Craft specified on the craft template (in PR Craft Template).
For labor lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.
The system will use this craft in conjunction with the class (specified to the right) to determine pay rates when processing payroll for this technician (in PR Payroll Process).

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Class

This field displays for Labor lines only.
Required.
Enter the class (from PR Craft Classes) under which this technician worked for this work completed line. Initially defaults the class assigned to the technician in PR Employees.
If the craft template associated with the work order or job (if a job work order) has a reciprocal agreement with a type of Override, the system will override the employee's standard craft with the Job Craft specified on the craft template (in PR Craft Template). If the employee's standard class does not exist for the Job Craft, you must either set up the class for the Job Craft in PR Craft Classes and in PR Craft Class Templates or select a valid class already set up for the Job Craft.
For labor lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.
 The class specified here will be updated to the technician's timesheet (in PR My Timesheet) and will be used in conjunction with the craft (specified to the left) to determine pay rates when processing payroll for this technician.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Shift

This field displays for Labor lines only.
Required.
Enter the shift worked by this technician when working on the specified work order scope. Initially defaults the shift assigned to the technician in PR Employees or '1' if no shift assigned.
For labor lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.
 The shift specified here will be updated to the technician's timesheet (in PR My Timesheet) and will be used to determine pay rates when processing payroll for this technician.

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Hrs Worked / Cost Qty

The Hrs Worked / Cost Qty field on the SM Work Orders form, Work Completed grid.

This title of this field differs depending on line type as follows:
Hrs WorkedThis field displays for 2-Labor lines only.
Required.Enter the number of hours the employee worked; that is, the actual hours for which the employee will be paid.
For labor lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- If this work completed line is associated with a closed scope (the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

Cost QtyThis field displays for 3-Misc and 4-Inventory lines only.
Enter the cost quantity for this work completed line.
 For work completed Inventory lines, this field defaults as blank. For work completed miscellaneous lines, this field defaults as follows:

- If you specified a standard item for this line and the Cost Rate defined for the standard item (in SM Standard Items) is not 0.000, this field defaults to 1.000.

- If you specified a standard item and the Cost Rate is 0.000, or you did not specify a standard item for the line, this field defaults as blank.

- If this work completed miscellaneous line originated in AP Transaction Entry, this field is disabled and cannot be edited.

- For work completed miscellaneous lines that originated in SM Work Orders, if the work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## IN Co

The IN Co field on the SM Work Orders form, Work Completed tab.
This field displays for Inventory lines only.
If the material used for this work order was pulled from inventory, enter the IN company from which the material was pulled or press F4 to select from a list of valid IN companies.
This field initially defaults the IN company specified for the active SM company in SM Company Parameters. If you specify a technician for the line, this field then defaults to the IN company specified for the technician in SM Technicians.
If the material used for this work order was not pulled from inventory, you can either accept the default or clear the field. The system will only use the value in this field if you enter a location in the Location field.
Note: If this work completed line is associated with a closed scope (that is, the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed. For work completed lines not associated with a closed scope, once you create and process an invoice (send it to AR), edits to this field are only allowed via the SM Invoice Review form (accessed by double-clicking the invoice line or selecting the line and clicking Edit Record).

## IN Location

The IN Location field on the SM Work Orders form, Work Completed tab.
This field displays for Inventory lines only and is enabled if you entered a company in the IN Co field.
Entry in this field is only required when capturing materials pulled from inventory.
This field initially defaults the IN company specified for the active SM company in SM Company Parameters. If you specify a technician for the line, this field then defaults to the IN company specified for the technician in SM Technicians. You may override the default as needed.

- If the material used for this work order was not pulled from inventory, you can either accept the default or clear the field. The system will only use the value in this field if you enter a location in the Location field.

- If you used a stocked material, accept the default or enter the IN location from which the material was pulled. Press F4 for a list of valid locations for the specified IN company.

- If you used a non-stocked or non-standard material, leave this field blank.

Note: If this work completed line is associated with a closed scope (that is, the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed. For work completed lines not associated with a closed scope, once you create and process an invoice (send it to AR), edits to this field are only allowed via the SM Invoice Review form (accessed by double-clicking the invoice line or selecting the line and clicking Edit Record).

## PO Co

This field only displays for work completed purchase lines (type 5-Purchase).
Display only, the PO company for the specified purchase order.

## PO #

This field only displays for work completed purchase lines (type 5-Purchase).
Display only, the PO number assigned to the purchase order in SM Purchase Order Entry or PO Purchase Order Entry.

## PO Item

This field displays for Purchase lines only.
Display only, the PO item associated with this work completed purchase line.

## PO Item Line

This field displays for Purchase lines only.
Display only, the PO item line associated with this work completed purchase line.
Note: PO item lines are part of the [PO Item Distribution](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-item-distribution-form) feature. If you do not use this feature, this field will always default as 1.
Tip: If you do not use the PO Item Distribution feature, you can hide the field using the [Field Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form) form (F3).

## PO Vendor

The PO Vendor field on the SM Work Order form, Work Completed tab.

This field is only visible for Purchase work completed lines only.
Display only, the vendor specified for the purchase order invoice in AP Transaction Entry. The system populates this field once you post the transaction (via AP Batch Process).

## PO Vendor Name

The PO Vendor Name field on the SM Work Orders form, Work Completed tab.

This field is only visible for Purchase work completed lines only.
Display only, the vendor's name from the purchase order invoice in AP Transaction Entry. The system populates this field once you post the transaction (via AP Batch Process).

## AP References

The AP References field on the SM Work Orders form, Work Completed tab.
This field is only visible for Purchase work completed lines only.
Display only, the AP reference number specified for the purchase order invoice in AP Transaction Entry. The system populates this field once you post the transaction (via AP Batch Process)

## Material

This field displays for Inventory and Purchase lines only.
For work completed inventory lines, enter the material used for the specified work order scope as follows:

- If you entered an IN Co and Location, enter a valid
 material for the location or press F4 to select from a list of valid
 materials.

- If you did not enter an IN Co and Location, enter a valid HQ Material or enter a non-standard material (one that is not in HQ Materials).

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

For work completed purchase lines, this field defaults the material specified on the purchase order item and is disabled. If this is a non-material purchase order, this field defaults as blank and is disabled.

## Material Description

The Material Description field on the SM Work Orders form, Work Completed tab.

This field displays for Inventory lines only.
For stocked and non-stocked materials, this field defaults the material description from HQ Materials. You may override the description as needed.
Note: Changing the description for a material here does not update the description in HQ Materials.

For non-standard materials (those not in HQ Materials), this field defaults as "Nonstandard Material". Enter a description of the material.

## Material Category

The Material Category field on the SM Work Orders form, Work Completed tab.

For stocked and non-stocked materials, this field defaults the category assigned to the material in HQ Materials and cannot be changed.
For non-standard materials (not in HQ Materials), this field defaults as blank. Enter the material category or press F4 to select from a list of valid material categories.

## Cost UM

The UM field on the SM Work Orders form, Work Completed tab.

This field displays for Inventory and Purchase lines only.
Accept the default or enter the Cost UM to use for this work completed line (cannot be LS).
For Inventory lines, this field defaults based on the material as follows:

- Stocked Materials (Inventory lines only) - Defaults the Standard UM defined for the material in HQ Materials. If you override the default value, you must enter a valid UM defined for the material on the Addl UMs tab in IN Location Materials.

- Non-stocked Materials (pulled from HQ Materials) - Defaults the standard UM defined in HQ Materials. If you override the default value, you must enter a valid UM defined for the material in HQ Materials.

- Non-Standard Materials (not in IN or HQ) - Defaults to EA. Accept the default or enter the new unit of measure (cannot be LS). Press F4 to select from a list of valid units of measure.

For work completed purchase lines, this field defaults from the purchase order item and cannot be changed.
This field is disabled if:

- The work completed line is associated with a closed scope (that is, the work order scope was closed after the work completed line was entered.

- You created and processed an invoice (sent it to AR) for the work completed line; in which case, you can only make changes to this field via the SM Invoice Review form (by double-clicking the invoice line or choosing the line and selecting Edit Record).

## Quantity

The Quantity field on the SM Work Orders form, Work Completed tab.

This field displays for Purchase lines only.
Display only, the quantity specified for the PO item. For purchase order items with a UM of LS (that is, the material is non-valid or no material was specified), this field defaults as 0.00 and is disabled.
Note: Edits to this quantity can only be made at the purchase order item level (in SM Purchase Order Entry or PO Purchase Order Entry). Once you post the PO batch, the system will update the quantity here.

## Cost UC

The Cost UC field on the SM Work Orders form, Work Completed tab and the SM Work Completed Misc, Inventory, and Purchase forms.
This field displays for Misc, Inventory, and Purchase lines only; however, it is only enabled for Inventory lines and Misc work completed lines entered in SM.
Enter the unit cost for this work completed line or accept the defaulted value.
This field defaults as follows:
Miscellaneous LinesFor Misc lines generated from an AP invoice, this field defaults the unit cost from the AP transaction line and is disabled. If a Misc Amt was posted to the invoice line, this field includes the Misc Amt (Gross Amt + Misc Amt / Units). You may only make changes to this value in AP Transaction EntryFor Misc lines entered directly in the Work Completed grid or the SM Work Completed Misc form, this field defaults as follows:

- If you entered a standard item that is assigned a cost rate in SM Standard Items, this field defaults the cost rate for the standard item.

- If you entered a standard item that is not assigned a cost rate or you did not enter a standard item, this field defaults as blank.

Inventory LinesDefaults the unit cost as follows:

- If you enter a location material, this field defaults the unit cost based on the Pricing Option for Service Sales in IN Company Parameters (Add'l Info tab) and the selected unit cost and markup/discount rate defined for Service in IN Location Materials. For example, if the Pricing Option for Service Sales is 1-Average Cost plus markup, this field defaults a calculation of the Avg Unit Cost plus the Service markup rate in IN Location Materials (Costs/Qtys tab).

- If you enter an HQ Material (no location specified), this field defaults the Standard Unit Cost defined for the material in HQ Materials.

- If you enter a non-valid material (not in IN Location Materials or HQ Materials), this field defaults to 0.00.

Note: You can only override the defaulted Cost UC value if the Allow Unit Cost Overrides checkbox is selected in IN Company Parameters.

Purchase LinesDefaults the unit cost from the purchase order item and is disabled. You may only change this value in SM Purchase Order Entry or PO Purchase Order Entry

## Cost Subtotal

The Cost Subtotal field on the SM Work Orders form, Work Completed tab and related work completed forms.

Displays only for 3-Misc, 4-Inventory and 5-Purchase lines.
This field defaults a calculation of Cost Qty x Cost Rate. You can only edit this value for:

- Misc lines entered directly in the Work Completed grid or related form.

- Inventory lines when the Allow Unit Cost Overrides checkbox is selected in IN Company Parameters.

For Misc lines generated via AP Transaction Entry, this amount is the sum of the AP line's Gross amount and the Misc Amt.

## Cost Tax Type

The Cost Tax Type field on the SM Work Orders form, Work Completed tab, and on the SM Work Completed Misc, SM Work Completed Inventory, and SM Work Completed Purchase forms.

This field applies to work completed Misc, Inventory, and Purchase lines only; however, it is enabled for Misc lines entered directly in SM and Inventory lines only.
Displays the cost tax type for the work completed line.

- 1-Sales

- 2-Use

- 3-VAT

Miscellaneous LinesFor Miscellaneous lines generated from an AP invoice, this field defaults the tax type from the AP transaction line. You may only make changes to this value in AP Transaction Entry. For Miscellaneous lines entered in the Work Completed grid or in the SM Work Completed Misc form, this field defaults based on the taxability of the line's SM Cost Type and the scope's Material Tax Override and Tax Option Override options. If the Tax Option Override field is blank for the work order scope, the system uses the Tax Option defined for the scope's Call Type to determine taxability.
Note: If the service site or service center (depending on the scope's Tax Source) is not assigned a tax code, the Tax Type field defaults as blank, regardless of the line's taxability and the scope settings. You may override any default as needed; however, only 1-Sales and 2-Use tax options are allowed. The 3-VAT option is only allowed for Misc lines entered in AP.

SM Cost TypeMaterial Tax OverrideTax OptionDefault
Not TaxableBlank, No Tax, Sales, UseAllBlank
TaxableBlank, No TaxBlank, N-Not Taxable, B-Taxable at Billing OnlyBlank
Sales Tax OnlyBlank, N-Not Taxable, B-Taxable at Billing OnlyBlank
P-Taxable at Purchase Only, M-Taxable at Purchase/Markup at Billing, F-Full Tax at Purchase and Billing1-Sales
Use Tax OnlyBlank, N-Not Taxable, B-Taxable at Billing OnlyBlank
P-Taxable at Purchase Only, M-Taxable at Purchase/Markup at Billing, F-Full Tax at Purchase and BillingBlank (if non-material SM CT)2-Use (if material SM CT)

Inventory LinesThis field defaults based on the taxability of the line's SM Cost Type and the scope's Material Tax Override and Tax Option Override options. If the Tax Option Override field is blank for the work order scope, the system uses the Tax Option defined for the scope's Call Type to determine taxabilityNote: You may override the default as needed; however, if you specify an inventory location, only tax option 2-Use is allowed.

SM Cost TypeLocation MaterialMaterial Tax OverrideTax OptionDefault
Not TaxableNot TaxableBlank, No Tax, Sales, or UseAllBlank
Taxable
TaxableNot TaxableNo Tax, Sales, or UseAllBlank
TaxableNo TaxAllBlank
Sales or UseBlank, N-Not Taxable, B-Taxable at Billing OnlyBlank
P-Taxable at Purchase Only, M-Taxable at Purchase/Markup at Billing, F-Full Tax at Purchase and Billing2-Use
Note: For Inventory lines entered without an IN Location, the default behavior is the same as for Misc lines. See the [Miscellaneous Lines](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-5d19be6a-77c6-475f-bccf-2710bc2177f1--en__MiscLines) table above.

Purchase LinesThis field defaults the tax type from the purchase order line. You may only change this value in SM Purchase Order Entry or PO Purchase Order Entry.

## Cost Tax Code

The Cost Tax Code field on the SM Work Orders form, Work Completed tab, and on the SM Work Completed Misc, SM Work Completed Inventory, and SM Work Completed Purchase forms.

This field applies to work completed Misc, Inventory, and Purchase lines only;
 however, it is only enabled for Misc lines entered directly in SM and for Inventory
 lines.
Accept the default value or enter the cost tax code for this work completed line. Must be a valid tax code for the specified tax type.
This field defaults as follows:

- For Miscellaneous lines generated from AP Transaction Entry,
 this field defaults the tax code from the AP invoice transaction line and is
 disabled. You may update the tax code if needed in AP Transaction Entry.For
 Miscellaneous lines entered directly in the Work Completed grid or the SM
 Work Completed Misc form, this field defaults the tax code from the service
 site or the service center, depending on the tax source specified for the
 work order scope. If no tax code is specified for the service site or
 service center, this field defaults as blank. You may override the default
 as needed

- For Purchase lines, this field defaults the tax code from the PO item and is
 disabled. You may update the tax code if needed in SM Purchase Order Entry or PO
 Purchase Order Entry.

- For Inventory lines, this field defaults the tax code from
 the service site or the service center, depending on the tax source specified
 for the work order scope. If no tax code is specified for the service site or
 service center, this field defaults as blank. You may override the default as
 needed.

## Cost Tax Basis

The Cost Tax Basis field on the SM Work Orders form, Work Completed tab, and the SM Work Completed Misc, SM Work Completed Inventory, and SM Work Completed Purchase forms.

This field applies to work completed Misc, Inventory, and Purchase lines only;
 however, it is enabled for Misc lines entered directly in SM and Inventory lines
 only.
Enter the cost tax basis or accept the defaulted amount.
This field defaults as follows:

- For Miscellaneous lines generated from AP Transaction Entry,
 this field defaults the tax basis from the AP invoice transaction line and is
 disabled. You may change the tax basis, if needed, in AP Transaction
 Entry.For Miscellaneous lines entered directly in the Work Completed grid
 or the SM Work Completed Misc form, this field defaults from the Cost
 Subtotal.

- For Purchase lines, this field defaults the tax basis from the PO item and is
 disabled. You may change the tax basis, if needed in SM Purchase Order Entry or
 PO Purchase Order Entry.

- For Inventory lines, this field defaults from the Cost
 Subtotal.

## Cost Tax Amt

The Cost Tax Amt field on the SM Work Order form, Work Completed tab, and on the SM Work Completed Misc, SM Work Completed Inventory, and SM Work Completed Purchase forms.

This field applies to work completed Misc, Inventory, and Purchase lines only.
The cost tax amount defaults as the cost tax basis x the tax rate for the specified cost tax code.
Note: If the Cost Tax Basis is not 0.00, but the Cost Tax Code has a rate of 0.00, this field is set to 0.00. Likewise, if the Cost Tax Basis is 0.00 (not blank), the system sets this amount to 0.00. However, in both cases, the system leaves the specified Cost Tax Type, Cost Tax Code, and Cost Tax Basis designations intact.

For Miscellaneous lines entered directly in this grid, you can override the
 tax amount if needed..
For Miscellaneous lines generated from AP Transaction Entry, this field
 defaults the tax amount from the AP invoice transaction line and is disabled.
For Purchase lines, this field defaults the tax amount from the PO item and is disabled.

## Cost Rate

The Cost Rate field on the SM Work Orders form, Work Completed tab.

Display only.
For lump sum (LS) items, this field is blank. For unit-based items, this field defaults based on the work completed line type as follows:Equipment LinesThe Cost Rate defaults from EM Revenue Rates by Equipment or EM Revenue Rates by Category (if no rate is defined at the equipment level), depending on the equipment and revenue code specified for the line. The system multiplies the Cost Rate by either the Time Units (if hour-based revenue code) or the Work Units (if unit-based revenue code) to derive the cost total (Actual Cost), which cannot be changed.Labor LinesThe Cost Rate defaults based on the technician and pay type specified on the line, as well as the cost method specified for the pay type as follows:

- If the cost method is Multiplier, the Cost Rate is a calculation of the technician's pay rate (from SM Technicians) x the pay type's factor. For example, if the pay rate is $55 and the factor is 1.5, the Cost Rate will be $82.50.

- If the cost method is Dollar Rate, the Cost Rate defaults the rate specified for the pay type in SM Pay Types.

Note: The system calculates the Cost Hrs x Cost Rate and displays the value in the ​Total Projected Cost​ field. Once payroll is processed and the employee paid, the system populates the Total Actual Cost field with the actual amount paid to the employee.
Miscellaneous LinesThese lines default a Cost Rate as follows:

- For Misc lines generated from an AP transaction, this field defaults as follows:

- If you did not apply taxes or a Misc Amt to the AP transaction, this field defaults equal to the Cost UC.

- If you applied taxes and/or a Misc Amt to the AP transaction, this field includes the posted tax and/or Misc Amt (calculated as Total Actual Cost / Cost Qty).For example, say the AP transaction Units=100, the Gross=1,000, the Misc Amt=50, and the Tax Amt=100, resulting in a Total Actual Cost of $1,150. In this case, the Cost Rate for the resulting Misc line will equal $11.50 ($1,150 / 100).

- For Misc lines entered directly in SM (via the Work Completed grid or the SM Work Completed Misc form) with no taxes applied, this field defaults equal to the Cost UC. If you applied cost taxes to the line, this field includes the tax amount (calculated as Total Actual Cost / Cost Qty).

Inventory LinesThe Cost Rate defaults as follows:

- If the work completed line does not include taxes, this field defaults equal to the Cost UC.

- If the work completed line includes taxes, this field includes the tax amount (calculated as Total Actual Cost / Quantity).

Purchase LinesThe Cost Rate defaults the unit cost from the purchase order item. However, if the purchase order item includes tax (Sales or Use), the Cost Rate for the resulting work completed purchase line includes the tax amount. For example, if the PO item is posted with 100.000 units, a unit cost of 5.00000, and tax of 50.00, the Cost Rate for the resulting work completed purchase line would be 5.500 (Total + Tax / Units). For purchase order items with a UM of LS (that is, material is non-valid or no material was specified), this field defaults as 0.00, regardless of whether you post tax to the line or not.

### Value Added Tax (VAT)

If you entered a Provincial Sales Tax (PST) code, the cost rate includes the PST amount. If you entered a Goods and Services Tax (GST) code, the cost rate excludes the GST amount. For multi-level tax codes that include both PST and GST, only the PST portion is included in the tax amount.

## Cost ECM

The Cost ECM field on the SM Work Orders form, Work Completed tab and related work completed forms.

This field only displays when the line type is 4-Inventory or 5-Purchase; however, it is enabled for Inventory lines only.
Specify the quantity that the Cost UC represents.

- E - Per each

- C - Per Hundred

- M - Per Thousand

For work completed inventory lines, this field defaults based on the material as follows:

- Stocked Material (pulled from INCo/Location) - Defaults from IN Location Materials based on the unit cost (last, average, or standard) or unit price used. For example, if using a material rate basis of V-Average Cost (in SM Rate Templates), this field defaults the ECM defined in the Avg Unit Cost field in IN Location Materials (Costs/Qtys tab).

- Non-stocked Materials (pulled from HQ Materials) - Defaults the ECM defined for the standard unit cost in HQ Materials.

- Non-Standard Materials (not in IN or HQ) - Defaults as E.

For work completed purchase lines, this field defaults from the purchase order item and is disabled. However, you can change this value for the related purchase order item (in SM Purchase Order Entry or PO Purchase Order Entry).
Note: For both Inventory and Purchase lines, if you change the Cost ECM value, the system automatically updates all related cost and billing values on the work completed line (Cost Subtotal, Cost Tax Basis, Cost Tax Amt, Bill Rate, and so forth).
 Please note, if you change the Cost ECM and then change the cost quantity, the Cost ECM is not updated.

## Total Projected Cost

The Total Projected Cost field on the SM Work Orders form, Work Completed grid.

This field displays for Labor and Purchase lines only.
Display only, the projected total cost for the work completed line.
The system calculates this value as follows:

- Labor - Cost Hrs x Cost Rate.

- Purchase - Quantity x Cost Rate.

Note: Purchase lines with lump sums (UM = LS) will have Quantity and Cost Rates of "0"; the
 Projected Cost Total
 column will reflect the lump sum total of the PO.

## Invoiced Units

The Invoiced Units field on the SM Work Orders form, Work Completed grid and the SM Work Completed Purchase form.

This field displays for work completed Purchase lines only.
Display only, the invoiced units for this work completed line. This field initially defaults as null. Once you invoice the purchase order item (in AP Transaction Entry), this field defaults the value from the AP transaction.

## Total Actual Cost

The Total Actual Cost field on the SM Work Order form, Work Completed grid.

This field is display only.
Defaults the total actual cost for the work completed line (if applicable). The system calculates this value as follows:

- 1-Equip - Defaults a calculation of Time Units x Cost Rate or Work Units x Cost Rate

- 2-Labor - Initially defaults as null. Once payroll is processed for the employee (technician), this field defaults the value from Payroll. If the employee has a SM Fixed Rate defined (in PR Employees), the actual cost calculation is based on the fixed rate, the SM Pay Type specified for the time entry, and the hours posted for the employee. For more information, see [SM Fixed Rate](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-0003814a--en).Note: If you have implemented 'bEmployee' datatype security and have secured the PRTH (PR Timecard Header) view, you will only see a value in this field if you have access to the specified employee; otherwise, this field displays as 0.00.

- 3-Misc - For Misc lines entered directly in the Work Completed grid (or the related SM Work Completed Misc form), this defaults a calculation of the Cost Subtotal + Cost Tax Amt (if applicable).For Misc lines generated from AP Transaction Entry or AP Unapproved Invoice Posting, this field defaults the invoice line's Gross amount + Misc Amt (if applicable) + Tax Amt (if applicable).

- 4-Inventory - Defaults a calculation of the Cost Subtotal + Cost Tax Amt (if applicable).

- 5-Purchase - Initially defaults as null. Once you invoice the purchase order (in AP Transaction Entry), the system updates this field with the actual cost from the AP transaction: Gross + Misc Amt (if applicable) + Tax Amt (if applicable). If the AP transaction includes a Misc Amt or the Tax Amt differs from the tax amount on the purchase order item, this value may differ from the Total Projected Cost. You can see the details of the AP transaction on the AP History tab on the SM Work Completed Purchase form.

### Value Added Tax (VAT)

If you entered a Provincial Sales Tax (PST) code, the Total Actual Cost includes the PST amount. If you entered a Goods and Services Tax (GST) code, the Total Actual Cost excludes the GST amount. For multi-level tax codes that include both PST and GST, only the PST portion is included in the Total Actual Cost.

## Received Units

This field only displays for work completed purchase lines (type 5-Purchase) when the UM for the purchase order item is not LS.
Display only, the units received against the purchase order item for this work completed purchase line. The system updates this field automatically when you receive units against the PO item in PO Receipts Entry.
Note: If you did not specify to receive the PO item (the
 Receiving box was not checked in SM Purchase Order Entry or PO Purchase
 Order Entry), this field will be updated when you invoice this line in AP Transaction
 Entry.

## Bill Hrs / Bill Qty

The Bill Hrs / Bill Qty field on the SM Work Orders form, Work Completed grid.
This title of this field differs depending on line type as follows:
Bill HrsThis field displays for 2-Labor lines only.Required.
Enter the number of billable hours for this work completed labor line. Defaults the number of hours specified in the Hrs Worked field.
This value is typically the number of hours charged for work done by this technician on the specified work order scope. However, you can use this field to enter "minimum" or "maximum" billable hours. For example, you might charge a minimum of one hour, even if the technician worked less than one hour.
Note: This field is disabled if:

- the Non-Billable checkbox is selected for the work completed line. Since the line is non-billable, this field defaults to blank.

- the work completed line is for a job work order with a Costing Method of Actual Cost. The value in this field will be set equal to the Cost Quantity.

Once you bill the work completed line (via SM Invoice Review for customer work orders and via Job Billing or Accounts Receivable for job work orders), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).
Bill QtyThis field displays for 3-Misc and 4-Inventory lines only.
Enter the billable quantity for this work completed line. Initially defaults from the line's Cost Qty, but you may override as needed.
Note: This field is disabled if:

- the Non-Billable checkbox is selected for the work completed line. Since the line is non-billable, this field defaults to blank.

- the work completed line is for a job work order with a Costing Method of Actual Cost. The value in this field will be set equal to the Cost Quantity.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Rate

The Bill Rate field on the SM Work Order form, Work Completed tab and on the related SM Work Completed forms.
Enter the billable rate for the work completed line or accept the default rate.

### Customer Work Orders

For all work completed lines posted to a Flat Price or Non-Billable work order scope, this field defaults as blank and is disabled.
 If you manually select the Non-Billable checkbox (for a work completed line), this field defaults as blank and is disabled, regardless of the scope's price method.
For work completed lines posted to a Time and Material work order scope, this field defaults as follows:
Equipment, Labor, and Misc LinesIf you entered units for the work completed line, this field defaults as Bill Subtotal / Bill Quantity. If you did not enter units for the work completed line (that is, you entered a lump sum amount), this field defaults as blankInventory LinesIf you entered units for the work completed line, this field defaults based on the Material Rates: Type and Materials Rates: Basis settings as follows:

- For scopes assigned a rate template with a Cost basis (Actual, Standard, Average, or Last):

- If the Type is Markup or Discount and no INCo/Location is specified, the bill rate defaults as Std Unit Cost (from HQ Materials) +/- (Std Unit Cost x Markup/Discount %, respectively)

- If the Type is Markup or Discount and an INCo/Location is specified, the bill rate defaults as the selected Basis +/- (Basis x Markup/Discount %, respectively). For example, if the Basis is Average Cost, the bill rate defaults as Avg Unit Cost (from IN Location Materials) +/- (Avg Unit Cost x Markup/Discount %, respectively).If the Basis is Actual Cost, this field calculates as Total Actual Cost +/- (Total Actual Cost x Markup/Discount %, respectively)

- For scopes assigned a rate template with a Price basis:

- If the Type is Markup or Discount and no INCo/Location is specified, the bill rate defaults as Standard Unit Price (from HQ Materials) +/- (Standard Unit Price x Markup/Discount %, respectively)

- If the Type is Markup or Discount and an INCo/Location is specified, the bill rate defaults as Std Unit Price (from IN Location Materials) +/- (Std Unit Price x Markup/Discount %, respectively)

Purchase LinesIf you entered units for the work completed line, this field defaults as Bill Subtotal / Bill Quantity x ECM (1, 100, 1000). If you did not enter units for the work completed line, this field defaults as blank

### Job Work Orders

For all line types, this field defaults based on the Costing Method (Actual Cost or Markup) specified for the work order.

- Actual Cost - For all work completed line types, if you selected this costing method, the system sets the Bill Rate equal to the Cost Rate and disables this field. The only way to change this value is to change the Cost Rate for the line.

- Markup - If you selected this costing method, the Bill Rate defaults in the same manner as Customer Work orders. See the Customer Work orders section above.

### Agreement Work Orders

If the work completed line is associated with a Flat Price or Non-Billable scope or you have manually selected the Non-Billable checkbox for the line.
If the work completed line is associated with a Time and Material scope and the Agreement Rates checkbox is selected for the work completed line, this field is disabled and defaults a value based on the rate template assigned to the agreement. If the Agreement Rates checkbox is unselected, this field is enabled and defaults a value based on the rate template assigned to the agreement service (generated scopes) or work order scope (manually added scopes). May be overridden.
If the work completed line is associated with a non-agreement scope (manually entered with no agreement assigned), but you entered an agreement at the work completed line level, this field defaults as follows:

- If you selected both the Non-Billable and Agreement Rates checkboxes for the work completed line, this field is enabled and defaults a value from the rate template assigned to the work order scope. May be overridden.

- If you selected the Non-Billable checkbox for the work completed line, this field is disabled and defaults as blank.

- If you selected the Agreement Rates checkbox for the work completed line, this field is disabled and defaults based on the rate template assigned to the agreement.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill ECM

The Bill ECM field on the SM Work Order form, Work Completed tab and the SM Work Completed Inventory and SM Work Completed Purchase forms.
This field only displays for Inventory and Purchase lines.
Enter the quantity the billable rate represents or accept the default (defaults from Cost ECM).

- E - Per each

- C - Per Hundred

- M - Per Thousand

Note: If you change the value in this field, the system automatically recalculates the Bill Subtotal and, if applicable, the Bill Tax Basis and Bill Tax Amt.

This field is disabled for:

- work completed lines with the Non-Billable checkbox selected.

- agreement-related work completed lines with the A-Agreement Rates checkbox selected.

- work completed lines on a job work order where the Costing Method is Actual Cost.

- work completed purchase lines on any job work order, regardless of the Costing Method.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Subtotal

The Bill Subtotal field on the SM Work Orders form, Work Completed tab and SM Work Completed forms.
For SM Work Completed Equipment and SM Work Completed Labor forms, this field shows as Billable Total.
For work completed lines referencing a Non-Billable or Flat Price scope,or where the Non-Billable checkbox is manually selected for the work completed line, this field defaults as blank and is disabled.
For work completed lines posted to a Time and Material scope, this field defaults as follows:
Equipment / Labor LinesDefaults as Total Actual Cost (incl tax) + (Total Actual Cost * Template Markup %).Miscellaneous LinesDefaults are as follows:If the work completed line is posted to a non-material SM Cost Type, this field defaults a value of Total Actual Cost (incl tax) + (Total Actual Cost * Template Markup %)
If the work completed line is material-related (posted to a material-related SM Cost Type), this field defaults as follows:

- If the scope's rate template has a type of Markup or Discount and a Cost basis (Actual, Std, Avg, Last), this field defaults a value of Total Actual Cost (incl tax) +/- (Total Actual Cost * Template Markup/Discount %, respectively)

- If the scope's rate template has a type of Markup or Discount and a Price basis, this field defaults a value of Total Actual Cost (incl tax) + (Total Actual Cost * Template Markup %).

For Miscellaneous lines posted in AP Transaction Entry:

- If the scope's rate template has a type of Markup or Discount and a Cost basis (Actual, Std, Avg, Last), this field defaults a value of Total Actual Cost (incl tax) +/- (Total Actual Cost * Template Markup/Discount %, respectively). This applies to transaction lines without a material, with an HQ Material, or with a non-HQ Material.

- If the scope's rate template has a type of Markup or Discount and a Price basis, and a valid HQ Material is specified, this field defaults a value of Total Actual Cost (incl tax) +/- (Total Actual Cost * Template Markup/Discount %, respectively)

- If the scope's rate template has a type of Markup or Discount and a Price basis, but no material is specified or a non-HQ Material is specified, this field defaults a value of Total Actual Cost (incl tax) + (Total Actual Cost * Template Markup %)

Inventory LinesFor Inventory lines, the Bill Subtotal is a calculation of the work completed line's Bill Rate x Bill Qty, with the Bill Rate being based on unit rates from HQ Materials or IN Location Materials. Calculations are as follows: Scopes assigned a rate template with a Cost basis (Actual, Std, Avg, Last):

- If you specify an HQ Material (no INCo/Location), this field defaults as the Std Unit Cost (from HQ Materials) +/- (Std Unit Cost x Markup/Discount %, respectively) x Bill Qty.

- If you specify an INCo/Location, this field defaults as Basis +/- (Basis x Markup/Discount %, respectively) x Bill Qty. For example, if the basis is Avg Unit Cost, the calculation will be Avg Unit Cost (from IN Location Materials) +/- (Avg Unit Cost x Markup/Discount %) x Bill Qty.

- If the Cost basis is Actual, this field defaults as Cost Rate +/- (Cost Rate x Markup/Discount %, respectively) x Bill Qty.

Scopes assigned a rate template with a Price basis:

- If you specify an HQ Material (no INCo/Location), this field defaults as the Std Unit Cost (from HQ Materials) +/- (Std Unit Cost x Markup/Discount %, respectively) x Bill Qty.

- If you specify an INCo/Location, this field defaults as Std Unit Price (from IN Location Materials) +/- (Std Unit Prices x Markup/Discount %, respectively) x Bill Qty.

Purchase LinesDefaults are as follows:

- If the scope's rate template has a type of Markup or Discount and a Cost basis (Actual, Std, Avg, Last), this field defaults a value of Total Actual Cost (incl tax) +/- (Total Actual Cost * Template Markup/Discount %, respectively). This applies to transaction lines without a material, with an HQ Material, or with a non-HQ Material.

- If the scope's rate template has a type of Markup or Discount and a Price basis, and a valid HQ Material is specified, this field defaults a value of Total Actual Cost (incl tax) +/- (Total Actual Cost * Template Markup/Discount %, respectively)

- If the scope's rate template has a type of Markup or Discount and a Price basis, but no material is specified or a non-HQ Material is specified, this field defaults a value of Total Actual Cost (incl tax) + (Total Actual Cost * Template Markup %)

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Tax Type

The Bill Tax Type field on the SM Work Orders form, Work Completed tab, and on the related work completed forms.

### Customer Work Orders

For work completed lines posted to a N - Non Billable or F - Flat Price work order scope, this field defaults as blank and cannot be changed.
For work completed lines posted to a T-Time and Material work order scope, accept the default value or enter the billing tax type for this work completed line.

- 1-Sales

- 3-VAT

For Equip and Labor lines, if the SM Cost Type is taxable, this field defaults the Bill Tax Type from the work order scope or as blank if the work order scope Tax Type is blank. The tax type also defaults as blank if you did not enter a cost type for the work completed line or if the cost type is not taxable.
For Misc, Inventory, and Purchase lines, this field defaults as indicated in the table below. The Tax Option Override options are defined as follows:

- blank

- N=Not Taxable

- P=Taxable at Purchase Only

- B=Taxable at Billing Only

- M=Taxable at Purchase/Markup at Billing

- F=Full Tax at Purchase and Billing

Work Completed SM Cost TypeWO Scope Tax Option OverrideBill Tax TypeCan Override?
blankblank, N, P, B, M, F Defaults as blankYes
Non-Taxableblank, N, P, B, M, FDefaults as blankYes
TaxableblankSystem uses the scope's Call Type Tax Option to determine taxability. If the call type's Tax Option is blank, N, or P, this field defaults as blank.If the call type's Tax Option is B, M, or F, this field defaults the Tax Type from the work order scope.
If the work order scope Tax Type is blank, this field defaults as blank.
Yes
N or PDefaults as blankYes
B, M, F Defaults the Tax Type from the work order scope. If the work order scope Tax Type is blank, this field defaults as blank.Yes

### Agreement-Related Work Orders

When you generate an agreement work order, the Price Method for the resulting work order scopes are set as follows:
Agreement Service Pricing Method: Work Order Scope Price Method
I - Included in AgreementNon-Billable
P - Periodic, Billed SeparatelyNon-Billable
P - Periodic, Not Billed SeparatelyNon-Billable
T - Time of Service, Flat RateFlat Price
T - Time of Service, Rate TemplateTime and Materials

For work completed lines posted to the Non-Billable and Flat Price scopes, the Bill Tax Type field defaults as blank and cannot be changed.
For work completed lines posted to a Time and Materials scope, the Bill Tax Type defaults as shown in the Customer Work Orders table above.

### Job Work Orders

You can only enter cost taxes for work completed lines associated with a Job work order. Therefore, the Bill Tax fields default as blank and are disabled.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Tax Code

The Bill Tax Code field on the SM Work Orders form, Work Completed tab, and on the related work completed forms.

### Customer Work Orders

For work completed lines posted to a N - Non Billable or F - Flat Price work order scope, this field defaults as blank and cannot be changed.
For work completed lines posted to a T-Time and Material work order scope, accept the default value or enter the tax code for this work completed line. Must be a valid tax code for the specified tax type.
For Equip and Labor lines, this field defaults the Bill Tax Code from the work order scope or as blank if the work order scope Tax Code is blank. The tax type also defaults as blank if you did not enter a cost type for the work completed line or if the cost type is not taxable.
For Misc, Inventory, and Purchase lines, this field defaults as indicated in the table below. The Tax Option Override options are defined as follows:

- blank

- N=Not Taxable

- P=Taxable at Purchase Only

- B=Taxable at Billing Only

- M=Taxable at Purchase/Markup at Billing

- F=Full Tax at Purchase and Billing

Work Completed SM Cost TypeWO Scope Tax Option OverrideBill Tax CodeCan Override?
blankblank, N, P, B, M, F Defaults as blankYes
Non-Taxableblank, N, P, B, M, FDefaults as blankYes
TaxableblankSystem uses the scope's Call Type Tax Option to determine taxability. If the call type's Tax Option is blank, N, or P, this field defaults as blank.If the call type's Tax Option is B, M, or F, this field defaults the Tax Code from the work order scope.
If the work order scope Tax Code is blank, this field defaults as blank.
Yes
N or PDefaults as blankYes
B, M, F Defaults the Tax Code from the work order scope. If the work order scope Tax Code is blank, this field defaults as blank.Yes

Note: Although work completed purchase lines are generated from purchase orders entered in SM Purchase Order Entry or PO Purchase Order Entry, the billable tax code does not default from the related purchase order item. Therefore, the tax code for the work completed line may differ from the tax code on the purchase order item.

Note: If you enter a tax basis of 0.00 or if the tax code's rate is set to 0.00, the system sets the Tax Amount to 0.00; however, the Tax Type, Tax Code, and Tax Basis designations are left intact.

### Agreement-Related Work Orders

When you generate an agreement work order, the Price Method for the resulting work order scopes are set as follows:
Agreement Service Pricing Method: Work Order Scope Price Method
I - Included in AgreementNon-Billable
P - Periodic, Billed SeparatelyNon-Billable
P - Periodic, Not Billed SeparatelyNon-Billable
T - Time of Service, Flat RateFlat Price
T - Time of Service, Rate TemplateTime and Materials

For work completed lines posted to the Non-Billable and Flat Price scopes, the Bill Tax Code field defaults as blank and cannot be changed.
For work completed lines posted to a Time and Materials scope, the Bill Tax Code defaults as shown in the Customer Work Orders table above.

### Job Work Orders

You can only enter cost taxes for work completed lines associated with a Job work order. Therefore, all Bill Tax fields default as blank and are disabled.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Tax Basis

The Bill Tax Basis field on the SM Work Orders form, Work Completed tab, and on the related work completed forms.
Applies only to lines with a Tax Type and Tax Code specified.
Enter the tax basis amount for this work completed line or accept the defaulted amount.
Note: If you enter a bill tax basis of 0.00, the system sets the bill tax amount to 0.00; however, the Billing Tax Type, Tax Code, and Tax Basis designations are left intact.

The following describes the default behavior for this field:

- If the work completed line is posted to a N - Non Billable or F - Flat Price work order scope, this field defaults as blank and cannot be changed.

- If the work completed line is posted to a Time and Material work order scope and the Tax Type and Tax Code are blank, this field defaults as blank.

- If the work completed line is posted to a Time and Material work order scope and you entered a Tax Type and Tax Code, this field defaults as shown below.

Equipment and Labor LinesDefaults the Bill Qty x Bill Rate.
Miscellaneous, Inventory, and Purchase LinesFor these work completed lines, this field defaults based on the Tax Option Override specified for the work order scope and whether you entered units or a lump sum amount for the work completed line.
 If the work order scope's Tax Option Override is blank, the system uses the Tax Option specified for the scope's assigned call type. If the call type's Tax Option is blank, this field defaults as blank.
Tax Option Override/Tax OptionUnit-based?Default
Note: Inventory lines do not allow entering lump sum amounts. Therefore, the non-unit based descriptions apply only to work completed Misc and Purchase lines.

N=Not TaxableP=Taxable at Purchase Only
Yblank
Nblank
B=Taxable at Billing OnlyF=Full Tax at Purchase and Billing
YBill Quantity x Bill Rate
N (Misc)Total Actual Cost (incl tax) + (Total Actual Cost x Template Markup/Discount %)*

N (Purchase)Total Projected Cost (incl tax) + (Total Projected Cost x Template Markup/Discount %)*
M=Taxable at Purchase/Markup at BillingYIf Bill Qty is >= Cost Qty, the Bill Tax Basis is calculated as:Bill Subtotal - (Cost Tax Basis + Cost Tax Amt)
If Bill Qty is < Cost Qty, the Bill Tax Basis is calculated as:
Bill Subtotal - ((Cost Tax Basis + Cost Tax Amt) * (Bill Qty / Cost Qty))
Note: If you did not capture taxes when recording costs, there is no credit to apply to the transaction at billing; therefore, the bill tax basis is calculated using the full billing subtotal, not just the markup.

N (Misc)If the Bill Qty is blank and the Bill Subtotal <= 0, then the Bill Tax Basis is set to 0.00If the Bill Qty is blank and the Bill Subtotal > 0, then the Bill Tax Basis is set equal to the Bill Subtotal.

N (Purchase)
* If the work completed line is posted to a non-material SM Cost Type, the system uses the Non-Material Purchases: Markup Percent specified for the rate template. If the work completed line is posted to a material-related SM Cost Type, the system uses the material rate type and basis defined for the template to determine the template markup or discount percent to use. For more information, see [Material Rates: Type](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form/field-definitions-sm-rate-template-form#ID-00043a13--en) and [Material Rates: Basis](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form/field-definitions-sm-rate-template-form#ID-00043a23--en).

Note: The system uses the Tax Option Override assigned to the work order scope to determine the taxability/default behavior for work completed lines. If the work order scope's Tax Option Override is blank, the system uses the Tax Option specified for the scope's assigned call type to determine taxability/tax defaults. If the call type's Tax Option is blank, all bill tax fields default as null and must be entered manually.

### Job Work Orders

You can only enter cost taxes for work completed lines associated with a Job work order. Therefore, all Bill Tax fields default as blank and are disabled.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Tax Amt

The Bill Tax Amt field on the SM Work Orders form, Work Completed tab, and on the related work completed forms.
This field defaults as blank and is disabled if the Non-Billable checkbox is selected for the work completed line.
If you entered a bill tax type and tax code for the work completed line, this field defaults the Bill Tax Amt as follows:

- If the bill tax basis is not 0.00, the system defaults the bill tax amount as a calculation of the tax basis times the tax rate defined for the tax code.

- If the bill tax basis is not 0.00, but the bill tax code has a rate of 0.00, the bill tax amount is set to 0.00; however, the system leaves the specified Bill Tax Type, Bill Tax Code, and Bill Tax Basis designations intact.

- If the bill tax basis is 0.00, the system sets the tax amount to 0.00, but leaves the specified Bill Tax Type, Bill Tax Code, and Bill Tax Basis designations intact.

For Misc, Inventory, and Purchase lines, you can override the default if needed; however, if you change the bill tax amount, the Bill Tax Basis is not recalculated.
For Equipment and Labor lines, this field is disabled.
Note: When you generate an invoice that includes this work completed line (T&M scopes only), the system recalculates the bill tax amount based on the tax rate applicable at the time of bill, if the date on the work completed line is falls before the tax rate Effective Date and the rate has changed for the specified tax code. If it differs from the amount calculated for the work completed line at the time of posting, the amount in this field is updated accordingly.

### Job Work Orders

You can only enter cost taxes for work completed lines associated with a Job work order. Therefore, all Bill Tax fields default as blank and are disabled.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## No Charge

Select this checkbox if the customer/service site will not be charged for the work associated with this work completed entry.
Note: Checking this box does not clear the cost/price information; although the customer/service site will not be charged for the work, the cost/price information will be included on the invoice.
Do not select this checkbox if the customer/service site will be charged for the work associated with this work completed entry. (Default setting).
Once you bill this work completed line (i.e., the invoice is sent to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Total Billable

The Total Billable field on the SM Work Orders form, Work Completed tab.

Display only, the total billable amount for this work completed line. The Total Billable amount is the calculation of the Billable Amount + Billing Tax Amt.
 Changes to this amount can only be handled by changes to other values in the line, as allowable.

## Equip EM Co

The Equip EM Co field on the SM Work Orders form, Work Completed tab.
For customer work orders only.
This field only displays a value if the work completed labor line was generated from PR Timecard Entry for a service timecard including equipment usage.
Display only, the EM Co specified for the service timecard in PR Timecard Entry. This is the EM company that will receive the revenue for the use of its equipment.
Note: Changes to this field can only be made in PR Timecard Entry.

## Equip Equipment

The Equip Equipment field on the SM Work Orders form, Work Completed tab.
For customer work orders only.
This field only displays a value if the work completed labor line was generated from PR Timecard Entry for a service timecard including equipment usage.
Display only, the equipment specified for the service timecard in PR Timecard Entry. This is the equipment used to perform the work for the specified work order and to which revenue will be posted.
Note: Changes to this field can only be made in PR Timecard Entry.

## Equip Rev Code

The Equip Rev Code field on the SM Work Orders form, Work Completed tab.
For customer work orders only.
This field only displays a value if the work completed labor line was generated from PR Timecard Entry for a service timecard including equipment usage.
Display only, the revenue code specified for the service timecard in PR Timecard Entry. This is the revenue code to which equipment usage will be posted.
Note: Changes to this field can only be made in PR Timecard Entry.

## Equip Phase

The Equip Phase field on the SM Work Orders form, Work Completed tab.
This field is not currently in use.

## Equip SM Cost Type

The Equip SM Cost Type field on the SM Work Orders form, Work Completed tab.
For customer work orders only.
This field only displays a value if the work completed labor line was generated from PR Timecard Entry for a service timecard including equipment usage.
Display only, the SM cost type for equipment usage specified for the service timecard in PR Timecard Entry. This cost type will differ from the SM cost type specified for the labor portion of the timecard.
Note: Changes to this field can only be made in PR Timecard Entry.

## Equip JC Cost Type

The Equip JC Cost Type field on the SM Work Orders form, Work Completed tab.
This field is not currently in use.

## Labor Line

The Labor Line field on the SM Work Orders form, Work Completed tab.
This field only displays for Equipment lines on a customer work order.
 If the work completed equipment line was generated from PR Timecard Entry for a service timecard including equipment usage, this display-only field shows the work completed labor line associated with the work completed equipment line. This cost type will differ from the SM cost type specified for the labor portion of the timecard.
If the work completed line was entered manually in SM Work Orders, this field displays as blank.
