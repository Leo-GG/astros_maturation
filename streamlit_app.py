import streamlit as st
import pandas as pd
import plotly.express as px
import scanpy as sc
import loompy


adata_Loo=sc.read_loom('Loo_ast.loom')
adata_Loo.obs_names=adata_Loo.obs.obs_names
adata_Loo.var_names=adata_Loo.var.var_names
df_Loo=pd.DataFrame(adata_Loo.X.todense(),columns=adata_Loo.var_names,index=adata_Loo.obs_names)
df_Loo['Condition']=adata_Loo.obs.Condition
df_Loo['UMAP1']=[i[0] for i in adata_Loo.obsm['X_umap']]
df_Loo['UMAP2']=[i[1] for i in adata_Loo.obsm['X_umap']]


adata=sc.read_loom('Bella_red.loom')#merged_adata.copy()
adata.obs_names=adata.obs.obs_names
adata.var_names=adata.var.var_names
df_Bella=pd.DataFrame(adata.X.todense(),columns=adata.var_names,index=adata.obs_names)
df_Bella['Condition']=adata.obs.Condition
df_Bella['UMAP1']=[i[0] for i in adata.obsm['X_umap']]
df_Bella['UMAP2']=[i[1] for i in adata.obsm['X_umap']]


common_genes=list(set(adata.var_names) & set(adata_Loo.var_names))

del(adata_Loo)
del(adata)

# Set up Streamlit app
st.title("Embryonic and post-natal mouse astrocytes and radial glia")
st.markdown("Data from [Loo et al.](https://www.nature.com/articles/s41467-018-08079-9)")

# Sidebar with dropdown menu
st.sidebar.title("Gene selection")
color_col = st.sidebar.selectbox("Select a variable to plot", ['Condition']+common_genes)

scatter_Loo= px.scatter(df_Loo,x='UMAP1',y='UMAP2',color=color_col)
strip_Loo = px.strip(df_Loo, x='Condition', y=color_col)
st.plotly_chart(scatter_Loo)
st.plotly_chart(strip_Loo)

scatter_fig= px.scatter(df_Bella,x='UMAP1',y='UMAP2',color=color_col)
strip_fig = px.strip(df_Bella, x='Condition', y=color_col)

st.plotly_chart(scatter_fig)
st.plotly_chart(strip_fig)
#st.write(df_Bella.shape)

