import streamlit as st
import plotly.express as px
import pandas as pd

class VisualizationData:
    def display_page(self, df_filtered: pd.DataFrame, total_month: float) -> None:
        st.title("Análise de Vendas")
        st.subheader(f"Total do mês: R${total_month:.2f}")
        st.markdown("---")

        st.header("Faturamento por método de pagamento")
        if not df_filtered.empty and 'FormaPagamento' in df_filtered.columns:
            fig_payment_method = px.pie(
                df_filtered,
                values='ValorTotalVenda',
                names='FormaPagamento',
                title='Faturamento por método de pagamento'
            )
            st.plotly_chart(fig_payment_method)
        else:
            st.write("Dados insuficientes para gerar gráfico de Faturamento por método de pagamento")

        st.markdown("---")

        st.header("Faturamento por forma de pagamento")
        if not df_filtered.empty and 'FormaPagamento' in df_filtered.columns:
            fig_city_sales = px.bar(
                df_filtered,
                x='FormaPagamento',
                y='ValorTotalVenda',
                title='Faturamento por forma de pagamento',
                labels={'FormaPagamento': 'Forma de Pagamento', 'ValorTotalVenda': 'Valor Total de Venda'},
                color='FormaPagamento'
            )
            st.plotly_chart(fig_city_sales)
        else:
            st.write("Dados insuficientes para gerar gráfico de Faturamento por forma de pagamento")

        st.markdown("---")

        st.header("Produto mais vendido")
        if not df_filtered.empty and 'Produto' in df_filtered.columns:
            fig_produto_mais_vendido = px.line(
                df_filtered,
                x='Mes',
                y='Produto',
                color='Produto',
                title='Produto mais vendido'
            )
            st.plotly_chart(fig_produto_mais_vendido)
        else:
            st.write("Dados insuficientes para gerar gráfico de Produto mais vendido")

        st.markdown("---")

        st.header("Valor da Venda vs Valor da Comissão")
        if not df_filtered.empty and 'ValorVenda' in df_filtered.columns and 'ValorComissão' in df_filtered.columns:
            fig_venda_x_comissao = px.scatter(
                df_filtered,
                x='ValorVenda',
                y='ValorComissão',
                color='Status',
                title='Valor da Venda vs Valor da Comissão',
                labels={'ValorVenda': 'Valor da Venda', 'ValorComissão': 'Valor da Comissão'}
            )
            st.plotly_chart(fig_venda_x_comissao)
        else:
            st.write("Dados insuficientes para gerar gráfico de Valor da Venda vs Valor da Comissão")

        st.markdown("---")

        st.header("Distribuição do Valor das Vendas")
        if not df_filtered.empty and 'ValorVenda' in df_filtered.columns:
            fig_histograma = px.histogram(
                df_filtered,
                x='ValorVenda',
                title='Distribuição do Valor das Vendas'
            )
            st.plotly_chart(fig_histograma)
        else:
            st.write("Dados insuficientes para gerar gráfico de Distribuição do Valor das Vendas")
