import base64

import dash_core_components as dcc
import dash_html_components as html


def app_page_layout(page_layout, app_title="Etalab Pseudo", light_logo=False):
    return html.Div(
        id='main_page',
        children=[
            dcc.Location(id='url', refresh=False),
            html.Div(
                id='app-page-header',
                children=[
                    html.A(
                        id='dashbio-logo', children=[
                            html.Img(
                                src="./assets/MarianneLogo-3-90x57.png"

                            )],
                        href="https://www.etalab.gouv.fr/"
                    ),
                    html.H2([app_title, html.Sup("β")]),

                    html.A(
                        id='gh-link',
                        children=[
                            'Voir sur Github'
                        ],
                        href="https://github.com/etalab-ia",
                        style={'color': 'white' if light_logo else 'black',
                               'border': 'solid 1px white' if light_logo else 'solid 1px black'}
                    ),

                    html.Img(
                        src='data:image/png;base64,{}'.format(
                            base64.b64encode(
                                open(
                                    './assets/GitHub-Mark-{}64px.png'.format(
                                        'Light-' if light_logo else ''
                                    ),
                                    'rb'
                                ).read()
                            ).decode()
                        )
                    )
                ],
            ),
            html.Div(
                id='app-page-content',
                children=page_layout
            )
        ],
    )