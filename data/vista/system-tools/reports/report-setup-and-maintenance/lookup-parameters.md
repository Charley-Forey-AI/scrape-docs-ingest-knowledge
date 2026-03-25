---
title: "Lookup Parameters | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/lookup-parameters"
---

# Lookup Parameters

Lookup Parameters are used to provide certain F4 Lookups with additional, necessary information in order to return only pertinent data; the most common parameter would be your current company.
Without these additional parameters, the associated lookups bring in more data than is necessary for accurate reporting (e.g., bringing data in from multiple companies).
Lookups used for standard reports are already hardcoded with parameters and do not require additional information to locate appropriate data. When copying a standard report, hardcoded parameters are utilized for the new report. When creating a custom lookup, you must ensure that report parameters exactly match the lookup parameters established for your report.
When creating custom reports, most lookups will require additional parameters, in addition to existing lookup parameters that must be included (based on the datatype specified in the Datatype field for the selected report parameter). See the table below for a sample list of lookups and their required Lookup Parameters.
Important: The parameters you define for lookups must exist in your report parameters. For example, if you use the JCOH lookup, you must have both the “?Company” and “?Job” parameter in your report, in that order. Otherwise, the F4 will not work. Additionally, the lookup parameters and report parameter names must be identical. If a parameter does not exist in the report, a warning displays. The user can then fix the problem in one of three ways: 1) Retype the parameter in RP Report Parameters; 2) Click the Update Parameters button in RP Report Titles and reload parameters or; 3) Delete the parameter from RP Report Parameters.
Viewpoint Type
Lookup
Title
Lookup Parameters

bACO
JCOH
Change Order Header
?Company, ?Job

bACOItem
JCOI
Change Order Items
?Company, ?Job , ?ACO

bBatchID
HQBCAll
HQ Batches - All
?Company, ?Month

bBillNumber
JBIN
JB Bill Number Lookup
?Company, ?BillMonth, ?BillType

bChgOrder
PMPCO
Pending Change Orders
?Company, ?Project, ?PCOType

bContractItem
JCCI
JC Contract Items
?Company, ?Contract

bGLRef
GLRF
References
?Company, ?Month, ?Journal

bPCO
PMPCO
Pending Change Orders
?Company, ?Project, ?PCOType

bPCOItem
PMPCOItem
Pending Chg Order Items
?Company, ?Project, ?PCOType ,?PCO

bPMACO
PMACOReport
Approved Change Orders
?Company, ?Project

bPMACOItem
JCOI
Change Order Items
?Company, ?Job, ?ACO

bPMMeeting
PMMeeting
PM Meeting
?Company, ?Project

bPOChgOrder
POChngOrdReports
PO Change Orders
?Company, ?PO

In some cases, a required report parameter can be substituted for another parameter, as long as the information correlates with both parameters. For example, you create an Approved Change Order report with parameters of “?Company, ?Job, and ?ACO”. You decide to use the F4 lookup for Datatype bPMACO (PMACOReport). The Lookup Parameters for PMACOReport are “?Company and ?Project”. You can subsitute the “?Project” lookup parameter to “?Job”, as both parameters refer to the same values. Refer to the example below:
Parameter Name
Seq
Type
Viewpoint Type
Description
Default
Lookup Parameters

?Company
1
N
bPMCO
Company

?Job
2
S
bJob
Job

?ACO
3
S
bPMACO
Approved Change Order

?Company, ?Job

Related information

- [About the RP Report Parameters Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form)

- [Report ID](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003d99f--en)

- [Parameter Name](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003d9a8--en)

- [Display Sequence](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003d9b6--en)

- [Datatype](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003d9be--en)

- [Input Type](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003d9d1--en)

- [Precision](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003d9de--en)

- [Input Mask](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003d9f7--en)

- [Input Length](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003da41--en)

- [Description](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003da4d--en)

- [Default Type](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003da56--en)

- [Default Value](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003da66--en)

- [Required](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003db32--en)

- [Lookup is Active](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003db3a--en)

- [Load Sequence #](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003db44--en)

- [Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003db4d--en)

- [Add'l Lookups: Lookup](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003db58--en)

- [Add'l Lookups: Lookup Parameters](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003db62--en)

- [Add'l Lookups: Load Sequence](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003db6d--en)

- [Add'l Lookups: Active](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-parameters-form/field-definitions-rp-report-parameters-form#ID-0003db76--en)

- [Additional Lookups](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/additional-lookups)
