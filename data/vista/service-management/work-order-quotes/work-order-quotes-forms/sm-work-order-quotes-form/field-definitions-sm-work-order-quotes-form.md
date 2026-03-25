---
title: "Field Definitions: SM Work Order Quotes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form/field-definitions-sm-work-order-quotes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form/field-definitions-sm-work-order-quotes-form"
---

# Field Definitions: SM Work Order Quotes Form

The following is a list of field descriptions for the SM Work
 Order Quotes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Quote ID

Enter a quote ID (up to 15 characters), or
 enter N, New, or + to have
 the system automatically assign the next sequential quote ID (using the Minimum WO Quote
 ID number defined in SM Company Parameters).
Note: When assigning quote IDs, the system will always check existing quote numbers and assign the first sequential number that is not already in use, regardless of the
 Minimum WO Quote ID
 specified in SM Company Parameters (since this value can be changed at any time). However, once the system assigns the next available quote ID here, it will update the
 Minimum WO Quote ID
 accordingly.

## Description

Enter a description for the quote, up to 60 characters.

## Work Order

The Work Order field on the SM Work Order Quotes form, Header Info tab.
Enter
 the existing work order to use when approving this quote or press F4 to select
 from a list of work orders. The screen automatically populates with the customer and
 service site assigned to the work order.
Note: If you have already entered a customer and service site for the quote and the work order you enter is for a different customer and service site, the system overrides the existing customer and service site with the work order customer and service site. If you entered the wrong work order, entering the correct work order will update the customer and service site accordingly.
Leave
 this field blank if you want the system to assign a new work order number when the quote is
 approved (based on the New Work Order Number field in SM Company
 Parameters).

## New Customer

The New Customer checkbox on the SM Work Order Quotes form, header Info tab.
This checkbox automatically defaults as selected for new work order quotes.
If this quote is for a new customer, accept the default. When this checkbox is selected, the customer name and address fields are enabled.
Note: You must click Create Customer / Site to set up a new customer (in AR Customers and SM Customers) and/or service site (in SM Service Sites). If any required information is missing, the system displays a warning and you must enter the required information and then re-click Create Customer / Site. Once the new customer and/or service is created, the system clears the New Customer and/or New Site checkboxes.

If this quote is for an existing customer, deselect this checkbox. The name and address fields are disabled and will default from SM Customers once you enter the customer ID.

## Customer: ID

The Customer: ID field in the SM Work Order Quotes form, header Info tab.
If you entered a work order for this quote (in the Work Order field), this field defaults the customer from the work order and is disabled.
If you did not enter a work order for the quote, you can enter either a new customer or an existing customer as follows:

- If you selected the New Customer checkbox, enter N or + in this field to have the system generate a number for you. You can also manually enter a customer number, as long as the number is not already in use in AR Customers or SM Customers.
 If you leave this field blank, the system automatically assigns the next available sequential number.
Note: You must click Create Customer / Site to set up a new customer (in AR Customers and SM Customers) and/or service site (in SM Service Sites). If any required information is missing, the system displays a warning and you must enter the required information and then re-click Create Customer / Site. Once the new customer and/or service is created, the system clears the New Customer and/or New Site checkboxes.

- If the quote is for an existing customer (the New Customer checkbox is not selected), enter the customer number or press F4 to select from a list of valid SM Customers. Once you enter the customer number, the screen populates with the customer's name and address information.

 .

## Customer: Name

The Customer: Name field (unlabeled) on the SM Work Order Quotes form, header Info tab.
If you entered a work order for this quote (in the Work Order field) or you entered an existing customer in the Customer ID field, this field defaults the customer name from AR Customers and is disabled.
If you did not enter a work order for the quote, this field is enabled only if you selected the New Customer checkbox.
Enter the name of the customer for this work order quote. Up to 60 characters allowed.
Note: You must click Create Customer / Site to set up a new customer (in AR Customers and SM Customers) and/or service site (in SM Service Sites). If any required information is missing, the system displays a warning and you must enter the required information and then re-click Create Customer / Site. Once the new customer and/or service is created, the system clears the New Customer and/or New Site checkboxes.

## Customer: Address

The Customer Address fields on the SM Work Order Quotes form, Header Info tab.
These fields are enabled only if you left the
 Customer ID field blank.
 If you entered a customer ID, these fields are display only and default the mailing address defined for the customer in AR Customers. Changes to this information in AR Customers will be updated to the corresponding fields here.
Enter the customer's address information in the following fields.

- Address - Enter the mailing address. This can be either the street address or a P.O. Box.

- Add'l Address - Enter additional address information, such as suite number, apartment, etc. If you entered a P.O. Box in the Address
 field, you can use this field to enter the street address.

- City - Enter the city.

- State - Enter a valid state (as defined in HQ
 States). The system validates the state based on the Default Country specified in HQ
 Company Setup for the active company. If not valid, an error displays, but entry is
 allowed. You must then enter a valid country for this state in the Country
 field.

- Zip Code - Enter the zip code or postal code, up to 12 digits.

- Country - Defaults from the Default
 Country field in HQ Company Setup for the active SM company. You will
 only need to change the default if the customer's address exists outside the default
 country.

## Customer Contact: Name

Enter the contact for this customer (up to 60
 characters) or press F4 to select an existing customer, site,
 or HQ contact.

## Customer Contact: Phone

Enter the phone number of the contact specified above. If you selected an existing contact, this field defaults the phone number defined for the contact in HQ Contacts.

## Center

Enter the service center that will be used to perform the work detailed on this quote. This service center will be used as the default for any work orders generated from this quote; may be overridden.

## New Site

The New Site checkbox on the SM Work Order Quotes form, header Info tab.
This checkbox automatically defaults as selected for new work order quotes.
If this quote is for a new service site (applies to new and existing customers), accept the default. When this checkbox is selected, the site address fields are enabled.
Note: You must click Create Customer / Site to set up a new customer (in AR Customers and SM Customers) and/or service site (in SM Service Sites). If any required information is missing, the system displays a warning and you must enter the required information and then re-click Create Customer / Site. Once the new customer and/or service is created, the system clears the New Customer and/or New Site checkboxes.

 If this quote is for an existing service site (existing customers only), deselect this checkbox. The address fields are disabled and will default from SM Service Sites once you enter the site ID.

## Site: ID

The Site: ID field in SM Work Order Quotes, Info tab.
If you entered a work order for this quote (in the Work Order field), this field defaults the service site from the work order and is disabled.
If you did not enter a work order for the quote, you can enter either a new service site or an existing service site as follows:

- If you selected the New Site checkbox (for a new or existing customer), enter N or + in this field to have the system generate a number for you. You can also manually enter a service site ID, as long as the ID is not already in use in SM Service Sites.
 Note: You must click Create Customer / Site to set up a new customer (in AR Customers and SM Customers) and/or service site (in SM Service Sites). If any required information is missing, the system displays a warning and you must enter the required information and then re-click Create Customer / Site. Once the new customer and/or service is created, the system clears the New Customer and/or New Site checkboxes.

- If this quote is for an existing service site (existing customers only), enter the service site ID or press F4 to select from a list of valid service sites. Once you enter the customer number, the screen populates with the customer's name and address information.

Note: If you enter a service site that is not associated with the customer you specified (in the Customer: ID field), the system automatically changes the Customer: ID to the customer associated with service site you entered and clears the New Customer checkbox (if selected).

## Site: Description

The Site: Description field (unlabeled) on the SM Work Order Quotes form, header Info tab.
If you entered a work order for this quote (in the Work Order field) or you entered an existing service site in the Site ID field, this field defaults the service site description from SM Service Sites and is disabled.
If you did not enter a work order for the quote, this field is enabled only if you selected the New Site checkbox.
Enter a description of the service site for this work order quote. Up to 60 characters allowed.
Note: You must click Create Customer / Site to set up a new customer (in AR Customers and SM Customers) and/or service site (in SM Service Sites). If any required information is missing, the system displays a warning and you must enter the required information and then re-click Create Customer / Site. Once the new customer and/or service is created, the system clears the New Customer and/or New Site.

## Site: Address

These fields are enabled only if you left the
 Site ID
 field blank.
 If you entered a site ID, these fields are display only and default the site address from SM Service Sites. Changes to this information in SM Service Sites will be updated to the corresponding fields here.
Enter the service site address information in the following fields.

- Address - Enter the mailing address. This can be either the street address or a P.O. Box.

- Add'l Address - Enter additional address information, such as suite number, apartment, etc. If you entered a P.O. Box in the Address
 field, you can use this field to enter the street address.

- City - Enter the city.

- State - Enter a valid state (as defined in HQ
 States). The system validates the state based on the Default Country specified in HQ
 Company Setup for the active company. If not valid, an error displays, but entry is
 allowed. You must then enter a valid country for this state in the Country
 field.

- Zip Code - Enter the zip code or postal code, up to 12 digits.

- Country - Defaults from the Default
 Country field in HQ Company Setup for the active SM company. You will
 only need to change the default if the customer's address exists outside the default
 country.

## Requested By: Name

Enter the name of the contact who requested this work order quote. Up to 60 characters allowed.
The person specified here can be an existing
 customer, site, or HQ contact, or any contact not already set up in the system. Press
 F4
 for a list of valid customer, site, or HQ contacts.

## Requested By: Phone

Enter the phone number of the 'requested by' contact specified above. If you selected an existing contact, this field defaults the phone number defined for the contact in HQ Contacts.

## Requested By: Date

Enter the date this work order quote was requested.

## Sales Rep

Enter the sales representative for this work
 order quote. Press F4 for a list of valid employees for the SM company.
Note: If you enter a non-valid employee, the description displays a warning that the employee is not valid; however, you will be able to save the record.

## Seq

Enter N, New, or + to add a new work order quote sequence;
 the system will automatically assign the next sequential number.

## Scope

Enter the work scope that represents the work
 to be done on this work order sequence. Press F4 for a list of valid work scopes.
Leave this field blank if this quote sequence is not associated with a work scope.

## Due

Specify the due date type for this work order quote sequence.

- 0-By — Select this option if the work associated with this quote sequence is due by a specific date. When selected, the second date field (right) is enabled; use this field to enter the "due by" date.

- 1-Within — Select this option if if the work associated with this quote sequence is due within a specified time-frame. When selected, both date fields (right) are enabled. Use these fields to enter the beginning and ending date in the "due within" date range.

When you approve the quote, the system will generate a work order and update this due date type to the related work order scope sequence.

## Start Date

This field is only enabled when due date type is 1-Within.
Enter the beginning date in a range of dates within which the work associated with this quote sequence is due.
When you approve the quote, the system will generate a work order and update this start date to the related work order scope sequence.

## End Date

This field is enabled when due date type is 0-By or 1-Within.
If you selected 0-By as the due date type, specify the date by which the work associated with this quote sequence is due.
If you selected 1-Within as the due date type, specify the ending date in a range of dates within which the work associated with this quote sequence is due.
When you approve the quote, the system will generate a work order and update this end date to the related work order scope sequence.

## Call Type

Enter the call type (from SM Call Types) for
 this quote sequence. Press F4 for a list of valid call types.

## Detail

Enter a description of the problem or work to be perfomed. Space allowance is virtually unlimited.

## Division

Enter the division for this quote sequence
 (e.g. the division that handles the type of work defined for this quote sequence). Press
 F4
 for a list of valid divisions for the service center specified above.

## Cust PO

Enter the PO number for this quote sequence. Up to 30 characters allowed.
Note: This number is typically provided by the customer if they require PO numbers for service work.

## Agreement

The Agreement field on the SM Work Order Quotes form, detail Info tab.
Applies to existing customers only.
If this quote is associated with an agreement, enter the agreement or press F4 for a list of valid agreements for the customer. The Rev field (to the right) populates automatically with the agreement's current revision number.

## Price Method

Select the price method for this quote sequence:

- Flat Price - Select this option if the work covered
 by this quote sequence will be included in the flat amount specified in the
 Price field (to the right).

- T-Time and Material - Select this option if the work
 covered by this quote sequence will be billed using the rate template specified in
 the Rate
 Template field below.

- D-Derived Flat Price- Select this option if you want the work covered by this quote sequence to calculate the flat price based on equipment, labor, misc and material entries using the rate template. Upon approval, this type of quote sequence becomes a flat-price work order.
Note: When using this method, the system also generates split revenue entries (in SM Flat Price Revenue) based on the total billable values for the equipment, labor, misc and material entries. If you need to edit the split revenue entries, you must do so via the equipment, labor, misc and material entries.

## Rate Template

The Rate Template field on the SM Work Order Quotes form, Info tab of quote scope section.

Required.
This field only displays if the Price Method is T-Time and Material.
Enter the rate template for this quote sequence. Press F4 for a list of valid rate templates.
This field defaults the rate template specified for the service site (in SM Service Sites). If no rate template is specified for the service site, it then defaults the rate template defined for the customer (in SM Customers). If no rate template is defined for the customer, this field defaults as blank.
The system uses the rate template specified here to determine equipment, labor, and material rates for work completed on work orders generated from this work order quote.

## Price

This field only displays if the Price Method is F-Flat Price or D-Derived Flat Price.
For Flat Price scopes only, enter the price that will be charged for the work covered by this quote sequence.
For Derived Flat Price scopes, this field is disabled and defaults a value based on required equipment, labor, misc and material entries.
When a work order is generated from this quote, all work completed lines associated with this sequence will have a Pricing Method of No Charge; the Billable Rate and Total Billable fields will be blank and cannot be changed.

## Margin

The Margin field on the SM Work Order Quotes form, detail Info tab.
This field displays only for Flat Price quote scopes.
Required if the Recognize Revenue as Costs Incurred checkbox is selected in SM Company Parameters.
Enter the expected margin percentage for this quote scope.
 When you generate a work order from this quote, the margin specified here defaults for the corresponding work order scope. During the revenue recognition process, the system applies the margin to the sum of all associated costs for the work order scope to determine the revenue to recognize.
For example, if the total cost posted to the work order scope is $2,500 and the margin is 20%, the recognized revenue will be $3000 ($2,500.00 x 1.2 = 3,000.00).
Note: When recognizing revenue for flat price scopes, the system will not exceed the Flat Price amount. If the total costs plus the margin will exceed the Flat Price amount, the system will stop recognizing revenue at the Flat Price amount.

## Tax Source

The Tax Source field on the SM Work Order Quotes form, scope Info tab.

This field is enabled only if a service site is specified for the work order quote.
From the drop-down menu, select the tax source for this quote scope:

- C - Service Center - Select this option to default tax information from the quote's assigned service center. If you did not specify a service site for the quote, the system defaults this option and disables the field.

- S - Service Site - Select this option to default tax information from the quote's assigned service center. This is the default option when a service site is specified for the quote. You may override the default as needed..

When you generate a work order from this quote, the tax source you specify here will default on the work order scope generated from this quote scope.

## Matl Tax Override

The Matl Tax Override drop-down on the SM Work Order Quotes form, quote scope Info tab.

Select the tax type override option for this quote scope. This field defaults the Matl Tax Override specified in SM Call Types for the call type assigned to this quote scope.

- Blank – Use the standard tax type defaulting behavior. For taxable material-related work completed lines, the tax type defaults as Sales. For non-taxable material-related work completed lines, the tax type defaults as blank.

- N - No Tax – Default the tax type as "blank" for material-related work completed lines.

- S - Sales Tax Only – Default the tax type for taxable material-related work completed lines as Sales (US) or VAT (AU/CA).

- U - Use Tax Only (US companies only) – Default the tax type as Use for taxable material-related work completed lines.

The Matl Tax Override only determines the
 default billing tax for Material work completed lines. For non-material work completed
 lines (Labor, Equipment, Purchase, and Misc lines with a non-material cost type) that
 are taxable, the billing tax type defaults to the correct type, regardless of the option
 selected in the Matl Tax Override field. Vista is designed to
 ignore this override for non-material lines. This ensures that non-material services are
 taxed correctly even when a Use Tax override is applied to
 materials on the same scope.
You may override the default on the work order scope as needed.

## Tax Option Override

The Tax Option Override drop-down on the SM Work Order Quotes form, Info tab of the quote scopes section.

This field defaults as blank. If you leave it blank, the
 Tax Option Override on work order scopes generated from this
 quote scope will default as blank. You can override the default at the work order scope
 level or leave it blank to use the [Tax Option](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-call-types-form/field-definitions-sm-call-type-form#concept-240b2b40-791b-47fb-9157-82e9bad15158--en) defined for the Call Type specified on the work order scope.
If you want to override this tax option, choose one of the overrides
 listed below. Options selected here will default on the work order generated from this
 work order quote.
Note: Changing the Call Type for this work order quote will not
 affect the value in this Tax Option Override field.

- N - Not Taxable - Do not apply taxes at the time of purchase or billing. The cost and billing tax types and tax codes default as blank, regardless of whether the SM cost type specified for the work completed line is taxable. You may override the defaults as needed.

- P - Taxable at Purchase Only - Apply taxes at the time of purchase only. If the cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope and the Cost Tax Code defaults from the service site or service center depending on the Tax Source defined for the work order scope. The billing tax type and billing tax code default as blank. If the cost type is not taxable or no cost type is specified, all tax fields default as blank. You may override as needed.

- B - Taxable at Billing Only - Apply taxes at the time of billing only. If the line's cost type is taxable, the billing tax type and billing tax code default to the Tax Type and Tax Code specified for the work order scope. The Cost Tax Type and Cost Tax Code default as blank. If the cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.

- M - Taxable at Purchase/Markup at Billing - Apply taxes at the time of purchase and also apply taxes to the markup amount at the time of billing. If the line's cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope and the Cost Tax Code defaults from the service site or service center depending on the Tax Source defined for the work order scope. The billing tax type and tax code default to the Tax Type and Tax Code specified for the work order scope; however, the tax basis defaults the markup amount only. If the line's cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.Note: For taxable purchases, the bill tax basis is reduced by the amount that was previously taxed at the time costs were recorded. If you did not capture taxes when recording costs, there is no credit to apply to the transaction at billing; therefore, the bill tax basis is calculated using the full billing subtotal, not just the markup.

- F - Full Tax at Purchase and Billing - Apply tax fully at time of purchase and at time of billing. If the line's cost type is taxable, the Cost Tax Type defaults based on the Matl Tax Override option specified for the work order scope, and the Cost Tax Code defaults from the service site or service center, depending on the Tax Source defined for the work order scope. The billing tax type and billing tax code default to the Tax Type and Tax Code specified for the work order scope, and the tax basis defaults the full billable amount. If the line's cost type is not taxable, all tax fields default as blank. You may override the defaults as needed.

Note: Quote scopes with a price method of
 Flat Price or Derived Flat Price
 will generate Flat Price work order scopes. Work completed lines associated with
 Flat Price work order scopes are non-billable; therefore, taxes may only be applied
 at the time of purchase (cost tax). If you select an option other than N-Not Taxable or P-Taxable at Purchase Only for
 the quote scope, the system ignores the "tax at billing" portion on the related work
 order.

## Approve Seq.

Approve Seq. checkbox on the SM Work Order Quotes form, Info tab of quote scope section.
Select this checkbox to approve the scope's quote sequence. This allows you to select individual work orders quote scopes to approve before approving a quote. 

## Derived

This field is disabled for Derived Flat Price scopes and defaults as selected.
Select this checkbox to calculate the budget totals (labor hours, cost, price, and estimated profit) for the quote scope based on the cost estimates entered for required material, equipment, labor, and miscellaneous lines.
 For time and material scopes, the system will also derive an estimated tax amount (shown below the Budget totals) from required materials and miscellaneous lines that include tax amounts. For flat price and derived flat price scopes, the estimated sales tax is derived from the taxable split revenue entries.
Note: If you have entered summarized cost estimates in SM WO Quote Cost Detail (accessed via the Detail button), selecting this checkbox will clear the budget totals for the quote scope; however, your summarized cost estimates will be left intact.
Do not select this checkbox if you want to calculate budget and tax values using the summarized cost estimates entered in SM WO Quote Cost Detail (accessed by clicking the Detail button on the quote scope).
 For detailed information about how the system updates the budget values, see [About Work Order Quote Scope Budgets](/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets).

## Cost Total

Display only, the total cost for this quote sequence as defined in SM Work Order Quote Scope Cost (accessed by clicking the Costs button) below.

## Est Profit

Display only, the estimated profit for this quote sequence. This value is a calculation of the quote Price less the Cost Total.

## Tax Type

The Tax Type field on the SM Work Order Quotes form, scope Info tab.

If work covered by this quote sequence is taxable, specify the tax type:

- 1 - Sales

- 3 - VAT

This field defaults as follows:

- For US companies, if the service center or service site is assigned a tax code (depending on the Tax Source), this field defaults as 1-Sales. If no tax code is assigned, the tax type defaults as null.

- For Australian and Canadian companies (where SM company's AR company is set up with a Default Country of AU or CA in HQ Company Setup), the Tax Type defaults to 3-VAT.

When you generate a work order from this quote, the tax type you specify here will default on the work order scope generated from this quote scope.

## Tax Code

The Tax Code field on the SM Work Order Quotes form, scope Info tab.

If work covered by this quote sequence is taxable, specify the tax code to use for determining the tax amount for this sequence. Must be a valid tax code for the specified tax type.
This field automatically defaults the tax code for the service site or service center, depending on the Tax Source specified for the quote scope. If no tax code is specified for the service site or service center, this field defaults as blank.
Note: For quote scopes with a price method of F-Flat Price or D-Derived Flat Price, once you enter a tax code, the system calculates a Tax Amount based on the taxable split revenue amounts (defined in SM Flat Price Revenue). See the [Tax Amount](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form/field-definitions-sm-work-order-quotes-form#ID-00044ec2--en) F1 help for more information.

When you generate a work order from this quote, the tax code you specify here will default on the work order scope generated from this quote scope.

## Tax Amount

This field only displays when the Price Method is
 F-Flat Price.
Display only, the estimated tax amount for this quote sequence (if applicable). The system calculates this amount based on the taxable split revenue sequence amounts and the tax rate for the specified tax code. For example, say the quote sequence price is 5,000.00. You have 3 split revenue sequences:
Because only $2,500.00 of the revenue amount is flagged as taxable, the system will calculate tax only on the $2,500.00, not the total flat price of $5,000.00.

## Not to Exceed

This field only displays when the Price Method is
 T-Time and Material.
Optional.
Enter the billable limit for this quote sequence. You will only enter a value here if work completed equipment, labor, parts (stocked and purchased), and miscellaneous charges associated with this sequence (on a work order) should not exceed a specified amount.

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

## Work Order

Work Order field on the Open Work tab of the SM Work Order Quotes form.
Work order associated with the quote.

## Work Order Scope

Work Order Scope field on the Open Work tab of the SM Work Order Quotes form.
Work order scope associated with the quote.

## Include

Include checkbox on the Open Work tab of the SM Work Order Quotes form.
Select this checkbox in order to include this work order on the quote.

## Price Method

Price Method field on the Open Work tab of the SM Work Order Quotes form.
Select the price method for this quote sequence:

- Non-Billable - Select this option if you are not charging for work covered by this work order scope. The system will automatically default this option for all work orders referencing a service site with the Non-Billable box checked (in SM Service Sites).

- T-Time and Material - elect this option to bill work completed using the rate template assigned to the work order scope. The system will automatically default this option for all work orders referencing a service site with the Non-Billable box unchecked (in SM Service Sites).

- Flat Price - Select this option to charge a flat price (designated to the right) for all work covered by this work order scope.

## Rate Template

Rate Template field on the Open Work tab of the SM Work Order Quotes form.
Enter the rate template for this quote sequence. Press F4 for a list of valid rate templates.

## Price

Price field on the Open Work tab of the SM Work Order Quotes form.
Enter the price that will be charged for the work covered by this quote sequence.
