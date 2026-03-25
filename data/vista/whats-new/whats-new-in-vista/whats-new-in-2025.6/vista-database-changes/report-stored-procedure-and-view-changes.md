---
title: "Report Stored Procedure and View Changes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/vista-database-changes/report-stored-procedure-and-view-changes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/whats-new-in-2025.6/vista-database-changes/report-stored-procedure-and-view-changes"
---

# Report Stored Procedure and View Changes

The following tables display all report stored procedures and/or views that have been modified, added, or deleted for the Vista 2025.6 release to improve performance or correct data display, along with the reports that are affected by this change.
Unless you have already followed instructions from previous
 release notes or Viewpoint's web
 site, please copy Viewpoint's
 standard stored procedures to a new name if you have copied or modified any of the
 reports listed below. For specific instructions on copying stored procedures, see
 the [Copying Stored
 Procedures](https://support.viewpoint.com/s/knowledgedetail?c__urlname=150925535527899) document available in the Support Knowledge Base area of the
 Viewpoint Customer Portal ([support.viewpoint.com](https://support.viewpoint.com/)). Reports can be found in the
 Vista Users section under Crystal
 Reports.
Unlike stored procedures, Viewpoint does not require customers to copy views (brv[view name]) for related reports used as starting points for customer-modified reports. If you have copied and modified any of the reports affected by view changes (listed below) however, you may need to open your own report in the Crystal Reports Designed and select Database > Verify Database.

## Stored Procedures


 There are no new/changed/deleted report stored procedures, stored procedure parameters, or views for the Vista 2025.6 release.


## New Report Stored Procedure Parameters

The following is a list of all new parameters for report stored procedures.
Stored Procedure
Parameter

urptExecDashCacheUpdate_TC1@MaxMonthsOfHistory

## Views

The following table displays all report views that were added or changed for this release, along with affected reports.
ViewReport TitleReport File NameReport ID
brvJCCDDetlDescJC DetailJCDetail.rpt506
brvJCCDDetlDescJC Unit Cost DrilldownJCUCDrillDown.rpt554
brvJCJobMatDetlDescJC Job MaterialsJCJobMaterials.rpt957
brvPRDL_APCOPR Deduction and Liability CodesPRDeductLiab.rpt792
brvPREC_PhsGrpPR Earnings CodesPREarnings.rpt803
brvPRECConvertPR Check PrintPRCheck.rpt772
brvPRECConvertPR Check Print StubPRCheckPrintStub.rpt773
brvPRECConvertPR EFT RemittancePREFTRemittance.rpt800
brvPRECConvertPR Check Print Stub By EmployeePRCheckPrintStubByEmployee.rpt1035
brvPRECConvertPR EFT Remittance By EmployeePREFTRemittanceByEmployee.rpt1036
brvPRECConvertPR Cheque PrintPRChequeCAN.rpt1037
brvPRECConvertPR Cheque Print StubPRChequePrintStubCAN.rpt1038
brvPRECConvertPR Cheque Print Stub By EmployeePRChequePrintStubByEmployeeCAN.rpt1039
brvPRECConvertPR Cheque EFT RemittancePRChequeEFTRemittanceCAN.rpt1040
brvPRECConvertPR Cheque EFT Remittance By EmployeePRChequeEFTRemittanceByEmployeeCAN.rpt1041
brvPRECConvertPR Cheque Print Stub By Employee - A/NZPRChequePrintStubByEmployeeAUS.rpt1075
brvPRECConvertPR Cheque Print Stub - A/NZPRChequePrintStubAUS.rpt1076
brvPRECConvertPR EFT Remittance By Employee - A/NZPREFTRemittanceByEmployeeAUS.rpt1077
brvPRECConvertPR EFT Remittance - A/NZPREFTRemittanceAUS.rpt1078
brvPRECConvertPR Cheque Print - A/NZPRChequeAUS.rpt1079
brvPRECConvertPR Cheque Print Stub - CA BilingualPRChequePrintStubCANBL.rpt1273
brvPRECConvertPR Cheque Print Stub By Employee - CA
 BilingualPRChequePrintStubByEmployeeCANBL.rpt1275
brvPRECConvertPR Cheque Print - CA BilingualPRChequeCANBL.rpt1276
vrvAPPBausAP Cheque Print - A/NZAPChequeAustralia.rpt1056
vrvAPPBausAP Cheque Print by Vendor - A/NZAPChequeByVendorAus.rpt1100
vrvJBLaborRatesJC Owner Job CostJCOwnerJobCost.rpt991
vrvPMContractAnalysisDDPM Contract Analysis DrilldownPMContractAnalysisDD.rpt1120
vrvPMContractAnalysisDDPM Contract Analysis Drilldown - A/NZPMContractAnalysisDDAUS.rpt1134
