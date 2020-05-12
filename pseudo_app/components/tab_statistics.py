import dash_bootstrap_components as dbc
import dash_html_components as html

from components.data_ETL import request_stats_api
from components.tab_upload import PSEUDO_REST_API_URL

TITLES_KEYS = {
    # row 1 (2 cols)
    "Documents pseudonymisés": "nb_analyzed_documents",
    "Phrases pseudonymisées": "nb_analyzed_sentences",
    # row 2 (2 cols)
    "Temps moyen de traitement par document [ms]": "avg_time_per_doc",
    "Temps moyen de traitement par phrase [ms]": "avg_time_per_sentence",
    # row 3 (3 cols)
    "Prénoms detectés": "PER_PRENOM", "Noms detectés": "PER_NOM", "Adresses detectées": "LOC",
    # row 4 (3 cols)
    "Requêtes conll": "output_type_conll", "Requêtes pseudonymized": "output_type_pesudonymized",
    "Requêtes tagged": "output_type_tagged"
}

tab_statistics_content = dbc.Tab(
    label='API Stats',
    tab_id="tab-statistics",
    children=dbc.Container(className='page', children="hola")
)


def pane_statistics_content(data):
    if "stats_content" in data and data["stats_content"]:
        return data["stats_content"], data

    stats_info = request_stats_api(pseudo_api_url=PSEUDO_REST_API_URL + "/api_stats")

    list_cards = []
    for title, key in TITLES_KEYS.items():
        if key not in stats_info:
            value = "N/A"
        else:
            value = f"{int(stats_info[key])}"
        temp_card = [
            dbc.CardBody(
                [
                    html.H5(title, className="card-title", style={"text-align": "center"}),
                    html.P(value, className="card-text", style={"text-align": "center", "font-size": "40px",
                                                                "font-weight": "bold"}),
                ]
            ),
        ]
        list_cards.append(temp_card)

    row_1 = dbc.Row(
        [
            dbc.Col(dbc.Card(list_cards[0], color="primary", outline=True)),
            dbc.Col(dbc.Card(list_cards[1], color="secondary", outline=True)),
        ],
        className="mb-4",
    )

    row_2 = dbc.Row(
        [
            dbc.Col(dbc.Card(list_cards[2], color="success", outline=True)),
            dbc.Col(dbc.Card(list_cards[3], color="dark", outline=True)),
        ],
        className="mb-4",
    )

    row_3 = dbc.Row(
        [
            dbc.Col(dbc.Card(list_cards[4], color="success", outline=True)),
            dbc.Col(dbc.Card(list_cards[5], color="warning", outline=True)),
            dbc.Col(dbc.Card(list_cards[6], color="primary", outline=True)),
        ],
        className="mb-4",
    )

    row_4 = dbc.Row(
        [
            dbc.Col(dbc.Card(list_cards[7], color="danger", outline=True)),
            dbc.Col(dbc.Card(list_cards[8], color="info", outline=True)),
            dbc.Col(dbc.Card(list_cards[9], color="dark", outline=True)),
        ]
    )
    children = html.Div([row_1, row_2, row_3, row_4], style={"margin-top": "1cm"})
    data["stats_content"] = children
    return children, data
