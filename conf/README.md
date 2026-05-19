# structure

mandatory yaml keys :
- building_name
- name
- suffix
- os_ep_path
- zones
- loops
- equipments

loops, zones and equipments are really straightforward to configure.

To add a pump in the equipments list, include the `pump` suffix. For a variable pump, include the `variable` suffix. To add a water to water heat pump, use the `hpwtw` suffix, and so on....

## sensors and controls

sensors can be used for ems control

The following yaml : 
- activates a temperature sensor on the plant_inlet of a loop called soil_loop
- uses the sensor to control 2 pumps

The pumps run with a 30% flow when temperature@soil_loop_plant_inlet < -5

The pumps restart at 80% flow when temperature@soil_loop_plant_inlet > -2

```
sensors:
  borehole_t:
    type: "System Node Temperature"
    loop: soil_loop
    side: plant
    port: inlet

controls:
  borehole_pump_control:
    sensor: borehole_t
    pilot: [soil_pump, inside_variable_pump]
    stop_below: -5
    start_above: -2
    min_flow: 0.3
    normal_flow: 0.8
```

## loops

A loop configuration requires 3 mandatory keys:
- a setpoint name
- the list of the equipments operating on the loop
- the branches, structured as list of equipments

The `parallel` keyword permits to manage parallel branches

To add a bypass in a parallel structure, add something with a `pipe` suffix in the equipments list and drop it as the last item of the parallel structure. 

Even if you use in the name something that may let think it is a baseboard equipment. the `pipe` suffix will fully determine the type.

```
water_heating_loop:
  setpoint: water_law_set_point
  operation: [hpatw_eir, gas_boiler]
  Loop_Type: heating_mix_DBOAT
  branches:
    plant: [inside_variable_pump, hpatw_eir, gas_boiler]
    demand:
      - parallel:
        - [baseboards_RDC]
        - [baseboards_RPLUS1]
        - [baseboards_bypass_pipe]
```

If mentionned, `Loop_Type` must begin with the loop type as required by the `PlantSizing` method, so `heating` or `cooling`.

It can also include the operation method : `Load` is the default, anything else will lead for now to `OutdoorDryBulb` temperature control.

If `Loop_Type` includes `mix`, a PlantEquipmentList will be created for each equipment in the yaml operation list. This is the way to go to manage energy mix.

## setpoints

only 2 available right now : 
- a outdoor air reset with a `water_law` suffix
- a constant setpoint with a `constant` suffix

```
water_law_set_point:
  Setpoint_at_Outdoor_Low_Temperature: 70
  Outdoor_Low_Temperature: -5
  Setpoint_at_Outdoor_High_Temperature: 40
  Outdoor_High_Temperature: 15

constant_set_point:
  temp: -10
```

## equipments

### type and force_side

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

### operation_range

To define the operating range of the equipment, as required for energy mix

If you use an `HeatpumpPlantloopEirHeating` (through the `hpatw` suffix) , you need `Control_Type: Load`in the equipment conf, otherwise the mix will not be successfull and energymix will only use the most efficient equipment

