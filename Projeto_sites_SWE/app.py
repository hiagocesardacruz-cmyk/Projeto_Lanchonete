import streamlit as st


st.set_page_config(page_title="Lanchonete", page_icon="🍔")


if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = []

cardapio = {
    "Coxinha": {'valor_unitário': 6},
    "Risole": {'valor_unitário': 7},
    "Coca lata 350 ml": {'valor_unitário': 10}
}

st.title("🍔 Lanchonete do kleber")


item_selecionado = st.selectbox("Selecione um item do cardápio:", list(cardapio.keys()))
quantidade = st.number_input("Quantidade:", min_value=1, value=1, step=1)


preco_unitario = cardapio[item_selecionado]['valor_unitário']
subtotal = preco_unitario * quantidade

st.write(f"**Valor unitário:** R$ {preco_unitario:.2f}")
st.write(f"**Subtotal deste item:** R$ {subtotal:.2f}")


if st.button("Adicionar ao Carrinho"):
    st.session_state["carrinho"].append({
        "item": item_selecionado,
        "quantidade": quantidade,
        "subtotal": subtotal
    })
    st.success(f"Adicionado: {quantidade}x {item_selecionado}!")


st.divider()
st.subheader("🛒 Carrinho de Compras")

if st.session_state["carrinho"]:
    total_geral = 0
    for i, produto in enumerate(st.session_state["carrinho"], start=1):
        st.write(f"{i}. {produto['item']} (Qtd: {produto['quantidade']}) - R$ {produto['subtotal']:.2f}")
        total_geral += produto['subtotal']
    
    st.markdown(f"### **Total Geral: R$ {total_geral:.2f}**")
    

    st.divider()
    st.subheader("💳 Forma de Pagamento")
    forma_pagamento = st.selectbox("Escolha como deseja pagar:", ["PIX", "Cartão de Crédito/Débito", "Dinheiro"])
    

    troco_para = 0.0
    if forma_pagamento == "Dinheiro":
        troco_para = st.number_input("Troco para quanto? (R$)", min_value=float(total_geral), value=float(total_geral), step=1.0)
    

    if st.button("Finalizar e Pagar Pedido"):
        st.success(f"✅ Pedido finalizado com sucesso! Pagamento via **{forma_pagamento}** registrado.")
        
        if forma_pagamento == "Dinheiro" and troco_para > total_geral:
            troco = troco_para - total_geral
            st.info(f"Troco a devolver: **R$ {troco:.2f}**")
            

        st.session_state["carrinho"] = []
        st.balloons() 
    
    if st.button("Limpar Carrinho"):
        st.session_state["carrinho"] = []
        st.rerun()
else:
    st.info("O carrinho está vazio.")