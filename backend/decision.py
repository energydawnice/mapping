import pandas as pd

GENSET_MIN = 44   # kW mínimo operación
PV_CAPACITY = 65  # kWp
SOC_MIN = 20      # %
SOC_MAX = 90      # %

def decision_engine(df):
    last = df.iloc[-1]
    soc = last["SOC"]
    load = last["Load"]
    pv   = last["PV"]
    recs = []

    if soc < SOC_MIN:
        recs.append("🔴 SOC bajo → cargar batería (forzar carga con genset/PV).")
    elif soc > SOC_MAX:
        recs.append("🟢 SOC alto → limitar carga, priorizar consumo directo.")

    if pv > 0 and load < GENSET_MIN:
        recs.append("⚠️ Load bajo → posible curtail de FV para respetar mínimo del genset.")

    if load > GENSET_MIN and soc < 50:
        recs.append("✅ Mantener genset ON para sostener la carga.")

    if not recs:
        recs.append("🔵 Condiciones normales, sin acción inmediata.")

    return {"Time": str(last["Time"]), "SOC": float(soc), "Load": float(load), "PV": float(pv), "Recs": recs}
