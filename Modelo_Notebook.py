{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Modelo Notebook.ipynb",
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyP0jrxItEEwftMvXBd5sN1k",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ErisonBarros/modelojupyternotebook/blob/erison.barros/Modelo_Notebook.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "<table class=\"ee-notebook-buttons\" align=\"left\">\n",
        "    <td><a target=\"_blank\"  href=\"https://github.com/giswqs/earthengine-py-notebooks/tree/master/Template/geemap_colab.ipynb\"><img width=32px src=\"https://www.tensorflow.org/images/GitHub-Mark-32px.png\" /> View source on GitHub</a></td>\n",
        "    <td><a target=\"_blank\"  href=\"https://nbviewer.jupyter.org/github/giswqs/earthengine-py-notebooks/blob/master/Template/geemap_colab.ipynb\"><img width=26px src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png\" />Notebook Viewer</a></td>\n",
        "    <td><a target=\"_blank\"  href=\"https://colab.research.google.com/github/giswqs/earthengine-py-notebooks/blob/master/Template/geemap_colab.ipynb\"><img src=\"https://www.tensorflow.org/images/colab_logo_32px.png\" /> Run in Google Colab</a></td>\n",
        "</table>"
      ],
      "metadata": {
        "id": "qBIUzWiMVxuM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<a href=\"https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/04.13-Geographic-Data-With-Basemap.ipynb\"><img align=\"left\" src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open in Colab\" title=\"Open and Execute in Google Colaboratory\"></a>\n"
      ],
      "metadata": {
        "id": "2rqmyyRuWFcl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Sumario\n",
        "\n",
        "1. [Introdução](#Intrudução)\n",
        "2. [Desenvolvimento](#Desenvolvimento)\n",
        "3. [Conclusão](#Conclusão)"
      ],
      "metadata": {
        "id": "MXUNDosoT33S"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Extraindo dados"
      ],
      "metadata": {
        "id": "4TwqA8oOcIdK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "! unzip /content/Dados_de_SR-20211110T142824Z-001.zip"
      ],
      "metadata": {
        "id": "Uxc2DOGFcKiA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Copiar da web e copiar numa pasta do google"
      ],
      "metadata": {
        "id": "sVCe3sbtcfMS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!wget -P \"/content/drive/MyDrive/Colab Notebooks/Dados_de_SR\" https://github.com/ErisonBarros/bookpython_ufpe/blob/master/Dados_de_SR-20211112T010207Z-001/Dados_de_SR/Dados_de_SR-20211112T010207Z-001.zip"
      ],
      "metadata": {
        "id": "myFlqDj7ceJQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Clone the entire repo.\n",
        "!git clone -l -s https://github.com/ErisonBarros/LegislacaoTerritorial.git cloned-repo\n",
        "%cd cloned-repo\n",
        "!ls"
      ],
      "metadata": {
        "id": "0ht3_4jkWEla"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# É possível clonar o repositório inteiro do GitHub utilizando o comando git.\n",
        "!git clone https://github.com/ErisonBarros/book_python.git"
      ],
      "metadata": {
        "id": "u5jBXhgeWzBx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%ldir"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nNuCoJLIXBru",
        "outputId": "330b8223-5553-4373-d5b1-c27929c3bdb5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "drwxr-xr-x 3 root  4096 Mar 20 03:24 \u001b[0m\u001b[01;34mii-unidade\u001b[0m/\n",
            "drwxr-xr-x 4 root  4096 Mar 20 03:24 \u001b[01;34mi-unidade\u001b[0m/\n",
            "drwxr-xr-x 2 root  4096 Mar 20 03:24 \u001b[01;34mreadme5\u001b[0m/\n",
            "drwxr-xr-x 2 root  4096 Mar 20 03:24 \u001b[01;34mreadme-7\u001b[0m/\n",
            "drwxr-xr-x 2 root  4096 Mar 20 03:24 \u001b[01;34muntitled\u001b[0m/\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%history"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NmBSms1-XFyM",
        "outputId": "51bc2fbb-dbfa-4a5b-db5b-76324906da75"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "# Clone the entire repo.\n",
            "!git clone -l -s https://github.com/ErisonBarros/LegislacaoTerritorial.git cloned-repo\n",
            "%cd cloned-repo\n",
            "!ls\n",
            "%ldir\n",
            "%history\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Baixar dados 0 Linux\n",
        "O comando WGET permite baixar (download) de arquivos remotos. Executar o comando: !wget http://tiagodemelo.info/datasets/dados-curso.csv"
      ],
      "metadata": {
        "id": "3K7a32pWXUJC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!wget http://tiagodemelo.info/datasets/dados-curso.csv"
      ],
      "metadata": {
        "id": "tG8awrdxXRAi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4. Badges\n",
        "<a name=\"badges\"></a>\n",
        "\n",
        "The theme also defines special classes to include [badges](https://shields.io/).\n",
        "\n",
        "This may turn out to be particularly useful in notebooks to include links to external services like [Google Colab](https://colab.research.google.com), [MyBinder](https://mybinder.org), or [NBViewer](https://nbviewer.jupyter.org),\n",
        "\n",
        "In order to do so, the theme provides the `CSS` class **`.badges`** that can be used in a Markdown cell:\n",
        "\n",
        "```html\n",
        "<div class=\"badges\"> ... </div>\n",
        "```\n",
        "\n",
        "Here is an example:\n",
        "\n",
        "<div class=\"badges\">\n",
        "\n",
        "[![Colab](https://colab.research.google.com/assets/colab-badge.svg)]()\n",
        "\n",
        "[![myBinder](https://mybinder.org/badge_logo.svg)]()\n",
        "    \n",
        "[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)]()\n",
        "</div>"
      ],
      "metadata": {
        "id": "UWTsoESgX09a"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Baixa dados"
      ],
      "metadata": {
        "id": "FEZAPbeSYUmR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!wget https://raw.githubusercontent.com/ErisonBarros/bookpython_ufpe/master/leitura%20dados.csv"
      ],
      "metadata": {
        "id": "6lvC7EmvYZqE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Verificar os arquivos na pasta"
      ],
      "metadata": {
        "id": "VI6UOG2MYgJD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!ls '/content/cloned-repo'"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9XNIUolVYmb5",
        "outputId": "7ce2151b-d445-4615-8ba1-88407faa85df"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " aquisicao-de-propriedade.md\n",
            " as-fundamentacoes-do-direito-registral-para-certificacao-de-imoveis-rurais.md\n",
            "'Bens Públicos 1.md'\n",
            "'Bens Públicos existentes no Brasil.md'\n",
            " Clonar_Repositorio.ipynb\n",
            "'Coletânea com a Legislação da Cartografia Nacional.md'\n",
            " _config.yml\n",
            "'Direito Agrário'\n",
            "'Direito das Coias.md'\n",
            "'DIREITO DAS COISAS.md'\n",
            "'Direito Urbanístico.md'\n",
            "'Dos direitos de vizinhança.md'\n",
            " estatuto-da-cidade.md\n",
            "'Estatuto da Cidade.md'\n",
            "'Estrutura do Direito das Coisas.md'\n",
            " google-classroom.md\n",
            " ii-unidade\n",
            " Indices.ipynb\n",
            " info.md\n",
            " INFORMAÇÃO.md\n",
            " Inicio\n",
            " Introdução.ipynb\n",
            " i-unidade\n",
            "'Legislação Ambiental.md'\n",
            " legislacao-para-drones.md\n",
            "'Lei de Uso e Ocupação do Solo.md'\n",
            "'Os Bens.md'\n",
            " pagina-de-check.md\n",
            " readme2.md\n",
            " readme3.md\n",
            " README4.md\n",
            " readme5\n",
            " readme5.md\n",
            " readme-7\n",
            " readme-7.md\n",
            " README.md\n",
            " REDME.md\n",
            " Summary.ipynb\n",
            " SUMMARY.md\n",
            "'Terrenos de Marinha.md'\n",
            " untitled\n",
            "'Welcome file.1.md'\n",
            " welcome-file.2.md\n",
            "'Welcome file.2.md'\n",
            "'Welcome file.3.md'\n",
            "'Welcome file.md'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Copiar arquivos\n",
        "%cp -av 'Caminho de origem' 'caminho de destino'"
      ],
      "metadata": {
        "id": "2MsMuC25Y8rx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%cp -av '/content/drive/MyDrive/CHC Gps' '/content/drive/MyDrive/BCKP_GPS'"
      ],
      "metadata": {
        "id": "5bceKKe3Y8Qp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Intrudução"
      ],
      "metadata": {
        "id": "jbRwE2C_Ujfs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "cDoMJo0yU9bi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Desenvolvimento"
      ],
      "metadata": {
        "id": "MfX8ciWBUtjS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "UcgCJmP_UqyK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Conclusão"
      ],
      "metadata": {
        "id": "-snq7FfmU33q"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aWS3BKO4MA-N"
      },
      "outputs": [],
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "KkpAdVxqfyAD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Gerar PDF"
      ],
      "metadata": {
        "id": "VA94soUQdfHP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%%capture\n",
        "!wget -nc https://raw.githubusercontent.com/ErisonBarros/modelojupyternotebook/erison.barros/Modelo_Notebook.ipynb\n",
        "from colab_pdf import colab_pdf\n",
        "colab_pdf('modeloNotebook.ipynb')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 352
        },
        "id": "kejNpk_bdegq",
        "outputId": "cb6a0f5b-263a-4765-d0e2-996e4b9eeedb"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-958ec52bbd3f>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mget_ipython\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msystem\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'wget -nc https://raw.githubusercontent.com/ErisonBarros/modelojupyternotebook/erison.barros/Modelo_Notebook.ipynb'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mcolab_pdf\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mcolab_pdf\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mcolab_pdf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'modeloNotebook.ipynb'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/content/cloned-repo/colab_pdf.py\u001b[0m in \u001b[0;36mcolab_pdf\u001b[0;34m(file_name, notebookpath)\u001b[0m\n\u001b[1;32m     20\u001b[0m     \u001b[0;31m# Check if the notebook exists in the Drive.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0misfile\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mjoin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnotebookpath\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfile_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 22\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"file '{file_name}' not found in path '{notebookpath}'.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     23\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m     \u001b[0;31m# Installing all the recommended packages.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mValueError\u001b[0m: file 'modeloNotebook.ipynb' not found in path '/content/drive/MyDrive/Colab Notebooks/'."
          ]
        }
      ]
    }
  ]
}