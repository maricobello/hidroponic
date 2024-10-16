import streamlit as st

# Função de Solução Nutritiva
def solucao_nutritiva():
    st.subheader("Calculadora de Solução Nutritiva")
    st.image("https://http2.mlstatic.com/D_NQ_NP_819013-MLA78857970962_092024-O.webp", caption="Solução Nutritiva", use_column_width=True)

    st.write("Use esta ferramenta para calcular a solução nutritiva ideal para o seu cultivo.")
    
    # Descrição dos sais em uma moldura
    st.markdown("""
    <div style="border: 1px solid #ddd; background-color:#f9f9f9; padding: 15px; border-radius: 10px;">
        <h4 style="color: #333;">Descrição dos Sais Utilizados</h4>
        - <strong>Plant Prod 7-11-27</strong>: Fertilizante completo rico em macronutrientes (NPK).<br>
        - <strong>Nitrato de Cálcio</strong>: Fonte de cálcio e nitrogênio.<br>
        - <strong>Sulfato de Magnésio (Sal Amargo)</strong>: Suplementa magnésio, essencial para a fotossíntese.<br>
        - <strong>MKP (Monopotássico Fosfato)</strong>: Fornece fósforo e potássio, essencial na fase de floração.
    </div>
    """, unsafe_allow_html=True)

    # Inputs de fase de crescimento e volume
    fase = st.selectbox("Fase de Crescimento", ["Vega", "Flora"])
    volume = st.number_input("Volume de solução nutritiva (L)", min_value=0.1, value=10.0)

    # Configuração dos sliders para cada fase
    if fase == 'Vega':
        sulfato_magnesio = st.slider("Sulfato de Magnésio (g/L)", min_value=0.3, max_value=0.5, value=0.3)
        nutrientes = calcular_solucao_nutritiva(volume, fase, sulfato_magnesio)
        exibir_resultado_solucao(fase, volume, nutrientes)
    else:
        sulfato_magnesio = st.slider("Sulfato de Magnésio (g/L)", min_value=0.6, max_value=0.8, value=0.6)
        mkp = st.slider("MKP (g/L)", min_value=0.6, max_value=1.2, value=0.6)
        nutrientes = calcular_solucao_nutritiva(volume, fase, sulfato_magnesio, mkp)
        exibir_resultado_solucao(fase, volume, nutrientes)

    # Parâmetros recomendados em uma moldura
    st.markdown("""
    <div style="border: 1px solid #ddd; background-color:#f9f9f9; padding: 15px; border-radius: 10px;">
        <h4 style="color: #333;">Parâmetros Recomendados</h4>
        - <strong>pH:</strong> Mantenha entre 5.8 e 6.2 para absorção ideal de nutrientes.<br>
        - <strong>EC Vega:</strong> 1.5-2.0 mS/cm<br>
        - <strong>EC Flora:</strong> 2.0-3.0 mS/cm<br>
        - Regue com 20%-30% de runoff para evitar acúmulo de nutrientes.
    </div>
    """, unsafe_allow_html=True)

    # Botão de Voltar ao Menu
    st.markdown("<div style='text-align: center;'><button style='background-color: #4CAF50; color: white; padding: 10px 24px; border: none; cursor: pointer; border-radius: 12px;' onclick='window.history.back()'>Voltar ao Menu</button></div>", unsafe_allow_html=True)

    # Desenvolvido por
    st.markdown("<p style='text-align: center;'>Desenvolvido por <a href='https://www.instagram.com/dungrow/' target='_blank'>@dungrow</a></p>", unsafe_allow_html=True)


# Função de cálculo da solução nutritiva
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

# Função para exibir os resultados
def exibir_resultado_solucao(fase, volume, nutrientes):
    if fase == 'Vega':
        st.markdown(f"""
        <div style='background-color:#4CAF50;padding:10px;border-radius:5px;text-align:center;'>
            <h4 style='color:black;font-size:22px;'>Solução Nutritiva para Vega ({volume}L)</h4>
            <p style='color:black; font-weight:bold;'><strong>Plant Prod:</strong> {nutrientes[0]:.2f}g<br>
            <strong>Nitrato de Cálcio:</strong> {nutrientes[1]:.2f}g<br>
            <strong>Sulfato de Magnésio:</strong> {nutrientes[2]:.2f}g</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='background-color:#4CAF50;padding:10px;border-radius:5px;text-align:center;'>
            <h4 style='color:black;font-size:22px;'>Solução Nutritiva para Flora ({volume}L)</h4>
            <p style='color:black; font-weight:bold;'><strong>Plant Prod:</strong> {nutrientes[0]:.2f}g<br>
            <strong>Nitrato de Cálcio:</strong> {nutrientes[1]:.2f}g<br>
            <strong>Sulfato de Magnésio:</strong> {nutrientes[2]:.2f}g<br>
            <strong>MKP:</strong> {nutrientes[3]:.2f}g</p>
        </div>
        """, unsafe_allow_html=True)

# Função para Manejo do Coco
def manejo_coco():
    st.subheader("Manejo do Coco (Hidroponia)")
    st.image("https://cococoirglobal.com/wp-content/uploads/2023/06/choosing-the-right-nutrient-mix-for-cannabis-growth-in-coco-coir.jpg", caption="Manejo do Coco", use_column_width=True)

    st.write("Use esta ferramenta para otimizar o manejo da fibra de coco no seu cultivo.")
    st.markdown("""
    <div style="border: 1px solid #ddd; background-color:#f9f9f9; padding: 15px; border-radius: 10px;">
        <h4 style="color: #333;">Carregar o Coco com Solução Nutritiva</h4>
        - A fibra de coco é um meio inerte, por isso precisa de uma dose inicial de solução nutritiva antes de inserir a planta.<br><br>

        <h4 style="color: #333;">Mistura de Coco com Perlita</h4>
        - Algumas misturas incluem perlita (~20% em volume) para melhorar a aeração do meio de cultivo.<br>
        - Coco com boa aeração é importante para evitar o excesso de retenção de água.<br><br>

        <h4 style="color: #333;">Manejo do Coco</h4>
        - Irrigações frequentes (a cada 3 a 4 horas) após a luz acender.<br>
        - Regue vasos menores com mais frequência para controle ideal de lavagem e menores volumes de solução nutritiva.<br>
        - Lave o coco uma vez por semana com 50% da solução nutritiva para eliminar sais acumulados.
    </div>
    """, unsafe_allow_html=True)

    # Botão de Voltar ao Menu
    st.markdown("<div style='text-align: center;'><button style='background-color: #4CAF50; color: white; padding: 10px 24px; border: none; cursor: pointer; border-radius: 12px;' onclick='window.history.back()'>Voltar ao Menu</button></div>", unsafe_allow_html=True)

    # Desenvolvido por
    st.markdown("<p style='text-align: center;'>Desenvolvido por <a href='https://www.instagram.com/dungrow/' target='_blank'>@dungrow</a></p>", unsafe_allow_html=True)

# Função de Cálculo de Iluminação
def calculo_potencia_indoor():
    st.subheader("Cálculo de Potência e Custo de Iluminação")
    st.image("https://cdn.shopify.com/s/files/1/2793/2316/files/4000k-photon-tube_1024x1024.png?v=1526675072", caption="Cálculo de Iluminação", use_column_width=True)

    st.write("Calcule a potência necessária para iluminação e o custo estimado de energia elétrica para seu grow.")
    
    # Inputs de medidas do grow
    altura = st.number_input("Altura do Grow (em metros)", min_value=0.1, value=2.0, step=0.1)
    comprimento = st.number_input("Comprimento do Grow (em metros)", min_value=0.1, value=1.0, step=0.1)
    largura = st.number_input("Largura do Grow (em metros)", min_value=0.1, value=1.0, step=0.1)

    area_m2 = comprimento * largura
    st.write(f"**Área do Grow:** {area_m2:.2f} m²")

    # Cálculo da altura recomendada para as plantas
    altura_vega = altura * 0.5
    altura_flora = altura * 0.8
    st.write(f"**Altura recomendada para plantas na fase de Vega:** {altura_vega:.2f} metros")
    st.write(f"**Altura recomendada para plantas na fase de Flora:** {altura_flora:.2f} metros")

    # Cálculo de potência com lumens/watt
    lumens_watt = st.number_input("Lumens/Watt da Lâmpada", min_value=60, value=90, step=1)
    potencia_min = 30000 / lumens_watt
    potencia_max = 60000 / lumens_watt
    potencia_sugerida = (potencia_min + potencia_max) / 2

    st.write(f"**Potência sugerida para {area_m2:.2f} m²:** {potencia_sugerida:.2f} Watts")

    # Inputs para semanas de vega e flora
    semanas_vega = st.number_input("Semanas de Vega", min_value=1, value=4)
    semanas_flora = st.number_input("Semanas de Flora", min_value=1, value=8)

    horas_vega = 18
    horas_flora = 12

    # Cálculo de custo de energia
    kwh_vega_mensal = (potencia_sugerida * horas_vega * 30) / 1000
    kwh_flora_mensal = (potencia_sugerida * horas_flora * 30) / 1000
    custo_vega_mensal = kwh_vega_mensal * 0.90
    custo_flora_mensal = kwh_flora_mensal * 0.90

    custo_vega_total = custo_vega_mensal * (semanas_vega / 4)
    custo_flora_total = custo_flora_mensal * (semanas_flora / 4)

    # Exibindo resultados de custos
    st.markdown(f"""
    ### Preço Estimado Mensal:
    <div style='background-color:#4CAF50;padding:10px;border-radius:5px;text-align:center;'>
        <p style='color:black; font-weight:bold;'>Custo Mensal - Vega (18h/dia): R$ {custo_vega_mensal:.2f}</p>
        <p style='color:black; font-weight:bold;'>Custo Mensal - Flora (12h/dia): R$ {custo_flora_mensal:.2f}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    ### Preço Estimado para o Ciclo Todo:
    <div style='background-color:#ffe6e6;padding:10px;border-radius:5px;text-align:center;'>
        <p style='color:black; font-weight:bold;'>Custo Total - Vega ({semanas_vega} semanas): R$ {custo_vega_total:.2f}</p>
        <p style='color:black; font-weight:bold;'>Custo Total - Flora ({semanas_flora} semanas): R$ {custo_flora_total:.2f}</p>
    </div>
    """, unsafe_allow_html=True)

    # Distância da luz e imagem
    st.markdown("### Distância da Luz LED")
    st.image("https://imgur.com/a/T4uciQy", caption="Distâncias Recomendadas do LED à Planta", use_column_width=True)

    # Botão de Voltar ao Menu
    st.markdown("<div style='text-align: center;'><button style='background-color: #4CAF50; color: white; padding: 10px 24px; border: none; cursor: pointer; border-radius: 12px;' onclick='window.history.back()'>Voltar ao Menu</button></div>", unsafe_allow_html=True)

    # Desenvolvido por
    st.markdown("<p style='text-align: center;'>Desenvolvido por <a href='https://www.instagram.com/dungrow/' target='_blank'>@dungrow</a></p>", unsafe_allow_html=True)

# Menu inicial com descrição das ferramentas
def menu():
    st.title("Ferramenta de Cultivo para Cannabis")
    st.write("Escolha a ferramenta abaixo para navegar no aplicativo.")

    st.markdown("""
    <div style='text-align:center'>
        <button style='background-color: #4CAF50; color: white; padding: 10px 24px; border: none; cursor: pointer; border-radius: 12px; margin: 10px;' onclick='window.location.href="/solucao_nutritiva"'>Solução Nutritiva</button><br>
        <button style='background-color: #4CAF50; color: white; padding: 10px 24px; border: none; cursor: pointer; border-radius: 12px; margin: 10px;' onclick='window.location.href="/manejo_coco"'>Manejo do Coco</button><br>
        <button style='background-color: #4CAF50; color: white; padding: 10px 24px; border: none; cursor: pointer; border-radius: 12px; margin: 10px;' onclick='window.location.href="/cultivo_organico"'>Cultivo Orgânico</button><br>
        <button style='background-color: #4CAF50; color: white; padding: 10px 24px; border: none; cursor: pointer; border-radius: 12px; margin: 10px;' onclick='window.location.href="/calculo_potencia"'>Cálculo de Potência</button><br>
        <button style='background-color: #4CAF50; color: white; padding: 10px 24px; border: none; cursor: pointer; border-radius: 12px; margin: 10px;' onclick='window.location.href="/colheita"'>Colheita e Pós-tratamento</button>
    </div>
    """, unsafe_allow_html=True)

    # Desenvolvido por no menu
    st.markdown("<p style='text-align: center;'>Desenvolvido por <a href='https://www.instagram.com/dungrow/' target='_blank'>@dungrow</a></p>", unsafe_allow_html=True)

# Definição da página inicial
if 'page' not in st.session_state:
    st.session_state.page = "menu"

# Navegação entre as abas
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
