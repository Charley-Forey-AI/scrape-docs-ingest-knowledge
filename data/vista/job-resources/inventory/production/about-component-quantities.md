---
title: "About Component Quantities | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/about-component-quantities"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/about-component-quantities"
---

# About Component Quantities

When you are setting up components on a bill of materials, you
 can enter quantities in either Units or by % Weight.
The method you use depends on how you measure the components needed to produce a finished good, and affects how the On Hand quantities are relieved.
Unit Quantities
Use 'Units' for a component when the components
 needed to produce a finished good are not based on a percentage of the good’s weight (for
 example, the finished good is in a unit of measure other than a weight-related unit such as
 TON).
For example:
Finished Good: 031010 2 x 8 Concrete Form Panel 
 Unit of Measure: EA
Component Material
UM
Units

310804 (3/4” H.D.O. FORM
 PLY)
SF
16.0000

600421 (2x4 - 8 - #2 - DF-
 KD)
BF
10.6720

600434 (2x4 -12 - 31 -DF
 -KD)
BF
8.0040

929311 (1-1/2” FLT HD
 SCREWS)
EA
0.5000

CORNERBRK (CORNER BRACKET
 NAILER)
EA
4.0000

TEEBRK (TEE BRACKET
 NAILER)
EA
2.0000

If 10 units of the finished good are produced, Inventory’s On Hand quantities would be relieved as follows:
Material
Units

310804
160.0000

600421
106.7200

600434
80.0400

929311
5.0000

CORNERBRK
40.0000

TEEBRK
20.0000

% Weight Quantities
Enter a weight percentage when the amount used of a component material is based on a percentage of the finished good weight (for exmaple, TON). If using this method of entering quantities, you must set up a weight conversion for the component material in the IN Location Materials form.
Once you have entered the weight % for a component
 material, the system automatically converts it into the number of units used in production
 so that the appropriate amounts can be relieved from Inventory. Since the conversion to
 units is based on the conversion factor specified for the component material, it is
 important to make sure accurate weight conversion factors are defined for the finished good
 and each of its component materials.
For example, you have a mix design for asphalt that
 calls for a certain percentage of asphalt oil. The standard unit of measure for the asphalt
 is TON, and the standard unit of measure for the oil is GAL. The oil makes up 6% of the
 finished good’s weight. Enter .06 in the % Weight field, and the system will automatically
 calculate the number of gallons. (For this example, we will assume the conversion factor
 for GAL/TON is 250.000.)
Component Material
UM
Units
%Weight

222020  (1/4” Minus
 Crushed Aggregate)
TON
0.4400
44.00%

222025 (1/2” x 1/4”
 Aggregate)
TON
0.2000
20.00%

222027 (3/8” Screenings)
TON
0.3000
30.00%

224001 (AR 4000 Asphalt
 Oil)
GAL
15.0000
6.00%

100.00%

If 10 units (TONS) of the finished good is produced,
 Inventory’s On Hand quantities would be relieved as follows:
Material
Units

222020
4.4000

222025
2.0000

222027
3.0000

224001
150.0000

Note:Typically, the percentage of weight
 for a finished good should equal 100%. (A running total of the percentage is provided as
 components are added.) However, to provide for those products that require a “waste”
 factor, the system does allow a single component or the total of the components to be
 greater than 100%.
