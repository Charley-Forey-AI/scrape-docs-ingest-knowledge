---
title: "Field Definitions: JB T M Bill Line Sequences Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-line-sequences-form/field-definitions-jb-t-m-bill-line-sequences-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-line-sequences-form/field-definitions-jb-t-m-bill-line-sequences-form"
---

# Field Definitions: JB T M Bill Line Sequences Form

The following is a list of field descriptions for the JB T M
 Bill Line Sequences form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Lines: Line

 This field is display only and shows the line number for this billing sequence. The system assigns the line number based on the template’s sort order and the type of data in the line. Numbers assignments are in increments of 10 to allow for adding future lines.

##  Lines: Template Seq

 This field automatically displays all sequences for the billing (based on the assigned template) during initialization.
 For manually entered lines, specify the template sequence to add to this billing. This must be a valid sequence defined for the template in JB T & M Template Setup. Press F4 for a list of valid sequences for the specified template.

##  Lines: Seq Type

 This field is display only, showing the type assigned to the sequence in JB T & M Template Setup (i.e. Source, Amount, Detail Add-on, etc.).

## Lines: Date

This field is for templates with sort order of ‘A-Actual’ or ‘D-Posting Date’ only.
During initialization, this field defaults a date based on the posted job cost detail and cannot be overridden.
For manually added lines, enter the date that applies to the line.
The date represented here depends on the template’s sort order. If the sort order is Actual Date, then this field represents the actual transaction date for the detail line. If the sort order is Posting Date, then this field represents the date the line posts.
If the template sort option is other than ‘Actual Date’, the system will compare this date against the Effective Date specified for labor, equipment, and material rates (as applicable) to determine whether to use the ‘old rate’ or ‘new rate’.

## Lines: Job

This
 field is for templates with sort order of Job/Phase only.
During initialization, this field defaults the job based on the posted job cost detail and cannot be overridden.
For manually added lines, enter the job (from
 JC Jobs) that applies to the line.

## Lines: Phase

This field is for templates with sort order of
 Job/Phase or Phase only.
During initialization, this field defaults the phase from the posted job cost detail and cannot be overridden.
For manually added lines, enter the phase
 (from JC Phases Maintenance) that applies to the line.

##  Lines: Item

 Specify the contract item to which this sequence applies. The system does not allow overrides.
 During initialization, this field defaults the contract item based on the posted job cost detail and cannot be overridden.
 For manually added lines, enter the contract item that applies to this line.

##  Lines: Description

 Enter a description for this line, up to 128 characters. Initially defaults the description assigned to the template sequence.

##  Lines: Basis

 This field displays the basis amount for this line.
 During initialization, this field automatically defaults an amount based on the posted job cost detail. If an add-on sequence, the template sequences assigned to the add-on determine the basis. Override this value as necessary.
 For manually added sequences with a type of ‘Source’, this field defaults as 0.00 and cannot be edited. Enter the sequence detail to determine the basis amount.
Note: If the Markup Option for the sequence is ‘U-Rate per Unit’, the basis will be a calculation of Total / (1 + Markup Rate), where Total is the sum of all associated line sequences.

##  Lines: Markup Rate

 This field displays the markup rate for this line.
 During initialization, this field automatically defaults a rate based on the template setup. Override this value as necessary.

##  Lines: Addl Markup

 This field displays any additional markup amount for this line.
 During initialization, this field automatically defaults an amount based on the template setup. Override this value as necessary.

##  Detail: Line Seq

 This field displays the sequence number for this line of detail. To add a new sequence, enter “New”, and the line sequence number generates automatically.

##  Detail: Source

 This field defaults the data source.
 If entering the line sequence manually, enter the desired source module. This must be a valid source for the template sequence. Available sources are:

- AP

- EM

- JC

- IN

- PR

- MS

Note: Transactions posted in JC Material Use will have either a source of IN (for entries with a JC Type of ‘IN-Inventory’) or JC (for entries with a JC Type of ‘MI-Miscellaneous’).

##  Detail: Cost Type

 This field displays the cost type for the detail line.
 If entering line manually, enter the desired cost type.

##  Detail: AP Co

 For sources of AP, this field displays the AP company from job cost detail.
 If entering the sequence manually, specify the AP company that applies to this detail line.

##  Detail: Vendor #

 This field is for AP sources only.
 If the template sequence’s sort and summary options require this information, this field will default a vendor based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually, and the
 template sequence requires this information, specify the vendor for this detail line. This
 must be a valid vendor from AP Vendors.

##  Detail: AP Ref #

The Detail: AP Ref# field on the JB T&M Bill Line Sequences form, line sequences Info tab.
 This field is for AP sources only.
 If the template sequence's sort and summary options require this information, this field will default the AP reference number based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually, and the
 template sequence requires this information, specify the AP reference number for this
 detail line. This must be a valid vendor from AP Vendors.

##  Detail: Pre Bill

 Check this box to have this line’s AP detail billed before the detail exists in JC. If checked, all JC transactions added to this or subsequent bills for the same APCo/VendorGroup/Vendor will display an error message indicating that the detail may be billed twice.
 Leave this box unchecked if you do not want this AP detail billed before the detail exists in JC.

## Detail: PO

For sources of AP only, with a cost type other than Subcontract.
If the template sequence’s sort and summary options require this information, this field will default the PO number based on the JC detail. If the template sequence does not require this information, this field is disabled.
If entering the sequence manually and the
 template sequence requires this information, specify the PO number for this detail line.
 This must be a valid vendor from AP Vendors.

##  Detail: PO Item

 For sources of AP only, with a cost type other than Subcontract.
 If the template sequence’s sort and summary options require this information, this field will default the PO item number based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually, and the
 template sequence requires this information, specify the PO item number for this detail
 line. This must be a valid vendor from AP Vendors.

##  Detail: Subcontract

 For sources of AP only, with a cost type of Subcontract.
 If the template sequence’s sort and summary options require this information, this field will default the subcontract number based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually, and the
 template sequence requires this information, specify the subcontract number for this detail
 line. This must be a valid vendor from AP Vendors.

##  Detail: SL Item

 For sources of AP only, with a cost type of Subcontract.
 If the template sequence’s sort and summary options require this information, this field will default the subcontract item number based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually, and the
 template sequence requires this information, specify the subcontract item number for this
 detail line. This must be a valid vendor from AP Vendors.

##  Detail: EM Co

 For sources of EM, displays the EM company from job cost detail.
 If entering the sequence manually, specify the EM company that applies to this detail line.

##  Detail: Equipment

 This field is for EM sources only.
 If the template sequence’s sort and summary options require this information, this field will default the equipment based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually, and the template sequence requires this information, specify the equipment for this detail line. This must be a valid piece of equipment from EM Equipment.

##  Detail: Rev Code

 This field is for EM sources only.
 If the template sequence’s sort and summary options require this information, this field will default a revenue code based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually, and the template sequence requires this information, specify the revenue code for this detail line. This must be a valid revenue code from EM Revenue Codes.

##  Detail: Time UM

 This field is for EM sources only.
 This field is display only, showing the time unit of measure for the specified revenue code. Revenue codes must be hourly-based; otherwise, this field displays as blank.

##  Detail: IN Co

 For sources of IN or MS, displays the IN company from the job cost detail.
 If entering the sequence manually, specify the IN company that applies to this detail line.

##  Detail: Location

 This field is for IN or MS sources.
 If the template sequence’s sort and summary options require this information, this field will default a location based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually, and the
 template sequence requires this information, specify the inventory location for this detail
 line. This must be a valid location from IN Locations.

##  Detail: MS Ticket #

 This field is for MS sources only.
 If the template sequence’s sort and summary options require this information, this field will default the ticket number based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually, and the template sequence requires this information, specify the ticket number for this detail line.

##  Detail: Material

 If the template sequence’s sort and summary options require this information, this field defaults the material based on the JC detail. If the template sequence does not require this information, this field is disabled.
Note: If a sequence is summarized and consists of multiple materials, this field defaults as blank.
 If entering the sequence manually, and the template sequence requires this information, specify the material for this detail line. This must be a valid material from HQ Materials.

##  Detail: Std UM

 Defaults the unit of measure for this line sequence from the JC detail. The system allows overrides.
 If entering the sequence manually, specify a valid unit of measure (from HQ Units of Measure).

##  Detail: Std Price

 Defaults the unit price for this line sequence based on the JC detail. The system allows overrides.
 If entering the sequence manually, specify the unit price.

##  Detail: ECM

 Specify which quantity the unit cost for this material represents.

- E – Cost is per each unit.

- C – Cost is per 100 units.

- M – Cost is per 1000 units.

##  Detail: PR Co

 For sources of PR, this field displays the PR company from the job cost detail.
 If entering the sequence manually, specify the PR company that applies to this detail line.

## Detail: Employee

This field is for PR sources only.
If the template sequence’s sort and summary options, and/or labor rates require this information, this field defaults as employee-based on JC detail. If the template sequence does not require this information, this field is disabled.
If entering the sequence manually and the template sequence requires this information, specify the employee for this detail line. This must be a valid employee from the specified PR company.

##  Detail: Craft

 This field is for PR sources only.
 If the template sequence’s sort and summary options, and/or labor rates require this information, this field defaults a craft based on JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually and the
 template sequence requires this information, specify the craft for this detail line. This
 must be a valid craft from PR Crafts.

##  Detail: Class

 This field is for PR sources only.
 If the template sequence’s sort and summary options, and/or labor rates require this information, this field defaults a class based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually and the template sequence requires this information, specify the class for this detail line. This must be a valid class from PR Craft Classes.

##  Detail: Shift

 This field is for PR sources only.
 If the template sequence’s sort and summary options, and/or labor rates require this information, this field defaults a shift based on JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually and the template sequence requires this information, specify the shift for this detail line.

##  Detail: Earn Type

 This field is for PR sources only.
 If the template sequence’s sort and summary options, and/or labor rates require this information, this field defaults an earnings type based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually and the template sequence requires this information, specify a valid earnings type for this detail line.

##  Detail: Factor

 This field is for PR sources only.
 If the template sequence’s sort and summary options, and/or labor rates require this information, this field will default a factor based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually and the template sequence requires this information, specify the factor for this detail line.

##  Detail: Category

 For labor, equipment, or material type sequences only, when the “Use Category” option is checked for that type on the template.
 This field defaults the category for this line detail sequence based on the JC detail.

## Detail: Date

For templates using a sort option other than ‘A-Actual Date:

- If template is set for full detail (Sum Opt is ‘1’), this field defaults the transaction date of the JC transaction associated with this detail sequence. If multiple transactions exist for the detail sequence, this field defaults the date of the oldest JC transaction.

- If template is set for summarized detail (Sum Opt is ‘99’), this field defaults as null. If you enter a date here, date will display for the detail line, but will not necessarily represent the transaction dates of the combined JC transactions.

Note: The system will compare this date against the Effective Date specified for labor, equipment, and material rates (as applicable) to determine whether to use the ‘old rate’ or ‘new rate’. For templates using a sort option of ‘A-Actual Date’:
This field defaults the date specified for the bill line. If you change the defaulted date, the following message displays:
The template upon which this bill is based is set to sort by Actual Date. The Bill Line’s Actual Date is not the same as this input date. Rates defaulted to this form are based upon an Effective Date equal to the Lines Actual Date value.
Note: For information about all JC transactions related to this detail sequence, click the JC Detail button at the end of this line.

##  Detail: Description

 Enter a description of the line detail sequence, up to 60 characters.

##  Detail: UM

 If the template sequence’s sort and summary options require this information, this field will default the unit of measure (i.e. posted UM) based on the JC detail. If the template sequence does not require this information, this field is disabled.
 If entering the sequence manually and the template sequence requires this information, specify the unit of measure (from HQ Units of Measure) for this detail line. This field defaults the material’s standard unit of measure from HQ Materials.
Material Transactions
 If a sequence is summarized and there are multiple material transactions, UM will default as follows:

- If materials are not the same, UM defaults as null.

- If materials are the same, but the UMs differ, UMs will be converted using the HQMU or INMU conversion factor (i.e. if the template's Price Opt is 'Price', uses HQMU. If the Price Opt is 'Location', uses INMU first, then HQMU if not in INMU). If UMs cannot be converted, UM defaults as null.

- If materials are the same, but the UMs differ and the Price Opt is 'Cost', UM defaults as null.

##  Detail: Units

 Defaults the number of units (i.e. posted units) for this line sequence from the JC detail. May be overridden. For labor transactions, this field defaults as 0.00.
 If entering the sequence manually, specify the number of units.
Material Transactions
 If a sequence is summarized and there are multiple material transactions, Units will default as follows:

- If materials are not the same, units will default as 0.00.

- If materials are the same, but the UMs differ, and the UMs can be converted, units will be adjusted accordingly. If UMs cannot be converted, units will default as 0.00.

- If materials are the same, but the UMs differ and the Price Opt is 'Cost', units will default as 0.00.
Equipment Transactions

 If a sequence is summarized, the units will default as follows:

- If hourly based and using straight hourly (i.e. Time U/M=Hrs, Hours/Time Unit=1), units will default as 0.00.

- If hourly based and using time units (e.g. Time U/M=Day, Hours/Time Unit=8), and Time UM is the same for all transactions, default will be total time units. If time units differ, units will default as 0.00 and only hours will be accumulated.

- If unit based and UMs are the same, default will be total units. If UMs differ, default will be 0.00.

- If both hour based and unit based transactions are combined, units (and hours) will default as 0.00 and only subtotal will be accumulated.

Note: The posted revenue code determines whether transactions are hour or unit based.

##  Detail: Unit Price

 If the template sequence’s sort and summary options specify to use full detail, this field will default a unit price based on the JC detail. However, if you have specified to summarize the template sequence (i.e. summarize multiple lines of detail), the unit price is a calculation of cost divided by units. For labor transactions, unit price will be a calculation based on subtotal divided by hours. If the template sequence does not require this information, this field is disabled.
 If entering you are manually entering the line sequence and the template sequence requires this information, specify the unit price for this detail line.
Material Transactions
 If a summarized sequence and multiple material transactions exist, unit price defaults as follows:

- If the materials are not the same, the unit price defaults as 0.00.

- If the materials are the same, but the UMs differ, the unit price will be adjusted accordingly if the UMs can be converted; otherwise, the unit price defaults as 0.00.

- If the materials are the same, but the UMs differ and the Price Opt is 'Cost', unit price defaults as 0.00.
Equipment Transactions

 If a summarized sequence, unit price defaults as follows:

- If hourly based and using straight hourly (i.e. Time U/M=Hrs, Hours/Time Unit=1), unit price will default as 0.00.

- If hourly based and using time units (e.g. Time U/M=Day, Hours/Time Unit=8), and Time UM is the same for all transactions, default will be total time units. If time units differ, unit price will default as 0.00.

- If unit based and UMs are the same, default will be total units. If UMs differ, default will be 0.00.

- If both hour based and unit based transactions are combined, unit price will default as 0.00 and only subtotal will be accumulated.

Note: The posted revenue code determines whether transactions are hour or unit based.

##  Detail: ECM

 Indicates which quantity the unit cost for this line detail sequence represents.

- E – Cost is per each unit.

- C – Cost is per 100 units.

- M – Cost is per 1000 units.
Material Transactions

 If a sequence is summarized and there are multiple material transactions, ECM will default as follows:

- If materials are not the same, ECM will default as 0.00.

- If materials are the same, but the UMs differ, and the UMs can be converted, ECM will be adjusted accordingly. If UMs cannot be converted, ECM will default as 0.00.

- If materials are the same, but the UMs differ and the Price Opt is 'Cost', ECM will default as 0.00.

##  Detail: Sub Total

 This field is the subtotal of this line detail sequence based on the number of units (or hours) and the unit price. This is the total of this line detail sequence before adding any markups.
Note: If overriding this amount, the Unit Price does not recalculate.

##  Detail: Hours

 Defaults the number of hours for this line sequence based on the JC detail. May be overridden.
 If entering the sequence manually, specify the number of hours, if applicable.
Equipment Transactions
 If a sequence is summarized, the hours will default as follows:

- If hourly based and using straight hourly (i.e. Time U/M=Hrs, Hours/Time Unit=1), defaults total number of hours.

- If hourly based and using time units (e.g. Time U/M=Day, Hours/Time Unit=8), time units will be converted to hours. Example: If time UM is Day and number of time units is '5', hours will default as '40' (5 x 8).

- If unit based, hours will default as 0.00.

- If both hour based and unit based transactions are combined, hours (and units) will default as 0.00 and only subtotal will be accumulated.

Note: The posted revenue code determines whether transactions are hour or unit based.

##  Detail: Markup Rate

 This field defaults the markup rate for this detail sequence from the template. May be overridden.
 If entering the sequence manually, specify the markup rate to use for this detail sequence. If no markup applicable, enter 0.00000.
Note: The Total Markup (including Additional Markup) for this detail sequence is displayed to the right of this field.

##  Detail: Addl Markup

 This field defaults any additional markup for the detail sequence from the template. This amount is added after the markup rate has been applied to the line detail. May be overridden.
 If entering the sequence manually, specify any additional markup for this detail sequence. If no additional markups apply, enter 0.00.

##  Detail: Markup Total

 Display only, the total markup for this detail sequence, including additional markup.

##  Detail: Total

 Display only, the total amount (subtotal plus all markups) for this detail sequence.

##  Detail: JC Month

 Display only, the JC month for this detail sequence. This field will only display a value when the template sequence is at full detail, and relates to a JC transaction. If multiple transactions exist for the detail sequence, will display the JC month for the oldest JC transaction.
Note: For information about all JC transactions related to this detail sequence, click the JC Detail button at the end of this line.

##  Detail: JC Trans

 Display only, the JC transaction number for this detail sequence. This field will only display a value when the template sequence is at full detail, and relates to a JC transaction. If multiple transactions exist for the detail sequence, will display the transaction number of the oldest JC transaction.
Note: For information about all JC transactions related to this detail sequence, click the JC Detail button at the end of this line.
