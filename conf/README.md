# structure

mandatory yaml keys :
- building_name
- name
- suffix
- os_ep_path
- zones
- loops
- equipments
- sensors

sensors can be empty

## sensors

sensors can be used for ems control

The following yaml : 
- activates a temperature sensor on the plant_inlet of a loop called soil_loop
- uses the sensor to control 2 pumps

The pumps run with a 10% flow when temperature@soil_loop_plant_inlet < -5

The pumps restart at normal flow when temperature@soil_loop_plant_inlet > -2

The 10% reduced flow permits to stop the borehole, but to continue the simulation

With a null flow, energyplus would stop the simulation, which would not be realistic  

```
sensors:
  soil_sensor:
    active: 1
    loop: soil_loop
    side: plant
    port: inlet
    type: "System Node Temperature"
    controls: [soil_pump, inside_variable_pump]
    stop_below: -5
    start_above: -2
    min_flow: 0.1
    normal_flow: 1.0
```


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
