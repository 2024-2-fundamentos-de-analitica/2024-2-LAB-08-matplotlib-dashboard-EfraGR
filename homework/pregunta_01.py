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
    data_file = pd.read_csv('files/input/shipping-data.csv')
    data_copy_A = data_file.copy()
    warehouse_distribution = data_copy_A['Warehouse_block'].value_counts()
    warehouse_distribution.plot.bar(
        title="Shipments per Warehouse",
        xlabel="Warehouse Block",
        ylabel="Number of Shipments",
        color="tab:blue",
        fontsize=8
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig('output/shipments_per_warehouse.png')
    data_copy_B = data_file.copy()
    plt.figure()
    shipment_distribution = data_copy_B['Mode_of_Shipment'].value_counts()
    shipment_distribution.plot.pie(
        title="Shipment Modes",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"],
    )
    plt.savefig('output/shipment_modes.png')
    data_copy_C = data_file.copy()
    plt.figure()
    rating_summary = (
        data_copy_C[["Mode_of_Shipment", "Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )
    rating_summary.columns = rating_summary.columns.droplevel()
    rating_summary = rating_summary[["mean", "min", "max"]]
    plt.barh(
        y=rating_summary.index.values,
        width=rating_summary["max"].values - 1,
        left=rating_summary["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8,
    )

    color_scheme = ["tab:green" if val >= 3.0 else "tab:orange" for val in rating_summary["mean"].values]
    plt.barh(
        y=rating_summary.index.values,
        width=rating_summary["mean"].values - 1,
        left=rating_summary["min"].values,
        color=color_scheme,
        height=0.5,
        alpha=1.0,
    )
    plt.title("Average Customer Rating")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)
    plt.savefig("output/average_customer_rating.png")
    data_copy_D = data_file.copy()
    plt.figure()
    data_copy_D.Weight_in_gms.plot.hist(
        title="Distribution of Shipped Weights",
        color="tab:orange",
        edgecolor="white",
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("output/weight_distribution.png")
    dashboard_html = """
    <!DOCTYPE html>
    <html lang="en">
    <body>
        <h1>Shipping Dashboard</h1>
        <div style="width: 45%; float: left">
            <img src="shipments_per_warehouse.png" alt="Warehouse Shipments" />
            <img src="shipment_modes.png" alt="Shipment Modes" />
        </div>
        <div style="width: 45%; float: left">
            <img src="average_customer_rating.png" alt="Customer Ratings" />
            <img src="weight_distribution.png" alt="Weight Distribution" />
        </div>
    </body>
    </html>
    """
    html_path = "output/index.html"
    with open(html_path, "w") as file:
        file.write(dashboard_html)
