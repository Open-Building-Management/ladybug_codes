# hvac.py

- PL = plantloop compatible
- AL = airloop supply side compatible

class/method|PL|AL
--|--|--
create_pipe|X|
create_branch|X|X
split_mix|X|
branchlist_update|X|X
pipe_splitter|X|
pipe_mixer|X|

## tous les objets de hvac.py
- **LoopNodes** : dataclass pour formater les noms de nodes pour les objets à side
- **Branches** : dataclass pour formater les noms de branches
- **EPValues** : StrEnum de valeurs EnergyPlus
- **EPApi** : StrEnum de noms de champs EnergyPlus
- **set_nodes**
- **node_name** : à partir du nom de branche, retourne `object_name_port_node` avec port valant `ìnlet` ou `outlet`
- **set_branch_list**
- **add_plant_loop**
- **create_pipe**
- **add_baseboard** : devrait être dans un fichier spécifique
- **create_branch**
- **object_name** : à partir du nom ou de l'EPBunch de branche, extrait le nom de l'objet en enlèvant le pattern `_branch`
- **split_mix** : devrait s'appeler connector_split_mix
- **branchlist_update** 
- **pipe_splitter**
- **pipe_mixer**
- **get_branch_inlet_outlet_nodes**


# hvac24_1_0.py

2 variables globales :
- **loops**
- **equipments**

objets de hvac24_1_0.py utilisés dans generate_hvac.py
- **loops**
- **equipments**
- schedule_typelimits
- schedule_objects : crée les schedules, avec basic_compact_schedule et constant_schedule
- zone_control : crée les thermostats de zone
- water_law
- constant_set_point
- pump
- gas_boiler
- resolve_side
- adjust_nodes_branch
- operation_list_scheme : run generate_operation
- zone_list

process_serie
- node_name (X2)
- **equipments**
- resolve_side
- set_nodes
- create_branch

process_series
- Branches
- node_name (X4)
- process_serie (x3)
- branchlist_update
- pipe_splitter
- pipe_mixer
- process_parallel

process_parallel
- **loops**
- branchlist_update (X2)
- get_branch_inlet_outlet_nodes (X2)
- process_series
- split_mix

adjust_nodes_branch
- LoopNodes (X2)
- process_series

generate_operation
- resolve_side
- **equipments (X4)**
