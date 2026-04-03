---
title: "Guide to Spectrum Files | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/guide-to-spectrum-files"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/guide-to-spectrum-files"
---

# Guide to Spectrum Files

Use the table provided for reference when completing the
 fields on the Spectrum Files screen.
Note: Spectrum user-defined variables are defined as
 separate files, not part of the main data file. The file name contains a U in the first
 position following the decimal point. For example, PR.UDEMP is the user-defined file
 associated with PR.EM1 and PR.EM2. User-defined files may be looked up in Table Directory
 Inquiry by requesting partial file PR.U or AP.U, and so forth.
Cat
Description
PROIV File name
SQL database table
Variables/Comments

A/P
Vendor master file
VN.MSTR
VN_VENDOR_MASTER_MC
1099 indicator, labels, state

Vendor open item file
VN.ITEMS
VN_OPEN_ITEMS
Types I and C, dates

Payment history file
VN.PHIST
VN_PAYMENT_HISTORY
Checks #, dates

Check reconciliation file
VN.RECON
VN_CHECK_RECONCILIATION
Manual vs. computer by vendor

Vendor AP G/L Header file
VN.GLHDR
VN_GL_DISTRIBUTION_HEADER
Acct # by header

Vender AP G/L Detail file
VN.GLDET
N_GL_DISTRIBUTION_DETAIL
Acct # by detail

Vendor remarks
VN.VNCOM
VN_VENDOR_COMMENTS

Subcontract file
VN.SUB
VN_SUBCONTRACT
Status, vendor, insurance

Subcontract remarks
VN.SUBM
VN_VENDOR_SUB_MESSAGE
Subcontract remarks

Change order header
VN.CRSCO
VN_SUB_CHANGE_ORDER_HDR
Vendor, subcontract #

Change request subcontractor cost header
VN.CRSH
VN_CHNG_REQ_SUB_HDR

Change request subcontractor cost detail
VN.CRSD
VN_CHNG_REQ_SUB_DET

A/R
Customer master file
CR.MSTR
CR_CUSTOMER_MASTER
Labels, terms, stmt cycle, tax code

Customer remarks
CR.CMCOM
CR_COMMENTS
Customer remarks

AR G/L Cash Receipts
CR.GLHIS
CR_CASH_RECEIPT_GL_HIST
Check #, customer, date

Open item file
CR.OITEM
CR_OPEN_ITEM
Finance charges

Payment history file
CR.PHIST
CR_PAY_ADJUST_HISTORY
Ck date vs. invoice date

Contract remarks
CR.CNTR
CR_CONTRACT_MASTER
Contract remarks

Executed change order heading
CR.COEH
CR_CHANGE_ORDER_HEADER

Progress billings/Draws
CR.BHM
Appl #, period to date

Change request header
CR.CRH
CR_CHNG_REQ_HDR
Customer, job, cr#

Change request revenue detail
CR.CRREV
CR_CHNG_REQ_REV

Change request contractor cost detail
CR.CRCD
CR_CHNG_REQ_CON_DET

Change order / change request cross reference
CR.COXCR
CR_CHNG_ORD_CHNG_REQ_XREF
Lists change requests on change order

C/E
Estimating subcontractor master file
CE.SUB

Phone # file
CE.SBNM

Job estimating header file
CE.JBHDR

Job estimating summary/total file
CE.JBSUM

E/C
Equipment file maintenance
EC.MSTR
EC_EQUIPMENT_MASTER
Ranking by # axles, gross weight-scale weight

Equipment remarks
PA.RMRK
PA_REMARKS
Equipment remarks

Equipment cost history file
EC.ACTCH
EC_ACTUAL_COST_HISTORY
Type, hours

Equipment revenue history file
EC.REVH
EC_REVENUE_HISTORY
Type

F/A
Fixed Assets master file
FA.MSTR
FA_ASSET_MASTER_FILE
Serial #, date purchased

Fixed Assets history file
FA.HIST
FA_HISTORY
Depreciation totals

G/L
Balance file
GL.BAL
GL_BALANCE

Detail file
GL.DET
GL_DETAIL
Type, source, JE#

I/C
Item master file
IM.MSTR
IM_ITEM_MASTER
List price per factor items

Warehouse item detail file
IM.ITEMS
IM_ITEM_WHSE
Physical inventory status, bin #, date last rec'd

Item remarks
IM.NOTES
IM_ITEM_COMMENTS
Inventory Item remarks

Item layer information
IM.QTY
IM_ITEM_QUANTITY
Inventory layers - quantities and unit costs

Item history file
IM.HIST
IM_TRANSACTION_HISTORY
Type, trans, inv. usage

Item assortment file
IM.MASST
IM_ASSORTMENT_MASTER
Specific components

J/C
Job master file
JC.JOB
JC_JOB_MASTER
Type, customer, contract amount, date

Job remarks
JC.JBRMK
JC_JOB_REMARKS
Job remarks

Job phase file
JC.PHSE
JC_PHASE_MASTER
Original vs. current budget

Job Cost history file
JC.HIST
JC_TRANSACTION_HISTORY
Source, type, summaries by EC and PR

Projected cost history file
JC.PHIST
JC_PROJ_COST_HISTORY
Date-sensitive Projection and Change Order Detail

O/P
Order header file
OE.SUM
OE_ORDER_HEADER_MC
Data, customer, terms

Order header file (Detail)
OE.DET
OE_ORDER_DETAIL_MC
Items, sales tax

Order header file (Detail)
OE.TOT
OE_ORDER_TOTALS_MC
Freight, weight

Invoice header file
IN.SUM
IN_INVOICE_HEADER
Date, customer, terms

Invoice header file (Detail)
IN.DET
IN_INVOICE_DETAIL
Items, sales tax

Invoice header file (Detail)
IN.TOT
IN_INVOICE_TOTALS
Freight, weight

Salesperson
CR.SMAN
CR_SALESMAN_MASTER
Xref by employee code

Message file
OE.MSG
OE_MESSAGE

Invoice G/L Distribution
IN.DGL
IN_TEMP_GL_DIST_REP
GL by customer, date

P/O
PO summary file
PO.HDR
PO_PURCHASE_ORDER_HEADER_MC
PO by vendor state

PO detail file (detail)
PO.DET
PO_PURCHASE_ORDER_DETAIL_MC
Items by vendor

PO history file
PO.HIST
PO_RECEIVING_HISTORY_MC
Vendor, dates, job

P/R
Employee master file
PR.EM1 & 2
PR_EMPLOYEE_MASTER_1 and _2
Hourly banks, terminated, wages code, union

Employee master file
PR.EM1 & 2
PR_EMPLOYEE_MASTER_1 and _2
Monthly totals, last pay rate change

Employee master file
PR.EM1 & 2
PR_EMPLOYEE_MASTER_1 and _2
Tax states

Employee remarks
PR.EMCOM
PR_EMPLOYEE_COMMENTS
Employee remarks

Employee earnings history
PR.EHIST
PR_CHECK_HISTORY
Gross earnings ranking, wk state, res state

Employee vol. deductions
PR.EMPVD
PR_EMPL_VOL_DEDUCT
Balance, accumulated

Check reconciliation file
PR.RCON
PR_CHECK_RECONCILIATION
Manual vs. computer

Time card history file
PR.TCHIS
PR_TIME_CARD_HISTORY
Job, employee, dates

Certified payroll file
PR.TCHIS
PR_TIME_CARD_HISTORY
Days/job

Union file
PR.UMSTR
PR_UNION_MASTER_1
Fringe by type

S/A
Sales analysis detail
SA.DET
SA_DETAIL
Sales history detail

S/C
System file
SC.SYS
SC_SYSTEM
Year installed, type, site ID

Component file
SC.COMP
SC_COMPONENT
Date installed, warranty

Contract file
SC.CNTR
SC_CONTRACT
W/O type, annual billing amount, begin date

Service Contract remarks
SC.CNNOT
SC_FILE_NOTES
Remarks

S/T
Small Tools master file
ST.MF
ST_TOOL_MASTER_MC
Tool by location

T/M
T&M billing history
TM.BILHT
TM_HISTORY_BILLING_TOTAL
Billing total file (history)

TM.BILHC
TM_HISTORY_BILL_COST_TYPE
History billing file by cost type

TM.BILHP
TM_HISTORY_BILL_PHASE
History billing file by phase

TM.BILHD
TM_BILLING_HISTORY_DETAIL
History billing file by detail

W/O
Work Order heading file
WO.HDR
WO_HEADER
Customer, tax, dept.

Work Order labor history file
WO.LDETH
WO_EMPL_HOURS_HIST_DETAIL
Employee

Work Order material history file
WO.MDETH
WO_MATERIAL_DETAIL_HIST
Items
