---
title: "Planning Considerations | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/writing-to-spectrum-tables/planning-considerations"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/writing-to-spectrum-tables/planning-considerations"
---

# Planning Considerations

Before an Info-Link data transfer is performed, it is essential that the layout for the Spectrum database table be taken into consideration.
Primary considerations include but aren't limited to:

- Determine what information will be transferred to the key column(s) of the table. Key information must be unique for each record, and may be left or right justified.

- Consider which columns in the table must require an entry be typed directly into Spectrum using regular table maintenance screens.

- Certain columns require validation when entered within Spectrum (such as valid G/L code) and this must be done very carefully if recorded via Info-Link.

- Column width

- Field type (alpha or numeric)

Using VN.MSTR as an example, here's an example of some of the considerations to be evaluated prior to data transfer of vendor table information.

- The key of VN.MSTR is VN.CODE.

- It is right-filled blank and is a maximum of 10 characters.

- Each code must of course be unique.

- By adding a sample vendor in Vendor File Maintenance, you can make note of the fields which require entry.

- It is then necessary to establish standards for entry into these fields, on a variable-by-variable basis.

## Required field entries in AP Vendor Maintenance

To learn which fields of a given screen are required, create an entry in that screen. Taking this action in the AP Vendor Maintenance form reveals these fields are required.Variable NameDescription
VN.CODEVendor code.
VN.NAMEVendor name.
VN.ALPHAAlpha reference (first six characters of the vendor name).
VN.10991099. N is the default, but you can set it to Y. If you do set this to Y, you will need to enter the social security number and federal ID number.
VN.PTERMSPayment terms CD. The system defaults to 10, but you can change it.
VN.PDAYSDays. the system defaults to 10, but you can change it.
VN.DPER%. There is no system default.
VN.HOLDDefault payment hold in the system defaults to N, but you can set it to Y.

Other columns in the vendor table may be left blank, but if entry is made, it must be carefully reviewed for compatibility with input in other tables.
For example, entry into VN.G/LCODE needs to be a code that has already been added to the Chart of Accounts in Spectrum. Each column within the table should be considered individually to determine appropriate data, if any, to be transferred into Spectrum.
To facilitate this process, it may be helpful to print the Table Directory Listing, with column detail, for the specific table. As an example, the column detail for VN.MSTR is shown here.
Data TypeVariable NameDescriptionMax LengthTable Size
KVN.CODEVendor code10
AVN.NAMEVendor name30
AVN.ALPHAVendor alpha cross reference6
AVN.TYPEVendor type cross reference6
AVN.ADDR1Vendor address 125
AVN.ADDR2Vendor address 225
AVN.ADDR3Vendor address 320
AVN.STATEVendor state2
AVN.ZIPVendor zip code10
AVN.PHONEVendor phone10
AVN.CONVendor contact name20
AVN.AREFOur account number with vendor10
AVN.1099Y or N to send 1099 at end of year1
AVN.SSVendor social security number9
NVN.LINVDate of last invoice entered for this vendor6
NVN.LPYMTDate last payment was made to this vendor6
AVN.PTERMSVendor payment terms due; (A) from invoice date, or (B) from 1st next month1
NVN.PDAYSNumber of days payment is due; from invoice date or 1st of next month3
AVN.DTERMSDisc eligible date is from (A) inv. date, or (B) 1st of next month1
NVN.DDAYSNumber of days from invoice, or 1st of next month for disc eligible3
NVN.DPERDiscount percentage amount6
AVN.G/LCODEDefault G/L account code for expense distribution of invoice12
AVN.HOLDDefault "hold pymt" indicator for entry of invoices1
NVN.BALVendor current balance13
NVN.INVTotal invoices entered for this vendor; 1-MTD or 2-YTD122
NVN.PYMTTotal payments made to this vendor; 1-MTD or 2-YTD122
NVN.DISCTotal discounts taken for this vendor; 1-MTD or 2-YTD122
AVN.NEGFNegative check flag: Y - Check will be 0 or negative, or N - Check will be positive1
AVN.FED#Federal ID number for 1099's12
NVN.RBILLTotal retention billed amount; 1 - MTD 2 - YTD132
NVN.RPYMTTotal retention paid amount; 1 - MTD or 2 - YTD132
NVN.RDISCTotal retention discount taken; 1 - MTD or 2 - YTD122
NVN.RBALTotal retention balance13
AVN.FAXThe vendor fax number10
AVN.INSUREnter "Y" if the vendor has an insurance certificate, otherwise enter "N"1
NVN.INSEXEnter the expiration date8
AVN.1099INDEnter 1099 payment indicator: 1-7, press F4 for descriptions1
AVN.DBETYPEEnter the disadvantaged business enterprise type10
AVN.DISADVEnter "Y" if this is a disadvantaged business enterprise, otherwise, enter "N" or leave blank1
AVN.ALT1099Enter the alternate vendor name30
