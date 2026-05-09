It is quite a lot of job to find how to configure an idf object. Of course, you can use the IDFEditor and reproduce all the fields one by one, but it is fastidious...

[feed_idf_autocomplete.py](src/idfhub/feed_idf_autocomplete.py) permits to generate helpers for any version of energyplus

You only have to point to the correct path where the `Energy+.idd` file can be found

```
cf src/idfhub
py feed_idf_autocomplete.py --os_ep_path=absolute_path_to_energy_plus
```

It will generate 2 files in `src/idfhub/idf_autocomplete/vX.Y.Z` :
- `idf_helpers_short.py`
- `idf_types_short.py`

These files will serve for autocompletion in vscode.


# basic autocompletion in vscode

https://code.visualstudio.com/download

![](https://github.com/user-attachments/assets/2f84fcaf-1d63-4512-90f6-ea1fb404a3c0)

# idfhub code file structure

[src/idfhub/hvac.py](src/idfhub/hvac.py) contains topology building blocks


[src/idfhub/hvac24_1_0.py](src/idfhub/hvac24_1_0.py) contains methods to configure equipments and some complementary topology methods which could be moved in 
[src/idfhub/hvac.py](src/idfhub/hvac.py)


[src/idfhub/hvac24_1_0_secondary.py](src/idfhub/hvac24_1_0_secondary.py) contains ems class and methods.

# add a new equipment

Add a `hvac24_1_0_<equipment_name>.py` in `src/idhub` and create a method to configure your equipment. All custom configuration details can be made available through the yml conf file. When including new keys for an equipment, dont create new names, just use the original names proposed via autocompletion.

Adapt `generate_hvac.py` to use your equipment.


