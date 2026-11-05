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
    # Tela de notícias
    st.title("📰 Notícias")
    st.markdown("""
    <style>
    .main {
        background-color: #f5f6fa;
    }


    .dashboard {
        font-family: Arial, sans-serif;
        color: #263238;
    }


    .hero {
        background: linear-gradient(120deg, #263c5a, #477b91);
        padding: 35px;
        border-radius: 18px;
        color: white;
        margin-bottom: 25px;
    }


    .hero h1 {
        font-size: 32px;
        margin-bottom: 10px;
    }


    .hero p {
        font-size: 16px;
        line-height: 1.6;
    }


    .card {
        background: white;
        padding: 22px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 3px 12px rgba(0,0,0,0.06);
    }


    .metric {
        font-size: 28px;
        font-weight: bold;
        color: #315c79;
    }


    .subtitle {
        color: #64748b;
        font-size: 14px;
    }


    .bar-bg {
        background: #e9edf2;
        height: 13px;
        border-radius: 10px;
        overflow: hidden;
        margin: 8px 0 15px;
    }


    .bar {
        height: 13px;
        border-radius: 10px;
        background: #477b91;
    }


    img {
        width: 100%;
        border-radius: 12px;
        object-fit: cover;
    }


    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
    }


    th {
        background: #315c79;
        color: white;
        padding: 12px;
    }


    td {
        padding: 12px;
        border-bottom: 1px solid #e5e7eb;
        text-align: center;
    }


    .footer {
        text-align: center;
        color: #64748b;
        font-size: 13px;
        padding: 20px;
    }
    </style>


    <div class="dashboard">


    <div class="hero">
        <h1>Trabalho doméstico e cuidados no Brasil</h1>
        <p>
        Uma análise da desigualdade na divisão das tarefas domésticas
        entre homens e mulheres e das diferenças entre grupos raciais
        no Brasil e nos estados do Amazonas, Bahia, Pernambuco e Ceará.
        </p>
        <p><b>Fonte principal:</b> IBGE — PNAD Contínua</p>
    </div>


    <div class="card">
        <img src="https://images.unsplash.com/photo-1556911220-e15b29be8c8f"
        alt="Pessoa realizando tarefas domésticas">


        <h2>1. A divisão do trabalho doméstico</h2>


        <p>
        O trabalho doméstico e os cuidados com pessoas fazem parte
        da rotina de milhões de brasileiros. Entretanto, essas
        responsabilidades não são divididas igualmente.
        Historicamente, as mulheres dedicam mais tempo a essas
        atividades do que os homens.
        </p>
    </div>


    <h2>2. Brasil: homens x mulheres</h2>


    <div class="card">
        <p class="subtitle">Média de horas semanais — 2022</p>


        <p>Mulheres</p>
        <div class="metric">21,3 horas</div>
        <div class="bar-bg">
            <div class="bar" style="width:100%"></div>
        </div>


        <p>Homens</p>
        <div class="metric">11,7 horas</div>
        <div class="bar-bg">
            <div class="bar" style="width:55%"></div>
        </div>


        <p>
        As mulheres dedicam aproximadamente 9,6 horas a mais
        por semana aos afazeres domésticos e cuidados.
        </p>
    </div>


    <h2>3. Comparação entre os estados</h2>


    <div class="card">
        <img src="https://images.unsplash.com/photo-1581578731548-c64695cc6952"
        alt="Atividades domésticas">


        <p class="subtitle">
        Média semanal de horas dedicadas às atividades domésticas e cuidados.
        </p>


        <table>
            <tr>
                <th>Estado</th>
                <th>Homens</th>
                <th>Mulheres</th>
            </tr>
            <tr>
                <td>Amazonas</td>
                <td>12,2 h</td>
                <td>18,8 h</td>
            </tr>
            <tr>
                <td>Bahia</td>
                <td>10,6 h</td>
                <td>22,6 h</td>
            </tr>
            <tr>
                <td>Pernambuco</td>
                <td>12,3 h</td>
                <td>23,4 h</td>
            </tr>
            <tr>
                <td>Ceará</td>
                <td>12,2 h</td>
                <td>23,0 h</td>
            </tr>
        </table>
    </div>


    <h2>4. Desigualdade racial</h2>


    <div class="card">
        <img src="https://images.unsplash.com/photo-1521737711867-e3b97375f902"
        alt="Grupo de pessoas">


        <p>
        A desigualdade também aparece quando observamos a divisão
        das tarefas por raça e cor. Mulheres pretas e pardas
        apresentam uma carga maior de trabalho doméstico e cuidados
        em comparação às mulheres brancas.
        </p>


        <h3>Horas semanais por grupo — Brasil</h3>


        <table>
            <tr>
                <th>Grupo</th>
                <th>Horas</th>
            </tr>
            <tr>
                <td>Homens brancos</td>
                <td>9,5 h</td>
            </tr>
            <tr>
                <td>Homens pretos e pardos</td>
                <td>9,4 h</td>
            </tr>
            <tr>
                <td>Mulheres brancas</td>
                <td>18,6 h</td>
            </tr>
            <tr>
                <td>Mulheres pretas e pardas</td>
                <td>20,4 h</td>
            </tr>
        </table>
    </div>


    <h2>5. Principais conclusões</h2>


    <div class="card">
        <p>
        • Mulheres dedicam mais horas ao trabalho doméstico
        do que os homens.
        </p>
        <p>
        • A desigualdade está presente nos quatro estados analisados.
        </p>
        <p>
        • Mulheres pretas e pardas enfrentam uma carga maior
        de trabalho doméstico.
        </p>
        <p>
        • A divisão desigual demonstra a permanência das
        diferenças sociais e de gênero no Brasil.
        </p>
    </div>


    <div class="card">
        <h2>6. Conclusão</h2>
        <p>
        Os dados mostram que o trabalho doméstico ainda é distribuído
        de maneira desigual na sociedade brasileira. As mulheres,
        especialmente as pretas e pardas, dedicam mais tempo aos
        cuidados e afazeres domésticos. Por isso, é importante
        promover uma divisão mais justa dessas responsabilidades,
        valorizando o trabalho realizado dentro de casa.
        </p>
    </div>


    <div class="footer">
        Fonte: IBGE — PNAD Contínua, Outras Formas de Trabalho.
        <br>
        Dados de referência: 2022.
    </div>


    </div>
    """, unsafe_allow_html=True
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