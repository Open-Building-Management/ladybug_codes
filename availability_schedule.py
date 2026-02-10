"""availability schedule
NOT USED
"""
from idfhub.idf_autocomplete.idf_helpers_short import(
    ScheduleDayInterval, ScheduleWeekDaily, ScheduleYear,
)
from idfhub.idf_autocomplete.idf_types_short import(
    ScheduleDayIntervalType, ScheduleWeekDailyType, ScheduleYearType,
)

from common import idf

#---------------------------------------------------------------------------------------------------
# # on crée un schedule d'availability, de type on/off : systems_year_availability
# mais on ne va pas s'en servir, car on va passer par un schedule compact pour les thermostat
#---------------------------------------------------------------------------------------------------
day_work = ScheduleDayIntervalType(
    Name="day_work",
    Schedule_Type_Limits_Name="on_off",
    Interpolate_to_Timestep="No",
    Time_1="07:00",
    Value_Until_Time_1=0,
    Time_2="17:00",
    Value_Until_Time_2=1,
    Time_3="24:00",
    Value_Until_Time_3=0
)
day_off = ScheduleDayIntervalType(
    Name="day_off",
    Schedule_Type_Limits_Name="on_off",
    Interpolate_to_Timestep="No",
    Time_1="24:00",
    Value_Until_Time_1=0
)
ScheduleDayInterval(idf, **day_work)
ScheduleDayInterval(idf, **day_off)

systems_week_availability = ScheduleWeekDailyType(
    Name="systems_week_availability",
    Sunday_ScheduleDay_Name="day_off",
    Monday_ScheduleDay_Name="day_work",
    Tuesday_ScheduleDay_Name="day_work",
    Wednesday_ScheduleDay_Name="day_work",
    Thursday_ScheduleDay_Name="day_work",
    Friday_ScheduleDay_Name="day_work",
    Saturday_ScheduleDay_Name="day_off",
    Holiday_ScheduleDay_Name="day_off",
    SummerDesignDay_ScheduleDay_Name="day_work",
    WinterDesignDay_ScheduleDay_Name="day_work",
    CustomDay1_ScheduleDay_Name="day_work",
    CustomDay2_ScheduleDay_Name="day_work"
)
ScheduleWeekDaily(idf, **systems_week_availability)
systems_year_availability = ScheduleYearType(
    Name="systems_year_availability",
    Schedule_Type_Limits_Name="on_off",
    ScheduleWeek_Name_1="systems_week_availability",
    Start_Day_1=1,
    Start_Month_1=1,
    End_Day_1=31,
    End_Month_1=12
)
ScheduleYear(idf, **systems_year_availability)

