import pandas as pd
import random

def finn_ledig_barnehage(ønsket_barnehage=None):
    # Les Excel-filen for tilgjengelige plasser
    kgdata = pd.ExcelFile('kgdata.xlsx')
    barnehage_df = pd.read_excel(kgdata, 'barnehage')  # Tilpass til riktig ark

    # Filtrer etter ønsket barnehage om angitt
    if ønsket_barnehage:
        valgt_barnehage = barnehage_df[(barnehage_df['barnehage_navn'] == ønsket_barnehage) & (barnehage_df['barnehage_ledige_plasser'] > 0)]
        if not valgt_barnehage.empty:
            return ønsket_barnehage

    # Velg en tilfeldig barnehage med ledig kapasitet hvis ingen spesifikk barnehage er valgt
    ledige_barnehager = barnehage_df[barnehage_df['barnehage_ledige_plasser'] > 0]['barnehage_navn'].tolist()
    if ledige_barnehager:
        return random.choice(ledige_barnehager)

    return "Ingen ledige plasser tilgjengelig"
