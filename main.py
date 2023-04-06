import streamlit as st


def main():
    st.set_page_config(page_title="Página Virando", page_icon="📖")
    st.title("Página Virando")

    st.markdown("""
    <html>
        <div class="book">
            <div class="page front">
                <h1 background-color="orange" align= 'center' color= "white" >Página de Frente</h1>
                <p margin= '10px'>  este é um exemplo de realidade virtual 
                este é um exemplo de realidade virtualeste é um exemplo de realidade virtualvvvveste é um exemplo de realidade virtualeste é um exemplo de realidade virtual</p>
                <img src="imagem5.png">
            </div>
            <div class="page midlle">
                <h1>Página de meio</h1>
                 <img src="imagem3.png">
            </div>
            <div class="page middle2">
                <h1>Página de pagina</h1>
            </div>
            <div class="page back">
                <h1>Página de Trás</h1>
            </div>
        </div>
        <head>
        <style>
            /* Definindo a área do livro */
            .book {
                position: relative;
                width: 80%;
                height: 550px;
                margin: 15% 15%;
                transform-style: preserve-3d;
            }

            /* Definindo as páginas */
            .page {
                position: absolute;
                margin: 0 auto;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: #92A8D1;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
                transform-origin: top left; /* define o ponto de origem da rotação */
                transform-style: preserve-3d;
                transition: transform 3s;
                #backface-visibility: hidden; /* oculta a parte de trás da página */
            }

            /* Definindo a página de frente */
            .front {
                transform: rotateY(0deg);
                z-index: 2;
            }

            /* Definindo a página de trás */
            .back {
                transform: rotateY(180deg);
                z-index: 1;
            }

            /* Definindo o efeito de hover */
            .page:hover {
                transform: rotateY(-180deg);
            }
            .video  {
                    position: fixed;
                    top: 50%;
                    left: 50%;
                    min-widht:100%;
                    min-height:100%;
                    width: auto;
                    height: auto;
                    transform: translate(-50%,-50%);
                    z-index: -1;
                    }
        </style>
        </head>
        <body>
        <video autoplay muted loop>
            <source src ="Video.mp4" type="video/mp4"
            </video>
            </body>
            </html>
        
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
