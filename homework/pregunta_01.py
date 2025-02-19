# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    datos_envio = pd.read_csv("files/input/shipping-data.csv")
    almacen_datos = datos_envio.copy()
    plt.figure()
    conteos_almacen = almacen_datos["Warehouse_block"].value_counts()
    conteos_almacen.plot.bar(
        title="Shipping per Warehouse",
        xlabel="Warehouse block",
        ylabel="Record count",
        color="tab:blue",
        fontsize=8
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/shipping_per_warehouse.png")

    modo_envio = datos_envio.copy()
    plt.figure()
    conteos_modo = modo_envio["Mode_of_Shipment"].value_counts()
    conteos_modo.plot.pie(
        title="Mode of shipment",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"],
    )
    plt.savefig("docs/mode_of_shipment.png")

    valoracion_clientes = datos_envio.copy()
    plt.figure()
    valoracion_clientes = (valoracion_clientes[["Mode_of_Shipment", "Customer_rating"]].groupby("Mode_of_Shipment").describe())
    valoracion_clientes.columns = valoracion_clientes.columns.droplevel()
    valoracion_clientes = valoracion_clientes[["mean", "min", "max"]] 
    plt.barh(
        y=valoracion_clientes.index.values,
        width=valoracion_clientes["max"].values - 1,
        left=valoracion_clientes["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8,
    )   

    colores_barras = [
        "tab:green" if valor >= 3.0 else "tab:orange" for valor in valoracion_clientes["mean"].values
    ]

    plt.barh(
        y=valoracion_clientes.index.values,
        width=valoracion_clientes["mean"].values - 1,
        left=valoracion_clientes["min"].values,
        height=0.5,
        color=colores_barras,
        alpha=1.0,
    )
    plt.title("Average Customer Rating")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)
    plt.savefig("docs/average_customer_rating.png")

    peso_envios = datos_envio.copy()
    plt.figure()
    peso_envios.Weight_in_gms.plot.hist(
        title="Shipping weight distribution",
        color="tab:orange",
        edgecolor="white",
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/weight_distribution.png")
