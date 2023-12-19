# Image-to-text in real time

A detecção e descrição de objetos em vídeos em tempo real têm se tornado uma área de pesquisa e aplicação cada vez mais relevante. Este projeto visa explorar a integração das bibliotecas Streamlit, OpenCV e Transformers para criar uma solução robusta e eficiente para identificação de objetos em vídeos ao vivo. A capacidade de descrever os objetos detectados em texto adiciona uma camada significativa de compreensão e interpretação aos dados capturados.

A solução pode atingir resultados ainda melhores usando o 'model=llava-hf/llava-1.5-7b-hf' na classe image_to_text_description.py, que não conseguimos aplicar com efeito pois houve o impedipento devido a recursos computacionais.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/job-nunes/GPT.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd GPT
    ```

3. Instale as dependências usando o arquivo requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```

## Como Executar

1.  Execute o seguinte comando na linha de comando para iniciar o programa:

    ```bash
    streamlit run ocv2.py
    ```
Isso iniciará a aplicação web usando o Streamlit.

## Funcionalidades

O programa possui as seguintes funcionalidades:

- **Captura de Vídeo:** O programa é capaz de capturar vídeo da webcam.
- **Identificação de Objetos:** Utilizando algoritmos de visão computacional, o programa identifica objetos na imagem.
- **Exibição Web:** Os resultados são apresentados em uma página web gerada pelo Streamlit.

## Uso

Após iniciar a aplicação, acesse a página web gerada no navegador. O usuário terá as seguintes opções:

- **Plotar:** Ao marcar esta opção, o programa irá gerar o texto mais vezes.
- **Parar:** Ao selecionar esta opção, a execução do programa será interrompida.

Certifique-se de ter uma webcam funcional para obter os melhores resultados.
