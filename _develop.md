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
pipe_mixer|X|X

## tous les objets de hvac.py
- **LoopNodes** : formate node names pour objets à side
- **Branches** : formate les noms de branches (no underscore?), utilisé seulement dans add_plant_loop (et dans add_airloop)
- **EPValues** : StrEnum de valeurs EnergyPlus
- **EPApi** : StrEnum de noms de champs EnergyPlus
- **set_nodes**
- **node_name** : object_name_inlet/outlet_node
- **set_branch_list** : utilisé seulement dans add_plant_loop (et dans add_airloop)
- **add_plant_loop**
- **create_pipe**
- **add_baseboard** : devrait être dans un fichier spécifique
- **create_branch**
- **object_name** : enlève le pattern _branch ds branch_name
- **split_mix** : devrait s'appeler connector_split_mix
- **branchlist_update** 
- **pipe_splitter**
- **pipe_mixer**
- **bypass_branch** : A SUPPRIMER - pas utilisé
- **get_branch_inlet_outlet_nodes**


# hvac24_1_0.py

- L = loops
- E = equipments
- BLU = branchlist_update

class/method|main|L|E|BLU
--|--|--|--|--
loops|X|||
equipments|X|||
schedule_typelimits|X|||
schedule_objects|X|||
zone_control|X|||
water_law|X|||
constant_set_point|X|||
pump|X|||
gas_boiler|X|||
resolve_side|X|||
process_serie|||X|X1
process_parallel||X||X2
adjust_nodes_branch|X|||
generate_operation|X||X||
operation_list_scheme|X|||
zone_list|X|||


## tous les objets de hvac24_1_0.py
- **loops** : VARIABLE GLOBALE
- **equipments** : VARIABLE GLOBALE
- **schedule_typelimits**
- **basic_compact_schedule**
- **constant_schedule**
- **schedule_objects** : crée les schedules, avec basic_compact_schedule et constant_schedule
- **summer**
- **two_season_schedule**
- **zone_control** : crée les thermostats de zone
- **water_law**
- **constant_set_point**
- **pump**
- **gas_boiler**
- **resolve_side**
- **process_serie** : Si pas fourni, produit des noms de branches génériques avec _branch
- **process_series** : run process_serie and process_parallel
- **process_parallel**
- **adjust_nodes_branch** : run process_series
- **generate_operation**
- **operation_list_scheme**
- **zone_list**

