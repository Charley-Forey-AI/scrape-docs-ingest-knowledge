---
title: "Field Definitions: JB T M Template Setup Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form/field-definitions-jb-t-m-template-setup-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form/field-definitions-jb-t-m-template-setup-form"
---

# Field Definitions: JB T M Template Setup Form

The following is a list of field descriptions for the JB T M
 Template Setup form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template

 Enter a name for this template, up to 10 characters.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Description

 Enter a description of the template, up to 30 characters.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Sort Order

 Specify the order in which detail lines will be grouped on the T&M invoice.

- Actual Date — Data is sorted by the actual transaction date from the JC Detail file to create a series of detail lines.

- Posting Date — Data is sorted using each unique posting date from the JC Detail file to create a series of detail lines.

- Contract Item — Data is sorted by contract item. Each item will include a series of source and detail lines.

- Job/Phase — Data is sorted by job number and phase code. Use this sort order if you want Job Billing invoices stored by contract/job/phase. Otherwise, invoices will be stored at the contract level.

- Phase — Data is sorted by phase. All jobs posting to the same phase will be combined.

- Template Sequence — Data is sorted by template sequence only. If detail is not found for a sequence, the sequence is not printed on the invoice.

Note: If a template sequence line is assigned a sequence type of S-Source, you must specify how the job cost detail is to be broken down within the sorted groups by specifying a Summary and Sort level. See Related Topics below for more information.
[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Labor Rate Effective Date

 This field is used to specify the effective
 date for labor rates. This allows new labor rates to be defined ahead of time, while
 preserving the current rates until the new ones are in effect. When initializing billings,
 or adding JC transactions to existing billings, the effective date determines which rates
 to use. Labor transactions with “actual” dates prior to the effective date will be billed
 at the old rate, whereas transactions with “actual” dates on or after the effective date
 will be billed at the new rate. If an effective date is not specified, the new rate is used
 and the old rate ignored.
Date field shortcuts
T or t
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Equipment Rate Effective Date

 This field is used to specify the effective
 date for equipment usage rates. This allows new usage rates to be defined ahead of time,
 while preserving the current usage rates until the new ones are in effect. When
 initializing billings, or adding JC transactions to existing billings, the effective date
 determines which usage rates to use. Equipment usage transactions with “actual” dates prior
 to the effective date will be billed at the old usage rate, whereas transactions with
 “actual” dates on or after the effective date will be billed at the new usage rate. If an
 effective date is not specified, the new rate is used and the old rate ignored.
Date field shortcuts
T or t
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Matl Rate Effective Date

 This field is used to specify the effective date for material billing rates. This allows new material rates to be defined ahead of time, while preserving the current rates until the new ones are in effect. When initializing billings, or adding JC transactions to existing billings, the effective date determines which rates to use. Material transactions with “actual” dates prior to the effective date will be billed at the old rate, whereas transactions with “actual” dates on or after the effective date will be billed at the new rate. If an effective date is not specified, the new rate is used and the old rate ignored.
Date Field Shortcuts
T or t
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

## Include PO Receipts

The Include PO Receipts checkbox on the JB T&M Template Setup form, header Info tab.
Select this checkbox to include purchase orders that have been received and expensed to a job, but not yet invoiced in JB T&M billings. During initialization (JB T&M Bill Initialization), the system includes receipted, not invoiced purchase orders for jobs associated with this template. PO transactions added to a billing appear in JB T&M Bill All JCDetail Lines and JB T&M Bill JCDetail by Seq with a JC Trans Type of "PO".

If this checkbox is not selected (default), the initialization process excludes received, not invoiced purchase orders, and you must invoice them using AP Transaction Entry.

##  Labor Categories

 Check this box to have job cost detail sorted and summarized by labor category. When checked, a labor category can be specified for each sequence with a PR source, and all job cost detail that matches the category will be included on the invoice.
Note: If using labor categories, you must specify a labor and/or burden cost type (i.e. cost type with a category of Labor or Burden) in the Cost Types grid below.
 Leave this box unchecked if not using labor categories to sort and summarize job cost detail on invoices.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Equipment Categories

 Check this box to have job cost detail sorted and summarized by equipment category. When checked, a category can be specified for each sequence with a EM source, and all job cost detail that matches the category will be included on the invoice.
Note: If using equipment categories, you must specify an equipment cost type (i.e. cost type with a category of Equipment) in the Cost Types grid below.
 Leave this box unchecked if not using equipment categories to sort and summarize job cost detail on invoices.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Material Categories

 Check this box to have job cost detail sorted and summarized by material category. When checked, a category can be specified for each sequence with an AP, IN, JC, or MS source, and all job cost detail that matches the category will be included on the invoice.
Note: If using material categories, you must specify a material cost type (i.e. cost type with a category of Material) in the Cost Types grid below.
 Leave this box unchecked if not using material categories to sort and summarize job cost detail on invoices.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

## Labor Rate Options

 The Labor Rate Options section determines how labor will be billed during the billing process. There are two options available: Cost and Rates.
Cost
 If using costs for labor, the system automatically pulls the actual dollar amounts posted to Job Cost for labor. If categories are used during the billing process, the system uses them only to sort and summarize labor and/or equipment by category. It does not use the rates defined for labor categories to calculate dollar amounts on the invoice.
Note: When this option is selected, the Allow Labor Rate Overrides checkbox is disabled.Rates
 If using labor rates, the billing amounts are based on rates set up for each labor category in JB T&M Template Labor Rates. (Labor categories are set up in JB T&M Labor Categories.)
 Rates are set up for each category in JB T&M Template Labor Rates (which can be accessed from the JB Programs folder or by double-clicking a record on the Labor Rates tab). Rates can be restricted by earnings type, earnings factor, and/or shift. The Rate Option defined for each category determines exactly how the labor rate is calculated. You can use the actual costs posted to JC, the rate specified for the category, or the earnings factor posted in Job Cost.
Allowing Labor Rate Overrides
 Although standard rates defined for a category may suffice for most billings, certain rates may need to be overridden for a variety of circumstances. Select the Allow Labor Rate Overrides checkbox to override category labor rates by employee, craft, and class. These overrides are set up and defined in JB T&M Template Labor Override (which can be accessed from the JB Programs folder or by double-clicking a record on the Labor Rate Overrides tab).
Note: If the Cost option is selected, the Allow Labor Rate Overrides checkbox is disabled.
 For information on setting up labor rates and labor rate overrides, see Related Topics below.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Allow Labor Rate Overrides

 This checkbox is only enabled if the Labor Rate Option is set to Rates.
 Check this box to allow labor rates defined for this template (in JB T&M Template Labor Rates) to be overridden by employee, craft, class, earn type, factor, or shift, or any combination of these options. Overrides are set up in JB Template Labor Rate Override, which may be accessed by double-clicking a record on the Labor Rate Overrides tab.
 Leave this box unchecked if labor category rates cannot be overridden for this template.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Equipment Rate Option

The Equipment Rate Options determine how equipment use will be billed during the billing process. There are three options available: Cost, Rates per Hour, and Rates per Time Unit.
Cost
If using costs for equipment, the system automatically pulls the actual dollar amounts posted to Job Cost for equipment use as noted below:

- Billed amount is ActualCost from the JC Cost Detail file (JCCD)

- Billed UnitCost is ActualCost / ActualHours from JCCD

If categories are used during the billing process, the system uses them only to sort and summarize equipment by category. It does not use the rates defined for equipment categories to calculate dollar amounts on the invoice.
Rates per Hour
The rates defined for each equipment category on a template will be multiplied by the number of hours posted to Job Cost. The rate option selected for the category in JB T&M Template Equipment Rates (JBER) determines how the rates are calculated:
if “R-Equip Rate”

- Billed amount is ActualHours * JBER Rate

- Billed UnitCost is JBER Rate
if “C-ActualCost”

- Billed amount is ActualCost from JCCD

- Billed UnitCost is ActualCost / ActualHours from JCCD
Rates per Time Unit

The rates defined for each equipment category on a template will be multiplied by the number of time units posted to Job Cost. The category's rate option determines how the rates are calculated:
if “R-Equip Rate”

- Billed amount is (ActualHours / HrsPerTimeUM) * JBER Rate

- Billed UnitCost is JBER Rate
if “C-Actual Cost”

- Billed amount is ActualCost from JCCD

- Billed UnitCost is ActualCost / (ActualHours / HrsPerTimeUM)

When equipment usage is posted to Job Cost, the time units are converted to hours based on the revenue code’s Hours/Time Unit factor (defined in EM Revenue Codes). When billing for usage in JB, the hours stored in JCCD will be converted back to time units and multiplied by the specified rate.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Sequence

 Enter a sequence number between 1 and 999999999. This number will become the line number when the bill is created, and is used to specify the order in which sources and add-ons will be calculated and printed.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

## Type

Specify the sequence type that will determine the source from which the sequence amount is derived.
Sequence Type
Description

S-Source
Used when the billable amount for a sequence line is derived from the accumulated total of all job costs for specified sources and cost types. Sources include AP, EM, IN, JC, MS, and PR.

A-Amount
Used when the billable amount for the sequence line is a flat amount and does not relate to Job Cost detail or other sources (i.e. AP, EM, IN, JC, MS, and PR). When selected, use the Flat Amt Option column to specify where the flat amount will come from when creating invoices. See Flat Amounts Option in Related Topics for more information.

D-Detailed Add-ons
Used primarily to add markup amounts (percentages or fixed) to the billable amount. They may also be used to add sales tax or to deduct retainage or discounts. A total is first accumulated from specified sources and add-ons that are set up to be the basis of the Detail Add-on. The detail add-on is then calculated and printed. For more information on entering add-ons, refer to Specifying the Basis for an Add-on in Related Topics below.

T-Total Add-ons
Total add-ons work the same as Detail add-ons, but only occur once on an invoice. As with Detail add-ons, they are calculated on the accumulated total of the specified sources for the add-on. For more information on entering add-ons, refer to Specifying the Basis for an Add-on in Related Topics below.

M-Miscellaneous
This type works similarly to a total add-on. However, the calculated values create entries in the Miscellaneous Distributions file and do not appear on the invoice, nor do the values affect the invoice amount.

N-No Bill
Used when costs for a specified Source/Cost Type/Category combination are defined as non-billable. These types are set up the same as Source sequence lines, but do not appear on the invoice and will always receive a billing status of 2 (non-billable).

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Description

 Enter a description of this sequence, up to 60 characters. This description will become the line’s description on the billing.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Group #

 Enter a number (1-999999999) that will be used to group sequences together for reporting purposes. Sequences with the same group number must also have the same sequence Type.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  AP, EM, IN, JC, MS, PR

 For each source, check the box if JC data of that source will be included in this sequence. The source can be either from the specified module or from job cost detail with transaction types of that module.
Note: If you are using categories (Use Labor, Equip, and Material Category boxes checked above) to restrict data for sequence lines, enter the source to which the category entered for the line applies. For example, if restricting by labor category, check the PR box. If restricting by equipment, check the EM box. If restricting by material, check the AP, IN, JC, and/or MS boxes.
 For transactions posted in JC Material Use, make sure to check the boxes for both IN (for entries with a JC Type of ‘IN-Inventory’) and JC (for entries with a JC Type of ‘MI-Miscellaneous’).

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Category

 This option is only used when restricting the inclusion of data by Labor, Equip, and/or Material Categories (checkboxes above).
 Specify the category to restrict data by for this sequence. Only categories for the specified source may be used, and only data matching the specified category will be included in this line.
Note: When billings are initialized, categories will only be used if labor, burden, equipment, or material cost types are specified on the Cost Types tab at the bottom of the screen. For example, if you are using labor categories and have specified a category for the sequence, then you must have a labor and/or burden cost type assigned to the sequence.
 Additionally, if more than one of the “Use Categories” options is checked above, each unique source must be set up as a different sequence in order to restrict by category. If multiple sources are set up for a single sequence, the system cannot distinguish what category goes with what source; therefore, entry of a category will not be allowed.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

## Sum Option

Use this field to specify the level of summarization for each sequence line using the specified template. If the summary options available do not include the detail needed on the invoice, select full detail (Option 1) for that sequence. Each source is summarized in a different manner.
Note: When initializing billings, the summary options defined for a template are used to determine billing rates. Rates defined at the highest level of detail override all other rates. For example, rates at the Craft/Class/Employee/EarnType/Factor/Shift level will override rates at the Craft/Class/Employee/Earn Type level.
If you use the ‘effective’ date functionality for labor rates, you have the option to summarize billings by rate, in addition to summarizing by a specified PR-Labor/Burden CT level. Using the ‘Include Rate in Summarization’ column in the chart below, locate the option that corresponds to the desired PR-Labor/Burden CT level and enter that in the Sum Opt field for the applicable sequence. For example, to summarize by craft/class/employee only, you would enter ‘2’ as the summary option. However, if you also want to summarize by rate, you would enter ‘102’ as the summary option. When billings are initialized, the system will summarize by craft, class, and employee, and where the rate has changed, add a separate bill line for transactions using the old rate (before effective date) and one for transactions using new rate (on or after effective date).The following table lists the summary levels available for each source:

Source
Sum Opt
Include Rate in Summarization
Description

All
1

Full detail. One invoice detail record per JC detail record.

99

Summary. One invoice detail record per source/CT/category.

PR - Labor/Burden CT
2
102
Craft/Class/Employee

3
103
Employee

4
104
Craft/Class

5
105
Craft/Class/Employee/Earn Type

6
106
Employee/Earn Type

7
107
Craft/Class/Earn Type

8
108
Earn Type

9
109
Craft/Class/Employee/Factor

10
110
Employee/Factor

11
111
Craft/Class/Factor

12
112
Factor

13
113
Craft/Liability Type

14
114
Liability Type

18
118
Craft/Class/Employee/Factor/EarnType (use Sort Level 13)

19
119
Craft/Class/Employee/Factor/Shift (use Sort Level 14)

20
120
Craft/Class/Factor/Shift (use Sort Level 14)

PR-Equipment CT
15

EMCo/Equip/EMGroup/RevCode/Craft/Class/Employee

16

EMCo/Equip/EMGroup/RevCode/Employee

17

EMCo/Equip/EMGroup/RevCode/Craft/Class

MaterialCT - not AP
2

Location/Material

3

Location

4/5/6

Material

MaterialCT - AP
2

Vendor/APRef/Material

3

Vendor/APRef

4

Vendor/Material

5

Vendor

6

Material

7

Vendor/APRef/PO/Item

8

Vendor/PO/Item

9

PO/Item

AP - Expense
2/3

Vendor/APRef

(not material or subcontract)
4/5

Vendor

7

Vendor/APRef/PO/Item

8

Vendor/PO/Item

9

PO/Item

AP - Subcontract CT
2

Vendor/APRef/Subcontract/Item

3

Vendor/APRef

4

Vendor/Subcontract/Item

5

Subcontract/Item

EM - Equipment CT
2

EMCo/Equip/EMGroup/RevCode

3

EMCo/Equip

4

EMGroup/RevCode

15

EMCo/Equip/EMGroup/RevCode /Craft/Class/Employee

16

EMCo/Equip/EMGroup/RevCode/Employee

17

EMCo/Equip/EMGroup/RevCode/Craft/Class

Other Sources/CT’s
2-9

Summary Only

Note: Summary levels are not used if the sequence type is “N-No Bill,” “A-Amount,” “T-Total Addon,” or “D-Detail.”.
JB T&M Template Setup
Summary Level Options

##  Sort Level

 Enter the sort level (1-14) for the source/sequence. This will identify the order in which detail will be sorted. The sort level will differ depending on the source. For a complete list of sort level descriptions by source, click the icon below.
For example, if the Sequence source is PR (Labor/Burden Cost Type) and “4” (Craft/Class) is entered in the Sum Option field, it would not be beneficial to set the Sort Level to “1” (Employee/Craft/Class/Earnings Type). The system would not be able to sort at this level because employees were not included in the detail summarization and would not be found during the sort process. It would be more beneficial instead, to enter “2” (Craft/Class/Employee/Earnings Type) in the Sum Option field. Detail would be sorted at the Craft/Class level, but further sorting at the Employee/Earnings Type level would not occur because the detail would not be available.
The following table lists the sort levels available for each source:

Source
Sort Level
Description

PR - Labor/Burden CT
1
Employee/Craft/Class/Earn Type

2
Craft/Class/Employee/Earn Type

3
Category/Employee/Craft/Class/Earn Type

4
Category/Craft/Class/Employee/Earn Type

5
Employee/Craft/Class/Factor

6
Craft/Class/Employee/Factor

7
Category/Employee/Craft/Class/Factor

8
Category/Craft/Class/Employee/Factor

9
Craft/Class/Liability Type/Employee

10
Category/Craft/Class/Employee/Liability Type

13
Craft/Class/Employee/Factor/EarnType

14
Craft/Class/Employee/Factor/Shift

PR-Equipment CT
11
EMCo/Equip/EMGroup/RevCode/Employee/Craft/Class

12
EMCo/Equip/EMGroup/RevCode/Craft/Class/ Employee

IN/MS - Material CT
1
Material/Location

2
Location/Material

3
Category/Material/Location

4
Location/Category/Material

MaterialCT - AP
1
Material/Vendor/APRef

2
Vendor/APRef/Material

3
Category/Material/Vendor/APRef

4
Vendor/APRef/Category/Material

5
PO/POItem/Vendor/APRef/Material

6
PO/Vendor/APRef/Material

7
Vendor/APRef/PO/POItem/Material

8
Vendor/APRef/PO/Material

AP - Expense
1
Vendor/APRef

(not material or subcontract)
2
PO/POItem/Vendor/APRef

3
PO/Vendor/APRef

4
Vendor/APRef/PO/POItem

5
Vendor/APRef/PO

AP - Subledger CT
1
SL/SLItem/Vendor/APRef

2
SL/Vendor/APRef

3
Vendor/APRef/SL/SLItem

4
Vendor/APRef/SL

EM - Equipment CT
1
EMCo/Equip/EMGroup/RevCode

2
EMGroup/RevCode/EMCo/Equip

3
Category/EMCo/Equip/EMGroup/RevCode

4
EMGroup/RevCode/Category/EMCo/Equip

11
EMCo/Equip/EMGroup/RevCode/Employee/Craft/Class

12
EMCo/Equip/EMGroup/RevCode/Craft/Class/ Employee

Note: Summary levels are not used if the sequence type is “N-No Bill,” “A-Amount,” “T-Total Addon,” or “D-Detail.”.
Sort Level Options
[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Earn/Liab Option

 For Payroll sources only, specify the earnings or liability type by which to restrict job cost detail for this sequence.

E-Earnings
 Only job cost detail matching the earnings type specified to the right of this field will be included in this sequence. If no earnings type specified, job cost detail for all earnings types will be included.
Note: Job cost detail with no earnings type specified will be skipped.

L-Liability
 Only job cost detail matching the liability type specified to the right of this field will be included in this sequence. If no liability type is specified, job cost detail for all liability types will be included.
Note: Job cost detail with no liability type will be skipped.

B-Both
 Only job cost detail matching the earnings and liability type specified to the right of this field will be included in this sequence. If no earnings type or liability type is specified, all earnings and liability types will be included in this sequence. If no earnings type specified, but a liability type is specified, job cost detail for any earnings type that has that liability type will be included. If an earnings type is specified, but no liability type, job cost detail for all liability types for the specified earnings type will be included.
Note: Job Cost detail with no earnings type and liability type specified will be skipped.

A-All
 All PR and JC transactions are included in this sequence, regardless of the value in the Liability Type or Earn Type fields.
Important: When using this option, the Liability Type and the Earn Type should not be set to null (blank) for any additional sequences; this generates a multiple sequence warning and the transaction is not placed.

Note: If this field is left blank for a sequence, the Liability Type and Earn Type columns will be set to 'null' and skipped. When initializing billings based on this template, this sequence will only pull job cost detail with no liability type and earnings type.
[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Liability Type

 This field is available when the Earn/Liab Opt field is set to “L-Liability” or “B-Both.”
 Specify the liability type (from HQ Liability Types) to restrict job cost detail by for this sequence. Only job cost detail with this liability type will be included in this sequence. Leave blank to include all liability types.
Important: This field should not be set to null (blank) when the Earn/Liab option has been set to A-All for another sequence; this generates a multiple sequence warning and the transaction is not placed.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Earn Type

 This field is available when the Earn/Liab Opt field is set to “E-Earnings” or “B-Both.”
 Specify the earnings type (from HQ Earn Types) to restrict job cost detail by for this sequence. Only job cost detail with this earnings type will be included in this sequence. Leave blank to include all earnings types.
Important: This field should not be set to null (blank) when the Earn/Liab option has been set to A-All for another sequence; this generates a multiple sequence warning and the transaction is not placed.
[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Price Option

 Specify which pricing option to use for determining what value will be used as the billing price for a material when creating material detail invoices.

- C-Actual Price – The actual unit cost is posted to JC Cost Detail (JCCD) for all materials, regardless of whether they are stocked or not. This option can be used for all sources (AP, EM, IN, JC, and MS).

- P-Std Price – The standard unit price from HQ Materials is used. If a standard price is not indicated in HQ Materials (which may be the case if the source is not IN or MS) the actual unit cost posted to JCCD is used.

- L-Location Price – If the source is IN or MS, and the posted material is stocked, the unit price for the material/location is used. For all other sources, the actual unit cost posted to JCCD is used. This option is only available if MS and/or IN are active.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Markup Option

This field is used to define the type of markup used when creating invoices. The sequence type determines what type of markup is applicable for the line.
Note: Sequences with an “Amount” type cannot be used with any markup option other than N (No Markup), as they are typically billed as a flat amount.
 The following table discusses each markup type and which types of sequences they can be used with.

Markup Option
Description
Used With Seq Type

N-No Markup
No markups are used.
ALL

S-Rate
Uses the rate entered in the Markup/Discount Rate field.
Source, Detail Addon, Total Addon

R-Retainage
Creates a retainage line for the sequence using the rate entered in the Markup/Discount Rate field.
Detail Addon, Total Addon

D-Discounts
Creates a discount line for the sequence using the rate entered in the Markup/Discount Rate field.
Detail Addon, Total Addon

T-Taxes
Adds taxes to the sequence line based on the tax code specified for the contract item.
Note: If you post intercompany invoices (i.e. the AR company in JC Company Parameters differs from the JC/JB company), and tax is applied to an invoice (billing), the tax liability remains with the AR company. For example, if JB Co #1 posts an invoice of $1050 (includes $50 tax) ARCo #2 will receive a debit of $1050 to its Receivables account, a credit of $50 to its Sales Tax Payable account, and a credit of $1000 to its Intercompany Payables account. JB/JC Co #1 receives a debit of $1000 to its Intercompany Receivables account and a credit of $1000 to its Contract Revenue account.
Source, Detail Addon, Total A`ddon

U-Rate per Unit
Adds a markup to the sequence line based on the number of posted units times the rate entered in the Markup/Discount Rate field.
Source, Detail Addon

H-Rate per Hour
Adds a markup to the sequence line based on the total hours for the detail add-on's source line (i.e. the sum of hours for all detail records for the source line) times rate entered in the Markup/Discount Rate field.
Detail Addon

X-Retainage Tax
Adds retainage tax to the sequence line based on the tax code specified for the contract item.
Detail Addon, Total Addon

 The markup rate is used in conjunction with the markup option to determine the actual markup or discount amount for the sequence line. For “source” type sequences, the markup/discount rate will be used to calculate the amount for internal markups. Markups are applied to the detail lines for each source. For “add-on” type sequences, this rate is used to calculate the add-on amount. For Detail Add-ons, the rate is applied to each source. For Total Add-ons, the rate will be applied to the total of all sources.
Note: For Total Addon sequence types where the Markup Opt is “S-Rate,” and a markup rate is not specified a contract item is, the markup rate defined for the contract item (in JC Contract Items) will be used when calculating the billing amount. If a markup rate has not been specified for the contract item, the individual rates for each item on the billing will be used.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Markup Rate

 If a “source” type sequence, this rate will be used to calculate the amount for internal markups. Markups are applied to the detail lines for each source.
 For “add-on” type sequences, this rate is used to calculate the add-on amount.

- Detail Add-ons – Rate is applied to each source.

- Total Add-ons – Rate is applied to the total of all sources. If a contract item is specified for the sequence (to the right) and no markup rate is specified here, the markup rate for the specified contract item (in JCCI) will be used. If no markup rate specified in JCCI, the individual markup rates specified for each item on the billing will be used.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

## Contract Item

 Use this field to direct flat billable amounts and/or total add-ons to a specific contract item. This field is only available for sequence types Amount or Total Addon (with a Markup Opt of Rate or Taxes).
Specify the contract item to which this sequence's bill amount will be posted. Make sure that the contract(s) that this template is assigned (in JB Contract Info) are set up with this contract item, or they will not be processed when initializing billings.
 If no contract item is specified for the template sequence, billing amounts will be posted individually to their respective contract items.
Amount
For Amount sequence types, the bill amount (determined by the 'Flat Amt Opt') will be posted to this contract item; however, the specified contract item must be associated with at least one phase on the job (in JCJP). Otherwise, no amount will be posted. If left blank, amount will be posted to contract item #1.
Total Addon
For Total Addon sequence types, the bill amount (add-on value for all items) will be posted to this contract item. If left blank, bill amounts will be posted to their respective contract items.

- If the add-on's markup option is “S-Rate”:

- and a markup rate is specified for the template, all items on the billing will be added and the specified markup rate applied to the total.

- and no markup rate is specified for the template sequence, the markup rate specified for the contract item (in JC Contract Items) is used. All items on the billing will be added and the sequence's markup rate applied to the total.

- and no markup rate is specified for the contract item, then the individual rates for each item on the billing will be used. In this case, each item value will be multiplied by its own rate (from JC Contract Items) and then all totals added together.

- If the add-on's markup option is “T-Tax”, the tax code specified for the item in JC Contract Items is used to determine tax rate. All items on the billing will be added and the tax rate applied to the total. If any of the items have a different tax code, calculation will not occur and an error will display. Errors must be corrected and bills repulled. Items with a null tax code will be skipped (i.e. not included in the total addon tax value). Also make sure that the contract item on each applicable contract has an assigned tax code. If no tax code is assigned, the sequence is skipped for that contract.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Flat Amt Opt

Use this field when the billable amount for a sequence line is a flat amount. Typically, flat amounts are used when the billable amount is not associated with job cost detail or detail from other sources (i.e. AP, PR, EM, IN, or MS). For example, if a job only requires a one-time billing, and the billable amount should be the value of the current contract, select “C-Curr Cont Amt” in this field. Or, if billing a recurring monthly fee (e.g. maintenance), select “F-Flat Bill Amt” to set up the monthly fee as a flat billing amount.

- O-Orig Cont Amt – Uses the original contract amount (total of all contract items with a Bill Type of T) as the billing amount for the sequence.

- C-Curr Cont Amt – Uses the current contract amount (including all change orders) as the billing amount for the sequence.

- F-Flat Bill Amt – Uses the T&M Flat Billing Amount specified for the contract (in JB Contract Info) as the billing amount for the sequence.

- A-Addon Amt – Uses the amount specified in the Add-on Amt field for the sequence.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Addon Amt

 For sequence type A (Amount) only, when Flat Amount Option is A (Add-on Amount).
 Enter the add-on amount for this sequence.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Misc Dist Code

 For miscellaneous type sequences, enter the miscellaneous distribution code (from AR Misc Distribution Codes) for this line’s amount.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Cost Types: Cost Type

 If you initialized cost types for this sequence (Initialize All Cost Types button to the right of grid), displays all cost types defined in JC Cost Types. Delete or add cost types as applicable to this sequence. (Each cost type's category is displayed in the CT Category column of the grid. This category will be used to group cost types together on the billing.)
Note: If you have specified to use Labor, Equipment, and/or Material categories, you must specify a corresponding cost type. For example, if using labor categories, you must specify a labor and/or burden cost type (i.e. cost type with a labor or burden category).
[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Cost Types: CT Category

 Display only, the category assigned to this cost type in JC Cost Types. Cost type category will be used to group cost types together on billings.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Sequence

 Automatically displays all sequences to which the selected add-on is applicable. Only sequences prior to the add-on sequence will be included. Each sequence’s Type, Group, and Description are displayed to the right.
 Template sequences may be deleted or added as needed.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Type

 Display only, the sequence type.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Description

 Display only, the description of the specified sequence.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Group #

 Display only, the group number assigned to the specified sequence.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Add-on Seq

 Automatically displays all add-ons to which the selected sequence is subject. Each add-on’s Type, Group, Description, Markup Option, Markup Rate, and Add-on Amt are displayed to the right.
 Add-on sequences may be deleted or added as needed.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Type

 Display only, the sequence type.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Description

 Display only, the description of the specified sequence.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Group #

 Display only, the group number assigned to the add-on sequence.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Markup Opt

 Display only, the markup option assigned to the add-on sequence.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Markup Rate

 Display only, the markup rate assigned to the add-on sequence.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup

##  Addon Amt

 Display only, the add-on amount specified for this add-on.

[](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)JB T&M Template Setup
