# structure

## equipments

In the energyplus initial API, inlet and outlet are usually fixed through `Inlet_Node_Name` and `Outlet_Node_Name`

But some equipments may have two sides : Source and Load, such as heatpumps.

Tanks may use : 
- `Use_Side_Inlet_Node_Name`
- `Use_Side_Outet_Node_Name`
- `Source_Side_Inlet_Node_Name`
- `Source_Side_Outet_Node_Name`

To fix the side, define `type` or `force_side`

For heatpumps, `type: heatpump` will lead to :
- `Source_Side_Outlet_Node_Name` if side is `Demand` or `Return`
- `Load_Side_Outlet_Node_Name` if side is `Plant` or `Supply`

`force_side: Boiler_Water` will override things and lead to `Boiler_Water_Outlet_Node_Name` which is the field to use for a `BoilerHotWater`
