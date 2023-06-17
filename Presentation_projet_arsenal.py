import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(layout="wide", initial_sidebar_state = "expanded" )
image = Image.open("Arsenal-logo.png")
image2 = Image.open("xhaka.png")
image3 = Image.open("mustafi.png")
image4 = Image.open("arteta.png")
image5 = Image.open("emery.png")
image6 = Image.open("pépé.png")
image7 = Image.open("saliba.png")
image8 = Image.open("wenger.png")
image9 = Image.open("leno.png")
image10 = Image.open("sokratis.png")
image11 = Image.open("torreira.png")
image12 = Image.open("sanchez.png")
image13 = Image.open("aubameyang.png")
image14 = Image.open("lacazette.png")



pages = ["Introduction", "Les facteurs globaux de déclin", "Saison 2016-2017", "Saison 2017-2018","Saison 2018-2019", "Saison 2019-2020", "Conclusion"]
st.sidebar.image(image)
menu = st.sidebar.radio(" ", (pages))
st.sidebar.header("Projet Arsenal DA FEV 2023 - Bootcamp")
st.sidebar.subheader("Team members")
st.sidebar.markdown("***Axel Haumont***")
st.sidebar.markdown("***Johann Touati***")
st.sidebar.markdown("***Sullivan Porchy***")

df_classement1020 = pd.read_csv("Classement1020.csv")
df_premiere_partie = df_classement1020[df_classement1020["Moment saison"]== "1ère partie saison"]
df_seconde_partie = df_classement1020[df_classement1020["Moment saison"]== "2ème partie saison"]
df_classement_fin_saison1020_top6 = pd.read_csv("Classement Top 6 1020.csv")
equipes_list = df_classement_fin_saison1020_top6["Nom équipe"].unique()
equipes_list2 = df_premiere_partie["Nom équipe"].unique().tolist()



if menu == pages[0]:
    st.title("Le constat du déclin")
    st.subheader("Des résultats en berne à partir de 2016")
  

    teamlist = df_classement_fin_saison1020_top6["Nom équipe"].unique().tolist()
    teamlist2 = df_classement_fin_saison1020_top6["Nom équipe"].unique().tolist()

    equipes = st.multiselect("Selectionnez les équipes", teamlist, default=["FC Arsenal"])
    st.text("Vous avez choisi: {}".format(", ".join(equipes)))
    

    dfs = {equipe: df_classement_fin_saison1020_top6[df_classement_fin_saison1020_top6["Nom équipe"] == equipe] for equipe in equipes}


    st.header("Classement des équipes sélectionnées")
    fig3 = go.Figure()
    for equipe, df_classement_fin_saison1020_top6 in dfs.items():
        fig3 = fig3.add_trace(go.Scatter(x=df_classement_fin_saison1020_top6["Saison"], y=df_classement_fin_saison1020_top6["Classement"], name=equipe  ))
    fig3.update_traces(marker=dict(color="red"), selector = ({'name':'FC Arsenal'}))
    fig3.update_traces(marker=dict(color="white"), selector = ({'name':'Tottenham'}))
    fig3.update_traces(marker=dict(color="#13BACB"), selector = ({'name':'Manchester City'}))
    fig3.update_traces(marker=dict(color="#5685EC"), selector = ({'name':'Chelsea'}))
    fig3.update_traces(marker=dict(color="#24B928"), selector = ({'name':'Liverpool'}))
    fig3.update_traces(marker=dict(color="#D22DC9"), selector = ({'name':'Manchester Utd.'}))
    fig3.update_layout(yaxis_range=[10,1])
    fig3.update_yaxes(nticks=10)
    fig3.update_layout(xaxis_title="Saison", yaxis_title="Classement")
    st.plotly_chart(fig3)
    st.text("Nous identifions deux périodes distinctes:\n"
            "* 2010-2016 - Arsenal ne sort pas du top 4\n"
            "* 2016-2020 - Arsenal est au mieux 5ème")

    st.header("Points par saison des équipes sélectionnées")
    fig = go.Figure()
    for equipe, df_classement_fin_saison1020_top6 in dfs.items():
        fig = fig.add_trace(go.Bar(x=df_classement_fin_saison1020_top6["Saison"], y=df_classement_fin_saison1020_top6["Points"], name=equipe))  
    fig.update_traces(marker=dict(color="red"), selector = ({'name':'FC Arsenal'}))
    fig.update_traces(marker=dict(color="white"), selector = ({'name':'Tottenham'}))
    fig.update_traces(marker=dict(color="#13BACB"), selector = ({'name':'Manchester City'}))
    fig.update_traces(marker=dict(color="#5685EC"), selector = ({'name':'Chelsea'}))
    fig.update_traces(marker=dict(color="#24B928"), selector = ({'name':'Liverpool'}))
    fig.update_traces(marker=dict(color="#D22DC9"   ), selector = ({'name':'Manchester Utd.'}))
    fig.update_layout(xaxis_title="Saison", yaxis_title="Points")
    st.plotly_chart(fig)
    st.text("Au niveau des points nous voyons les données suivantes:\n"
            "* 2012-2017 Arsenal marque plus de 70 pts \n"
            "* 2017-2020 Arsenal est en dessous de cette marque")
    
    st.header("Nombre de buts Arsenal 2010-2021")
    df_buts = pd.read_csv("nombre_de_buts.csv")
    df_buts["Saison2"] = ["10/11", "11/12", "12/13", "13/14", "14/15", "15/16", "16/17", "17/18", "18/19", "19/20", "20/21"]
                                                
    
    fig24 = px.line(df_buts, x = 'Saison2', y = 'Chiffre Max', labels={
                     "Chiffre Max": "Nombre de buts",
                     "Saison2" : "Saison"})
    fig24.update_layout(yaxis_range=[50, 80])
    fig24.update_yaxes(nticks=5)
    fig24.update_traces(line_color='red')
    st.plotly_chart(fig24)

if menu == pages[1]:
    df_classement_Arsenal = pd.read_csv("Classement Arsenal.csv")
    df_classement_champion = pd.read_csv("Classement champion.csv")
    df_classement_podium = pd.read_csv("Classement podium.csv")
    df_difference_buts_domicile = pd.read_csv("Difference de buts domicile.csv")
    df_difference_buts_domicile = df_difference_buts_domicile.head(10)
    df_difference_buts_exterieur = pd.read_csv("Difference de buts extérieur.csv")
    df_difference_buts_exterieur = df_difference_buts_exterieur.head(10)
    st.header("Facteurs principaux du déclin d'Arsenal 2016-2020")

    st.header("Des prestations catastrophiques à l'extérieur")
    st.subheader("Différence de buts Arsenal par saison domicile vs extérieur")
    fig8 = make_subplots(rows=1, cols=2, shared_yaxes = True)
    fig8.add_trace(go.Bar(x=df_difference_buts_domicile["season"], y=df_difference_buts_domicile["sg_match_ft"], name = "Domicile"), row=1, col=1)
    fig8['layout']['xaxis'].update(title_text='Saison')
    fig8.add_trace(go.Bar(x=df_difference_buts_exterieur["season"], y=df_difference_buts_exterieur["sg_match_ft_away"], name = "Extérieur"), row=1, col=2)
    fig8['layout']['xaxis2'].update(title_text='Saison')
    fig8.update_traces(marker=dict(color="red"), selector = ({'name':'Domicile'}))
    fig8.update_traces(marker=dict(color="yellow"), selector = ({'name':'Extérieur'}))
    fig8.update_layout(yaxis_range=[-15,35])
    fig8.update_yaxes(nticks=10)
    fig8.update_layout(yaxis_title="Différence de buts")
    st.plotly_chart(fig8)

    st.header("Une concurrence de plus en plus forte sportivement et économiquement")
    st.subheader("L'écart sportif qui s'accroît")
    fig7 = go.Figure()
    fig7.add_trace(go.Line(x=df_classement_Arsenal["Saison"], y=df_classement_Arsenal["Points"], name = "Arsenal", line_color="red"))
    fig7.add_trace(go.Line(x=df_classement_champion["Saison"], y=df_classement_champion["Points"], name = "Champion", line_color = "yellow"))
    fig7.add_trace(go.Line(x=df_classement_podium["Saison"], y=df_classement_podium["Points"], name = "Podium", line_color = 'orange'))
    fig7.update_layout(xaxis_title="Saison", yaxis_title="Points")
    st.plotly_chart(fig7)

    st.subheader("Un écart d'investissement financier énorme sur la période 2010-2021")

    df_investissements_financiers = pd.read_csv("transfert10-11to20-21.csv")
    df_investissements_financiers = df_investissements_financiers.head(10)
    fig22 = px.bar(df_investissements_financiers, x = 'Club(s)', y = 'Depenses', 
             color = 'Club(s)',
             color_discrete_map = {'FC Arsenal' : 'red',
                                   'FC Liverpool' : '#24B928',
                                   'Manchester United' : '#D22DC9',
                                    'Tottenham Hotspur' : 'white', 
                                     'Manchester City' : '#13BACB', 
                                     'Chelsea FC' : '#5685EC'})
    fig22.update_layout(showlegend=False)
    fig22.update_layout(xaxis_title="Equipe", yaxis_title="Dépenses en M€")
    st.plotly_chart(fig22)

    st.header("Une prise de valeur de l'effectif limitée")
    st.subheader("Valeur de l'effectif par saison pour les équipes sélectionnées selon Transfermarkt")
    df_valeur_equipe = pd.read_csv("Valeur équipe.csv")
    teamlist11 = df_valeur_equipe["Equipe"].unique().tolist()
    equipes11 = st.multiselect("Selectionnez les équipes", teamlist11, default = "FC Arsenal ")
    st.text("Vous avez choisi: {}".format(", ".join(equipes11)))
    dfs11 = {equipe: df_valeur_equipe[df_valeur_equipe["Equipe"] == equipe] for equipe in equipes11}
    
    fig9 = go.Figure()
    for equipe, df_valeur_equipe in dfs11.items():
        fig9 = fig9.add_trace(go.Scatter(x=df_valeur_equipe["Saison"], y=df_valeur_equipe["Valeur_totale_equipe_en_m€"], name=equipe))
    fig9.update_traces(marker=dict(color="red"), selector = ({'name':'FC Arsenal '}))
    fig9.update_traces(marker=dict(color="white"), selector = ({'name':'Tottenham Hotspur '}))
    fig9.update_traces(marker=dict(color="#13BACB"), selector = ({'name':'Manchester City '}))
    fig9.update_traces(marker=dict(color="#5685EC"), selector = ({'name':'Chelsea FC '}))
    fig9.update_traces(marker=dict(color="#24B928"), selector = ({'name':'FC Liverpool '}))
    fig9.update_traces(marker=dict(color="#D22DC9"), selector = ({'name':'Manchester United '}))
    fig9.update_layout(xaxis_title="Saison", yaxis_title="Valeur en m€")
    st.plotly_chart(fig9)

    df_matchs_manques = pd.read_csv("matchs_manques_par_equipe.csv")
    st.header("La poisse d'Arsenal, une réalité")
    st.subheader("Nombre de matches manqués par équipe sur la période 2010/2021")
    fig10 = px.bar(df_matchs_manques, x = 'Equipe', y = 'Matchs manqués',
             color = 'Equipe',
             color_discrete_map = {'Arsenal' : 'red',
                                   'Liverpool' : '#24B928',
                                   'Manchester United' : '#D22DC9',
                                    'Tottenham' : 'white', 
                                     'Manchester City' : '#13BACB', 
                                     'Chelsea' : '#5685EC'})
    fig10.update_layout(showlegend=False)
    st.plotly_chart(fig10)


if menu == pages[2]:
    st.title("2016-2017 : Le changement de stratégie et les premiers signes annonciateurs")
    st.subheader("Arsenal - 5ème - 75 pts")
    
    df_blessures_saison = pd.read_csv("blessures_equipe_saison.csv")
    df_blessures_saison1516 = df_blessures_saison[df_blessures_saison["Saison"] == "15/16"]

    st.header("Une saison gâchée par les blessures")
    
    fig11 = px.bar(df_blessures_saison1516, x = 'Equipe', y = 'Matchs manqués',
             color = 'Equipe',
             color_discrete_map = {'Arsenal' : 'red',
                                   'Liverpool' : '#24B928',
                                   'United' : '#D22DC9',
                                    'Tottenham' : 'white', 
                                     'City' : '#13BACB', 
                                     'Chelsea' : '#5685EC'})
    fig11.update_layout(showlegend=False)
    st.plotly_chart(fig11)

    df_blesses_1617 = pd.read_csv("arsenal_16_17_blessures.csv")
    df_blesses_1617 = df_blesses_1617.drop('Unnamed: 0', axis = 1)
    with st.expander("Voir les principaux blessés de la saison 2016-2017", expanded = False):
        st.write(df_blesses_1617.head(10))

    st.header("Un changement de stratégie notable")
    st.subheader("Une augmentation des investissements financiers")
    df_investissements_financiers2 = pd.read_csv("transfert16.17to20-21.csv")
    df_investissements_financiers2 = df_investissements_financiers2.head(10)
    df_investissements_financiers2["Depenses"] = df_investissements_financiers2["Depenses"].apply(lambda x : x[:-7]).apply(lambda x: x.replace(',','.')).astype(float)
    fig23 = px.bar(df_investissements_financiers2, x = 'Club(s)', y = 'Depenses',
             color = 'Club(s)',
             color_discrete_map = {'FC Arsenal' : 'red',
                                   'FC Liverpool' : '#24B928',
                                   'Manchester United' : '#D22DC9',
                                    'Tottenham Hotspur' : 'white', 
                                     'Manchester City' : '#13BACB', 
                                     'Chelsea FC' : '#5685EC'})
    fig23.update_layout(showlegend=False)
    fig23.update_layout(xaxis_title="Equipe", yaxis_title="Dépenses en M€")
    st.plotly_chart(fig23)

    st.text("De 2010 à 2016, Arsenal dépense un peu plus de 300m€ sur le marché des transferts, tandis que de 2016 à 2021, le club investit quasiment 600m€.")

    st.subheader("Arsenal à contre-courant du changement de stratégie en Premier League")

    df_moyenne_age = pd.read_csv("moyenne_age_2.csv")        
    df_moyenne_age["Saison2"] = ["10/11", "11/12", "12/13", "13/14", "14/15", "15/16", "16/17", "17/18", "18/19", "19/20", "20/21", 
                                 "10/11", "11/12", "12/13", "13/14", "14/15", "15/16", "16/17", "17/18", "18/19", "19/20", "20/21",
                                 "10/11", "11/12", "12/13", "13/14", "14/15", "15/16", "16/17", "17/18", "18/19", "19/20", "20/21",
                                 "10/11", "11/12", "12/13", "13/14", "14/15", "15/16", "16/17", "17/18", "18/19", "19/20", "20/21",
                                 "10/11", "11/12", "12/13", "13/14", "14/15", "15/16", "16/17", "17/18", "18/19", "19/20", "20/21",
                                 "10/11", "11/12", "12/13", "13/14", "14/15", "15/16", "16/17", "17/18", "18/19", "19/20", "20/21"]
    
    teamlist30 = df_moyenne_age["equipe"].unique().tolist()

    equipes30 = st.multiselect("Select team", teamlist30, default=["Arsenal"])
    st.text("You selected: {}".format(", ".join(equipes30)))
    

    dfs30 = {equipe: df_moyenne_age[df_moyenne_age["equipe"] == equipe] for equipe in equipes30}


    st.subheader("Moyenne d'âge des équipes sélectionnées")
    fig30 = go.Figure()
    for equipe, df_moyenne_age in dfs30.items():
        fig30 = fig30.add_trace(go.Scatter(x=df_moyenne_age["Saison2"], y=df_moyenne_age["moyenne_age"], name=equipe))
    fig30.update_traces(marker=dict(color="red"), selector = ({'name':'Arsenal'}))
    fig30.update_traces(marker=dict(color="white"), selector = ({'name':'Tottenham'}))
    fig30.update_traces(marker=dict(color="#13BACB"), selector = ({'name':'Manchester City'}))
    fig30.update_traces(marker=dict(color="#5685EC"), selector = ({'name':'Chelsea'}))
    fig30.update_traces(marker=dict(color="#24B928"), selector = ({'name':'Liverpool'}))
    fig30.update_traces(marker=dict(color="#D22DC9"), selector = ({'name':'Manchester United'}))
    fig30.update_layout(xaxis_title="Saison", yaxis_title="Moyenne d'âge")
    st.plotly_chart(fig30)

    st.text("Nous voyons ici que la courbe d'Arsenal est assez différente des autres équipes de PL qui semble observer une stratégie de rajeunissement à partir de 2017.")

    
    df_age = pd.read_csv("age.csv")
    fig25 = px.box(df_age, x = 'Saison', y = 'Age', color = 'Saison')
    fig25.update_layout(showlegend=False)
    st.plotly_chart(fig25)

    st.text("Nous confirmons ici le rajeunissement global des équipes de Premier League alors que nous voyons au-dessus que ce n'est pas le cas d'Arsenal.")


    st.header("Premiers recrutements peu convaicants")
    st.image([image2, image3])
    st.text("Au mercato d'été 2016, Arsenal achète Granit Xhaka (à gauche) et Shkodra Mustafi (à droite) pour la somme totale de 86m€. Xhaka s'avère être un joueur correct mais Mustafi n'est pas à la hauteur des attentes.")



if menu == pages[3]:
    st.title("2017-2018 : Une année à part entre instabilité et déceptions individuelles")
    st.subheader("Arsenal - 6ème - 63 pts")

    st.header("Des ratios offensifs en baisse")
    st.subheader("Ratios buts marqués / tirs cadrés faits Arsenal ")
    df_ratios_arsenal_offensifs = pd.read_csv("Ratios Arsenal offensifs.csv")
    ratios_list2 = ("ratios buts / tirs cadrés global", "ratio buts / tirs cadrés domicile", "ratio buts / tirs cadrés extérieur")
    ratios2 = st.selectbox("Choisir un ratio à afficher", ratios_list2)
    
    fig6 = px.line(data_frame = df_ratios_arsenal_offensifs, x = df_ratios_arsenal_offensifs["season"], y = ratios2)
    fig6.update_traces(line_color='red')
    fig6.update_layout(xaxis_title="Saison", yaxis_title="Ratio sélectionné")
    st.plotly_chart(fig6)

    st.text("Nous identifions une claire chute du ratio en 2017-2018, démontrant un important manque d'efficacité")

    st.header("Une forte instabilité offensive causant le manque d'efficacité")
    st.image([image12, image14, image13])
    st.text("La saison 2017-2018 voit de nombreux buteurs différents cohabiter:\n"
            "* Alexis Sanchez (à gauche), meilleur buteur du club en 2016/2017 voit son efficacité s'écrouler en 2017-2018, il quitte Arsenal au mercato d'hiver\n"
            "* Alexandre Lacazette (au centre), recruté à l'intersaison 2017 pour 53m€ fait de bonnes prestations pour sa première saison\n"
            "* Pierre-Emerick Aubameyang (à droite), arrive au mercato d'hiver 2017-2018 pour la somme de 63m€ en remplacement de Sanchez")

    df_ratios_arsenal_defensifs = pd.read_csv("Ratios Arsenal défensifs.csv")
    ratios_list = ("ratios buts / tirs cadrés global", "ratio buts / tirs cadrés domicile", "ratio buts / tirs cadrés extérieur")

    st.header("Des ratios défensifs en forte hausse")
    st.subheader("Ratios buts encaissés / tirs cadrés subis Arsenal")
    
    fig5 = px.line(data_frame = df_ratios_arsenal_defensifs, x = df_ratios_arsenal_defensifs["season"], y = ratios2)
    fig5.update_traces(line_color='red')
    fig5.update_layout(xaxis_title="Saison", yaxis_title="Ratio sélectionné")
    st.plotly_chart(fig5)

    st.text("Nous identifions une nette hausse du ratio en 2017-2018, montrant un net manque d'impact du gardien de but ")

    df_qualite_match = pd.read_csv("Qualité match par saison.csv")
    df_qualite_match1516 = df_qualite_match[df_qualite_match["season"] == "15/16"]
    df_qualite_match1617 = df_qualite_match[df_qualite_match["season"] == "16/17"]
    df_qualite_match1718 = df_qualite_match[df_qualite_match["season"] == "17/18"]
    st.header("Le déclin de Petr Cech")
    st.subheader("Qualité des matches du gardien par saison")
    fig6 = make_subplots(rows=1, cols=3,shared_yaxes=True)
    fig6.add_trace(go.Bar(x=df_qualite_match1516["Qualité du match"], y=df_qualite_match1516["counts"], name = "2015/2016"), row=1, col=1)
    fig6.add_trace(go.Bar(x=df_qualite_match1617["Qualité du match"], y=df_qualite_match1617["counts"], name = "2016/2017"), row=1, col=2)
    fig6['layout']['xaxis2'].update(title_text='Qualité')
    fig6.add_trace(go.Bar(x=df_qualite_match1718["Qualité du match"], y=df_qualite_match1718["counts"], name = "2017/2018"), row=1, col=3)
    fig6.update_xaxes(categoryorder='array', categoryarray= ['Très bon', 'Bon', 'Moyen', 'Mauvais', 'Très mauvais'])
    fig6.update_layout(yaxis_range=[0,22])
    fig6.update_yaxes(nticks=11)
    fig6.update_traces(marker=dict(color="yellow"), selector = ({'name':'2015/2016'}))
    fig6.update_traces(marker=dict(color="orange"), selector = ({'name':'2016/2017'}))
    fig6.update_traces(marker=dict(color="red"), selector = ({'name':'2017/2018'}))
    fig6.update_layout(yaxis_title="Nb de matches")
    st.plotly_chart(fig6)
    st.text("Nous identifions clairement ici le déclin soudain de Petr Cech en 2017-2018 avec un nombre de très bonnes prestations en nette baisse et un nombre de très mauvais matchs en hausse")

    df1718PetrCech = pd.read_csv("1718 matches PetrCech.csv")
    mauvais_matches_cech_declin = df1718PetrCech[df1718PetrCech["Qualité du match"] == "Très mauvais"]
    mauvais_matches_cech_declin = mauvais_matches_cech_declin.reset_index()
    liste_mauvais_matches = []
    for index in range(len(mauvais_matches_cech_declin)):
        liste_mauvais_matches.append(mauvais_matches_cech_declin['home_team'].loc[index] + "-" + mauvais_matches_cech_declin['away_team'].loc[index] + " " + mauvais_matches_cech_declin['result_full'].loc[index])
    with st.expander("Voir les mauvais matches de Petr Cech en 2017-2018", expanded = False):
        st.write(liste_mauvais_matches)


    



if menu == pages[4]:
    st.title("2018-2019 : La fin de l'ère Wenger")
    st.subheader("Arsenal - 5ème - 70 pts")


    
    df_blessures_saison = pd.read_csv("blessures_equipe_saison.csv")
    df_blessures_saison1819 = df_blessures_saison[df_blessures_saison["Saison"] == "18/19"]
    st.header("La malchance de l'équipe continue")
    fig12 = px.bar(df_blessures_saison1819, x = 'Equipe', y = 'Matchs manqués',
             color = 'Equipe',
             color_discrete_map = {'Arsenal' : 'red',
                                   'Liverpool' : '#24B928',
                                   'United' : '#D22DC9',
                                    'Tottenham' : 'white', 
                                     'City' : '#13BACB', 
                                     'Chelsea' : '#5685EC'})
    fig12.update_layout(showlegend=False)
    st.plotly_chart(fig12)


    df_blesses_1819 = pd.read_csv("arsenal_18_19_blessures.csv")
    df_blesses_1819 = df_blesses_1819.drop('Unnamed: 0', axis = 1)
    with st.expander("Voir les principaux blessés de la saison 2018-2019", expanded = False):
        st.write(df_blesses_1819.head(10))

    st.header("Un héritage de 22 ans difficile à assumer")
    st.image([image8, image5])
    st.text("L'intersaison 2018 marque la fin d'un cycle pour Arsenal avec le départ de leur entraîneur emblématique depuis 22 ans : Arsène Wenger.\n"
            "L'héritage est dur à assumer et la mise en route compliquée pour le nouvel entraîneur Unai Emery.")
    
    st.header("Un mercato actif et inégal")
    st.image([image9, image11, image10])
    st.text("Le mercato 2018, au delà du changement d'entraîneur connaît d'importants mouvements sur le plan de l'effectif pour des résultats assez variés.\n"
            "Trois joueurs arrivent pour un montant supérieur à 15m€ : \n"
            "* Bernd Leno (à gauche), gardien de but, remplace avec brio le déclinant Petr Cech\n"
            "* Lucas Torreira (au centre), un jeune milieu, fait de bonnes prestations avec le club\n"
            "* Sokratis Papastathopoulos (à droite), défenseur, est une erreur de casting et ne solidifie pas la défense d'Arsenal")
    
    
if menu == pages[5]:
    st.title("2019-2020 : L'échec Emery et l'arrivée d'Arteta")
    st.subheader("Arsenal - 8ème - 56 pts")
  
    st.header("Le pire début de saison de la décennie")
    teamlist3 = df_premiere_partie["Nom équipe"].unique().tolist()
    st.subheader("Nombre de points des équipes sélectionnées en 1ère partie de saison")
    equipes_list2 = st.multiselect("Select team", teamlist3, default=["FC Arsenal"])
    st.text("You selected: {}".format(", ".join(equipes_list2)))
    

    dfs2 = {equipe: df_premiere_partie[df_premiere_partie["Nom équipe"] == equipe] for equipe in equipes_list2}


    
    fig4 = go.Figure()
    for equipe, df_premiere_partie in dfs2.items():
        fig4 = fig4.add_trace(go.Scatter(x=df_premiere_partie["Saison"], y=df_premiere_partie["Points"], name=equipe))
    fig4.update_traces(marker=dict(color="red"), selector = ({'name':'FC Arsenal'}))
    fig4.update_traces(marker=dict(color="white"), selector = ({'name':'Tottenham'}))
    fig4.update_traces(marker=dict(color="#13BACB"), selector = ({'name':'Manchester City'}))
    fig4.update_traces(marker=dict(color="#5685EC"), selector = ({'name':'Chelsea'}))
    fig4.update_traces(marker=dict(color="#24B928"), selector = ({'name':'Liverpool'}))
    fig4.update_traces(marker=dict(color="#D22DC9"), selector = ({'name':'Manchester Utd.'}))
    fig4.update_layout(xaxis_title="Saison", yaxis_title="Points 1ère partie de saison")
    st.plotly_chart(fig4)
    st.text("Nous identifions ici clairement que la 1ère partie de saison 2019-2020 est la pire de la décennie pour Arsenal")

    st.header("L'éviction d'Emery et l'arrivée d'Arteta, ancien joueur emblématique d'Arsenal")
    st.image([image5, image4])
    st.text("Le 20 décembre 2019, Unai Emery (à gauche) est démis de ses fonctions et remplacé par Mikel Arteta, adjoint à Manchester City et ancien joueur d'Arsenal de 2011 à 2016")

    st.header("Un mercato 2019 catastrophique, malgré d'importantes dépenses")
    st.image([image6, image7])
    st.text("Le mercato 2019 est marqué par des dépenses records de la part du club avec l'arrivée de Nicolas Pépé (à gauche) pour 80m€ et William Saliba (à droite) pour 30m€.\n"
            "Ces dépenses très importantes ne sont pas suivies de résultat puisque Pépé est prêté à Nice en 2022 et Saliba a enchainé les prêts en Ligue 1 de 2019 à 2022. ")

if menu == pages[6]:
    st.header("Une multitude de facteurs minimes qui conduit à un cycle négatif de déclin expliqué par:")
    st.subheader("1/ Le côté sportif")
    st.text("* une incapacité à voyager et une énorme perte de points à l'extérieur")
    st.text("* de l'instabilité à certains postes clés (attaquants, gardiens de but)")
    st.text("* une fin de cycle au niveau de l'entraineur")
    st.text("\n")
    st.subheader("2/ Le côté financier")
    st.text("* des investissements trop faibles pour rivaliser avec les meilleurs")
    st.text("* un changement de stratégie avec l'achat de joueurs plus expérimentés qui ne paye pas")
    st.text("* une suite de mauvais choix en termes de recrutement")
    st.text("\n")
    st.subheader("3/ La malchance")
    st.text("* un nombre de blessures impressionnant par rapport à la concurrence sur la période")
    st.text("* des saisons qui voient un trop gros nombre de blessures pour être compétitif")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    st.header("Axes d'approfondissement")
    with st.expander("Voir les axes d'appronfondissement", expanded = False):
        st.subheader("1/ Analyses de sentiment via l'étude de la presse sur des sujets précis:")
        st.text("* Changements d'entraîneurs")
        st.text("* Changement de propriétaire")
        st.text("* Arrivées et départs aux mercatos")
        st.text("* Articles de fond sur Arsenal en enlevant les articles ayant deux équipes de Premier League dans leur titre")
        st.subheader("2/ Analyse de données sportives plus précises non disponibles sur le DataFrame de base")
        st.text("* Expected Goals")
        st.text("* Statistique par zone de terrain")
        st.text("* Données individuelles des joueurs pour identifier leur impact")
        st.subheader("3/ Analyse plus poussée de la partie financière")
        st.text("* Evolution des sources de revenus")
        st.text("* Masse salariale comparée aux autres clubs")