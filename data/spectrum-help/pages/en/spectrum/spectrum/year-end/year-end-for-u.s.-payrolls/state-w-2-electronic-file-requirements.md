---
title: "State W-2 Electronic File Requirements | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/state-w-2-electronic-file-requirements"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/state-w-2-electronic-file-requirements"
---

# State W-2 Electronic File Requirements

Information on how you might modify the standard Federal file to adhere to the U.S. state(s) you're filing with.
Spectrum's electronic file export uses the basic formatting of the Federal EFW2 specifications.
Support doesn't assist with modifying electronic files for state-specific formats. You may opt to contract with Technical Services or Professional Services or an outside consultant for such assistance.

## Electronic Filing Instructions for States with Different W-2 Forms

The states listed below require an electronic file format that differs from the basic Federal EFW2 electronic filing specifications. To the best of our knowledge, the state-specific variations are those listed below. Contact the individual taxing authority of each state you are filing in for information on the current electronic filing specifications.
After creating the standard W2REPORT, open it in Notepad and modify the file per the state's requirements.

## Alabama

Requires 4 rows in the RS record for each employee that are optional/not applicable in the Federal EFW2 specifications. These are:

- Field 248-257. Your State EIN number. Alabama doesn't want it zero filled.

- Field 298-307. Federal Tax Withheld. This is optional in the Federal EFW2 specifications.

- Field 338-348. Misc Income Field. This is optional "Supplemental Data" in the Federal EFW2 specifications.

- Field 393-396. Payment year field. This is optional "Supplemental Data" in the Federal EFW2 specifications.

## Colorado

Requires a carriage return character at the end of each record. This is optional in Federal specifications.

## Connecticut

Requires a carriage return character at the end of each record. This is optional in Federal specifications.

## Georgia

Requires a carriage return character at the end of each RS record. This is optional in Federal specifications.

## Idaho

Requires a carriage return character at the end of each record. This is optional in Federal specifications.

## Maryland

Requires a carriage return character at the end of each RS record. This is optional in Federal specifications.

## Minnesota

Requires the "number of RW records" in the RT record must match the actual count for the employee.
RS Record Location 248-267 State Employer Tax ID is left justified. Leading zeros must be removed; add spaces to the end to maintain field length.

## Mississippi

Requires a carriage return character at the end of each record. This is optional in Federal specifications.
Requires a date in spaces 197-202 of each RS record. The field is six digits and formatted as "period end and year", so entering mmyyyy is successful.
RW record field 88-109 cannot be blank. This field is the delivery address for the employee.
RW record field 265-275 must be blank. Replace zeros with blanks.
RS record field 95-116 cannot be blank. This field is the delivery address for the employee.
RS record field 225-226 must be numeric. This is "number of weeks worked" and relates to state unemployment.

## Nebraska

Requires additional information in the RV record.
Location 1-2 RV
Location 3-9 Total RS records for Nebraska
Location 10-24 Total Taxable wages for Nebraska
Location 25-39 Total Nebraska income tax withheld
Location 40-512 Leave blank

## North Carolina

Requires a carriage return after the 512th position on each line.
Requires a Software Vendor Code in positions 20-23 of the RE record. This is optional in the Federal specifications, and Viewpoint does not have a Software Vendor Code.

## Ohio

Requires a carriage return after the 512th position on each line.

## Oregon

Requires additional information in the RV record.
Location 1-2 RV
Location 3-9 Total RS records for Oregon
Location 10-24 Total Taxable wages for Oregon
Location 25-39 Total Oregon income tax withheld
Location 40-512 Leave blank

## Pennsylvania

Requires a carriage return character at the end of each record. This is optional in Federal specifications.
Requires the employers 8-digit state employer ID inserted in positions 505-512 on the RE record.

## South Carolina

Requires a date in spaces 197-202 of each RS record. The field is 6 digits and formatted as "period end and year", so entering mmyyyy is successful.

## Vermont

Requires a carriage return character at the end of each record. This is optional in Federal specifications.
Location 248-267 RS record State Employer Tax ID is left justified. Leading zeros must be removed, add spaces to the end to maintain field length.

## West Virginia

Location 248-267 RS record State Employer Tax ID is left justified. Leading zeros must be removed, add spaces to the end to maintain field length.

## Wisconsin

Location 248-267 RS record State Employer Tax ID (15 digits) is left justified. Leading zeros must be removed, add spaces to the end to maintain field length.
