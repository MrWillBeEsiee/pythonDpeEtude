from dash import html

class Utils:

    @staticmethod
    def make_break(numBreaks):
        br_list = [html.Br()] * numBreaks
        return br_list

    # fonction d'ajout du logo
    @staticmethod
    def add_logo():
        corp_logo = html.Img(
            src='https://www.usinenouvelle.com/mediatheque/4/3/0/000271034_image_600x315.jpg',
            style={'margin': '20px 20px 5px 5px',
                   'border': '1px dashed lightblue',
                   'display': 'inline-block'})
        return corp_logo
    @staticmethod
    def addConsommationImage():
        corp_logo = html.Img(
            src='https://www.mesdepanneurs.fr/sites/default/files/blog/etiquette-energie-GES.jpeg',
            style={'margin': '20px 20px 5px 5px',
                   'border': '1px dashed lightblue',
                   'display': 'inline-block'})
        return corp_logo

    @staticmethod
    def style_c():
        layout_style = {
            'display': 'inline-block',
            'margin': '0 auto',
            'padding': '20px',
        }
        return layout_style

