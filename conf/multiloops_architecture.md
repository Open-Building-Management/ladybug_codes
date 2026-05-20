
# 3 loops & HX architecture with a single loop for all zones

HX : fluid to fluid exchanger.

HX can be used in energyplus to implement a behaviour similar to a 3 way valve.


## soil loop


```
 ---soil_pump --> borehole-->
|                            |
|                            |
 <-----------hpwtw<----------

```

## heatpump loop

```
 -----hp_pump>---->hpwtw---->
|                            |
|                            |
 <-------------HX<-----------

```

## building loop

```
 -----zone_pump----->HX----->
|                            |
|       ------RDC------      |
|------|               |----- 
        ----RPLUS1-----
```

# multiloops architecture

we may not use parallel branches to split between zones but HX exchangers
