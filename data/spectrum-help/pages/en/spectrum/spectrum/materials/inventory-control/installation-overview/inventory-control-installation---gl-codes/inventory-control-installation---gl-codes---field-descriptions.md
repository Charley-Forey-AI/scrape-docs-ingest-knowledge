---
title: "Inventory Control Installation - G/L Codes - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/installation-overview/inventory-control-installation---gl-codes/inventory-control-installation---gl-codes---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/installation-overview/inventory-control-installation---gl-codes/inventory-control-installation---gl-codes---field-descriptions"
---

# Inventory Control Installation - G/L Codes - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field
Button

Sales G/L account code
Enter the default General Ledger code you want to use to post sales transactions, or double-click in this field to select from a list of valid G/L account codes.
Note: The system uses this field only when the Order Processing
 module is utilized. If Order Processing is not present in this company,
 entry in this field is irrelevant.

Cost of sales G/L account code
Enter the General Ledger account code you want to use to post cost of sales, or double-click in this field to select from a list of valid G/L account codes.
Note: The system uses this field only when Order Processing module
 is utilized. If Order Processing module is not present in this company,
 entry in this field is irrelevant.

Inventory value G/L account code
Enter the primary G/L account code you plan to title "Inventory" (or similar name) in your Spectrum chart of accounts, or double-click in this field to select from a list of valid G/L account codes. Be sure to include this G/L account number when you enter your chart of accounts. Enter your default inventory account even if you do not have the General Ledger module installed on your computer.
The system will offer this G/L account code when you add inventory G/L
 departments, but you may override this account code as needed. This G/L
 account code will also be used during an inventory transaction update if the
 designated department has been deleted from the Inventory G/L
 Department File Maintenance screen; the software will utilize
 the account code in this field only as a last resort.

Adjustments G/L account code
Enter the primary G/L account code you plan to title "Cost of Goods Sold" or "Inventory Adjustment expense" (or similar name) in your Spectrum chart of accounts, or double-click in this field to select from a list of valid General Ledger account codes. Be sure to include this G/L account number when you enter your chart of accounts. Enter your default adjustments account even if you do not have General Ledger module installed on your computer.
The G/L account specified in the inventory G/L department file for "adjustments" will be debited and the G/L account code for "inventory" will be credited when negative inventory adjustments are updated.
The system will offer this G/L account code when you add inventory G/L
 departments, but you can override this account code as needed. This G/L
 account code will also be used during an inventory transaction update if the
 designated G/L department has been deleted from the Inventory G/L
 Department File Maintenance screen; the software will utilize
 the account code in this field only as a last resort.

Credit return G/L account code
Enter the primary G/L account code you plan to title "Receipts" or "Purchase Variance" (or similar name) in your Spectrum chart of accounts, or double-click in this field to select from a list of valid G/L account codes. Be sure to include this G/L account number when you enter your chart of accounts. Enter your default receipts G/L account code even if you do not have General Ledger module installed on your computer.
The G/L account specified in the inventory G/L department file for "receipts" will be debited and the G/L account code for "inventory" will be credited when inventory receipts are updated.
 The system will offer this G/L account code when you add inventory G/L
 departments, but you may override this account code as needed. This G/L
 account code will also be used during an inventory transaction update if the
 designated department has been deleted from the Inventory G/L
 Department File Maintenance screen; the software will utilize
 the account code in this field only as a last resort.
Note: Generally, these G/L accounts will only be used if you are tracking
 receipts and returns directly through inventory; for example, by not
 using the Purchase Order module.

Receipts G/L account code
Enter the primary G/L account code you plan to title "Receipts" or "Purchase Variance" (or similar name) in your Spectrum chart of accounts, or double-click in this field to select from a list of valid G/L account codes. Be sure to include this G/L account number when you enter your chart of accounts. Enter your default receipts account even if you do not have General Ledger module installed on your computer.
The G/L account specified in the inventory G/L department file for "receipts" will be credited and the G/L account code for "inventory" will be debited when inventory receipts are updated.
The system will offer this G/L account code when you add inventory
 departments, but you may override this account code as needed. This G/L
 account code will also be used during an inventory transaction update if the
 designated department has been deleted from the Inventory G/L
 Department File Maintenance; the software will utilize the
 account code in this field only as a last resort.
Note: The G/L account entered here is the same account you have in
 Accounts Payable for inventory purchases and returns.

Job Cost markup G/L account code
Enter the primary G/L account code you plan to title "Job Markup" (or similar name) in your Spectrum chart of accounts, or double-click in this fieldto select from a list of valid G/L account codes. Be sure to include this G/L account number when you enter your chart of accounts. Enter your default markup account even if you do not have General Ledger module installed on your computer.
The G/L account specified in the Inventory G/L Department File
 Maintenance for "JC markup" will be credited and the G/L
 account code for "JC direct cost" will be debited when job requisitions are
 updated, in the amount of specified markup.
The system will offer this G/L account code when you add inventory
 departments, but you may override this account code as needed. This G/L
 account code will also be used during an inventory transaction update if the
 designated department has been deleted from the Inventory G/L
 Department File Maintenance screen; the software will utilize
 the account code in this field only as a last resort.

Job Cost direct cost G/L account code
Enter the primary G/L account code you plan to title "Direct Materials" (or similar name) in your Spectrum chart of accounts, or double-click in this field to select from a list of valid G/L account codes. Be sure to include this G/L account number when you enter your chart of accounts. Enter your default Job Cost account even if you do not have the General Ledger module installed on your computer.
The G/L account specified in the Inventory G/L Department File
 Maintenance for "JC markup" will be credited and the G/L
 account code for "JC direct cost" will be debited when job requisitions are
 updated, in the amount of specified markup.
The system will offer this G/L account code when you add inventory
 departments, but you may override this account code as needed. This G/L
 account code will also be used during an inventory transaction update if the
 designated department has been deleted from Inventory G/L
 Department File Maintenance; the software will utilize the
 account code in this field only as a last resort.

Mix usage G/L account code
Enter the primary G/L account code you plan to title Cost of Goods Sold or Inventory Usage Expense (or similar name) in the Spectrum chart of accounts, or double-click in this field to select from a list of valid G/L account codes. Be sure to include this G/L account number when you enter your chart of accounts. Enter your default mix usage account, even if you do not have the General Ledger installed on your system.
The G/L account code specified in the department file for mix usage will be debited and the G/L account code for Inventory will be credited when mix transactions are updated.
The system will offer this G/L account code when the user adds inventory G/L departments, but the user may override this account code, as needed. This G/L account code will also be used during an inventory transaction update if the designated department has been deleted from the department file; Spectrum will utilize the account code in this field only as a last resort.

Equipment cost G/L account code
Enter the primary G/L account code you plan to use for materials associated with equipment costs, or double-click in this field to select from a list of valid G/L account codes. Be sure to include this G/L account number when you enter your chart of accounts. Enter your default account, even if you do not have the General Ledger installed on your system.
The G/L account code specified in the department file for equipment cost will be debited and the G/L account code for inventory will be credited when mix transactions are updated.
The system will offer this G/L account code when the user adds inventory G/L departments, but the user may override this account code, as needed. This G/L account code will also be used during an inventory transaction update if the designated department has been deleted from the department file; Spectrum will utilize the account code in this field only as a last resort.

Transfer costs G/L account code
Enter the default G/L account code for transfer costs, or double-click in this field to select from a list of valid G/L codes.

Transfer freight variance G/L account code
Enter the default G/L account code for Materials Management transfer freight variance, or double-click in this field to select from a list of valid G/L codes.
 If charges for miscellaneous freight are recorded in Inventory Control > Inventory Receipts Entry, the department specified will increase valuation and will
 credit the corresponding G/L account. A freight charge debited to the
 Inventory value G/L account
 code and the same amount will be credited to the Transfer freight variance G/L account
 code.

Receipts freight variance G/L account code
Enter the default G/L account code for Materials Management receipts freight variance, or double-click in this field to select from a list of valid G/L codes.
If charges for miscellaneous freight are recorded in Inventory
 Control > G/L Department
 Maintenance, the department specified will increase valuation and will
 credit the corresponding G/L account. If a freight charge is debited to the
 Inventory value G/L account code, the same amount will be credited to the
 Transfer freight variance G/L account code.

Inter-company G/L account code
Enter the G/L account code you plan to title "inter-company receivable" (or
 similar name) in your Spectrum chart of accounts. This G/L account code may
 not be the same code designated elsewhere in the Inventory Control
 Installation. Be sure to include this G/L account number when
 you enter your chart of accounts. The system will automatically update
 inter-company transactions to this G/L account code when you run the
 Inventory Transaction Report. This G/L account code is the default account,
 unless another account code is specified in the Inter-company G/L Code
 portion of this screen.
Note: This field will be skipped if the Multi-company payroll
 checkbox is not selected.

Inter-company G/L Code
Enter the Company and G/L inter-company account codes to track inter-company relationships with multiple account numbers. Entry in this section is optional, and any companies listed may override the default G/L account code in the Inter-company G/L account code field.
