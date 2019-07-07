from storage_module.template_dao import TemplateDao
import json

dao = TemplateDao()

document="""{
      "key":"default",
      "name":"Formulário Caieiras",
      "display":"block",
      "description":"Utilize para informar sobre o andamento e conclusão de ações de vistoria associadas a ocorrências relatadas por terceiros ou identificadas pelo próprio agente.",
      "location":{},
      "customFilter":{
        "filter":{
          "default":"",
          "label":"Natureza da ocorrência",
          "name":"natureza",
          "list":[
            {"label":"Colmeia de abelhas","value":"option-1"},
            {"label":"Padrão de luz","value":"option-2"},
            {"label":"Queda de árvore","value":"option-3"}
          ]
        }
      },
      "sessions":[
        {
          "key":"s1",
          "name":"Natureza da ocorrência"
        },
        {
          "key":"s2",
          "name":"Solicitante"
        },
        {
          "key":"s3",
          "name":"Data/Hora"
        },
        {
          "key":"s4",
          "name":"Detalhamento"
        },
        {
          "key":"s5",
          "name":"Parecer"
        }
      ]
    }"""
jsonDoc=json.loads(document)
dao.addTemplateMeta(jsonDoc)

document="""{
      "key":"landslide",
      "name":"Risco de escorregamento",
      "display":"block",
      "description":"Utilize em ações de vistoria que avaliam riscos de escorregamento de terra e/ou rochas.",
      "location":{},
      "sessions":[
        {
          "key":"s1",
          "name":"Dados gerais sobre as moradias"
        },
        {
          "key":"s2",
          "name":"Caracterização do local"
        },
        {
          "key":"s3",
          "name":"Água"
        },
        {
          "key":"s4",
          "name":"Vegetação no talude ou proximidades"
        },
        {
          "key":"s5",
          "name":"Sinais de movimentação (feições de instabilidade)"
        },
        {
          "key":"s6",
          "name":"Tipos de processos de instabilização esperados ou já ocorridos"
        },
        {
          "key":"s7",
          "name":"Determinação do grau de risco",
          "help":"Agora junte tudo o que você viu: caracterização do local das moradias, a água na área, vegetação, os sinais de movimentação, os tipos de escorregamentos que já ocorreram ou são esperados. Avalie, principalmente usando os sinais, se esta área está em movimentação ou não e se o escorregamento poderá atingir alguma moradia. Utilize a tabela de classificação dos níveis de risco. Caso não haja sinais, mas a sua observação dos dados mostra que a área é perigosa, coloque alto ou médio, mas que deve ser observada sempre. Cadastre só as situações de risco, marcando também as de baixo risco."
        },
        {
          "key":"s8",
          "name":"Necessidade de remoção (para as moradias em risco muito alto)"
        },
        {
          "key":"s9",
          "name":"Outras informações"
        }
      ]
    }"""

jsonDoc=json.loads(document)
dao.addTemplateMeta(jsonDoc)