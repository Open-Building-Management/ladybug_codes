# structure

mandatory yaml keys :
- building_name
- name
- suffix
- os_ep_path
- zones
- loops
- equipments

zones are really straightforward to configure.

Some reserved keys are to be used for loops and equipments declaration.

reserved keys|loop type
--|--
`*soil*` | plant loop with glycol 30%
`*water_heating*` | plant loop with water


reserved keys|equipments
--|--
`*pump*` or `*pump_variable*` | constant or variable pumps
`*pipe*` | pipe connectors
`*boiler*` | gaz boiler
`*hp*` | heatpump
`*HX*` | fluid to fluid exchanger
`*borehole*` | field of vertical geothermal probes (far-field ground model : Kusudaachenbach)
`*baseboards*` | baseboards radiant and convective heaters

Never use `heatpump` or `heat_pump` for a heatpump key or it will be seen as a pump :-)

To add a pump in the equipments list, include the `pump` suffix. For a variable pump, include the `variable` suffix. To add a water to water heatpump, use the `hpwtw` suffix, for an air to water heatpump, use the `hpatw` suffix, and so on....

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
    type: Pump_Flow_Rate_Schedule_Name
    pilot: [soil_pump, inside_variable_pump]
    stop_below: -5
    start_above: -2
    min: 0.3
    max: 0.8
```

## loops configuration

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
  Loop_Type: heating_mix
  branches:
    plant: [inside_variable_pump, hpatw_eir, gas_boiler]
    demand:
      - parallel:
        - [baseboards_RDC]
        - [baseboards_RPLUS1]
        - [baseboards_bypass_pipe]
```

If mentionned, `Loop_Type` must begin with the loop type as required by the `PlantSizing` method, so `heating` or `cooling`.

If `Loop_Type` includes `mix`, a PlantEquipmentList will be created for each equipment in the yaml operation list, and you will have the possibility to define an `operation_range` for each equipment of the loop

You can use `setpoints` instead or in addition to `setpoint` to add a setpoint at the output/outlet of each equipment of the loop

```
setpoints: [water_law_set_point_5535, water_law_set_point_7040]
```
You may add a `staging_mode` key, not sure this term is correct

With no `staging_mode` defined, the default value will be `Load` and will lead to `PlantEquipmentOperation:HeatingLoad` or `PlantEquipmentOperation:CoolingLoad`

Other operation modes are available :
- `OutdoorDryBulb`
- `ComponentSetpoint`

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

