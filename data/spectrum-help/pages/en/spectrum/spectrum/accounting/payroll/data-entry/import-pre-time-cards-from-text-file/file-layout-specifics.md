---
title: "File Layout Specifics | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/file-layout-specifics"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/file-layout-specifics"
---

# File Layout Specifics

The import file must be a comma delimited text file.
The first fields are necessary for processing and must be filled out. The optional fields
 follow, and are not necessary for processing. The optional fields can be left blank or the
 file can be truncated. For example, if you only need to write fields batch through pay rate
 level, then only these fields are needed in the file.
Note: If cost centers are being used, an optional cost center field will display on the
 File Layout list.
Important: The routine that reads the file needs to have the
 variables in the correct order. If fields are skipped, then a comma must still be present
 to hold the position. In the following example, the job/phase/ct are blank, and the record
 ends after the pay rate level field.File Layout Specifics -
 Information FlowWhen defaulting, the software will work by
 first looking to the comma delimited text file. If the comma delimited text file
 contains a variable that is not required, then it will use it. Otherwise, it will use
 the default from Spectrum.This is the layout that Spectrum
 will be expecting.
Field #
Descriptions
Notes
Type
Max Len
Required?

1
Batch Code
batch for pre-time card processing.
alpha
8
yes

2
Employee Code
validated
alpha
11
yes

3
Department
must be valid department
alpha
6
yes

4
Pay Type,
Add-on or Deduction code
All pay types are supported including: R, O, D, H, V, S, C, M, SA ,ER, EO, ED,
 EU, RP, JX, 1, 2, 3, Q (only applies to Quantity), U. Incentive pay types
 are supported (for example: IR, IO, ID when "I" is specified on the
 Payroll Installation screen.)
All valid add-on and deductions are supported.
alpha
2
yes

5
Hours
hours worked
numeric
10
yes

6
Job
validated
alpha
10
yes*

7
Phase
validated
alpha
20
yes*

8
Cost Type
validated
alpha
3
yes*

9
Date
work date in MM/DD/YY format
alpha
8
no

10
Message Line
alpha
30
no

11
Pay Rate Level
1 - 9
alpha
1
no

12
Wage Code
validated
alpha
2
no

13
Union Code / Pay group
validated
alpha
6
no

14
Worker's Comp
validated
alpha
6
no

15
State Tax Code
validated
alpha
2
no

16
County Tax Code
validated
alpha
2
no

17
Local Tax Code
validated
alpha
2
no

18
Equipment Code**
must be valid code
alpha
10
no

19
Equipment Hours
not validated
numeric
8
no

20
Quantity***
non-zero
numeric
11
no

21
Company code
must be valid company
alpha
3
no

22
Pay rate
not validated
numeric
11
no

23
Equipment cost category
validated
alpha
4
no

24
Crew number
validated
alpha
10
no

25
Cost center
validated (if cost centers are turned on in the Enterprise
 Installation screen)
alpha
10
no****

26
Work order
the work order will be from the company code specified above
alpha
10
no

27
Site equipment
validated
alpha
8
yes*****

28
Site component
validated
numeric
2
yes*****

29
Contract
validated
alpha
10
no

30
Equipment work order
validated
alpha
10
no

31
Billing code
validated as a time + material code for direct job cost entries, or as a work order code for time cards referencing a work order.
alpha
10
no

32
Billing rate
validated
numeric
10
no

* If direct cost department, then this field is mandatory; otherwise it must be blank.
** Provided that a valid equipment code is included in the text file, the ER, EO, ED, and EU pay types will be imported into the Pre-Time Card Detail file with the standard defaults.
*** The records associated with the Quantity pay type will be imported into the Pre-Time Card Quantity Detail file. Validation will be performed to assure the phase code is valid and the quantity itself is non-zero.
**** If the cost center field is blank and it's a non-direct department, Spectrum sends it to the error file. For direct job and direct equipment departments, Spectrum assigns the cost center, regardless of the validity of the entry in the import.
***** If the Work Order Installation option for 'Require equipment/component code for work order transactions?' is selected, then a valid equipment and component code is required.
The following is an example of a comma delimited text file.
J18,BUHJAY,1J,R,8,200,010200,L,06/18/03,has a job,1,,WA020,0101,,,,,,,XYZ,11.13
J18,BUHJAY,1J,O,2,200,010200,L,06/18/03,has a job,1,,WA020,0101,,,,,,,XYZ,25.66
J18,BUHJAY,1J,D,1,200,010200,L,06/18/03,has a job,1,,WA020,0101,,,,,,,XYZ,31.897
J18,BUHJAY,1E,R,8,,,,06/18/03,has equipment,1,,WA020,0101,,,,BL14,,,XYZ,1.568
J18,BUHJAY,1E,O,2,,,,06/18/03,has equipment,1,,WA020,0101,,,,BL14,,,XYZ,7.896
J18,BUHJAY,1E,D,1,,,,06/18/03,has equipment,1,,WA020,0101,,,,BL14,,,XYZ,9.995
J18,BUHJAY,1J,ER,8,200,096800,L,06/19/03,has job and equipment,1,,WA020,0101,,,,BL16,7,,XYZ,15.66
J18,BUHJAY,1J,EO,2,200,096800,L,06/19/03,has job and equipment,1,,WA020,0101,,,,BL16,2,,XYZ,33.22
J18,BUHJAY,1J,ED,1,200,096800,L,06/19/03,has job and equipment,1,,WA020,0101,,,,BL16,1,,XYZ,12.123
J18,BUHJAY,1J,EU,8,200,096800,E,06/20/03,has job and equipment,1,,WA020,0101,,,,BL16,8,,XYZ,30.987
J18,BUHJAY,1A,ER,8,,,,06/22/03,has equipment,1,,WA020,0101,,,,BL16,7,,XYZ,6.667
J18,BUHJAY,1A,EO,2,,,,06/22/03,has equipment,1,,WA020,0101,,,,BL16,2,,XYZ,19.785
J18,BUHJAY,1A,ED,1,,,,06/22/03,has equipment,1,,WA020,0101,,,,BL16,1,,XYZ,45.446
J18,BUHJAY,1A,EU,8,,,,06/23/03,has equipment,1,,WA020,0101,,,,BL16,8,,XYZ,62.33
J18,BUHJAY,1J,R,1,200,010200,L,06/24/03,line,1,,,,,,,,,,XYZ,101.22
J18,BUHJAY,1E,O,2,,,,06/24/03,needs category,1,,,,,,,BL14,,,XYZ,7.432
J18,BUHJAY,1J,ED,1,200,096800,L,06/24/03,line,1,,,,,,,BL16,,,XYZ,7.89
J18,BUHJAY,1A,ER,2,,,l,06/24/03,doesn't need category,1,,,,,,,BL16,,,XYZ,25.60
J18,BUHJAY,1A,R,1,,,,06/24/03,line,1,,,,,,,,,,XYZ,60.10
J18,BUHJAY,1A,EU,3,,,,06/24/03,line,1,,,,,,,BL16,3,,XYZ,33.668
J18,BUHJAY,1J,EU,2,200,096800,E,06/24/03,line,1,,,,,,,BL16,2,,XYZ,88.51
J18,,,Q,,200,096800,L,06/24/03,QUANITY LINE,6,,,1200,OR,X2,Y1,,,17,XYZ,,
J18,,,Q,,130,02000,L,06/25/03,QUANTITY LINE ELE,,,,,,,,,,22,
J18,BUHJAY,DA,R,1,,,,06/25/03,ELE line,1,,,,,,,,,,,67.60
J18,BUHJAY,DJ,R,1,130,02000,L,06/25/03,ELE line,1,,,,,,,,,,,1025.22
J18,BUHJAY,DJ,EO,1.75,130,14000,L,06/25/03,ELE line,1,C1,WA020,,,,,TN33,7,,,77.89
J18,WILDAN,1A,H,8,,,,06/26/03,ELE line,1,,,,,,,,,,XYZ,60.10
