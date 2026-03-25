---
title: "PR Timecard Entry (PRTB) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pr-timecard-entry-prtb"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/form-information-and-sample-text-files/pr-timecard-entry-prtb"
---

#  PR Timecard Entry (PRTB)

Time Card Entry - Table bPRTB

 Columns that are typically used for importing are in yellow

Column Name
Type
Importable
Default Available
Length & Scale
Required
Comments

Co
company
Yes
No
### - 0 to 999
yes
Payroll Company number.Must exist in HQCO.

Mth
bMonth
Yes
Yes
MM/YY
yes
Month can be derived from Payroll ending date.

BatchId
bBatchID
No
Yes
##########
yes
Viewpoint Import will create next BatchId.

BatchSeq
int
No
Yes
##########
yes
Viewpoint Import will always generate the next Batch Sequence.

BatchTransType
char
No
Yes
1 Character
yes
Viewpoint Import will always set this value to "A" for additions.

Employee
bEmployee
Yes
No
######
yes
Unique number identifying this employee.

PaySeq
tinyint
Yes
No
###
yes
Payment Sequence used to indicate separate payments within a Pay Period.If an Employee is to receive more than one payment in the Pay Period, multiple sequences must be setup.

PostSeq
smallint
No
No
#####
no
Posting sequence number used to keep entry unique within Pay Period, Employee, and Payment Sequence.Assigned as next available number when added.Not editable. Viewpoint Import will generate next posting batch number.

Type
char
Yes
No
1 Character
yes
J=Uses Job timecard entry grid.Time may be posted to a Job or simply expensed.Equipment usage may be posted. M=Uses the mechanics timecard entry grid.Time may be posted to an equipment maintenance Work Order.

DayNum
tinyint
Yes
No
###
yes
Day number relative to the beginning date of pay period.1 would be the first date of the pay period, 2 would be the second, etc.Typically used to make date entry easier on weekly and bi-weekly payrolls, but can be used with any pay frequency.

PostDate
bDate
Yes
No
MM/DD/YY
yes
Date earnings are posted.Used when determining whether old or new rates should be applied with Craft deductions and liabilities.

JCCo
bCompany
Yes
No
###
no
JC Company these earnings will be posted to.Only expensed to JC if both Job and Phase are entered.If entered, must be a valid JC Company.

Job
bJob
Yes
No
10 Characters
no
Job to be expensed with these earnings.Only expensed to JC if both Job and Phase are entered.If entered, must be a valid Job, using standard validation logic.

PhaseGroup
bGroup
No
No
###
no
Phase Group used to qualify Phase code.Pulled from bHQCO based on JC Co#.Not editable.

Phase
bPhase
Yes
No
20 Characters
no
Phase to be expensed with these earnings.Null if not posted to a Job.Can be null even if Job is entered, if "Allow No Phase" option in bPRCO is flagged.Earnings will not be expensed to the JC unless Job and Phase are both entered.

GLCo
bCompany
Yes
Yes
###
yes
GL Company to be expensed with these earnings.Based on JC Co# if earnings are posted to a Job, based on EM Co# if earnings are posted as mechanics pay.May be entered if not expensed to a Job or Equipment.

EMCo
bCompany
Yes
No
###
no
EM Company to receive equipment revenue if usage is posted, or EM Company to be expensed if earnings posted as mechanics time.

WO
bWO
Yes
No
10 Characters
no
Equipment Work Order referenced when posting mechanics time.Not required.

WOItem
bItem
Yes
No
#####
no
Work Order Item number referenced by these earnings when posting mechanics time.Null unless Work Order is entered.

Equipment
bEquip
Yes
No
10 Characters
no
Equipment code credited with the revenue if usage is posted, or expensed with the labor costs if posting mechanics time.

EMGroup
bGroup
No
No
###
no
Used to qualify Cost Code.Pulled from bHQCO based on EM Co#.Not editable.

CostCode
bCostCode
No
No
10 Characters
no
Used to qualify Cost Code.Pulled from bHQCO based on EM Co#.Not editable.

CompType
varchar
Yes
No
10 Characters
no
Component type.Optional level of cost trackingon equipment.If entered, must be valid for the equipment.

Component
bEquip
Yes
No
10 Characters
no
Component of the equipment.Optional level of tracking costs for equipment.If a component type is entered, a valid component must also be entered.

RevCode
bRevCode
Yes
No
10 Characters
no
Equipment revenue code.Optional, only available if posting equipment usage with a job costed timecard.

EquipPhase
bPhase
Yes
No
20 Characters
no
Equipment Phase tracking equipment use.

EquipCType
bJCCType
Yes
No
###
no
JC Cost type tracking equipent use.Pulled from bEMEM based on Equipment.Not editable.

UsageUnits
bHrs
Yes
No
########.##
no
Number of usage units, usually hours.Only available if posting equipment usage on job costed timecards.

TaxState
bState
Yes
Yes
2 Characters
no
State used to determine which TaxState based deductions and liabilities are to be calculated.

LocalCode
bLocalCode
Yes
Yes
10 Characters
no
Local Code used to identify city, county, or other local taxing district.

UnempState
bState
Yes
Yes
2 Characters
no
State used to determine which Unemployement based deductions and liabilities are to be calculated.

InsState
bState
Yes
Yes
2 Characters
no
State used to determine which Insurance based deductions and liabilities are to be calculated.

InsCode
bInsCode
Yes
Yes
10 Characters
no
Used with InsuranceState to determine which Worker Comp deduction and liabilities are to be calculated.

PRDept
bDept
Yes
Yes
10 Characters
yes
PR Department assigned to this Employee.May be overridden, but must be a valid PR Department.Will be used to determine GL Accounts during GL update unless earnings have been posted to a Job, and"PRUseJCDept" option in JCCO is "Y".

Crew
varchar
Yes
Yes
10 Characters
no
Crew this Employee was working with.May be null, but if entered, must be a valid Crew in PRCR.

Cert
bYN
Yes
Yes
1 Character
yes
Indicated whether this timecard should appear on a Certified Payroll Report. Y=Certified time card.Will appear on Certified Payroll Transcript reports. N=Excluded from Certified Payroll reports.

Craft
bCraft
Yes
Yes
10 Characters
no
Indicated whether this timecard should appear on a Certified Payroll Report.Y=Certified time card.Will appear on Certified Payroll Transcript reports. N=Excluded from Certified Payroll reports.

Class
bClass
Yes
Yes
10 Characters
no
Work classification used to determine pay rates, and Craft based deductions, and liabilities.Required if Craft has been entered.Must be null if Craft is null.If entered, must be a valid Craft/Class combination setup in PRCC.

EarnCode
bEDLCode
Yes
Yes
#####
yes
Posted earnings code.Required, must be a valid earnings code setup in bPREC.

Shift
tinyint
Yes
Yes
###
yes
Shift ofwork these earnings occurred under.Used to determine default pay rates.Required, but need only be valid if Craft and Class have been entered.

Hours
bHrs
Yes
No
########.##
yes
Hours worked.Required, but may be negative.

Rate
bUnitCost
Yes
Yes
###########.#####
yes
Hourly earning rate.Required.

Amt
bDollar
Yes
Yes
##########.##
yes
Posted amount of earnings.Required.

Memo
varchar
Yes
No
500 Characters
no

StartTime
bTime
Yes
No
hh:mm
no
Hours in 24-hour format

StopTime
bTime
Yes
No

no
Hours in 24-hour format

BreakHours
bHrs
Yes
No
##,###,##0.00
no
Maximum value is 24 hours

Table Guidelines
The definition of each of the table’s columns is outlined below.

- Column Name – The name of the column/field in the database table.

- Type – The column’s SQL data type. Types starting with a “b” are Viewpoint defined data types.

- Importable – The field is available for import.

- Default Available – Indicated if a programmatic default value is available for this field. Defaults use the same logic as a posting program to determine a value.

- Length and Scale – Indicates the format of the field.

- Required – Indicates if the data is required.
A hard coded default value can be specified in IM Template; when importing files this value overwrites the imported value.
Note:Use the Template Detail tab in the IM Template form to add any additional fields for importing.
