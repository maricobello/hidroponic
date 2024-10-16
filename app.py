import streamlit as st

# CSS para personalizar botões
def add_custom_css():
    st.markdown("""
    <style>
    div.stButton > button {
        background-color: green;
        color: black;
        border-radius: 5px;
        width: 100%;
        padding: 8px 16px;
        font-size: 18px;
    }
    div.stButton > button:hover {
        background-color: #32a852;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# Funcionalidade de Solução Nutritiva com resultados em tempo real
def solucao_nutritiva():
    st.subheader("Calculadora de Solução Nutritiva")
    st.image("https://http2.mlstatic.com/D_NQ_NP_819013-MLA78857970962_092024-O.webp", caption="Solução Nutritiva", use_column_width=True)

    st.write("Use esta ferramenta para calcular a solução nutritiva ideal para o seu cultivo.")
    st.write("""
    ### Descrição dos Sais Utilizados:
    - **Plant Prod 7-11-27**: Fertilizante completo rico em macronutrientes como nitrogênio, fósforo e potássio.
    - **Nitrato de Cálcio**: Fonte de cálcio e nitrogênio.
    - **Sulfato de Magnésio (Sal Amargo)**: Suplementa magnésio, essencial para a fotossíntese.
    - **MKP (Monopotássico Fosfato)**: Fornece fósforo e potássio adicionais, especialmente durante a fase de floração.
    """)

    fase = st.selectbox("Fase de Crescimento", ["Vega", "Flora"])
    volume = st.number_input("Volume de solução nutritiva (L)", min_value=0.1, value=10.0)

    if fase == 'Vega':
        sulfato_magnesio = st.slider("Sulfato de Magnésio (g/L)", min_value=0.3, max_value=0.5, value=0.3)
        nutrientes = calcular_solucao_nutritiva(volume, fase, sulfato_magnesio)
        exibir_resultado_solucao(fase, volume, nutrientes)
    else:
        sulfato_magnesio = st.slider("Sulfato de Magnésio (g/L)", min_value=0.6, max_value=0.8, value=0.6)
        mkp = st.slider("MKP (g/L)", min_value=0.6, max_value=1.2, value=0.6)
        nutrientes = calcular_solucao_nutritiva(volume, fase, sulfato_magnesio, mkp)
        exibir_resultado_solucao(fase, volume, nutrientes)

    # Instruções adicionais
    st.markdown("""
    <div style='background-color:#f7f7f7;padding:10px;border-radius:5px;'>
        <p style='color:black; font-weight:bold;'>Mantenha entre <strong>pH 5.8 e 6.2</strong> para absorção ideal de nutrientes.</p>
        <p style='color:black; font-weight:bold;'><strong>EC Vega:</strong> 1.5-2.0 mS/cm<br>
        <strong>EC Flora:</strong> 2.0-3.0 mS/cm</p>
        <p style='color:black;'><strong>Recomendações:</strong> Regue com 20%-30% de runoff para evitar acúmulo de nutrientes. <br>
        </p>
	<p style='color:black;'>1x por semana, regue com 50% da solução nutritiva.<br></p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Voltar ao Menu"):
        st.session_state.page = "menu"

# Função para cálculo de solução nutritiva
def calcular_solucao_nutritiva(volume, fase, sulfato_magnesio, mkp=None):
    plant_prod = 1.15
    nitrato_calcio = 0.78
    total_plant_prod = plant_prod * volume
    total_nitrato_calcio = nitrato_calcio * volume
    total_sulfato_magnesio = sulfato_magnesio * volume

    if fase == 'Flora' and mkp:
        total_mkp = mkp * volume
        return total_plant_prod, total_nitrato_calcio, total_sulfato_magnesio, total_mkp
    return total_plant_prod, total_nitrato_calcio, total_sulfato_magnesio

# Função para exibir resultados da solução nutritiva em tempo real
def exibir_resultado_solucao(fase, volume, nutrientes):
    if fase == 'Vega':
        st.markdown(f"""
        <div style='background-color:#d4edda;padding:10px;border-radius:5px;text-align:center;'>
            <h4 style='color:black;font-size:22px;'>Solução Nutritiva para Vega ({volume}L)</h4>
            <p style='color:black; font-weight:bold;'><strong>Plant Prod:</strong> {nutrientes[0]:.2f}g<br>
            <strong>Nitrato de Cálcio:</strong> {nutrientes[1]:.2f}g<br>
            <strong>Sulfato de Magnésio:</strong> {nutrientes[2]:.2f}g</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='background-color:#d4edda;padding:10px;border-radius:5px;text-align:center;'>
            <h4 style='color:black;font-size:22px;'>Solução Nutritiva para Flora ({volume}L)</h4>
            <p style='color:black; font-weight:bold;'><strong>Plant Prod:</strong> {nutrientes[0]:.2f}g<br>
            <strong>Nitrato de Cálcio:</strong> {nutrientes[1]:.2f}g<br>
            <strong>Sulfato de Magnésio:</strong> {nutrientes[2]:.2f}g<br>
            <strong>MKP:</strong> {nutrientes[3]:.2f}g</p>
        </div>
        """, unsafe_allow_html=True)

# Função para o Menu principal
def menu():
    st.title("Ferramenta de Cultivo para Cannabis")
    st.markdown("<p style='text-align: center;'>Desenvolvido por <a href='https://www.instagram.com/dungrow/' target='_blank'>@dungrow</a></p>", unsafe_allow_html=True)
    st.write("Escolha a ferramenta abaixo:")

    if st.button("Solução Nutritiva"):
        st.session_state.page = "solucao_nutritiva"
    if st.button("Manejo do Coco"):
        st.session_state.page = "manejo_coco"
    if st.button("Cultivo Orgânico"):
        st.session_state.page = "cultivo_organico"
    if st.button("Colheita e Pós-tratamento"):
        st.session_state.page = "colheita"
    if st.button("Cálculo de Potência para Indoor"):
        st.session_state.page = "calculo_potencia"

# Cálculo de iluminação com simulação de custo de energia elétrica
def calculo_potencia_indoor():
    st.subheader("Cálculo de Iluminação LED")
    st.image("https://cdn.shopify.com/s/files/1/2793/2316/files/4000k-photon-tube_1024x1024.png?v=1526675072", caption="Cálculo de Iluminação", use_column_width=True)

    st.write("Calcule a potência de iluminação ideal e o custo mensal estimado de energia elétrica.")

    area_m2 = st.number_input("Área de cultivo (m²)", min_value=0.1, value=1.0)
    lumens_watt = st.number_input("Lumens/Watt da Lâmpada", min_value=70, value=150)
    horas_vega = 18
    horas_flora = 12

    eficiencia_led = 50  # Mínimo 50W/m²
    potencia_total = eficiencia_led * area_m2
    rendimento_estimado = potencia_total * (0.7 * (0.6))  # Rendimento 30% menor
    kwh_vega = (potencia_total * horas_vega * 30) / 1000
    kwh_flora = (potencia_total * horas_flora * 30) / 1000
    custo_vega = kwh_vega * 0.90  # R$/kWh
    custo_flora = kwh_flora * 0.90

    st.markdown(f"""
    <div style='background-color:#d4edda;padding:10px;border-radius:5px;text-align:center;'>
        <h4 style="font-size:22px;color:black;">Potência Requerida: {potencia_total:.2f} Watts</h4>
        <p style='color:black; font-weight:bold;'>Rendimento Estimado: {rendimento_estimado:.2f} gramas</p>
        <p style='color:black; font-weight:bold;'>Custo estimado (Vega - 18h/dia): R$ {custo_vega:.2f}/mês</p>
        <p style='color:black; font-weight:bold;'>Custo estimado (Flora - 12h/dia): R$ {custo_flora:.2f}/mês</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Voltar ao Menu"):
        st.session_state.page = "menu"

# Página de Manejo do Coco
def manejo_coco():
    st.subheader("Manejo do Coco (Hidroponia)")
    st.image("https://imgur.com/a/T4uciQy", caption="Manejo do Coco", use_column_width=True)

    st.write("Use esta ferramenta para otimizar o manejo da fibra de coco no seu cultivo.")
    st.write("""
    ### Manejo do Coco:
    - A fibra de coco é um meio inerte, por isso precisa de uma dose inicial de solução nutritiva antes de inserir a planta.
    - Irrigações frequentes (a cada 3 a 4 horas) após a luz acender.
    - Regue vasos menores com mais frequência para controle ideal de lavagem e menores volumes de solução nutritiva.
    - Lave o coco uma vez por semana com 50% da solução nutritiva para eliminar sais acumulados.
    """)

    if st.button("Voltar ao Menu"):
        st.session_state.page = "menu"

# Página de Cultivo Orgânico
def cultivo_organico():
    st.subheader("Cultivo Orgânico")
    st.image("https://www.growweedeasy.com/wp-content/uploads/2014/10/baby-vegetative-plants-super-soil.jpg", caption="Cultivo Orgânico", use_column_width=True)

    
    st.write("Use esta ferramenta para informações e dicas sobre o cultivo orgânico.")


    st.subheader("Receita de Solo Orgânico - Litros!")
    st.write("""
    Mistura para ~150L de solo:
    - 45L de substrato Carolina Soil
    - 45L de perlita 
    - 40L de húmus de minhoca
    - 10L de pó de coco ou casca de arroz carbonizada
    - 2 copos de farinha de osso
    - 2 copos de farinha de algas
    - 2 copos de torta de algodão ou semente de girassol
    - 2 copos de bokashi
    - 1 copo de Yoorin master 1S
    - 1 copo de Yoorin Ekosil
    - 1 copo de gesso agrícola
    - 3 colheres de Sal Amargo
    - 2 copos de farinha de ostras
    - 1 copo de farinha de peixe
    """)

    st.write("""
    ### Dicas de Manejo de Rega e Solo:
    - Regue com 20% do volume do vaso.
    - Nos dias mais quentes, o solo seca mais rapidamente, ajustando a frequência de rega.
    - Temperatura e Umidade recomendadas:
        - **Vega**: 24-26°C, Umidade 60-70%
        - **Flora**: 22-24°C, Umidade 50-60%
    """)

    if st.button("Voltar ao Menu"):
        st.session_state.page = "menu"

# Página de Colheita e Pós-tratamento
def colheita_pos_tratamento():
    st.subheader("Colheita e Pós-tratamento")
    st.image("https://imgur.com/a/T4uciQy", caption="Colheita e Secagem", use_column_width=True)

    st.write("Use esta ferramenta para seguir as melhores práticas de colheita e pós-tratamento.")
    st.write("""
    ### Passos para Colheita e Pós-tratamento:
    1. **Colheita**: Corte os ramos com cuidado e evite manusear os buds diretamente.
    2. **Secagem**: Pendure as plantas em um local escuro e ventilado com umidade de 50% e temperatura de 10°C (50°F).
    3. **Trima (pós-seco)**: Após a secagem completa, faça a trima (aparação) das folhas grandes e secas.
    4. **Armazenamento**: Armazene os buds em frascos de vidro herméticos para manter a qualidade.
    """)

    if st.button("Voltar ao Menu"):
        st.session_state.page = "menu"

# Carregar CSS customizado ao iniciar a aplicação
add_custom_css()

# Definição da página de navegação atual
if 'page' not in st.session_state:
    st.session_state.page = 'menu'

# Navegação
if st.session_state.page == "menu":
    menu()
elif st.session_state.page == "solucao_nutritiva":
    solucao_nutritiva()
elif st.session_state.page == "manejo_coco":
    manejo_coco()
elif st.session_state.page == "cultivo_organico":
    cultivo_organico()
elif st.session_state.page == "colheita":
    colheita_pos_tratamento()
elif st.session_state.page == "calculo_potencia":
    calculo_potencia_indoor()
