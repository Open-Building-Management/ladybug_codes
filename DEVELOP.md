It is quite a lot of job to find how to configure an idf object

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
