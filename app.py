import pandas as pd
import streamlit as st
import plotly.express as px


path = "Tabela 1.1.1.xls"
bruto = pd.read_excel(path, engine="xlrd")


indicador_1 = bruto.iloc[8:41].copy()
indicador_1.columns = [
    "uf_regiao",
    "total",
    "total_branca",
    "total_preta_parda",
    "homem_branca",
    "homem_preta_parda",
    "mulher_branca",
    "mulher_preta_parda",
]


indicador_1 = indicador_1.reset_index(drop=True)


for col in indicador_1.columns[1:]:
    indicador_1[col] = pd.to_numeric(indicador_1[col], errors="coerce")


if "show_news" not in st.session_state:
    st.session_state.show_news = False


st.sidebar.header("🔍 Filtros")
localidades_disponiveis = indicador_1["uf_regiao"].unique().tolist()
localidades_padrao = [localidade for localidade in ["Amazonas", "Bahia", "Pernambuco", "Ceará"] if localidade in localidades_disponiveis]


localidades_selecionadas = st.sidebar.multiselect(
    "Selecione os Estados:",
    options=localidades_disponiveis,
    default=localidades_padrao
)


if st.sidebar.button("Ver Notícias"):
    st.session_state.show_news = True


if st.sidebar.button("Voltar ao Dashboard"):
    st.session_state.show_news = False


if st.session_state.show_news:

    st.title("📰 Notícias")

    st.header("Trabalho doméstico e cuidados no Brasil")

    st.write("""
    Uma análise da desigualdade na divisão das tarefas domésticas
    entre homens e mulheres e das diferenças entre grupos raciais
    no Brasil e nos estados do Amazonas, Bahia, Pernambuco e Ceará.
    """)

    st.caption("Fonte principal: IBGE — PNAD Contínua")

    st.divider()

    # 1. Divisão do trabalho doméstico
    st.subheader("1. A divisão do trabalho doméstico")

    st.image(
        "https://images.unsplash.com/photo-1556911220-e15b29be8c8f",
        caption="Pessoa realizando tarefas domésticas"
    )

    st.write("""
    O trabalho doméstico e os cuidados com pessoas fazem parte
    da rotina de milhões de brasileiros. Entretanto, essas
    responsabilidades não são divididas igualmente.

    Historicamente, as mulheres dedicam mais tempo a essas
    atividades do que os homens.
    """)

    st.divider()

    # 2. Brasil: homens x mulheres
    st.subheader("2. Brasil: homens x mulheres")

    st.caption("Média de horas semanais — 2022")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Mulheres",
            value="21,3 horas"
        )

    with col2:
        st.metric(
            label="Homens",
            value="11,7 horas"
        )

    st.write("""
    As mulheres dedicam aproximadamente 9,6 horas a mais
    por semana aos afazeres domésticos e cuidados.
    """)

    st.divider()

    # 3. Comparação entre estados
    st.subheader("3. Comparação entre os estados")

    st.image(
        "https://images.unsplash.com/photo-1581578731548-c64695cc6952",
        caption="Atividades domésticas"
    )

    st.caption(
        "Média semanal de horas dedicadas às atividades domésticas e cuidados."
    )

    dados_estados = {
        "Estado": [
            "Amazonas",
            "Bahia",
            "Pernambuco",
            "Ceará"
        ],
        "Homens": [
            "12,2 h",
            "10,6 h",
            "12,3 h",
            "12,2 h"
        ],
        "Mulheres": [
            "18,8 h",
            "22,6 h",
            "23,4 h",
            "23,0 h"
        ]
    }

    st.table(dados_estados)

    st.divider()

    # 4. Desigualdade racial
    st.subheader("4. Desigualdade racial")

    st.image(
        "https://images.unsplash.com/photo-1521737711867-e3b97375f902",
        caption="Grupo de pessoas"
    )

    st.write("""
    A desigualdade também aparece quando observamos a divisão
    das tarefas por raça e cor.

    Mulheres pretas e pardas apresentam uma carga maior
    de trabalho doméstico e cuidados em comparação às mulheres brancas.
    """)

    st.markdown("### Horas semanais por grupo — Brasil")

    dados_raciais = {
        "Grupo": [
            "Homens brancos",
            "Homens pretos e pardos",
            "Mulheres brancas",
            "Mulheres pretas e pardas"
        ],
        "Horas": [
            "9,5 h",
            "9,4 h",
            "18,6 h",
            "20,4 h"
        ]
    }

    st.table(dados_raciais)

    st.divider()

    # 5. Principais conclusões
    st.subheader("5. Principais conclusões")

    st.write("""
    - Mulheres dedicam mais horas ao trabalho doméstico do que os homens.
    - A desigualdade está presente nos quatro estados analisados.
    - Mulheres pretas e pardas enfrentam uma carga maior de trabalho doméstico.
    - A divisão desigual demonstra a permanência das diferenças sociais e de gênero no Brasil.
    """)

    st.divider()

    # 6. Conclusão
    st.subheader("6. Conclusão")

    st.write("""
    Os dados mostram que o trabalho doméstico ainda é distribuído
    de maneira desigual na sociedade brasileira.

    As mulheres, especialmente as pretas e pardas, dedicam mais tempo
    aos cuidados e afazeres domésticos.

    Por isso, é importante promover uma divisão mais justa dessas
    responsabilidades, valorizando o trabalho realizado dentro de casa.
    """)

    st.divider()

    st.caption(
        "Fonte: IBGE — PNAD Contínua, Outras Formas de Trabalho. "
        "Dados de referência: 2022."
    )
    
else:
    st.title("📊 Dashboard: Horas Dedicadas a Cuidados e Afazeres Domésticos")
    st.markdown(
        "Este dashboard permite explorar as discrepâncias nas horas dedicadas aos afazeres domésticos entre homens e mulheres, considerando gênero, cor e região."
    )


    estados_filtrados = indicador_1[indicador_1["uf_regiao"].isin(localidades_selecionadas)]


    st.subheader(f"📋 Dados Filtrados ({', '.join(localidades_selecionadas)})")
    st.dataframe(estados_filtrados)


    st.markdown("---")


    st.subheader("📊 Comparação por Gênero e Cor")
    if not estados_filtrados.empty:
        df_melted = estados_filtrados.melt(
            id_vars=["uf_regiao"],
            value_vars=["homem_branca", "mulher_branca", "homem_preta_parda", "mulher_preta_parda"],
            var_name="Sexo",
            value_name="Horas Semanais"
        )


        fig_bar = px.bar(
            df_melted,
            x="uf_regiao",
            y="Horas Semanais",
            color="Sexo",
            barmode="group",
            title="Média de Horas por Sexo e Cor",
            color_discrete_sequence=px.colors.qualitative.Set2,
            labels={
                "Horas Semanais": "Horas/Semana",
                "uf_regiao": "Região/UF",
                "Sexo": "Gênero e Cor"
            }
        )
        fig_bar.update_layout(
            title=dict(font=dict(size=18), x=0.3),
            xaxis=dict(title_font=dict(size=14), tickangle=-45),
            yaxis=dict(title_font=dict(size=14)),
            legend=dict(title="Legenda", orientation="h", y=-0.4, x=0.5, xanchor="center"),
            margin=dict(l=40, r=40, t=60, b=80)
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.write("Nenhum dado disponível para as localidades selecionadas.")


    st.subheader("📈 Evolução Temporal")
    if not estados_filtrados.empty:
        df_melted = estados_filtrados.melt(
            id_vars=["uf_regiao"],
            value_vars=["homem_branca", "mulher_branca", "homem_preta_parda", "mulher_preta_parda"],
            var_name="Sexo",
            value_name="Horas Semanais"
        )


        fig_line = px.line(
            df_melted,
            x="uf_regiao",
            y="Horas Semanais",
            color="Sexo",
            markers=True,
            title="Histórico de Horas Semanais por Sexo e Região",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            labels={
                "uf_regiao": "Região/UF",
                "Horas Semanais": "Horas/Semana",
                "Sexo": "Gênero e Cor"
            }
        )
        fig_line.update_layout(
            title=dict(font=dict(size=18), x=0.2),
            xaxis=dict(title_font=dict(size=14), tickangle=-45),
            yaxis=dict(title_font=dict(size=14)),
            legend=dict(title="Legenda", orientation="h", y=-0.4, x=0.5, xanchor="center"),
            margin=dict(l=40, r=40, t=60, b=80)
        )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.write("Nenhum dado disponível para as localidades selecionadas.")