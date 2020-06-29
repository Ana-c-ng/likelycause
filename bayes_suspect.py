{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "bayes_suspect.py",
      "provenance": [],
      "mount_file_id": "1D6KGl0nO-ujJjRBnJknvHybgdAtFqReD",
      "authorship_tag": "ABX9TyNLpgITiQPkuZoFUohk8mEv",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/Ana-c-ng/likelycause/blob/master/bayes_suspect.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UW98i4IUJJFY",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "a3b23df4-803c-481a-df9d-d18d0dc33869"
      },
      "source": [
        "\"\"\"My Bayes Suspect Clever Function\"\"\"\n",
        "\n",
        "import scipy\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "import scipy.stats\n",
        "from statsmodels.distributions.empirical_distribution import ECDF\n",
        "\n",
        "def fvlikelihood (df,a,value,interval,min,b='NULL'):    \n",
        "    if b == 'NULL':\n",
        "        return [len(df),scipy.stats.gaussian_kde(df[a]).integrate_box_1d((1-interval)*df[a].iloc[value],(1+interval)*df[a].iloc[value])]\n",
        "    else:    \n",
        "        if len(df[(df[a]<df[a].iloc[value]*(1+interval))&(df[a]>df[a].iloc[value]*(1-interval))])<=min:\n",
        "            return [0,0]\n",
        "        else:\n",
        "            return [len(df[(df[a]<df[a].iloc[value]*(1+interval))&(df[a]>df[a].iloc[value]*(1-interval))]),\n",
        "            scipy.stats.gaussian_kde(df[(df[a]<df[a].iloc[value]*(1+interval))&(df[a]>df[a].iloc[value]*(1-interval))][b]).integrate_box_1d((1-interval)*df[b].iloc[value],(1+interval)*df[b].iloc[value])]"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/root\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}