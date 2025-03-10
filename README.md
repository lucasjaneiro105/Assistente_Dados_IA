# Mini-Assistente de Dados 🧠🐼

Um assistente inteligente para análise de dados via linguagem natural, combinando a biblioteca `PandasAI` e modelos da OpenAI (GPT-3.5-turbo) em uma interface web simples construída com Streamlit. Permite que usuários carreguem arquivos CSV e interajam com os dados através de perguntas em português, gerando insights e visualizações automáticas.

## Visão Geral ⚙️

O projeto é uma aplicação web que simplifica a análise de dados por meio de:
- **Upload de CSV**: Carregamento de dados tabulares.
- **Processamento com IA**: Interpretação de perguntas em linguagem natural usando GPT-3.5-turbo.
- **Geração de Respostas**: Respostas textuais e gráficas (como visualizações do Seaborn/Matplotlib).
- **Interface Interativa**: Histórico de conversas e exibição de dados.

## Características Principais

- 📋 **Upload de CSV**: Suporte a arquivos CSV com separador `;`.
- 🗨️ **Perguntas em Português**: Interação natural (ex: *"Quais são os outliers na coluna X?"*).
- 📊 **Visualizações Automáticas**: Geração de gráficos (salvos em `exports/charts`) exibidos diretamente na interface.
- 🔄 **Histórico de Conversas**: Mantém um registro das interações na sessão.
- 🤖 **Integração com OpenAI**: Utiliza o modelo `gpt-3.5-turbo` para processamento das queries.

## Limitações

- 🔐 **Dependência da OpenAI**: Requer chave de API (via arquivo `.env`) e créditos na plataforma.
- 📁 **Tamanho do Arquivo**: Não otimizado para datasets muito grandes (limitações de memória do Streamlit).
- 🖼️ **Geração de Imagens**: O caminho da pasta de gráficos (`exports/charts`) está fixo no código, podendo causar erros em outros sistemas.
- ⚠️ **Precisão da IA**: Respostas podem variar dependendo da complexidade da pergunta e qualidade dos dados.
- 🌐 **Idioma**: Apesar de aceitar perguntas em português, parte do processamento interno é em inglês.

## Como Executar

1. **Clone o repositório**:
```bash
git clone <repository-url>
cd <repository-folder>
```

2. **Instale as dependências**: Certifique-se de ter Python 3.8+ instalado.
```bash
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente**: Crie um arquivo .env na raiz do projeto com sua chave de API:
```bash
OPENAI_API_KEY=<sua-chave-api>
```

4. **Inicie a aplicação:**:
```bash
streamlit run main.py
```
