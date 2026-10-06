"""fit coeffs for energyplus heatpumps equationfit like"""
import json
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
FILE = "trane_axiom_EXW120.csv"
FILE = "trane_axiom_EXW240.csv"

# temperature in kelvin
T_REF = 283.15
# flow rate in GPM
# Q in mbtuh and P in KW but as we normalize things, there is no effet
# w : load side inlet temperature
# x : source side inlet temperature
# y : load side flow rate
# z : source side flow rate
HEADER = {
    "Q": "HC_Mbtuh",
    "P": "Power_kW", 
    "w": "EWT_load_F",
    "x": "EWT_source_F",
    "y": "Flow_load_GPM",
    "z": "Flow_source_GPM"
}

GPM_TO_M3S = 0.00006309

def kelvin(
    *,
    fahrenheit: float|npt.NDArray[np.float64]|None = None,
    celsius: float|npt.NDArray[np.float64]|None = None
) -> float|npt.NDArray[np.float64]|None:
    """conversion to celsius"""
    if celsius is not None:
        return celsius + 273.15
    if fahrenheit is not None:
        return (fahrenheit - 32) * 5 / 9  + 273.15
    return None

def kw(
    *,
    mbtuh: float|npt.NDArray[np.float64]|None
) -> float|npt.NDArray[np.float64]|None:
    """conversion to kw"""
    if mbtuh is not None:
        return mbtuh * 1000 / 3412
    return None


def fit(a, b, variable):
    """fitting"""
    # lstsq résout a @ x = b
    coefficients, residuals, rank, singular_values = np.linalg.lstsq(a, b, rcond=None)
    print(f"COEFFICIENTS : {coefficients}")
    print(f"résiduals: {residuals}")
    print(f"rank: {rank}")
    print(f"singular values: {singular_values}")
    b_pred = a @ coefficients
    r2 = 1 - np.sum((b - b_pred) ** 2) / np.sum((b - np.mean(b)) ** 2)
    print(f"r2 is {r2}")
    _, ax = plt.subplots()
    plt.suptitle(f"{variable} curve")
    ax.scatter(b, b_pred, label="Modèle")
    bmin = min(b.min(), b_pred.min())
    bmax = max(b.max(), b_pred.max())

    ax.plot(
        [bmin, bmax],
        [bmin, bmax],
        linestyle="--",
        label="Parfait"
    )
    ax.set_xlabel("Données constructeur")
    ax.set_ylabel("Prédictions")
    ax.legend()
    ax.grid()
    plt.show()
    return {
        "c": coefficients[0],
        "w": coefficients[1],
        "x": coefficients[2],
        "y": coefficients[3],
        "z": coefficients[4]
    }


def imperial_values_to_equationfit():
    """use constructor values in imperial system"""
    data = np.genfromtxt(
        FILE,
        delimiter=",",
        names=True
    )

    i = np.argmax(data[HEADER["Q"]])
    q_ref = data[HEADER["Q"]][i]
    p_ref = data[HEADER["P"]][i]
    y_ref = data[HEADER["y"]][i]
    z_ref = data[HEADER["z"]][i]

    result = {}

    print(f"""
        Q_ref is {q_ref} = {kw(mbtuh=q_ref)} kw,
        P_ref is {p_ref} kw,
        y_ref is {y_ref} = {y_ref*GPM_TO_M3S} m3/s,
        z_ref is {z_ref} = {z_ref*GPM_TO_M3S} m3/s
    """)

    result["Reference_Heating_Capacity"] = int(kw(mbtuh=q_ref) * 1000) # watt
    result["Reference_Heating_Power_Consumption"] = p_ref * 1000
    result["Reference_Load_Side_Flow_Rate"] = y_ref*GPM_TO_M3S #m3s
    result["Reference_Source_Side_Flow_Rate"] = z_ref*GPM_TO_M3S

    nb = len(data)
    print(nb)
    cwxyz = np.ones((nb, 5))

    w = kelvin(fahrenheit=data[HEADER["w"]])
    if w is None:
        raise ValueError("Conversion Kelvin impossible")
    cwxyz[:,1] =  w / T_REF
    x = kelvin(fahrenheit=data[HEADER["x"]])
    if x is None:
        raise ValueError("Conversion Kelvin impossible")
    cwxyz[:,2] = x / T_REF
    cwxyz[:,3] = data[HEADER["y"]] / y_ref
    cwxyz[:,4] = data[HEADER["z"]] / z_ref

    labels = {
        "w": f"w = load_inlet_temp/{T_REF}",
        "x": f"x = source_inlet_temp/{T_REF}",
        "y": f"y = load_flow/{y_ref}",
        "z": f"z = source_flow/{z_ref}"
    }

    for i, (variable, label) in enumerate(labels.items()):
        min_val = np.min(cwxyz[:,i+1])
        max_val = np.max(cwxyz[:,i+1])
        result[variable] = {
            "min": min_val,
            "max": max_val
        }
        print(f"{label} is between {min_val} and {max_val}")


    q_vals = data[HEADER["Q"]] / q_ref
    q_min = np.min(q_vals)
    q_max = np.max(q_vals)
    print(f"Q/{q_ref} is between {q_min} and {q_max}")


    result["capacity_curve"] = fit(cwxyz, q_vals, "capacity")
    result["capacity_curve"]["min"] = q_min
    result["capacity_curve"]["max"] = q_max

    p_vals = data[HEADER["P"]] / p_ref
    p_min = np.min(p_vals)
    p_max = np.max(p_vals)
    print(f"P/{p_ref} is between {p_min} and {p_max}")

    result["power_curve"] = fit(cwxyz, p_vals, "power")
    result["power_curve"]["min"] = p_min
    result["power_curve"]["max"] = p_max

    name = FILE.split(".", maxsplit=1)[0]
    with open(f'{name}.json', 'w', encoding="utf-8") as f:
        json.dump(result, f)


if __name__ == "__main__":
    imperial_values_to_equationfit()
